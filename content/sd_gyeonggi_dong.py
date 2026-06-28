# 경기 핵심 동 (1차-C). 구를 둔 시는 /gyeonggi/<시>/<구>/<동>/, 아닌 시는 /gyeonggi/<시>/<동>/.
from .sudogwon import P

# (city_slug, city_name, gu_slug, gu_name, dong_slug, dong_name, 대표 성격)  gu_slug="" 면 구 없음
GYEONGGI_DONG = [
    ("suwon", "수원", "paldal-gu", "팔달구", "ingye-dong", "인계동", "인계동·나혜석거리"),
    ("suwon", "수원", "yeongtong-gu", "영통구", "yeongtong-dong", "영통동", "영통·아주대"),
    ("seongnam", "성남", "bundang-gu", "분당구", "jeongja-dong", "정자동", "정자·카페거리"),
    ("seongnam", "성남", "bundang-gu", "분당구", "seohyeon-dong", "서현동", "서현·AK플라자"),
    ("seongnam", "성남", "bundang-gu", "분당구", "yatap-dong", "야탑동", "야탑·터미널"),
    ("yongin", "용인", "suji-gu", "수지구", "jukjeon-dong", "죽전동", "죽전·신도시"),
    ("yongin", "용인", "giheung-gu", "기흥구", "singal-dong", "신갈동", "신갈·기흥"),
    ("goyang", "고양", "ilsanseo-gu", "일산서구", "juyeop-dong", "주엽동", "주엽·호수공원"),
    ("anyang", "안양", "dongan-gu", "동안구", "pyeongchon-dong", "평촌동", "평촌·학원가"),
    ("bucheon", "부천", "", "", "jung-dong", "중동", "중동신도시"),
    ("bucheon", "부천", "", "", "sang-dong", "상동", "상동·상권"),
    ("hwaseong", "화성", "", "", "bansong-dong", "반송동", "동탄신도시"),
]


def _mk(city_slug, city_name, gu_slug, gu_name, dong_slug, dong_name, areas):
    if gu_slug:
        path = f"gyeonggi/{city_slug}/{gu_slug}/{dong_slug}/"
        crumbs = [("경기", "/gyeonggi/"), (city_name, f"/gyeonggi/{city_slug}/"),
                  (gu_name, f"/gyeonggi/{city_slug}/{gu_slug}/"), (dong_name, "")]
        h1 = f"{city_name} {gu_name} {dong_name} 출장마사지·홈타이 안내"
    else:
        path = f"gyeonggi/{city_slug}/{dong_slug}/"
        crumbs = [("경기", "/gyeonggi/"), (city_name, f"/gyeonggi/{city_slug}/"), (dong_name, "")]
        h1 = f"{city_name} {dong_name} 출장마사지·홈타이 안내"
    return P(
        path,
        f"{dong_name} 출장마사지｜{city_name} {dong_name} 생활권 안내",
        f"{city_name} {dong_name} 출장마사지·홈타이 예약 전 {areas} 생활권을 확인하세요.",
        h1, crumbs,
    )


PAGES = [_mk(*row) for row in GYEONGGI_DONG]
