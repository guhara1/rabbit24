# 인천 구·군 → 통합 동/읍면 드릴다운. 번호동은 대표동 1개로 통합.
# 핵심 지역(content/bodies/incheon__<구>__<동>.html)은 빌드 오버레이로 풍부한 본문 적용,
# 나머지는 얇은 본문 → 자동 noindex(도어웨이 회피).
from .sudogwon import P

INCHEON = {
    "jung-gu": ("중구", [
        ("sinpo-dong", "신포동"), ("hang-dong", "항동"), ("unseo-dong", "운서동"),
        ("unnam-dong", "운남동"), ("jungsan-dong", "중산동"), ("yeongjong-dong", "영종동"),
    ]),
    "dong-gu": ("동구", [
        ("songnim-dong", "송림동"), ("hwasu-dong", "화수동"), ("manseok-dong", "만석동"),
        ("songhyeon-dong", "송현동"), ("geumgok-dong", "금곡동"), ("changyeong-dong", "창영동"),
    ]),
    "michuhol-gu": ("미추홀구", [
        ("juan-dong", "주안동"), ("dohwa-dong", "도화동"), ("yonghyeon-dong", "용현동"),
        ("hakik-dong", "학익동"), ("sungui-dong", "숭의동"), ("gwangyo-dong", "관교동"),
        ("munhak-dong", "문학동"),
    ]),
    "yeonsu-gu": ("연수구", [
        ("songdo-dong", "송도동"), ("yeonsu-dong", "연수동"), ("cheonghak-dong", "청학동"),
        ("dongchun-dong", "동춘동"), ("okryeon-dong", "옥련동"), ("seonhak-dong", "선학동"),
    ]),
    "namdong-gu": ("남동구", [
        ("guwol-dong", "구월동"), ("nonhyeon-dong", "논현동"), ("mansu-dong", "만수동"),
        ("ganseok-dong", "간석동"), ("seochang-dong", "서창동"), ("jangsu-dong", "장수동"),
    ]),
    "bupyeong-gu": ("부평구", [
        ("bupyeong-dong", "부평동"), ("sangok-dong", "산곡동"), ("bugae-dong", "부개동"),
        ("samsan-dong", "삼산동"), ("cheongcheon-dong", "청천동"), ("galsan-dong", "갈산동"),
        ("sipjeong-dong", "십정동"),
    ]),
    "gyeyang-gu": ("계양구", [
        ("gyesan-dong", "계산동"), ("jakjeon-dong", "작전동"), ("hyoseong-dong", "효성동"),
        ("imhak-dong", "임학동"), ("byeongbang-dong", "병방동"), ("gyulhyeon-dong", "귤현동"),
    ]),
    "seo-gu": ("서구", [
        ("cheongna-dong", "청라동"), ("gajeong-dong", "가정동"), ("geomam-dong", "검암동"),
        ("seoknam-dong", "석남동"), ("gajwa-dong", "가좌동"), ("sinhyeon-dong", "신현동"),
        ("dangha-dong", "당하동"), ("majeon-dong", "마전동"), ("bullo-dong", "불로동"),
        ("wondang-dong", "원당동"),
    ]),
    "ganghwa-gun": ("강화군", [
        ("ganghwa-eup", "강화읍"), ("gilsang-myeon", "길상면"), ("seonwon-myeon", "선원면"),
        ("hwado-myeon", "화도면"), ("yangdo-myeon", "양도면"), ("naega-myeon", "내가면"),
    ]),
    "ongjin-gun": ("옹진군", [
        ("yeongheung-myeon", "영흥면"), ("baengnyeong-myeon", "백령면"), ("yeonpyeong-myeon", "연평면"),
        ("deokjeok-myeon", "덕적면"), ("jawol-myeon", "자월면"), ("bukdo-myeon", "북도면"),
    ]),
}


def _area_body(gu_slug, gu_name, a_slug, a_name, areas):
    sibs = [(s, n) for s, n in areas if s != a_slug][:10]
    sib_li = "".join(f'<li><a href="/incheon/{gu_slug}/{s}/">{n}</a></li>' for s, n in sibs)
    return f"""
<section>
<h2>인천 {gu_name} {a_name} 출장마사지·홈타이 안내</h2>
<p>{a_name}은(는) 인천 {gu_name}에 속한 지역입니다. 토끼24 마사지는 {a_name} 일대의 자택·숙소·오피스텔 등으로 직접 방문하는 출장마사지·홈타이 관리를 안내합니다. 예약 전 방문 주소와 건물 출입 방식, 예약 가능 시간을 먼저 확인하시면 대기 없이 진행됩니다. 외곽·도서 지역은 이동 시간과 추가 이동비를 함께 확인해 주세요.</p>
<p>예약과 문의는 <a href="tel:0508-202-4719">0508-202-4719</a>로 받습니다. 원하시는 날짜·시간과 방문 장소 유형을 알려주시면 가능한 일정을 안내해 드립니다.</p>
</section>
<section>
<h2>{gu_name} 인접 지역 안내</h2>
<p>{gu_name}의 다른 지역도 함께 확인하실 수 있습니다.</p>
<ul>{sib_li}</ul>
</section>
<section>
<h2>{a_name} 이용 안내</h2>
<ul>
<li><a href="/incheon/{gu_slug}/">{gu_name} 전체 안내</a></li>
<li><a href="/incheon/">인천 출장마사지</a></li>
<li><a href="/find/incheon/">인천에서 찾기</a></li>
<li><a href="/check/">예약 전 확인</a></li>
</ul>
</section>
"""


def _area_list_section(gu_slug, gu_name, areas):
    li = "".join(f'<li><a href="/incheon/{gu_slug}/{s}/">{n}</a></li>' for s, n in areas)
    return (
        f'<section>\n<h2>{gu_name} 동·읍면 안내</h2>\n'
        f'<p>인천 {gu_name}의 지역별 출장마사지·홈타이 방문 안내입니다(번호동은 대표동으로 통합). '
        f'지역을 선택해 안내와 예약 전 확인사항을 확인하세요.</p>\n<ul>\n{li}\n</ul>\n</section>'
    )


PAGES = []
for _gs, (_gn, _areas) in INCHEON.items():
    for _as, _an in _areas:
        PAGES.append(P(
            f"incheon/{_gs}/{_as}/",
            f"{_an} 출장마사지｜인천 {_gn} {_an} 안내",
            f"인천 {_gn} {_an} 출장마사지·홈타이 예약 전 생활권과 이용 기준을 확인하세요.",
            f"인천 {_gn} {_an} 출장마사지·홈타이 안내",
            [("인천", "/incheon/"), (_gn, f"/incheon/{_gs}/"), (_an, "")],
            body=_area_body(_gs, _gn, _as, _an, _areas),
        ))
