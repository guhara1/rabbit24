#!/usr/bin/env python3
"""안산 출장마사지 — 정적 사이트 빌드 스크립트.

content/ 패키지의 페이지 정의를 읽어 정적 HTML을 생성한다.

규칙(자동 적용):
  - 본문 텍스트 2,000자 미만 페이지는 robots noindex 처리
  - sitemap.xml 에는 index 허용 페이지만 포함
"""
import html
import json
import os
import re
import shutil
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from content import PAGES
from content.site import (BASE_URL, BRAND, NAV, PHONE, PHONE_DISPLAY)
from content.reviews import REVIEWS

# 후기 집계(표시 후기 = 스키마 후기 동일). 가짜 평점 금지 — 실제 후기로 교체 운영.
_REVIEW_COUNT = len(REVIEWS)
_REVIEW_AVG = round(sum(r["rating"] for r in REVIEWS) / _REVIEW_COUNT, 1) if _REVIEW_COUNT else 0

ROOT = os.path.dirname(os.path.abspath(__file__))
# Cloudflare Pages가 빌드를 실행하지 않고 저장소 루트를 그대로 배포하므로
# 빌드 결과물을 저장소 루트에 직접 출력한다.
PUBLIC_DIR = ROOT
MIN_INDEX_CHARS = 2000


def text_length(body_html: str) -> int:
    """태그를 제거한 본문 글자수(공백 포함, 연속 공백은 1자).
    공통 요금 블록은 페이지 고유 본문이 아니므로 측정에서 제외한다."""
    text = re.sub(r'<section class="pricing">.*?</section>', " ", body_html, flags=re.S)
    text = re.sub(r"<[^>]+>", " ", text)
    text = html.unescape(text)
    text = re.sub(r"\s+", " ", text).strip()
    return len(text)


def render_nav(current_path: str) -> str:
    items = []
    for label, href, children in NAV:
        active = " is-active" if href == "/" + current_path else ""
        if children:
            sub = "".join(
                f'<li><a href="{c_href}">{c_label}</a></li>'
                for c_label, c_href in children
            )
            items.append(
                f'<li class="nav-item has-sub{active}">'
                f'<a href="{href}">{label}</a>'
                f'<ul class="sub-menu">{sub}</ul></li>'
            )
        else:
            items.append(
                f'<li class="nav-item{active}"><a href="{href}">{label}</a></li>'
            )
    return "".join(items)


def render_breadcrumb(crumbs) -> str:
    if not crumbs:
        return ""
    parts = ['<nav class="breadcrumb" aria-label="현재 위치"><ol>']
    parts.append('<li><a href="/">홈</a></li>')
    for label, href in crumbs:
        if href:
            parts.append(f'<li><a href="{href}">{label}</a></li>')
        else:
            parts.append(f"<li><span>{label}</span></li>")
    parts.append("</ol></nav>")
    return "".join(parts)


def inject_toc(body: str):
    """본문 섹션(h2)에 id를 보장하고 좌측 목차 데이터를 만든다."""
    items = []
    counter = [0]

    def repl(m):
        attrs, title = m.group(1), m.group(2)
        idm = re.search(r'id="([^"]+)"', attrs)
        if idm:
            sid = idm.group(1)
            opening = f"<section{attrs}>"
        else:
            counter[0] += 1
            sid = f"sec-{counter[0]}"
            opening = f'<section id="{sid}"{attrs}>'
        label = re.sub(r"<[^>]+>", "", title).strip()
        items.append((sid, label))
        return f"{opening}<h2>{title}</h2>"

    body = re.sub(r"<section([^>]*)>\s*<h2>(.*?)</h2>", repl, body, flags=re.S)
    return body, items


def render_toc(items) -> str:
    if len(items) < 3:
        return ""
    links = "".join(
        f'<li><a href="#{sid}">{label}</a></li>' for sid, label in items
    )
    return (
        '<aside class="page-toc"><nav aria-label="페이지 목차">'
        '<p class="toc-title">목차</p>'
        f"<ul>{links}</ul></nav></aside>"
    )


