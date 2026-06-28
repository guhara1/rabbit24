# 경기 시 → (일반구) → 동 드릴다운. 구가 있는 시는 시>구>동, 없는 시는 시>동.
# 번호동 통합. 핵심 동은 빌드 오버레이로 풍부 본문 색인, 나머지는 자동 noindex(도어웨이 회피).
from .sudogwon import P

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
            PAGES.append(P(
                f"gyeonggi/{cs}/{gslug}/{ds}/",
                f"{dn} 출장마사지｜{cn} {gn} {dn} 안내",
                f"{cn} {gn} {dn} 출장마사지·홈타이 예약 전 생활권과 이용 기준을 확인하세요.",
                f"{cn} {gn} {dn} 출장마사지·홈타이 안내",
                [("경기", "/gyeonggi/"), (cn, f"/gyeonggi/{cs}/"), (gn, base), (dn, "")],
                body=_body(dn, f"{cn} {gn}", base, base, [(s, n) for s, n in dongs if s != ds][:10]),
            ))
# 구가 없는 시
for cs, (cn, dongs) in CITY_DONGS.items():
    base = f"/gyeonggi/{cs}/"
    for ds, dn in dongs:
        PAGES.append(P(
            f"gyeonggi/{cs}/{ds}/",
            f"{dn} 출장마사지｜{cn} {dn} 안내",
            f"{cn} {dn} 출장마사지·홈타이 예약 전 생활권과 이용 기준을 확인하세요.",
            f"{cn} {dn} 출장마사지·홈타이 안내",
            [("경기", "/gyeonggi/"), (cn, f"/gyeonggi/{cs}/"), (dn, "")],
            body=_body(dn, cn, base, base, [(s, n) for s, n in dongs if s != ds][:10]),
        ))
