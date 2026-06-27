# 수도권(서울·경기·인천) 출장마사지 사이트 공통 설정

BASE_URL = "https://ansan-massage1.pages.dev"

BRAND = "토끼24 마사지"
PHONE = "0508-202-4719"
PHONE_DISPLAY = "0508-202-4719"

# 상단 메뉴 — 지시서 4장: 키워드 반복 없이 짧고 명확하게.
NAV = [
    ("수도권 홈", "/", []),
    ("지역 선택", "/find/", [
        ("서울에서 찾기", "/find/seoul/"),
        ("경기에서 찾기", "/find/gyeonggi/"),
        ("인천에서 찾기", "/find/incheon/"),
        ("지하철역 기준", "/find/station/"),
        ("생활권 기준", "/find/life/"),
        ("숙소 기준", "/find/lodging/"),
        ("외곽 지역 기준", "/find/outer/"),
    ]),
    ("이용 상황", "/use/", [
        ("자택 이용", "/use/home/"),
        ("호텔·숙소 이용", "/use/hotel/"),
        ("오피스텔 이용", "/use/officetel/"),
        ("업무지구 이용", "/use/business-district/"),
        ("역세권 이용", "/use/station-area/"),
        ("야간 예약", "/use/night/"),
        ("외곽 지역 이용", "/use/outer-area/"),
        ("공항·도서 이용", "/use/airport-island/"),
    ]),
    ("서울", "/seoul/", [
        ("강남역·역삼", "/seoul/life/gangnam-yeoksam/"),
        ("잠실·송파", "/seoul/life/jamsil-songpa/"),
        ("홍대·합정", "/seoul/life/hongdae-hapjeong/"),
        ("여의도·영등포", "/seoul/life/yeouido-yeongdeungpo/"),
        ("성수·왕십리", "/seoul/life/seongsu-wangsimni/"),
        ("용산·서울역", "/seoul/life/yongsan-seoulstation/"),
    ]),
    ("경기", "/gyeonggi/", [
        ("수원역·인계동", "/gyeonggi/life/suwon-station-ingye/"),
        ("분당·판교", "/gyeonggi/life/bundang-pangyo/"),
        ("동탄신도시", "/gyeonggi/life/dongtan/"),
        ("부천역·상동", "/gyeonggi/life/bucheon-station-sangdong/"),
        ("일산·킨텍스", "/gyeonggi/life/ilsan-kintex/"),
        ("안산 전지역", "/gyeonggi/ansan/"),
    ]),
    ("인천", "/incheon/", [
        ("송도국제도시", "/incheon/life/songdo-international-city/"),
        ("구월·인천시청", "/incheon/life/guwol-cityhall/"),
        ("부평역·부평시장", "/incheon/life/bupyeong-market/"),
        ("청라국제도시", "/incheon/life/cheongna-international-city/"),
        ("검단신도시", "/incheon/life/geomdan-new-city/"),
        ("인천공항", "/incheon/life/incheon-airport/"),
    ]),
    ("지하철역", "/find/station/", []),
    ("예약 전 확인", "/check/", []),
    ("문의하기", "/policy/contact/", []),
]