def _ld(obj: dict) -> str:
    """JSON-LD 스크립트 블록 1개를 만든다."""
    return (
        '<script type="application/ld+json">\n'
        + json.dumps(obj, ensure_ascii=False, indent=2)
        + "\n</script>\n"
    )


def make_image_object() -> dict:
    """선호 썸네일(대표 이미지) ImageObject — og:image와 동일 이미지를 명시 지정.
    구글이 임의로 썸네일을 크롤링하지 않도록 schema.org에서 선호 이미지를 지정한다."""
    base = BASE_URL.rstrip("/")
    return {
        "@type": "ImageObject",
        "@id": base + "/#primaryimage",
        "url": base + "/assets/og-image.webp",
        "contentUrl": base + "/assets/og-image.webp",
        "width": 1200,
        "height": 675,
        "encodingFormat": "image/webp",
        "caption": BRAND + " 서울·경기·인천 출장마사지·홈타이 안내",
    }


def make_org_schema() -> dict:
    """사이트 전역 Organization 스키마 (모든 페이지 공통)."""
    base = BASE_URL.rstrip("/")
    return {
        "@context": "https://schema.org",
        "@type": "Organization",
        "@id": base + "/#organization",
        "name": BRAND,
        "url": base + "/",
        "logo": base + "/assets/apple-touch-icon.png",
        "image": {"@id": base + "/#primaryimage"},
        "telephone": PHONE,
        "sameAs": ["https://t.me/googleseolab"],
        "areaServed": [{"@type": "City", "name": "서울특별시"}, {"@type": "AdministrativeArea", "name": "경기도"}, {"@type": "City", "name": "인천광역시"}],
        "contactPoint": {
            "@type": "ContactPoint",
            "telephone": PHONE,
            "contactType": "reservations",
            "availableLanguage": ["ko"],
            "areaServed": "KR",
        },
    }


def make_website_schema() -> dict:
    """WebSite 스키마 — 사이트 전역 정체성."""
    base = BASE_URL.rstrip("/")
    return {
        "@context": "https://schema.org",
        "@type": "WebSite",
        "@id": base + "/#website",
        "name": BRAND,
        "url": base + "/",
        "inLanguage": "ko",
        "publisher": {"@id": base + "/#organization"},
    }


def make_service_schema() -> dict:
    """Service 스키마 — 방문형 관리 서비스 제공 범위 + 후기/평점.
    후기는 페이지에 실제로 노출되는 항목과 동일하다(구글 정책 준수)."""
    base = BASE_URL.rstrip("/")
    schema = {
        "@context": "https://schema.org",
        "@type": "Service",
        "@id": base + "/#service",
        "name": BRAND + " 출장마사지·홈타이",
        "serviceType": "출장마사지·홈타이 방문 관리",
        "provider": {"@id": base + "/#organization"},
        "areaServed": [{"@type": "City", "name": "서울특별시"}, {"@type": "AdministrativeArea", "name": "경기도"}, {"@type": "City", "name": "인천광역시"}],
        "availableChannel": {
            "@type": "ServiceChannel",
            "servicePhone": {"@type": "ContactPoint", "telephone": PHONE},
        },
        "offers": [
            {"@type": "Offer", "name": "60분 코스", "price": "90000", "priceCurrency": "KRW"},
            {"@type": "Offer", "name": "90분 코스", "price": "150000", "priceCurrency": "KRW"},
            {"@type": "Offer", "name": "120분 코스", "price": "180000", "priceCurrency": "KRW"},
        ],
    }
    if _REVIEW_COUNT:
        schema["aggregateRating"] = {
            "@type": "AggregateRating",
            "ratingValue": _REVIEW_AVG,
            "reviewCount": _REVIEW_COUNT,
            "bestRating": 5,
            "worstRating": 1,
        }
        schema["review"] = [
            {
                "@type": "Review",
                "author": {"@type": "Person", "name": r["author"]},
                "datePublished": r["date"],
                "reviewRating": {"@type": "Rating", "ratingValue": r["rating"], "bestRating": 5, "worstRating": 1},
                "reviewBody": r["body"],
            }
            for r in REVIEWS
        ]
    return schema


