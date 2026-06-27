# 수도권(서울·경기·인천) 출장마사지 — 신규 사이트 구조
# 지시서 기준: 지역 선택기 + 이용 상황 매칭형. 본문은 content/bodies/<slug>.html 오버레이로 채운다.
# (메인 페이지만 인라인 본문을 가진다.)
import json
from .site import BRAND, BASE_URL, PHONE

_BASE = BASE_URL.rstrip("/")


def P(path, title, desc, h1, crumbs, body="", hero="", extra_head=""):
    page = {
        "path": path,
        "title": title,
        "desc": desc,
        "h1": h1,
        "breadcrumb": crumbs,
        "body": body,
    }
    if hero:
        page["hero"] = hero
    if extra_head:
        page["extra_head"] = extra_head
    return page


# ───────────────────────── 메인 (/) ─────────────────────────
_MAIN_FAQ = [
    ("수도권 출장마사지는 어떤 서비스인가요?",
     "고객이 계신 자택, 호텔·숙소, 오피스텔 등으로 전문 관리사가 방문하는 방문형 관리 서비스입니다. 서울·경기·인천 수도권 주요 생활권으로 방문 가능합니다."),
    ("서울·경기·인천은 예약 기준이 어떻게 다른가요?",
     "서울은 지하철역과 생활권 중심, 경기는 시·군과 차량 이동 기준, 인천은 원도심·신도시·공항·도서 지역이 섞여 방문 가능 여부를 먼저 확인하는 것이 중요합니다."),
    ("예약 전 무엇을 확인해야 하나요?",
     "방문 주소와 건물 출입 방식, 예약 가능 시간, 추가 이동비, 개인정보 처리 기준, 불법·선정적 서비스 불가 안내를 먼저 확인하시는 것이 좋습니다."),
    ("외곽이나 공항·도서 지역도 방문이 가능한가요?",
     "경기 외곽, 인천 강화·옹진, 공항 인접 지역은 도심과 기준이 다릅니다. 차량 이동 가능 여부와 추가 이동비, 사전 예약 가능 시간을 먼저 확인해 안내드립니다."),
]
_MAIN_FAQ_SCHEMA = {
    "@context": "https://schema.org",
    "@type": "FAQPage",
    "mainEntity": [
        {"@type": "Question", "name": q,
         "acceptedAnswer": {"@type": "Answer", "text": a}}
        for q, a in _MAIN_FAQ
    ],
}
_MAIN_EXTRA_HEAD = (
    '<script type="application/ld+json">\n'
    + json.dumps(_MAIN_FAQ_SCHEMA, ensure_ascii=False, indent=2)
    + "\n</script>"
)

_MAIN_HERO = """<div class="hero">
  <div class="hero-content">
    <div class="hero-badge">서울 · 경기 · 인천 수도권 방문 관리</div>
    <h1 class="hero-title">서울·경기·인천 출장마사지<br><span class="hero-accent">수도권 홈타이</span><br>지역 선택 안내</h1>
    <p class="hero-lead">서울, 경기, 인천 주요 생활권별 방문 가능 지역과 자택·호텔·오피스텔·업무지구·외곽 지역 이용 기준을 안내합니다. 지역명보다 이용 상황을 먼저 선택하세요.</p>
    <div class="hero-cta">
      <a href="/find/" class="btn btn-primary">지역 선택</a>
      <a href="/use/" class="btn btn-secondary">이용 상황</a>
      <a href="/seoul/" class="btn btn-secondary">서울 보기</a>
      <a href="/gyeonggi/" class="btn btn-secondary">경기 보기</a>
      <a href="/incheon/" class="btn btn-secondary">인천 보기</a>
      <a href="/check/" class="btn btn-secondary">예약 전 확인</a>
    </div>
  </div>
  <div class="hero-stats">
    <div class="stat"><div class="stat-number">3</div><div class="stat-label">서울·경기·인천</div></div>
    <div class="stat"><div class="stat-number">8</div><div class="stat-label">이용 상황별</div></div>
    <div class="stat"><div class="stat-number">24</div><div class="stat-label">대표 생활권</div></div>
    <div class="stat"><div class="stat-number">24H</div><div class="stat-label">상담 가능</div></div>
  </div>
</div>"""

