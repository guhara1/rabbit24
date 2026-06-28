# 경기 시 → (일반구) → 동 드릴다운. 구가 있는 시는 시>구>동, 없는 시는 시>동.
# 번호동 통합. 핵심 동은 빌드 오버레이로 풍부 본문 색인, 나머지는 자동 noindex(도어웨이 회피).
from .sudogwon import P
from .titles import make_title, make_desc

# 구가 있는 시: city_slug -> (city_name, {gu_slug: (gu_name, [(dong_slug,dong_name)])})
GU_CITIES = {
    "suwon": ("수원", {
        "jangan-gu": ("장안구", [
            ("jeongja-dong", "정자동"), ("yuljeon-dong", "율전동"), ("cheoncheon-dong", "천천동"),
            ("yeonghwa-dong", "영화동"), ("pajang-dong", "파장동"), ("jowon-dong", "조원동"),
            ("yeonmu-dong", "연무동"),
        ]),
        "gwonseon-gu": ("권선구", [
            ("gwonseon-dong", "권선동"), ("seryu-dong", "세류동"), ("seodun-dong", "서둔동"),
            ("guun-dong", "구운동"), ("geumgok-dong", "금곡동"), ("homaesil-dong", "호매실동"),
            ("ipbuk-dong", "입북동"),
        ]),
        "paldal-gu": ("팔달구", [
            ("ingye-dong", "인계동"), ("maesan-dong", "매산동"), ("godeung-dong", "고등동"),
            ("hwaseo-dong", "화서동"), ("ji-dong", "지동"), ("uman-dong", "우만동"),
            ("haenggung-dong", "행궁동"),
        ]),
        "yeongtong-gu": ("영통구", [
            ("yeongtong-dong", "영통동"), ("maetan-dong", "매탄동"), ("woncheon-dong", "원천동"),
            ("gwanggyo-dong", "광교동"), ("mangpo-dong", "망포동"),
        ]),
    }),
    "seongnam": ("성남", {
        "sujeong-gu": ("수정구", [
            ("sinheung-dong", "신흥동"), ("taepyeong-dong", "태평동"), ("sujin-dong", "수진동"),
            ("dandae-dong", "단대동"), ("sanseong-dong", "산성동"), ("bokjeong-dong", "복정동"),
            ("wirye-dong", "위례동"),
        ]),
        "jungwon-gu": ("중원구", [
            ("seongnam-dong", "성남동"), ("geumgwang-dong", "금광동"), ("eunhaeng-dong", "은행동"),
            ("sangdaewon-dong", "상대원동"), ("hadaewon-dong", "하대원동"), ("dochon-dong", "도촌동"),
        ]),
        "bundang-gu": ("분당구", [
            ("seohyeon-dong", "서현동"), ("jeongja-dong", "정자동"), ("yatap-dong", "야탑동"),
            ("imae-dong", "이매동"), ("sunae-dong", "수내동"), ("bundang-dong", "분당동"),
            ("pangyo-dong", "판교동"), ("baekhyeon-dong", "백현동"), ("sampyeong-dong", "삼평동"),
            ("gumi-dong", "구미동"), ("geumgok-dong", "금곡동"),
        ]),
    }),
    "yongin": ("용인", {
        "cheoin-gu": ("처인구", [
            ("gimnyangjang-dong", "김량장동"), ("yeokbuk-dong", "역북동"), ("samga-dong", "삼가동"),
            ("pogok-eup", "포곡읍"), ("mohyeon-eup", "모현읍"), ("namsa-eup", "남사읍"),
        ]),
        "giheung-gu": ("기흥구", [
            ("singal-dong", "신갈동"), ("gugal-dong", "구갈동"), ("sanggal-dong", "상갈동"),
            ("bora-dong", "보라동"), ("dongbaek-dong", "동백동"), ("mabuk-dong", "마북동"),
            ("bojeong-dong", "보정동"), ("yeongdeok-dong", "영덕동"),
        ]),
        "suji-gu": ("수지구", [
            ("pungdeokcheon-dong", "풍덕천동"), ("jukjeon-dong", "죽전동"), ("dongcheon-dong", "동천동"),
            ("sanghyeon-dong", "상현동"), ("seongbok-dong", "성복동"), ("sinbong-dong", "신봉동"),
        ]),
    }),
    "goyang": ("고양", {
        "deogyang-gu": ("덕양구", [
            ("hwajeong-dong", "화정동"), ("haengsin-dong", "행신동"), ("wonheung-dong", "원흥동"),
            ("jichuk-dong", "지축동"), ("jugyo-dong", "주교동"), ("hwajeon-dong", "화전동"),
        ]),
        "ilsandong-gu": ("일산동구", [
            ("jeongbalsan-dong", "정발산동"), ("madu-dong", "마두동"), ("baekseok-dong", "백석동"),
            ("janghang-dong", "장항동"), ("pungsan-dong", "풍산동"), ("siksa-dong", "식사동"),
        ]),
        "ilsanseo-gu": ("일산서구", [
            ("juyeop-dong", "주엽동"), ("daehwa-dong", "대화동"), ("tanhyeon-dong", "탄현동"),
            ("ilsan-dong", "일산동"), ("songsan-dong", "송산동"),
        ]),
    }),
    "anyang": ("안양", {
        "manan-gu": ("만안구", [
            ("anyang-dong", "안양동"), ("bakdal-dong", "박달동"), ("seoksu-dong", "석수동"),
        ]),
        "dongan-gu": ("동안구", [
            ("pyeongchon-dong", "평촌동"), ("bisan-dong", "비산동"), ("gwanyang-dong", "관양동"),
            ("hogye-dong", "호계동"), ("buheung-dong", "부흥동"),
        ]),
    }),
}

