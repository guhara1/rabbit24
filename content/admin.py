# 서울 자치구 → 통합 행정동 전체 구조 (드릴다운).
# 번호동(1·2·3동 등)은 대표동 1개로 통합. 본문이 얇은 동은 빌드 규칙상 자동 noindex
# (검색 비노출·내부 탐색용) → 도어웨이(색인 대량 저가치 페이지) 위험 회피.
# 핵심 동(content/bodies/seoul__<구>__<동>.html 존재)은 빌드 오버레이로 풍부한 본문 적용.
from .sudogwon import P

# 구 slug: (구 이름, [(동 slug, 동 이름), ...])  — 통합 행정동
SEOUL = {
    "gangnam-gu": ("강남구", [
        ("yeoksam-dong", "역삼동"), ("samseong-dong", "삼성동"), ("daechi-dong", "대치동"),
        ("cheongdam-dong", "청담동"), ("sinsa-dong", "신사동"), ("nonhyeon-dong", "논현동"),
        ("apgujeong-dong", "압구정동"), ("dogok-dong", "도곡동"), ("gaepo-dong", "개포동"),
        ("ilwon-dong", "일원동"), ("suseo-dong", "수서동"), ("segok-dong", "세곡동"),
    ]),
    "seocho-gu": ("서초구", [
        ("seocho-dong", "서초동"), ("banpo-dong", "반포동"), ("jamwon-dong", "잠원동"),
        ("bangbae-dong", "방배동"), ("yangjae-dong", "양재동"), ("umyeon-dong", "우면동"),
        ("naegok-dong", "내곡동"),
    ]),
    "songpa-gu": ("송파구", [
        ("jamsil-dong", "잠실동"), ("sincheon-dong", "신천동"), ("songpa-dong", "송파동"),
        ("seokchon-dong", "석촌동"), ("samjeon-dong", "삼전동"), ("garak-dong", "가락동"),
        ("munjeong-dong", "문정동"), ("jangji-dong", "장지동"), ("bangi-dong", "방이동"),
        ("ogeum-dong", "오금동"), ("geoyeo-dong", "거여동"), ("macheon-dong", "마천동"),
        ("pungnap-dong", "풍납동"),
    ]),
    "gangdong-gu": ("강동구", [
        ("cheonho-dong", "천호동"), ("seongnae-dong", "성내동"), ("gil-dong", "길동"),
        ("dunchon-dong", "둔촌동"), ("amsa-dong", "암사동"), ("myeongil-dong", "명일동"),
        ("godeok-dong", "고덕동"), ("sangil-dong", "상일동"), ("gangil-dong", "강일동"),
    ]),
    "gwanak-gu": ("관악구", [
        ("bongcheon-dong", "봉천동"), ("sinlim-dong", "신림동"), ("namhyeon-dong", "남현동"),
    ]),
    "dongjak-gu": ("동작구", [
        ("noryangjin-dong", "노량진동"), ("sangdo-dong", "상도동"), ("heukseok-dong", "흑석동"),
        ("sadang-dong", "사당동"), ("daebang-dong", "대방동"), ("sindaebang-dong", "신대방동"),
        ("bon-dong", "본동"),
    ]),
    "yeongdeungpo-gu": ("영등포구", [
        ("yeongdeungpo-dong", "영등포동"), ("yeouido-dong", "여의도동"), ("dangsan-dong", "당산동"),
        ("mullae-dong", "문래동"), ("yangpyeong-dong", "양평동"), ("singil-dong", "신길동"),
        ("daerim-dong", "대림동"), ("dorim-dong", "도림동"),
    ]),
    "guro-gu": ("구로구", [
        ("guro-dong", "구로동"), ("sindorim-dong", "신도림동"), ("gocheok-dong", "고척동"),
        ("gaebong-dong", "개봉동"), ("oryu-dong", "오류동"), ("garibong-dong", "가리봉동"),
        ("onsu-dong", "온수동"), ("gung-dong", "궁동"), ("cheonwang-dong", "천왕동"),
        ("hang-dong", "항동"),
    ]),
    "geumcheon-gu": ("금천구", [
        ("gasan-dong", "가산동"), ("doksan-dong", "독산동"), ("siheung-dong", "시흥동"),
    ]),
    "gangseo-gu": ("강서구", [
        ("hwagok-dong", "화곡동"), ("magok-dong", "마곡동"), ("deungchon-dong", "등촌동"),
        ("yeomchang-dong", "염창동"), ("gayang-dong", "가양동"), ("balsan-dong", "발산동"),
        ("gonghang-dong", "공항동"), ("banghwa-dong", "방화동"),
    ]),
    "yangcheon-gu": ("양천구", [
        ("mok-dong", "목동"), ("sinjeong-dong", "신정동"), ("sinwol-dong", "신월동"),
    ]),
    "mapo-gu": ("마포구", [
        ("seogyo-dong", "서교동"), ("hapjeong-dong", "합정동"), ("mangwon-dong", "망원동"),
        ("yeonnam-dong", "연남동"), ("seongsan-dong", "성산동"), ("sangam-dong", "상암동"),
        ("gongdeok-dong", "공덕동"), ("ahyeon-dong", "아현동"), ("dohwa-dong", "도화동"),
        ("yonggang-dong", "용강동"), ("daeheung-dong", "대흥동"), ("yeomri-dong", "염리동"),
        ("sinsu-dong", "신수동"), ("sangsu-dong", "상수동"), ("donggyo-dong", "동교동"),
    ]),
    "seodaemun-gu": ("서대문구", [
        ("sinchon-dong", "신촌동"), ("hongje-dong", "홍제동"), ("hongeun-dong", "홍은동"),
        ("yeonhui-dong", "연희동"), ("namgajwa-dong", "남가좌동"), ("bukgajwa-dong", "북가좌동"),
        ("bukahyeon-dong", "북아현동"), ("daehyeon-dong", "대현동"), ("changcheon-dong", "창천동"),
        ("chungjeongno", "충정로"),
    ]),
    "eunpyeong-gu": ("은평구", [
        ("bulgwang-dong", "불광동"), ("eungam-dong", "응암동"), ("yeokchon-dong", "역촌동"),
        ("nokbeon-dong", "녹번동"), ("daejo-dong", "대조동"), ("galhyeon-dong", "갈현동"),
        ("gusan-dong", "구산동"), ("sinsa-dong", "신사동"), ("jeungsan-dong", "증산동"),
        ("susaek-dong", "수색동"), ("jingwan-dong", "진관동"),
    ]),
    "jongno-gu": ("종로구", [
        ("sajik-dong", "사직동"), ("samcheong-dong", "삼청동"), ("gahoe-dong", "가회동"),
        ("buam-dong", "부암동"), ("pyeongchang-dong", "평창동"), ("hyehwa-dong", "혜화동"),
        ("myeongnyun-dong", "명륜동"), ("changsin-dong", "창신동"), ("sungin-dong", "숭인동"),
        ("muak-dong", "무악동"), ("ihwa-dong", "이화동"),
    ]),
    "jung-gu": ("중구", [
        ("myeong-dong", "명동"), ("euljiro-dong", "을지로"), ("hoehyeon-dong", "회현동"),
        ("sogong-dong", "소공동"), ("sindang-dong", "신당동"), ("hwanghak-dong", "황학동"),
        ("jungnim-dong", "중림동"), ("jangchung-dong", "장충동"), ("pil-dong", "필동"),
        ("yaksu-dong", "약수동"),
    ]),
    "seongdong-gu": ("성동구", [
        ("seongsu-dong", "성수동"), ("wangsimni-dong", "왕십리동"), ("oksu-dong", "옥수동"),
        ("geumho-dong", "금호동"), ("haengdang-dong", "행당동"), ("eungbong-dong", "응봉동"),
        ("majang-dong", "마장동"), ("sageun-dong", "사근동"), ("songjeong-dong", "송정동"),
        ("yongdap-dong", "용답동"),
    ]),
    "gwangjin-gu": ("광진구", [
        ("guui-dong", "구의동"), ("jayang-dong", "자양동"), ("hwayang-dong", "화양동"),
        ("neung-dong", "능동"), ("gwangjang-dong", "광장동"), ("junggok-dong", "중곡동"),
        ("gunja-dong", "군자동"),
    ]),
    "dongdaemun-gu": ("동대문구", [
        ("cheongnyangni-dong", "청량리동"), ("jeonnong-dong", "전농동"), ("dapsimni-dong", "답십리동"),
        ("jangan-dong", "장안동"), ("imun-dong", "이문동"), ("hwigyeong-dong", "휘경동"),
        ("hoegi-dong", "회기동"), ("jegi-dong", "제기동"), ("yongdu-dong", "용두동"),
        ("sinseol-dong", "신설동"),
    ]),
    "jungnang-gu": ("중랑구", [
        ("myeonmok-dong", "면목동"), ("sangbong-dong", "상봉동"), ("junghwa-dong", "중화동"),
        ("muk-dong", "묵동"), ("mangu-dong", "망우동"), ("sinnae-dong", "신내동"),
    ]),
    "seongbuk-gu": ("성북구", [
        ("donam-dong", "돈암동"), ("jeongneung-dong", "정릉동"), ("gireum-dong", "길음동"),
        ("jongam-dong", "종암동"), ("anam-dong", "안암동"), ("bomun-dong", "보문동"),
        ("samseon-dong", "삼선동"), ("seongbuk-dong", "성북동"), ("seokgwan-dong", "석관동"),
        ("jangwi-dong", "장위동"), ("wolgok-dong", "월곡동"),
    ]),
    "gangbuk-gu": ("강북구", [
        ("mia-dong", "미아동"), ("suyu-dong", "수유동"), ("beon-dong", "번동"), ("ui-dong", "우이동"),
    ]),
    "dobong-gu": ("도봉구", [
        ("chang-dong", "창동"), ("ssangmun-dong", "쌍문동"), ("banghak-dong", "방학동"),
        ("dobong-dong", "도봉동"),
    ]),
    "nowon-gu": ("노원구", [
        ("sanggye-dong", "상계동"), ("junggye-dong", "중계동"), ("hagye-dong", "하계동"),
        ("gongneung-dong", "공릉동"), ("wolgye-dong", "월계동"),
    ]),
    "yongsan-gu": ("용산구", [
        ("hannam-dong", "한남동"), ("itaewon-dong", "이태원동"), ("hangangno-dong", "한강로동"),
        ("ichon-dong", "이촌동"), ("seobinggo-dong", "서빙고동"), ("bogwang-dong", "보광동"),
        ("huam-dong", "후암동"), ("cheongpa-dong", "청파동"), ("hyochang-dong", "효창동"),
        ("yongmun-dong", "용문동"),
    ]),
}