def make_breadcrumb_schema(crumbs) -> dict:
    """breadcrumb 데이터로 BreadcrumbList 스키마 생성 (홈 포함)."""
    base = BASE_URL.rstrip("/")
    items = [{
        "@type": "ListItem",
        "position": 1,
        "name": "홈",
        "item": base + "/",
    }]
    # breadcrumb 데이터의 첫 항목이 루트("/")를 가리키면 홈과 중복되므로 건너뛴다.
    rest = crumbs[1:] if crumbs and crumbs[0][1] == "/" else crumbs
    for i, (label, href) in enumerate(rest, start=2):
        entry = {"@type": "ListItem", "position": i, "name": label}
        if href:
            entry["item"] = base + href
        items.append(entry)
    return {
        "@context": "https://schema.org",
        "@type": "BreadcrumbList",
        "itemListElement": items,
    }


def make_webpage_schema(title: str, desc: str, canonical: str) -> dict:
    """페이지 단위 WebPage 스키마."""
    base = BASE_URL.rstrip("/")
    return {
        "@context": "https://schema.org",
        "@type": "WebPage",
        "name": title,
        "description": desc,
        "url": canonical,
        "inLanguage": "ko",
        "isPartOf": {"@id": base + "/#website"},
        "publisher": {"@id": base + "/#organization"},
        "primaryImageOfPage": {"@id": base + "/#primaryimage"},
    }


def make_faqpage_schema(body: str):
    """본문의 <dl class="faq-list"> 에서 dt/dd 쌍을 추출해 FAQPage 스키마를 만든다.
    FAQ가 없으면 None을 반환한다."""
    m = re.search(r'<dl class="faq-list">(.*?)</dl>', body, flags=re.S)
    if not m:
        return None
    pairs = re.findall(r"<dt[^>]*>(.*?)</dt>\s*<dd>(.*?)</dd>", m.group(1), flags=re.S)
    if not pairs:
        return None

    def clean(s):
        return re.sub(r"\s+", " ", html.unescape(re.sub(r"<[^>]+>", "", s))).strip()

    return {
        "@context": "https://schema.org",
        "@type": "FAQPage",
        "mainEntity": [
            {
                "@type": "Question",
                "name": clean(q),
                "acceptedAnswer": {"@type": "Answer", "text": clean(a)},
            }
            for q, a in pairs
        ],
    }


_LI_LINK_RE = re.compile(r"^\s*<a href=\"[^\"]+\">[^<]+</a>\s*$")


def buttonize_link_lists(body: str) -> str:
    """본문의 <ul> 중 모든 <li>가 '링크 1개만' 인 목록을 버튼형 그리드로 변환한다.
    (구·시·동 드릴다운, 인접 지역, 관련 페이지 등 내비게이션 목록 → .region-grid)
    설명이 붙은 목록(체크리스트 등)은 변환하지 않는다."""
    def repl(m):
        inner = m.group(1)
        lis = re.findall(r"<li>(.*?)</li>", inner, flags=re.S)
        if len(lis) >= 3 and all(_LI_LINK_RE.match(li) for li in lis):
            return '<ul class="region-grid">' + inner + "</ul>"
        return m.group(0)

    return re.sub(r"<ul>(.*?)</ul>", repl, body, flags=re.S)


def make_price_table() -> str:
    """코스 시간별 기본 요금표 — 전 페이지 공통 노출."""
    return (
        '<section class="price-table" aria-label="기본 요금">'
        '<div class="price-head"><h2>코스 시간으로 보는 기본 요금</h2>'
        '<p>관리 시간(60·90·120분)을 기준으로 정리한 기본 금액입니다. '
        '표시되지 않은 별도 비용은 두지 않는 것을 원칙으로 안내합니다.</p></div>'
        '<div class="price-cards">'
        '<div class="price-card"><p class="price-name">60분 코스</p>'
        '<p class="price-amount">90,000<span>원</span></p><p class="price-min">60분</p>'
        '<p class="price-desc">핵심 부위 위주 가벼운 이완</p>'
        f'<a class="price-cta" href="tel:{PHONE}">예약 문의</a></div>'
        '<div class="price-card is-featured"><span class="price-badge">추천</span>'
        '<p class="price-name">90분 코스</p>'
        '<p class="price-amount">150,000<span>원</span></p><p class="price-min">90분</p>'
        '<p class="price-desc">전신 균형 표준 구성·아로마 포함</p>'
        f'<a class="price-cta" href="tel:{PHONE}">예약 문의</a></div>'
        '<div class="price-card"><p class="price-name">120분 코스</p>'
        '<p class="price-amount">180,000<span>원</span></p><p class="price-min">120분</p>'
        '<p class="price-desc">구석구석 집중하는 프리미엄 구성</p>'
        f'<a class="price-cta" href="tel:{PHONE}">예약 문의</a></div>'
        '</div>'
        '<p class="price-note">방문 지역과 시간대, 이동 거리에 따라 최종 금액은 통화 시 확정됩니다. '
        '<a href="/check/transfer-fee/">요금·예약 기준 자세히 보기 →</a></p>'
        "</section>"
    )


