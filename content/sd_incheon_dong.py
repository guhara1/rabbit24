# 인천 핵심 동 (1차-C). 경로: /incheon/<구>/<동>/
from .sudogwon import P

# (gu_slug, gu_name, dong_slug, dong_name, 대표 성격)
INCHEON_DONG = [
    ("namdong-gu", "남동구", "guwol-dong", "구월동", "구월·인천시청"),
    ("namdong-gu", "남동구", "nonhyeon-dong", "논현동", "논현·소래"),
    ("michuhol-gu", "미추홀구", "juan-dong", "주안동", "주안·상권"),
    ("yeonsu-gu", "연수구", "songdo-dong", "송도동", "송도국제도시"),
    ("yeonsu-gu", "연수구", "yeonsu-dong", "연수동", "연수·원인재"),
    ("bupyeong-gu", "부평구", "bupyeong-dong", "부평동", "부평역·상권"),
    ("seo-gu", "서구", "cheongna-dong", "청라동", "청라국제도시"),
    ("seo-gu", "서구", "gajeong-dong", "가정동", "가정·루원시티"),
    ("gyeyang-gu", "계양구", "gyesan-dong", "계산동", "계산·상권"),
    ("jung-gu", "중구", "unseo-dong", "운서동", "영종·운서·공항"),
]

PAGES = [
    P(
        f"incheon/{gu_slug}/{dong_slug}/",
        f"{dong_name} 출장마사지｜인천 {gu_name} {dong_name} 안내",
        f"인천 {gu_name} {dong_name} 출장마사지·홈타이 예약 전 {areas} 생활권을 확인하세요.",
        f"인천 {gu_name} {dong_name} 출장마사지·홈타이 안내",
        [("인천", "/incheon/"), (gu_name, f"/incheon/{gu_slug}/"), (dong_name, "")],
    )
    for gu_slug, gu_name, dong_slug, dong_name, areas in INCHEON_DONG
]
