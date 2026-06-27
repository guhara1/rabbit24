# 서울 25개 자치구 페이지 (1차-B). 본문은 content/bodies/seoul__<slug>.html 오버레이.
from .sudogwon import P

# (slug, 구 이름, 대표 생활권 요약)
SEOUL_GU = [
    ("gangnam-gu", "강남구", "강남·역삼·삼성"),
    ("seocho-gu", "서초구", "서초·반포·교대"),
    ("songpa-gu", "송파구", "잠실·문정·가락"),
    ("gangdong-gu", "강동구", "천호·길동·고덕"),
    ("mapo-gu", "마포구", "홍대·합정·공덕"),
    ("yeongdeungpo-gu", "영등포구", "여의도·영등포·당산"),
    ("yongsan-gu", "용산구", "용산·이태원·한남"),
    ("seongdong-gu", "성동구", "성수·왕십리·옥수"),
    ("gwangjin-gu", "광진구", "건대·구의·자양"),
    ("dongdaemun-gu", "동대문구", "청량리·회기·장안"),
    ("jungnang-gu", "중랑구", "면목·상봉·중화"),
    ("seongbuk-gu", "성북구", "성신여대·길음·돈암"),
    ("gangbuk-gu", "강북구", "수유·미아·번동"),
    ("dobong-gu", "도봉구", "창동·쌍문·방학"),
    ("nowon-gu", "노원구", "노원·상계·중계"),
    ("eunpyeong-gu", "은평구", "연신내·불광·응암"),
    ("seodaemun-gu", "서대문구", "신촌·홍제·충정로"),
    ("jongno-gu", "종로구", "종로·광화문·혜화"),
    ("jung-gu", "중구", "명동·을지로·서울역"),
    ("gangseo-gu", "강서구", "마곡·발산·화곡"),
    ("yangcheon-gu", "양천구", "목동·신정·신월"),
    ("guro-gu", "구로구", "구로·신도림·구디"),
    ("geumcheon-gu", "금천구", "가산·독산·시흥"),
    ("dongjak-gu", "동작구", "노량진·사당·이수"),
    ("gwanak-gu", "관악구", "신림·서울대입구·봉천"),
]

PAGES = [
    P(
        f"seoul/{slug}/",
        f"{name} 출장마사지｜서울 {name} {areas} 생활권 안내",
        f"{name} 출장마사지·홈타이 예약 전 {areas} 생활권과 이용 기준을 확인하세요.",
        f"{name} 출장마사지·홈타이 안내",
        [("서울", "/seoul/"), (name, "")],
    )
    for slug, name, areas in SEOUL_GU
]