_MAIN_BODY = """
<section id="situation">
  <h2>수도권 출장마사지는 이용 상황에 따라 확인 기준이 다릅니다</h2>
  <p>서울, 경기, 인천은 같은 수도권이라도 예약 기준이 다릅니다. 서울은 지하철역과 생활권 중심이고, 경기는 시·군이 넓어 차량 이동 기준이 중요하며, 인천은 원도심·신도시·공항·도서 지역이 함께 있어 방문 가능 여부를 먼저 확인해야 합니다.</p>
  <p>그래서 이 사이트는 지역명을 나열하기보다 <a href="/use/">이용 상황</a>과 방문 가능 기준을 먼저 안내합니다. 어디에서(자택·호텔·오피스텔·업무지구·외곽), 어떤 시간에 이용하실지 정한 뒤 <a href="/find/">지역 선택</a>에서 본인 위치에 맞는 페이지로 이동하시면 예약이 한결 수월합니다.</p>
</section>

<section id="use-cases">
  <h2>이용 장소별 확인사항</h2>
  <div class="card-grid">
    <a href="/use/home/" class="card"><h3>자택</h3><p>주소와 공동현관, 주차 가능 여부를 확인합니다.</p></a>
    <a href="/use/hotel/" class="card"><h3>호텔·숙소</h3><p>숙소 정책과 객실 방문 가능 여부를 확인합니다.</p></a>
    <a href="/use/officetel/" class="card"><h3>오피스텔</h3><p>건물 출입 방식과 관리 규정을 확인합니다.</p></a>
    <a href="/use/business-district/" class="card"><h3>업무지구</h3><p>예약 시간과 건물 출입 기준을 확인합니다.</p></a>
    <a href="/use/station-area/" class="card"><h3>역세권</h3><p>역 주변 방문 주소와 이동 동선을 확인합니다.</p></a>
    <a href="/use/night/" class="card"><h3>야간</h3><p>야간 방문 가능 시간과 출입 방식을 확인합니다.</p></a>
    <a href="/use/outer-area/" class="card"><h3>외곽</h3><p>차량 이동 가능 여부와 추가 이동비를 확인합니다.</p></a>
    <a href="/use/airport-island/" class="card"><h3>공항·도서</h3><p>사전 예약 가능 여부와 이동 시간을 확인합니다.</p></a>
  </div>
</section>

<section id="regions">
  <h2>서울·경기·인천 지역별 안내</h2>
  <p>수도권은 행정구역만 보면 가까워 보여도 실제 방문 동선과 예약 기준은 지역마다 다릅니다. 서울은 지하철 노선이 촘촘해 강남역·잠실역·홍대입구역처럼 역과 생활권을 함께 보면 위치를 빠르게 좁힐 수 있고, 경기는 시·군 면적이 넓어 분당·동탄·일산처럼 신도시와 차량 이동 기준이 중요합니다. 인천은 송도·청라·검단 같은 신도시와 부평·구월 같은 원도심, 그리고 영종·공항권이 함께 있어 방문 가능 여부를 먼저 확인하는 편이 좋습니다.</p>
  <div class="card-grid">
    <a href="/seoul/" class="card"><h3>서울</h3><p>강남, 잠실, 홍대, 여의도, 성수, 용산 등 생활권 중심<span class="card-arrow">→</span></p></a>
    <a href="/gyeonggi/" class="card"><h3>경기</h3><p>수원, 분당, 부천, 일산, 동탄, 안산 등 시·군·신도시 중심<span class="card-arrow">→</span></p></a>
    <a href="/incheon/" class="card"><h3>인천</h3><p>송도, 부평, 구월, 청라, 검단, 공항권 중심<span class="card-arrow">→</span></p></a>
  </div>
  <p class="notice">지역 기준으로 바로 찾으시려면 <a href="/find/seoul/">서울에서 찾기</a>, <a href="/find/gyeonggi/">경기에서 찾기</a>, <a href="/find/incheon/">인천에서 찾기</a>, 또는 <a href="/find/station/">지하철역 기준</a>을 이용하세요.</p>
</section>

<section id="life-areas">
  <h2>수도권 주요 생활권</h2>
  <p>아래는 수도권에서 출장마사지·홈타이 방문 수요가 많은 대표 생활권입니다. 같은 동이라도 어느 역·상권에 가까운지에 따라 분위기와 방문 동선이 달라지므로, 생활권 단위로 보면 방문 주소와 이동 시간을 더 정확하게 맞출 수 있습니다. 각 생활권 페이지에서 포함 지역, 가까운 역, 이용 장소별 확인사항과 예약 전 체크리스트를 확인하세요. 경기 안산 전지역은 별도 허브에서 상록구·단원구 생활권까지 상세히 안내합니다.</p>
  <h3>서울</h3>
  <ul>
    <li><a href="/seoul/life/gangnam-yeoksam/">강남역·역삼</a></li>
    <li><a href="/seoul/life/jamsil-songpa/">잠실·송파</a></li>
    <li><a href="/seoul/life/hongdae-hapjeong/">홍대·합정</a></li>
    <li><a href="/seoul/life/yeouido-yeongdeungpo/">여의도·영등포</a></li>
    <li><a href="/seoul/life/seongsu-wangsimni/">성수·왕십리</a></li>
    <li><a href="/seoul/life/yongsan-seoulstation/">용산·서울역</a></li>
  </ul>
  <h3>경기</h3>
  <ul>
    <li><a href="/gyeonggi/life/suwon-station-ingye/">수원역·인계동</a></li>
    <li><a href="/gyeonggi/life/bundang-pangyo/">분당·판교</a></li>
    <li><a href="/gyeonggi/life/dongtan/">동탄신도시</a></li>
    <li><a href="/gyeonggi/life/bucheon-station-sangdong/">부천역·상동</a></li>
    <li><a href="/gyeonggi/life/ilsan-kintex/">일산·킨텍스</a></li>
    <li><a href="/gyeonggi/ansan/">안산 전지역</a></li>
  </ul>
  <h3>인천</h3>
  <ul>
    <li><a href="/incheon/life/songdo-international-city/">송도국제도시</a></li>
    <li><a href="/incheon/life/guwol-cityhall/">구월·인천시청</a></li>
    <li><a href="/incheon/life/bupyeong-market/">부평역·부평시장</a></li>
    <li><a href="/incheon/life/cheongna-international-city/">청라국제도시</a></li>
    <li><a href="/incheon/life/geomdan-new-city/">검단신도시</a></li>
    <li><a href="/incheon/life/incheon-airport/">인천공항</a></li>
  </ul>
</section>

<section id="checklist">
  <h2>예약 전 반드시 확인할 내용</h2>
  <ul>
    <li><a href="/check/address/">방문 주소</a>를 정확히 확인했나요?</li>
    <li><a href="/check/entry/">공동현관 또는 건물 출입 방식</a>이 있나요?</li>
    <li>호텔·숙소·오피스텔 이용 가능 여부를 확인했나요?</li>
    <li><a href="/check/transfer-fee/">외곽 지역 추가 이동비</a>가 있나요?</li>
    <li><a href="/check/available-time/">예약 가능 시간</a>과 <a href="/check/change-policy/">변경·취소 기준</a>을 확인했나요?</li>
    <li><a href="/check/privacy/">개인정보 처리 기준</a>을 확인했나요?</li>
    <li><a href="/check/illegal-notice/">불법·선정적 서비스 불가 안내</a>를 확인했나요?</li>
  </ul>
</section>

<section id="faq">
  <h2>수도권 출장마사지 자주 묻는 질문</h2>
  <dl class="faq-list">
    <dt id="faq-1">수도권 출장마사지는 어떤 서비스인가요?</dt>
    <dd>고객이 계신 자택, 호텔·숙소, 오피스텔 등으로 전문 관리사가 방문하는 방문형 관리 서비스입니다. 서울·경기·인천 수도권 주요 생활권으로 방문 가능합니다.</dd>
    <dt id="faq-2">서울·경기·인천은 예약 기준이 어떻게 다른가요?</dt>
    <dd>서울은 지하철역과 생활권 중심, 경기는 시·군과 차량 이동 기준, 인천은 원도심·신도시·공항·도서 지역이 섞여 방문 가능 여부를 먼저 확인하는 것이 중요합니다.</dd>
    <dt id="faq-3">예약 전 무엇을 확인해야 하나요?</dt>
    <dd>방문 주소와 건물 출입 방식, 예약 가능 시간, 추가 이동비, 개인정보 처리 기준, 불법·선정적 서비스 불가 안내를 먼저 확인하시는 것이 좋습니다.</dd>
    <dt id="faq-4">외곽이나 공항·도서 지역도 방문이 가능한가요?</dt>
    <dd>경기 외곽, 인천 강화·옹진, 공항 인접 지역은 도심과 기준이 다릅니다. 차량 이동 가능 여부와 추가 이동비, 사전 예약 가능 시간을 먼저 확인해 안내드립니다.</dd>
  </dl>
</section>
"""

