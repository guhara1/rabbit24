# 서울 핵심 행정동 (1차-C). 검색 수요·상업 성격이 뚜렷한 동만 선별(구/역/생활권과 차별화).
# 경로: /seoul/<구>/<동>/
from .sudogwon import P

# (gu_slug, gu_name, dong_slug, dong_name, 대표 성격)
SEOUL_DONG = [
    ("gangnam-gu", "강남구", "yeoksam-dong", "역삼동", "테헤란로·강남역"),
    ("gangnam-gu", "강남구", "samseong-dong", "삼성동", "코엑스·삼성역"),
    ("gangnam-gu", "강남구", "cheongdam-dong", "청담동", "청담·명품거리"),
    ("gangnam-gu", "강남구", "sinsa-dong", "신사동", "가로수길·신사역"),
    ("seocho-gu", "서초구", "seocho-dong", "서초동", "교대·법조타운"),
    ("seocho-gu", "서초구", "banpo-dong", "반포동", "반포·고속터미널"),
    ("songpa-gu", "송파구", "jamsil-dong", "잠실동", "잠실·롯데타워"),
    ("songpa-gu", "송파구", "garak-dong", "가락동", "가락시장·문정"),
    ("yeongdeungpo-gu", "영등포구", "yeouido-dong", "여의도동", "여의도·금융가"),
    ("seongdong-gu", "성동구", "seongsu-dong", "성수동", "성수·서울숲"),
    ("mapo-gu", "마포구", "seogyo-dong", "서교동", "홍대·합정"),
    ("gangseo-gu", "강서구", "magok-dong", "마곡동", "마곡·발산"),
]

PAGES = [
    P(
        f"seoul/{gu_slug}/{dong_slug}/",
        f"{dong_name} 출장마사지｜서울 {gu_name} {dong_name} 안내",
        f"서울 {gu_name} {dong_name} 출장마사지·홈타이 예약 전 {areas} 생활권을 확인하세요.",
        f"서울 {gu_name} {dong_name} 출장마사지·홈타이 안내",
        [("서울", "/seoul/"), (gu_name, f"/seoul/{gu_slug}/"), (dong_name, "")],
    )
    for gu_slug, gu_name, dong_slug, dong_name, areas in SEOUL_DONG
]