def _dong_body(gu_slug, gu_name, dong_slug, dong_name, all_dongs):
    sibs = [(s, n) for s, n in all_dongs if s != dong_slug][:10]
    sib_li = "".join(
        f'<li><a href="/seoul/{gu_slug}/{s}/">{n}</a></li>' for s, n in sibs
    )
    return f"""
<section>
<h2>{gu_name} {dong_name} 출장마사지·홈타이 안내</h2>
<p>{dong_name}은(는) 서울 {gu_name}에 속한 동네입니다. 토끼24 마사지는 {dong_name} 일대의 자택·숙소·오피스텔 등으로 직접 방문하는 출장마사지·홈타이 관리를 안내합니다. 예약 전 방문 주소와 건물 출입 방식, 예약 가능 시간을 먼저 확인하시면 대기 없이 진행됩니다.</p>
<p>예약과 문의는 <a href="tel:0508-202-4719">0508-202-4719</a>로 받습니다. 원하시는 날짜·시간과 방문 장소 유형을 알려주시면 가능한 일정을 안내해 드립니다.</p>
</section>
<section>
<h2>{gu_name} 인접 동 안내</h2>
<p>{gu_name}의 다른 동도 함께 확인하실 수 있습니다.</p>
<ul>{sib_li}</ul>
</section>
<section>
<h2>{dong_name} 이용 안내</h2>
<ul>
<li><a href="/seoul/{gu_slug}/">{gu_name} 전체 안내</a></li>
<li><a href="/seoul/">서울 출장마사지</a></li>
<li><a href="/find/seoul/">서울에서 찾기</a></li>
<li><a href="/check/">예약 전 확인</a></li>
</ul>
</section>
"""