MAIN = P(
    path="",
    title="서울·경기·인천 출장마사지｜수도권 지역별 홈타이 예약 전 확인 안내",
    desc="서울·경기·인천 출장마사지·홈타이 예약 전 강남, 수원, 송도 등 수도권 생활권을 확인하세요.",
    h1="서울·경기·인천 출장마사지 · 수도권 지역 선택 안내",
    crumbs=[],
    body=_MAIN_BODY,
    hero=_MAIN_HERO,
    extra_head=_MAIN_EXTRA_HEAD,
)


# ───────────────────────── 지역 선택 /find/ ─────────────────────────
_find_hub = P("find/", "수도권 출장마사지 지역 선택｜서울·경기·인천 방문 지역 찾기",
    "수도권 출장마사지 지역 선택. 서울·경기·인천 방문 가능 지역을 찾아보세요.",
    "수도권 방문 가능 지역 선택", [("지역 선택", "")])
_finders = [
    P("find/seoul/", "서울에서 찾기｜서울 출장마사지 방문 지역 선택",
      "서울에서 출장마사지 방문 가능 지역 찾기. 강남, 잠실, 홍대 등 생활권 안내.",
      "서울에서 출장마사지 방문 지역 찾기", [("지역 선택", "/find/"), ("서울에서 찾기", "")]),
    P("find/gyeonggi/", "경기에서 찾기｜경기 출장마사지 방문 지역 선택",
      "경기에서 출장마사지 방문 가능 지역 찾기. 수원, 분당, 일산, 부천 등 안내.",
      "경기에서 출장마사지 방문 지역 찾기", [("지역 선택", "/find/"), ("경기에서 찾기", "")]),
    P("find/incheon/", "인천에서 찾기｜인천 출장마사지 방문 지역 선택",
      "인천에서 출장마사지 방문 가능 지역 찾기. 송도, 부평, 청라, 검단 등 안내.",
      "인천에서 출장마사지 방문 지역 찾기", [("지역 선택", "/find/"), ("인천에서 찾기", "")]),
    P("find/station/", "지하철역 기준 찾기｜수도권 역세권 출장마사지",
      "수도권 지하철역 기준 출장마사지 찾기. 강남역, 수원역, 부평역 등 역세권 안내.",
      "지하철역 기준 출장마사지 찾기", [("지역 선택", "/find/"), ("지하철역 기준", "")]),
    P("find/life/", "생활권 기준 찾기｜수도권 생활권 출장마사지",
      "수도권 생활권 기준 출장마사지 찾기. 도심·신도시·역세권 생활권 안내.",
      "생활권 기준 출장마사지 찾기", [("지역 선택", "/find/"), ("생활권 기준", "")]),
    P("find/lodging/", "숙소 기준 찾기｜호텔·오피스텔 출장마사지",
      "숙소 기준 출장마사지 찾기. 호텔·오피스텔·자택 방문 가능 여부를 확인하세요.",
      "숙소 기준 출장마사지 찾기", [("지역 선택", "/find/"), ("숙소 기준", "")]),
    P("find/outer/", "외곽 지역 기준 찾기｜수도권 외곽 출장마사지",
      "수도권 외곽 지역 출장마사지 찾기. 차량 이동·추가 이동비를 먼저 확인하세요.",
      "외곽 지역 기준 출장마사지 찾기", [("지역 선택", "/find/"), ("외곽 지역 기준", "")]),
]