def _locality_label(page: dict) -> str:
    for label, href in reversed(page.get("breadcrumb") or []):
        if label and label != "수도권":
            return label
    return ""


def make_longtail_links(page: dict) -> str:
    """페이지 지역에 맞춘 롱테일 내부링크 컴포넌트(이용 상황·예약 전 확인 조합)."""
    path = page["path"]
    region = path.startswith(("seoul/", "gyeonggi/", "incheon/")) and not path.startswith("gyeonggi/ansan/")
    loc = _locality_label(page)
    if region and loc:
        groups = [
            (f"{loc} 이용 상황별 안내", [
                (f"{loc} 자택 방문 출장마사지", "/use/home/"),
                (f"{loc} 호텔·숙소 홈타이", "/use/hotel/"),
                (f"{loc} 오피스텔 방문 관리", "/use/officetel/"),
                (f"{loc} 업무지구 이용 안내", "/use/business-district/"),
                (f"{loc} 야간 예약 안내", "/use/night/"),
            ]),
            (f"{loc} 예약 전 확인사항", [
                (f"{loc} 방문 주소 확인", "/check/address/"),
                (f"{loc} 건물 출입 방식", "/check/entry/"),
                (f"{loc} 추가 이동비 안내", "/check/transfer-fee/"),
                (f"{loc} 예약 가능 시간", "/check/available-time/"),
                (f"{loc} 예약 변경·취소 기준", "/check/change-policy/"),
            ]),
        ]
    else:
        groups = [
            ("지역별 출장마사지 바로가기", [
                ("서울 출장마사지", "/seoul/"), ("경기 출장마사지", "/gyeonggi/"),
                ("인천 출장마사지", "/incheon/"), ("강남역 출장마사지", "/seoul/station/gangnam-station/"),
                ("수원 출장마사지", "/gyeonggi/suwon/"), ("분당 홈타이", "/gyeonggi/life/bundang-pangyo/"),
                ("송도 출장마사지", "/incheon/yeonsu-gu/songdo-dong/"), ("부평 출장마사지", "/incheon/bupyeong-gu/"),
            ]),
            ("이용 상황별 안내", [
                ("자택 방문", "/use/home/"), ("호텔·숙소", "/use/hotel/"), ("오피스텔", "/use/officetel/"),
                ("업무지구", "/use/business-district/"), ("야간 예약", "/use/night/"), ("외곽·공항", "/use/outer-area/"),
            ]),
        ]
    parts = ['<section class="longtail" aria-label="함께 보면 좋은 안내"><p class="longtail-head">함께 보면 좋은 안내</p>']
    for title, links in groups:
        chips = "".join(f'<a class="chip" href="{href}">{html.escape(t)}</a>' for t, href in links)
        parts.append(
            f'<div class="longtail-group"><p class="longtail-title">{html.escape(title)}</p>'
            f'<div class="chips">{chips}</div></div>'
        )
    parts.append("</section>")
    return "".join(parts)


