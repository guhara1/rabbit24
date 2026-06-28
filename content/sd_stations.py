# 수도권 핵심 역세권 페이지 (1차-C). 지역 하위에 둔다: /seoul|gyeonggi|incheon/station/<slug>/
# 역명 기준 1개 URL(출구·노선별 분리 없음).
from .sudogwon import P
from .titles import make_title, make_desc

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
    # 2차 확장
    ("sinchon-station", "seoul/", "서울", "신촌역", "신촌·연희·대학가"),
    ("wangsimni-station", "seoul/", "서울", "왕십리역", "왕십리·성수·행당"),
    ("suseo-station", "seoul/", "서울", "수서역", "수서·일원·강남 동남부"),
    ("cheonho-station", "seoul/", "서울", "천호역", "천호·길동·강동"),
    ("yeongdeungpo-station", "seoul/", "서울", "영등포역", "영등포·신길·당산"),
    ("guro-digital-station", "seoul/", "서울", "구로디지털단지역", "구디·대림·신대방"),
    ("jeongja-station", "gyeonggi/", "경기", "정자역", "정자·분당·판교"),
    ("indeogwon-station", "gyeonggi/", "경기", "인덕원역", "인덕원·평촌·의왕"),
    ("uijeongbu-station", "gyeonggi/", "경기", "의정부역", "의정부·민락·녹양"),
    ("sanbon-station", "gyeonggi/", "경기", "산본역", "산본·금정·군포"),
    ("anyang-station", "gyeonggi/", "경기", "안양역", "안양·만안·박달"),
    ("gwangmyeong-station", "gyeonggi/", "경기", "광명역", "광명역·소하·일직"),
    ("jakjeon-station", "incheon/", "인천", "작전역", "작전·계산·계양"),
    ("dongincheon-station", "incheon/", "인천", "동인천역", "동인천·신포·원도심"),
    ("incheon-nonhyeon-station", "incheon/", "인천", "인천논현역", "논현·소래·남동"),
    ("geomam-station", "incheon/", "인천", "검암역", "검암·청라·서구"),
    # 3차 확장
    ("seolleung-station", "seoul/", "서울", "선릉역", "선릉·역삼·테헤란로"),
    ("gangbyeon-station", "seoul/", "서울", "강변역", "강변·구의·동서울"),
    ("migeum-station", "gyeonggi/", "경기", "미금역", "미금·분당·정자"),
    ("giheung-station", "gyeonggi/", "경기", "기흥역", "기흥·신갈·동백"),
    ("moran-station", "gyeonggi/", "경기", "모란역", "모란·성남·중원"),
    ("central-park-station", "incheon/", "인천", "센트럴파크역", "송도·센트럴파크"),
]

PAGES = [
    P(
        f"{region_path}station/{slug}/",
        make_title(name, f"{region_label} 역세권", f"{region_path}station/{slug}/"),
        make_desc(f"{region_label} {name}", f"{region_path}station/{slug}/"),
        f"{name} 출장마사지·홈타이 안내",
        [(region_label, "/" + region_path), (name, "")],
    )
    for slug, region_path, region_label, name, areas in STATIONS
]