# ───────────────────────── 이용 상황 /use/ ─────────────────────────
_use_hub = P("use/", "출장마사지 이용 상황별 안내｜자택·호텔·오피스텔·업무지구",
    "출장마사지 이용 상황별 안내. 자택·호텔·오피스텔·업무지구 기준을 확인하세요.",
    "이용 상황별 예약 전 확인사항", [("이용 상황", "")])
_uses = [
    P("use/home/", "자택 출장마사지｜자택 홈타이 예약 안내",
      "자택 출장마사지 안내. 주소·공동현관·주차·예약 가능 시간을 확인하세요.",
      "자택 이용 출장마사지 안내", [("이용 상황", "/use/"), ("자택 이용", "")]),
    P("use/hotel/", "호텔·숙소 출장마사지｜숙소 홈타이 예약 안내",
      "호텔·숙소 출장마사지 안내. 숙소 정책과 방문 가능 여부를 확인하세요.",
      "호텔·숙소 이용 출장마사지 안내", [("이용 상황", "/use/"), ("호텔·숙소 이용", "")]),
    P("use/officetel/", "오피스텔 출장마사지｜오피스텔 홈타이 예약 안내",
      "오피스텔 출장마사지 안내. 건물 출입 방식과 관리 규정을 확인하세요.",
      "오피스텔 이용 출장마사지 안내", [("이용 상황", "/use/"), ("오피스텔 이용", "")]),
    P("use/business-district/", "업무지구 출장마사지｜오피스 밀집지 홈타이 안내",
      "업무지구 출장마사지 안내. 예약 시간과 건물 출입 기준을 확인하세요.",
      "업무지구 이용 출장마사지 안내", [("이용 상황", "/use/"), ("업무지구 이용", "")]),
    P("use/station-area/", "역세권 출장마사지｜지하철역 인근 홈타이 안내",
      "역세권 출장마사지 안내. 역 주변 방문 주소와 이동 동선을 확인하세요.",
      "역세권 이용 출장마사지 안내", [("이용 상황", "/use/"), ("역세권 이용", "")]),
    P("use/night/", "야간 출장마사지｜야간 예약 홈타이 안내",
      "야간 출장마사지 예약 안내. 야간 방문 가능 시간과 출입 방식을 확인하세요.",
      "야간 예약 출장마사지 안내", [("이용 상황", "/use/"), ("야간 예약", "")]),
    P("use/outer-area/", "외곽 지역 출장마사지｜수도권 외곽 홈타이 안내",
      "외곽 지역 출장마사지 안내. 차량 이동 가능 여부와 추가 이동비를 확인하세요.",
      "외곽 지역 이용 출장마사지 안내", [("이용 상황", "/use/"), ("외곽 지역 이용", "")]),
    P("use/airport-island/", "공항·도서 지역 출장마사지｜공항권 홈타이 안내",
      "공항·도서 지역 출장마사지 안내. 사전 예약 가능 여부와 이동 시간을 확인하세요.",
      "공항·도서 지역 이용 출장마사지 안내", [("이용 상황", "/use/"), ("공항·도서 이용", "")]),
]


