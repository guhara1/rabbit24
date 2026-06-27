# 수도권 핵심 역세권 페이지 (1차-C). 지역 하위에 둔다: /seoul|gyeonggi|incheon/station/<slug>/
# 역명 기준 1개 URL(출구·노선별 분리 없음).
from .sudogwon import P

# (slug, region_path, region_label, 역명, 대표 생활권)
STATIONS = [
    ("gangnam-station", "seoul/", "서울", "강남역", "강남·역삼·테헤란로"),
    ("jamsil-station", "seoul/", "서울", "잠실역", "잠실·송파·롯데타워"),
    ("hongdae-station", "seoul/", "서울", "홍대입구역", "홍대·합정·연남"),
    ("yeouido-station", "seoul/", "서울", "여의도역", "여의도·영등포"),
    ("seongsu-station", "seoul/", "서울", "성수역", "성수·서울숲"),
    ("konkuk-univ-station", "seoul/", "서울", "건대입구역", "건대·자양·구의"),
    ("sinlim-station", "seoul/", "서울", "신림역", "신림·서울대입구"),
    ("sadang-station", "seoul/", "서울", "사당역", "사당·이수·방배"),
    ("suwon-station", "gyeonggi/", "경기", "수원역", "수원역·매산·인계"),
    ("pangyo-station", "gyeonggi/", "경기", "판교역", "판교·테크노밸리"),
    ("yatap-station", "gyeonggi/", "경기", "야탑역", "야탑·성남·분당"),
    ("dongtan-station", "gyeonggi/", "경기", "동탄역", "동탄신도시"),
    ("bucheon-station", "gyeonggi/", "경기", "부천역", "부천·심곡·상동"),
    ("beomgye-station", "gyeonggi/", "경기", "범계역", "평촌·범계 로데오"),
    ("bupyeong-station", "incheon/", "인천", "부평역", "부평·부평시장"),
    ("juan-station", "incheon/", "인천", "주안역", "주안·미추홀"),
    ("incheon-cityhall-station", "incheon/", "인천", "인천시청역", "구월·인천시청"),
    ("incheon-univ-station", "incheon/", "인천", "인천대입구역", "송도국제도시"),
]

PAGES = [
    P(
        f"{region_path}station/{slug}/",
        f"{name} 출장마사지｜{areas} 역세권 홈타이 안내",
        f"{name} 출장마사지·홈타이 예약 전 {areas} 생활권과 이용 기준을 확인하세요.",
        f"{name} 출장마사지·홈타이 안내",
        [(region_label, "/" + region_path), (name, "")],
    )
    for slug, region_path, region_label, name, areas in STATIONS
]