def _dong_list_section(gu_slug, gu_name, dongs):
    """구 페이지에 넣을 '행정동 전체' 드릴다운 섹션 HTML."""
    li = "".join(f'<li><a href="/seoul/{gu_slug}/{s}/">{n}</a></li>' for s, n in dongs)
    return (
        f'<section>\n<h2>{gu_name} 행정동 안내</h2>\n'
        f'<p>{gu_name}의 행정동별 출장마사지·홈타이 방문 안내입니다(번호동은 대표동으로 통합). '
        f'동을 선택해 해당 지역 안내와 예약 전 확인사항을 확인하세요.</p>\n<ul>\n{li}\n</ul>\n</section>'
    )


PAGES = []
for _gu_slug, (_gu_name, _dongs) in SEOUL.items():
    for _ds, _dn in _dongs:
        PAGES.append(P(
            f"seoul/{_gu_slug}/{_ds}/",
            f"{_dn} 출장마사지｜서울 {_gu_name} {_dn} 안내",
            f"서울 {_gu_name} {_dn} 출장마사지·홈타이 예약 전 생활권과 이용 기준을 확인하세요.",
            f"서울 {_gu_name} {_dn} 출장마사지·홈타이 안내",
            [("서울", "/seoul/"), (_gu_name, f"/seoul/{_gu_slug}/"), (_dn, "")],
            body=_dong_body(_gu_slug, _gu_name, _ds, _dn, _dongs),
        ))