# ───────────────────────── 예약 전 확인 /check/ ─────────────────────────
_check_hub = P("check/", "출장마사지 예약 전 확인사항｜방문 전 체크리스트",
    "출장마사지 예약 전 확인사항. 방문 주소·출입·이동비·시간을 확인하세요.",
    "예약 전 확인사항", [("예약 전 확인", "")])
_checks = [
    P("check/address/", "방문 주소 확인｜출장마사지 예약 전 안내",
      "방문 주소 확인 안내. 정확한 주소와 건물 유형을 예약 전 확인하세요.",
      "방문 주소 확인", [("예약 전 확인", "/check/"), ("방문 주소 확인", "")]),
    P("check/entry/", "건물 출입 방식 확인｜출장마사지 예약 전 안내",
      "건물 출입 방식 확인. 공동현관·자동문·경비 출입을 예약 전 확인하세요.",
      "건물 출입 방식 확인", [("예약 전 확인", "/check/"), ("건물 출입 방식", "")]),
    P("check/transfer-fee/", "추가 이동비 확인｜출장마사지 예약 전 안내",
      "추가 이동비 확인 안내. 기본 이동권과 외곽 추가 이동비를 확인하세요.",
      "추가 이동비 확인", [("예약 전 확인", "/check/"), ("추가 이동비 확인", "")]),
    P("check/available-time/", "예약 가능 시간 확인｜출장마사지 예약 전 안내",
      "예약 가능 시간 확인. 희망 시간대 방문 가능 여부를 미리 확인하세요.",
      "예약 가능 시간 확인", [("예약 전 확인", "/check/"), ("예약 가능 시간", "")]),
    P("check/change-policy/", "예약 변경·취소 기준｜출장마사지 예약 전 안내",
      "예약 변경·취소 기준 안내. 변경·취소 절차와 기준을 확인하세요.",
      "예약 변경·취소 기준", [("예약 전 확인", "/check/"), ("예약 변경 기준", "")]),
    P("check/privacy/", "개인정보 처리 기준｜출장마사지 예약 전 안내",
      "개인정보 처리 기준 안내. 예약 시 수집·이용·보관 방식을 확인하세요.",
      "개인정보 처리 기준", [("예약 전 확인", "/check/"), ("개인정보 처리 기준", "")]),
    P("check/illegal-notice/", "불법·선정적 서비스 불가 안내｜건전한 방문 관리",
      "불법·선정적 서비스 불가 안내. 건전한 방문 관리 서비스만 제공합니다.",
      "불법·선정적 서비스 불가 안내", [("예약 전 확인", "/check/"), ("불법·선정적 불가", "")]),
]