# 구가 없는 시: city_slug -> (city_name, [(dong_slug,dong_name)])
CITY_DONGS = {
    "bucheon": ("부천", [
        ("jung-dong", "중동"), ("sang-dong", "상동"), ("simgok-dong", "심곡동"),
        ("wonmi-dong", "원미동"), ("sosa-dong", "소사동"), ("songnae-dong", "송내동"),
        ("yeokgok-dong", "역곡동"), ("ojeong-dong", "오정동"), ("gogang-dong", "고강동"),
    ]),
    "hwaseong": ("화성", [
        ("bansong-dong", "반송동"), ("byeongjeom-dong", "병점동"), ("jinan-dong", "진안동"),
        ("gisan-dong", "기산동"), ("bongdam-eup", "봉담읍"), ("namyang-eup", "남양읍"),
    ]),
    "pyeongtaek": ("평택", [
        ("bijeon-dong", "비전동"), ("seojeong-dong", "서정동"), ("segyo-dong", "세교동"),
        ("dongsak-dong", "동삭동"), ("anjung-eup", "안중읍"), ("paengseong-eup", "팽성읍"),
        ("cheongbuk-eup", "청북읍"),
    ]),
    "siheung": ("시흥", [
        ("jeongwang-dong", "정왕동"), ("baegot-dong", "배곧동"), ("daeya-dong", "대야동"),
        ("sincheon-dong", "신천동"), ("eunhaeng-dong", "은행동"), ("mokgam-dong", "목감동"),
        ("yeonseong-dong", "연성동"),
    ]),
    "gimpo": ("김포", [
        ("gimpo-dong", "김포본동"), ("sau-dong", "사우동"), ("pungmu-dong", "풍무동"),
        ("janggi-dong", "장기동"), ("gurae-dong", "구래동"), ("unyang-dong", "운양동"),
        ("tongjin-eup", "통진읍"), ("gochon-eup", "고촌읍"),
    ]),
    "namyangju": ("남양주", [
        ("dasan-dong", "다산동"), ("byeollae-dong", "별내동"), ("pyeongnae-dong", "평내동"),
        ("hopyeong-dong", "호평동"), ("hwado-eup", "화도읍"), ("jinjeop-eup", "진접읍"),
        ("onam-eup", "오남읍"), ("wabu-eup", "와부읍"),
    ]),
    "paju": ("파주", [
        ("unjeong-dong", "운정동"), ("geumchon-dong", "금촌동"), ("gyoha-dong", "교하동"),
        ("munsan-eup", "문산읍"), ("jori-eup", "조리읍"), ("paju-eup", "파주읍"),
    ]),
    "uijeongbu": ("의정부", [
        ("uijeongbu-dong", "의정부동"), ("howon-dong", "호원동"), ("jangam-dong", "장암동"),
        ("singok-dong", "신곡동"), ("millak-dong", "민락동"), ("ganeung-dong", "가능동"),
        ("nogyang-dong", "녹양동"), ("songsan-dong", "송산동"),
    ]),
    "hanam": ("하남", [
        ("sinjang-dong", "신장동"), ("deokpung-dong", "덕풍동"), ("misa-dong", "미사동"),
        ("pungsan-dong", "풍산동"), ("wirye-dong", "위례동"), ("gamil-dong", "감일동"),
    ]),
    "gwangmyeong": ("광명", [
        ("gwangmyeong-dong", "광명동"), ("cheolsan-dong", "철산동"), ("haan-dong", "하안동"),
        ("soha-dong", "소하동"), ("iljik-dong", "일직동"), ("noonsa-dong", "노온사동"),
    ]),
    "guri": ("구리", [
        ("galmae-dong", "갈매동"), ("inchang-dong", "인창동"), ("gyomun-dong", "교문동"),
        ("sutaek-dong", "수택동"), ("topyeong-dong", "토평동"),
    ]),
    "gunpo": ("군포", [
        ("sanbon-dong", "산본동"), ("geumjeong-dong", "금정동"), ("dangjeong-dong", "당정동"),
        ("bugok-dong", "부곡동"), ("daeya-dong", "대야동"),
    ]),
    "osan": ("오산", [
        ("osan-dong", "오산동"), ("segyo-dong", "세교동"), ("unam-dong", "운암동"),
        ("busan-dong", "부산동"), ("galgot-dong", "갈곶동"), ("won-dong", "원동"),
    ]),
    "uiwang": ("의왕", [
        ("naeson-dong", "내손동"), ("ojeon-dong", "오전동"), ("gocheon-dong", "고천동"),
        ("bugok-dong", "부곡동"), ("cheonggye-dong", "청계동"), ("poil-dong", "포일동"),
    ]),
    "gwacheon": ("과천", [
        ("jungang-dong", "중앙동"), ("byeolyang-dong", "별양동"), ("burim-dong", "부림동"),
        ("galhyeon-dong", "갈현동"), ("munwon-dong", "문원동"),
    ]),
    "gwangju-si": ("광주", [
        ("gyeongan-dong", "경안동"), ("songjeong-dong", "송정동"), ("taejeon-dong", "태전동"),
        ("ssangnyeong-dong", "쌍령동"), ("opo-eup", "오포읍"), ("gonjiam-eup", "곤지암읍"),
        ("chowol-eup", "초월읍"),
    ]),
    "icheon": ("이천", [
        ("changjeon-dong", "창전동"), ("jungni-dong", "중리동"), ("jeungpo-dong", "증포동"),
        ("bubal-eup", "부발읍"), ("janghowon-eup", "장호원읍"), ("majang-myeon", "마장면"),
    ]),
    "yangpyeong": ("양평", [
        ("yangpyeong-eup", "양평읍"), ("yongmun-myeon", "용문면"), ("gangha-myeon", "강하면"),
        ("okcheon-myeon", "옥천면"), ("seojong-myeon", "서종면"), ("gangsang-myeon", "강상면"),
    ]),
}