def make_reviews_section() -> str:
    """이용 후기 컴포넌트 — 노출 후기 = Service 스키마 review 와 동일."""
    if not REVIEWS:
        return ""
    avg_round = round(_REVIEW_AVG)
    head_stars = "★" * avg_round + "☆" * (5 - avg_round)
    cards = []
    for r in REVIEWS:
        rs = "★" * r["rating"] + "☆" * (5 - r["rating"])
        cards.append(
            f'<figure class="review-card"><div class="review-stars" aria-label="{r["rating"]}점">{rs}</div>'
            f'<blockquote>{html.escape(r["body"])}</blockquote>'
            f'<figcaption><span class="review-author">{html.escape(r["author"])}</span>'
            f'<span class="review-loc">{html.escape(r["locality"])} · {html.escape(r["date"])}</span></figcaption></figure>'
        )
    return (
        '<section class="reviews" aria-label="이용 후기">'
        '<div class="reviews-head"><h2>이용 후기</h2>'
        f'<p class="reviews-score"><span class="reviews-stars" aria-hidden="true">{head_stars}</span> '
        f'<strong>{_REVIEW_AVG}</strong><span class="reviews-out">/ 5</span> '
        f'<span class="reviews-count">· 후기 {_REVIEW_COUNT}건</span></p></div>'
        f'<div class="review-grid">{"".join(cards)}</div>'
        "</section>"
    )