# ───────────────────────── 운영 기준 /policy/ ─────────────────────────
_policy_hub = P("policy/", "토끼24 마사지 운영 기준｜정책 안내",
    "토끼24 마사지 운영 기준. 개인정보·유의사항·콘텐츠 품질 기준을 안내합니다.",
    "운영 기준 안내", [("운영 기준", "")])
_policies = [
    P("policy/privacy/", "개인정보처리방침｜토끼24 마사지",
      "개인정보처리방침. 개인정보 수집·이용·보관·보호 정책을 안내합니다.",
      "개인정보처리방침", [("운영 기준", "/policy/"), ("개인정보처리방침", "")]),
    P("policy/terms/", "고객 유의사항｜토끼24 마사지 이용 기준",
      "고객 유의사항. 건전한 방문 관리 서비스 이용 기준을 안내합니다.",
      "고객 유의사항", [("운영 기준", "/policy/"), ("고객 유의사항", "")]),
    P("policy/content-quality/", "콘텐츠 품질 기준｜토끼24 마사지",
      "콘텐츠 품질 기준. 정확하고 도움되는 지역 정보 제공 원칙을 안내합니다.",
      "콘텐츠 품질 기준", [("운영 기준", "/policy/"), ("콘텐츠 품질 기준", "")]),
    P("policy/contact/", "문의하기｜토끼24 마사지 예약·제휴 문의",
      "토끼24 마사지 문의하기. 예약·제휴·웹사이트 제작 문의를 안내합니다.",
      "문의하기", [("운영 기준", "/policy/"), ("문의하기", "")]),
]


# ───────────────────────── 서울·경기·인천 허브 ─────────────────────────
_region_hubs = [
    P("seoul/", "서울 출장마사지｜강남·잠실·홍대·여의도 생활권 안내",
      "서울 출장마사지·홈타이 예약 전 강남, 잠실, 홍대, 여의도 등 생활권을 확인하세요.",
      "서울 출장마사지 · 생활권별 방문 안내", [("서울", "")]),
    P("gyeonggi/", "경기 출장마사지｜수원·분당·일산·부천·안산 생활권 안내",
      "경기 출장마사지·홈타이 예약 전 수원, 분당, 일산, 부천, 안산 등 생활권을 확인하세요.",
      "경기 출장마사지 · 시·군별 생활권 안내", [("경기", "")]),
    P("incheon/", "인천 출장마사지｜송도·부평·구월·청라·검단 생활권 안내",
      "인천 출장마사지·홈타이 예약 전 송도, 부평, 구월, 청라, 검단 등 생활권을 확인하세요.",
      "인천 출장마사지 · 구·군별 생활권 안내", [("인천", "")]),
]


# ───────────────────────── 대표 생활권 24 ─────────────────────────
def _life(region_label, region_path, slug, name, desc):
    return P(
        f"{region_path}life/{slug}/",
        f"{name} 출장마사지｜{region_label} 생활권 홈타이 안내",
        desc,
        f"{name} 출장마사지·홈타이 안내",
        [(region_label, f"/{region_path}"), (name, "")],
    )


