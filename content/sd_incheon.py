# 인천 현행 구·군 페이지 (1차-B).
from .sudogwon import P

INCHEON_GUGUN = [
    ("jung-gu", "중구", "중앙동·신포·영종"),
    ("dong-gu", "동구", "송림·화수·만석"),
    ("michuhol-gu", "미추홀구", "주안·도화·용현"),
    ("yeonsu-gu", "연수구", "송도·연수·청학"),
    ("namdong-gu", "남동구", "구월·논현·만수"),
    ("bupyeong-gu", "부평구", "부평·산곡·부개"),
    ("gyeyang-gu", "계양구", "계산·작전·임학"),
    ("seo-gu", "서구", "청라·검단·가정"),
    ("ganghwa-gun", "강화군", "강화읍·길상"),
    ("ongjin-gun", "옹진군", "영흥·백령·연평"),
]

PAGES = [
    P(
        f"incheon/{slug}/",
        f"{name} 출장마사지｜인천 {name} {areas} 생활권 안내",
        f"인천 {name} 출장마사지·홈타이 예약 전 {areas} 생활권과 이용 기준을 확인하세요.",
        f"인천 {name} 출장마사지·홈타이 안내",
        [("인천", "/incheon/"), (name, "")],
    )
    for slug, name, areas in INCHEON_GUGUN
]