def render_page(page: dict) -> str:
    path = page["path"]
    title = page["title"]
    desc = page["desc"]
    h1 = page["h1"]
    body = page["body"]
    crumbs = page.get("breadcrumb") or []
    extra_head = page.get("extra_head", "")
    hero = page.get("hero", "")

    chars = text_length(body)
    noindex = page.get("noindex", False) or chars < MIN_INDEX_CHARS
    robots = (
        '<meta name="robots" content="noindex,follow">'
        if noindex
        else '<meta name="robots" content="index,follow">'
    )
    canonical = BASE_URL.rstrip("/") + "/" + path

    # 히어로가 있는 페이지(메인)는 H1을 히어로 안에서 출력한다.
    if hero:
        page_head = hero
    else:
        page_head = ""

    h1_html = "" if hero else f"<h1>{h1}</h1>"

    # 비히어로(지역 등) 페이지 상단 대표 이미지 배너 — 전 페이지 공통
    if hero:
        page_media = ""
    else:
        alt = re.sub(r"<[^>]+>", "", h1).strip() or BRAND
        page_media = (
            '<div class="page-media">'
            f'<img src="/assets/og-image.webp" width="1200" height="675" alt="{alt} 관리실" '
            'loading="lazy" decoding="async"></div>'
        )

    # 기존 인라인 요금 블록(구버전)은 제거하고 통일된 요금표로 대체한다.
    body = re.sub(r'<section class="pricing">.*?</section>', "", body, flags=re.S)
    body, toc_items = inject_toc(body)
    body = buttonize_link_lists(body)
    toc_html = render_toc(toc_items)
    layout_cls = "page-layout has-toc" if toc_html else "page-layout"

    # 요금표 + 롱테일 내부링크 + 이용 후기 컴포넌트(전 페이지 공통)
    price_html = make_price_table()
    longtail_html = make_longtail_links(page)
    reviews_html = make_reviews_section()

    # 스키마 자동 주입.
    # 공통: ImageObject(선호 썸네일) + Organization + WebSite 를 모든 페이지에 주입한다.
    # 메인(hero 보유)은 main.py의 extra_head에 풍부한 스키마가 이미 있으므로 공통 블록만 보강하고,
    # 나머지 페이지는 추가로 WebPage + BreadcrumbList 를 생성한다.
    # Service(후기·평점 포함)는 모든 페이지에 주입한다.
    common = [make_image_object(), make_org_schema(), make_website_schema(), make_service_schema()]
    blocks = common + [make_webpage_schema(title, desc, canonical)]
    if crumbs:
        blocks.append(make_breadcrumb_schema(crumbs))
    # 히어로 페이지(메인·안산허브)는 extra_head에 FAQPage가 이미 있어 본문 FAQ 스키마는 생략.
    if not hero:
        faq_schema = make_faqpage_schema(body)
        if faq_schema:
            blocks.append(faq_schema)
    auto_schema = "".join(_ld(b) for b in blocks)

    return f"""<!DOCTYPE html>
<html lang="ko">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title>
<meta name="description" content="{desc}">
{robots}
<link rel="canonical" href="{canonical}">
<meta property="og:type" content="website">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{desc}">
<meta property="og:url" content="{canonical}">
<meta property="og:site_name" content="{BRAND}">
<meta property="og:image" content="{BASE_URL.rstrip('/')}/assets/og-image.webp">
<meta property="og:image:type" content="image/webp">
<meta property="og:image:width" content="1200">
<meta property="og:image:height" content="675">
<meta property="og:image:alt" content="{BRAND} 출장마사지·홈타이 관리실">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:image" content="{BASE_URL.rstrip('/')}/assets/og-image.webp">
<link rel="icon" type="image/svg+xml" href="/assets/favicon.svg?v=2">
<link rel="icon" type="image/png" sizes="32x32" href="/assets/favicon-32.png?v=2">
<link rel="icon" href="/favicon.ico?v=2" sizes="48x48">
<link rel="apple-touch-icon" href="/assets/apple-touch-icon.png?v=2">
<meta name="theme-color" content="#0a1120">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Noto+Sans+KR:wght@400;500;700&family=Noto+Serif+KR:wght@600;700;900&display=swap" rel="stylesheet">
<link rel="stylesheet" href="https://cdn.jsdelivr.net/gh/orioncactus/pretendard/dist/web/static/pretendard.css">
<link rel="stylesheet" href="/assets/style.css">
{auto_schema}{extra_head}</head>
<body>
<header class="site-header">
  <div class="header-accent" aria-hidden="true"></div>
  <div class="header-top">
    <div class="header-inner">
      <a class="brand" href="/"><span class="brand-mark" aria-hidden="true">토</span> <span class="brand-text">{BRAND}</span></a>
      <p class="header-tagline"><span class="tag-gem">◆</span> 서울·경기·인천 전지역 방문 관리 <span class="tag-gem">◆</span> 24시간 상담</p>
      <a class="header-call" href="tel:{PHONE}"><span class="call-label">예약전화</span> {PHONE_DISPLAY}</a>
      <button class="nav-toggle" aria-label="메뉴 열기" aria-expanded="false"><span></span><span></span><span></span></button>
    </div>
  </div>
  <nav class="main-nav" aria-label="주 메뉴">
    <div class="nav-inner"><ul class="nav-list">{render_nav(path)}</ul></div>
  </nav>
</header>
{page_head}<main class="site-main">
  <div class="container {layout_cls}">
    {toc_html}
    <article class="page-content">
      {render_breadcrumb(crumbs)}
      {page_media}
      {h1_html}
      {body}
      {price_html}
      {longtail_html}
      {reviews_html}
    </article>
  </div>
</main>
<footer class="site-footer">
  <div class="container footer-grid">
    <div class="footer-col footer-about">
      <p class="footer-brand">{BRAND}</p>
      <p class="footer-desc">서울·경기·인천 수도권 전지역 방문 출장마사지·홈타이 안내 사이트입니다. 모든 서비스는 안내된 관리 범위와 위생·안전 기준 안에서만 제공됩니다.</p>
      <address class="footer-contact">
        <span class="footer-contact-row"><span class="footer-label">예약전화</span> <a href="tel:{PHONE}">{PHONE_DISPLAY}</a></span>
        <span class="footer-contact-row"><span class="footer-label">상담시간</span> 연중무휴 24시간</span>
        <span class="footer-contact-row"><span class="footer-label">서비스 지역</span> 서울·경기·인천 수도권 전지역</span>
      </address>
    </div>
    <nav class="footer-col" aria-label="지역 안내">
      <p class="footer-title">지역</p>
      <ul>
        <li><a href="/find/">지역 선택</a></li>
        <li><a href="/seoul/">서울 출장마사지</a></li>
        <li><a href="/gyeonggi/">경기 출장마사지</a></li>
        <li><a href="/incheon/">인천 출장마사지</a></li>
        <li><a href="/find/station/">지하철역 기준</a></li>
      </ul>
    </nav>
    <nav class="footer-col" aria-label="이용 안내">
      <p class="footer-title">이용 안내</p>
      <ul>
        <li><a href="/use/">이용 상황별 안내</a></li>
        <li><a href="/check/">예약 전 확인</a></li>
        <li><a href="/policy/contact/">문의하기</a></li>
      </ul>
    </nav>
    <nav class="footer-col" aria-label="정책 및 기준">
      <p class="footer-title">정책</p>
      <ul>
        <li><a href="/policy/privacy/">개인정보처리방침</a></li>
        <li><a href="/policy/terms/">고객 유의사항</a></li>
        <li><a href="/policy/content-quality/">콘텐츠 품질 기준</a></li>
        <li><a href="/policy/sitemap/">사이트맵</a></li>
      </ul>
    </nav>
  </div>
  <div class="footer-bottom">
    <div class="container footer-bottom-inner">
      <nav class="footer-refs" aria-label="공식·지역 정보 참고 링크">
        <span class="footer-refs-title">지역·생활 정보</span>
        <a href="https://www.ansan.go.kr" target="_blank" rel="noopener">안산시청</a>
        <a href="https://www.gg.go.kr" target="_blank" rel="noopener">경기도청</a>
        <a href="https://health.kdca.go.kr" target="_blank" rel="noopener">국가건강정보포털</a>
        <a href="https://korean.visitkorea.or.kr" target="_blank" rel="noopener">대한민국 구석구석</a>
      </nav>
      <p class="footer-copy">&copy; {BRAND}. All rights reserved.</p>
      <p class="footer-note">건전한 방문 관리 서비스를 운영하며, 불법적인 요청은 어떤 경우에도 응하지 않습니다.</p>
      <div class="footer-actions">
        <a class="btn-telegram" href="https://t.me/googleseolab" target="_blank" rel="noopener nofollow" title="웹사이트 제작문의">📱 웹사이트 제작문의</a>
        <a class="btn-partnership" href="https://t.me/googleseolab" target="_blank" rel="noopener nofollow" title="제휴문의">🤝 제휴문의</a>
      </div>
    </div>
  </div>
</footer>
<a class="call-fab" href="tel:{PHONE}" aria-label="전화 예약 {PHONE_DISPLAY}">
  <svg viewBox="0 0 24 24" aria-hidden="true"><path d="M6.62 10.79c1.44 2.83 3.76 5.14 6.59 6.59l2.2-2.2c.27-.27.67-.36 1.02-.24 1.12.37 2.33.57 3.57.57.55 0 1 .45 1 1V20c0 .55-.45 1-1 1-9.39 0-17-7.61-17-17 0-.55.45-1 1-1h3.5c.55 0 1 .45 1 1 0 1.25.2 2.45.57 3.57.11.35.03.74-.25 1.02l-2.2 2.2z"/></svg>
  <span class="call-fab-label">예약 전화</span>
</a>
<script src="/assets/nav.js"></script>
</body>
</html>
"""