_life_pages = [
    # 서울 8
    _life("서울", "seoul/", "gangnam-yeoksam", "강남역·역삼", "강남역·역삼 출장마사지·홈타이 예약 전 생활권과 이용 기준을 확인하세요."),
    _life("서울", "seoul/", "jamsil-songpa", "잠실·송파", "잠실·송파 출장마사지·홈타이 예약 전 생활권과 이용 기준을 확인하세요."),
    _life("서울", "seoul/", "hongdae-hapjeong", "홍대·합정", "홍대·합정 출장마사지·홈타이 예약 전 생활권과 이용 기준을 확인하세요."),
    _life("서울", "seoul/", "yeouido-yeongdeungpo", "여의도·영등포", "여의도·영등포 출장마사지·홈타이 예약 전 생활권과 이용 기준을 확인하세요."),
    _life("서울", "seoul/", "seongsu-wangsimni", "성수·왕십리", "성수·왕십리 출장마사지·홈타이 예약 전 생활권과 이용 기준을 확인하세요."),
    _life("서울", "seoul/", "yongsan-seoulstation", "용산·서울역", "용산·서울역 출장마사지·홈타이 예약 전 생활권과 이용 기준을 확인하세요."),
    _life("서울", "seoul/", "mokdong-yangcheon", "목동·양천", "목동·양천 출장마사지·홈타이 예약 전 생활권과 이용 기준을 확인하세요."),
    _life("서울", "seoul/", "nowon-sanggye", "노원·상계", "노원·상계 출장마사지·홈타이 예약 전 생활권과 이용 기준을 확인하세요."),
    # 경기 8
    _life("경기", "gyeonggi/", "suwon-station-ingye", "수원역·인계동", "수원역·인계동 출장마사지·홈타이 예약 전 생활권과 이용 기준을 확인하세요."),
    _life("경기", "gyeonggi/", "bundang-pangyo", "분당·판교", "분당·판교 출장마사지·홈타이 예약 전 생활권과 이용 기준을 확인하세요."),
    _life("경기", "gyeonggi/", "jukjeon-suji", "죽전·수지", "죽전·수지 출장마사지·홈타이 예약 전 생활권과 이용 기준을 확인하세요."),
    _life("경기", "gyeonggi/", "dongtan", "동탄신도시", "동탄신도시 출장마사지·홈타이 예약 전 생활권과 이용 기준을 확인하세요."),
    _life("경기", "gyeonggi/", "bucheon-station-sangdong", "부천역·상동", "부천역·상동 출장마사지·홈타이 예약 전 생활권과 이용 기준을 확인하세요."),
    _life("경기", "gyeonggi/", "ilsan-kintex", "일산·킨텍스", "일산·킨텍스 출장마사지·홈타이 예약 전 생활권과 이용 기준을 확인하세요."),
    _life("경기", "gyeonggi/", "uijeongbu-millak", "의정부역·민락", "의정부역·민락 출장마사지·홈타이 예약 전 생활권과 이용 기준을 확인하세요."),
    _life("경기", "gyeonggi/", "hanam-misa", "하남·미사", "하남·미사 출장마사지·홈타이 예약 전 생활권과 이용 기준을 확인하세요."),
    # 인천 8
    _life("인천", "incheon/", "songdo-international-city", "송도국제도시", "송도국제도시 출장마사지·홈타이 예약 전 생활권과 이용 기준을 확인하세요."),
    _life("인천", "incheon/", "guwol-cityhall", "구월·인천시청", "구월·인천시청 출장마사지·홈타이 예약 전 생활권과 이용 기준을 확인하세요."),
    _life("인천", "incheon/", "bupyeong-market", "부평역·부평시장", "부평역·부평시장 출장마사지·홈타이 예약 전 생활권과 이용 기준을 확인하세요."),
    _life("인천", "incheon/", "juan-dohwa", "주안·도화", "주안·도화 출장마사지·홈타이 예약 전 생활권과 이용 기준을 확인하세요."),
    _life("인천", "incheon/", "cheongna-international-city", "청라국제도시", "청라국제도시 출장마사지·홈타이 예약 전 생활권과 이용 기준을 확인하세요."),
    _life("인천", "incheon/", "geomdan-new-city", "검단신도시", "검단신도시 출장마사지·홈타이 예약 전 생활권과 이용 기준을 확인하세요."),
    _life("인천", "incheon/", "yeongjong-unseo", "영종·운서", "영종·운서 출장마사지·홈타이 예약 전 생활권과 이용 기준을 확인하세요."),
    _life("인천", "incheon/", "incheon-airport", "인천공항", "인천공항 출장마사지·홈타이 예약 전 생활권과 이용 기준을 확인하세요."),
]


PAGES = (
    [MAIN]
    + [_find_hub] + _finders
    + [_use_hub] + _uses
    + [_check_hub] + _checks
    + [_policy_hub] + _policies
    + _region_hubs
    + _life_pages
)