def _body(area_name, parent_label, parent_path, base_path, sibs):
    sib_li = "".join(f'<li><a href="{base_path}{s}/">{n}</a></li>' for s, n in sibs)
    return f"""
<section>
<h2>{parent_label} {area_name} 출장마사지·홈타이 안내</h2>
<p>{area_name}은(는) 경기 {parent_label}에 속한 지역입니다. 토끼24 마사지는 {area_name} 일대의 자택·숙소·오피스텔 등으로 직접 방문하는 출장마사지·홈타이 관리를 안내합니다. 예약 전 방문 주소와 건물 출입 방식, 예약 가능 시간을 먼저 확인하시면 대기 없이 진행됩니다. 외곽 지역은 차량 이동과 추가 이동비를 함께 확인해 주세요.</p>
<p>예약과 문의는 <a href="tel:0508-202-4719">0508-202-4719</a>로 받습니다. 원하시는 날짜·시간과 방문 장소 유형을 알려주시면 가능한 일정을 안내해 드립니다.</p>
</section>
<section>
<h2>{parent_label} 인접 지역 안내</h2>
<p>{parent_label}의 다른 지역도 함께 확인하실 수 있습니다.</p>
<ul>{sib_li}</ul>
</section>
<section>
<h2>{area_name} 이용 안내</h2>
<ul>
<li><a href="{parent_path}">{parent_label} 전체 안내</a></li>
<li><a href="/gyeonggi/">경기 출장마사지</a></li>
<li><a href="/find/gyeonggi/">경기에서 찾기</a></li>
<li><a href="/check/">예약 전 확인</a></li>
</ul>
</section>
"""


def list_section(title, base_path, areas, note="번호동은 대표동으로 통합"):
    li = "".join(f'<li><a href="{base_path}{s}/">{n}</a></li>' for s, n in areas)
    return (
        f'<section>\n<h2>{title}</h2>\n'
        f'<p>지역별 출장마사지·홈타이 방문 안내입니다({note}). 지역을 선택해 안내와 예약 전 확인사항을 확인하세요.</p>\n'
        f'<ul>\n{li}\n</ul>\n</section>'
    )


PAGES = []
# 구가 있는 시
for cs, (cn, gus) in GU_CITIES.items():
    for gslug, (gn, dongs) in gus.items():
        base = f"/gyeonggi/{cs}/{gslug}/"
        for ds, dn in dongs:
            _p = f"gyeonggi/{cs}/{gslug}/{ds}/"
            PAGES.append(P(
                _p,
                make_title(dn, f"{cn} {gn}", _p),
                make_desc(f"{cn} {gn} {dn}", _p),
                f"{cn} {gn} {dn} 출장마사지·홈타이 안내",
                [("경기", "/gyeonggi/"), (cn, f"/gyeonggi/{cs}/"), (gn, base), (dn, "")],
                body=_body(dn, f"{cn} {gn}", base, base, [(s, n) for s, n in dongs if s != ds][:10]),
            ))
# 구가 없는 시
for cs, (cn, dongs) in CITY_DONGS.items():
    base = f"/gyeonggi/{cs}/"
    for ds, dn in dongs:
        _p = f"gyeonggi/{cs}/{ds}/"
        PAGES.append(P(
            _p,
            make_title(dn, cn, _p),
            make_desc(f"{cn} {dn}", _p),
            f"{cn} {dn} 출장마사지·홈타이 안내",
            [("경기", "/gyeonggi/"), (cn, f"/gyeonggi/{cs}/"), (dn, "")],
            body=_body(dn, cn, base, base, [(s, n) for s, n in dongs if s != ds][:10]),
        ))
