import os
import re

from . import main, areas, stations, areas_and_stations, info, hubs, sudogwon, sd_seoul

# 안산 확장 본문은 수도권 본문과 슬러그가 겹치지 않도록 bodies/ansan/ 에 둔다.
_BODIES = os.path.join(os.path.dirname(__file__), "bodies", "ansan")

# 안산 페이지를 경기 하위(/gyeonggi/ansan/)로 재배치(rehome)한다.
# 소스 모듈은 그대로 두고, 조립 시점에 경로·내부링크·브레드크럼만 변환한다.
_ANSAN_PREFIX = "gyeonggi/ansan/"
# 안산 내부 링크로 인식해 접두어를 붙일 최상위 경로들.
_ANSAN_ROOTS = ("danwon-gu", "sangnok-gu", "station", "area",
                "reservation", "check", "guide", "support")


def _prefix_links(html_str: str, prefix: str) -> str:
    html_str = re.sub(
        r'href="/(' + "|".join(_ANSAN_ROOTS) + r')(/|")',
        r'href="/' + prefix + r"\1\2",
        html_str,
    )
    # 홈 링크("/")는 안산 허브로 연결한다.
    html_str = re.sub(r'href="/"', 'href="/' + prefix + '"', html_str)
    return html_str


def _rehome(page: dict, prefix: str = _ANSAN_PREFIX) -> dict:
    p = dict(page)
    old = p["path"]
    p["path"] = prefix + old

    # 확장 본문 파일이 있으면 인라인으로 끌어와 링크까지 변환한다.
    old_slug = old.rstrip("/").replace("/", "__")
    body = p.get("body", "")
    fp = os.path.join(_BODIES, old_slug + ".html")
    if old and os.path.exists(fp):
        with open(fp, encoding="utf-8") as f:
            body = f.read()
    p["body"] = _prefix_links(body, prefix)
    if p.get("hero"):
        p["hero"] = _prefix_links(p["hero"], prefix)

    # 브레드크럼: 수도권 > 경기 > 안산 을 앞에 둔다.
    crumbs = page.get("breadcrumb") or []
    if old == "":
        p["breadcrumb"] = [("수도권", "/"), ("경기", "/gyeonggi/"), ("안산", "")]
    else:
        rest = crumbs[1:] if crumbs else []
        new_cr = [("수도권", "/"), ("경기", "/gyeonggi/"), ("안산", "/" + prefix)]
        for label, href in rest:
            if href and href.startswith("/"):
                href = "/" + prefix + href.lstrip("/")
            new_cr.append((label, href))
        p["breadcrumb"] = new_cr
    return p


_ansan_pages = (
    [main.PAGE]
    + areas.PAGES
    + stations.PAGES
    + areas_and_stations.PAGES
    + info.PAGES
    + hubs.PAGES
)

PAGES = sudogwon.PAGES + sd_seoul.PAGES + [_rehome(p) for p in _ansan_pages]