BODIES_DIR = os.path.join(ROOT, "content", "bodies")


def body_override(path: str) -> str | None:
    """content/bodies/<slug>.html 가 있으면 해당 본문으로 교체한다.
    slug 규칙: 경로의 '/'를 '__'로, 끝 슬래시 제거. 빈 경로(메인)는 제외."""
    if not path:
        return None
    slug = path.rstrip("/").replace("/", "__")
    fp = os.path.join(BODIES_DIR, slug + ".html")
    if os.path.exists(fp):
        with open(fp, encoding="utf-8") as f:
            return f.read()
    return None


def _page_label(page: dict) -> str:
    crumbs = page.get("breadcrumb") or []
    if crumbs and crumbs[-1][0]:
        return crumbs[-1][0]
    return re.sub(r"<[^>]+>", "", page.get("h1", "")).strip()


def make_html_sitemap(pages) -> str:
    """전체 페이지를 섹션별로 묶은 사람용 HTML 사이트맵 본문을 생성한다."""
    groups = [
        ("지역 선택", "find/", lambda p: p.startswith("find/")),
        ("이용 상황", "use/", lambda p: p.startswith("use/")),
        ("서울", "seoul/", lambda p: p.startswith("seoul/")),
        ("경기", "gyeonggi/", lambda p: p.startswith("gyeonggi/") and not p.startswith("gyeonggi/ansan/")),
        ("인천", "incheon/", lambda p: p.startswith("incheon/")),
        ("안산(경기)", "gyeonggi/ansan/", lambda p: p.startswith("gyeonggi/ansan/")),
        ("예약 전 확인", "check/", lambda p: p.startswith("check/")),
        ("운영 기준", "policy/", lambda p: p.startswith("policy/")),
    ]
    out = [
        '<section><h2>토끼24 마사지 사이트맵</h2>',
        '<p>서울·경기·인천 수도권 출장마사지·홈타이 안내의 전체 페이지를 섹션별로 정리했습니다. '
        '찾으시는 지역이나 이용 안내로 바로 이동하세요. 지역 선택은 '
        '<a href="/find/">지역 선택</a>, 이용 상황별 안내는 <a href="/use/">이용 상황</a>에서도 확인할 수 있습니다.</p></section>',
    ]
    used = set()
    for title, _pref, match in groups:
        items = []
        for p in pages:
            path = p["path"]
            if not path or path in used:
                continue
            if match(path):
                used.add(path)
                items.append((path, _page_label(p)))
        if not items:
            continue
        lis = "".join(f'<li><a href="/{path}">{html.escape(label)}</a></li>' for path, label in items)
        out.append(f'<section><h2>{title}</h2><ul>{lis}</ul></section>')
    return "\n".join(out)


def build() -> None:
    report = []
    sitemap_urls = []

    # public 디렉터리가 없으면 생성
    os.makedirs(PUBLIC_DIR, exist_ok=True)

    # 1차: 본문 오버레이를 먼저 적용한다.
    for page in PAGES:
        if page["path"] == "policy/sitemap/":
            continue
        ov = body_override(page["path"])
        if ov is not None:
            page["body"] = ov

    # HTML 사이트맵은 '색인 대상 페이지'만 섹션별로 싣는다(noindex 미세동 제외).
    indexed_pages = [
        p for p in PAGES
        if p["path"] and p["path"] != "policy/sitemap/"
        and not p.get("noindex", False)
        and text_length(p["body"]) >= MIN_INDEX_CHARS
    ]
    html_sitemap_body = make_html_sitemap(indexed_pages)

    for page in PAGES:
        path = page["path"]
        if path == "policy/sitemap/":
            page["body"] = html_sitemap_body
        out_dir = os.path.join(PUBLIC_DIR, path)
        os.makedirs(out_dir, exist_ok=True)
        html_out = render_page(page)
        with open(os.path.join(out_dir, "index.html"), "w", encoding="utf-8") as f:
            f.write(html_out)

        chars = text_length(page["body"])
        noindex = page.get("noindex", False) or chars < MIN_INDEX_CHARS
        if not noindex:
            sitemap_urls.append(BASE_URL.rstrip("/") + "/" + path)
        report.append((path or "/", chars, "noindex" if noindex else "index"))

    # sitemap.xml
    urls = "\n".join(
        f"  <url><loc>{u}</loc></url>" for u in sitemap_urls
    )
    with open(os.path.join(PUBLIC_DIR, "sitemap.xml"), "w", encoding="utf-8") as f:
        f.write(
            '<?xml version="1.0" encoding="UTF-8"?>\n'
            '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
            f"{urls}\n</urlset>\n"
        )

    # robots.txt
    with open(os.path.join(PUBLIC_DIR, "robots.txt"), "w", encoding="utf-8") as f:
        f.write(
            "User-agent: *\nAllow: /\n\n"
            f"Sitemap: {BASE_URL.rstrip('/')}/sitemap.xml\n"
        )

    # .nojekyll (GitHub Pages)
    open(os.path.join(PUBLIC_DIR, ".nojekyll"), "w").close()

    width = max(len(p) for p, _, _ in report)
    print(f"{'PATH'.ljust(width)}  CHARS  ROBOTS")
    for p, c, r in sorted(report):
        flag = "" if (r == "noindex" or MIN_INDEX_CHARS <= c <= 2500) else "  ⚠"
        print(f"{p.ljust(width)}  {str(c).rjust(5)}  {r}{flag}")
    print(f"\n{len(report)} pages built, {len(sitemap_urls)} in sitemap.")


if __name__ == "__main__":
    build()
