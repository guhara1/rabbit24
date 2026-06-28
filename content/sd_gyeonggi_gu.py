# 경기 일반구 페이지 (1차-B). 구를 둔 시: 수원·성남·용인·고양·안양.
# (부천·화성·평택은 일반구 없음, 안산은 /gyeonggi/ansan/ 로 운영)
from .sudogwon import P
from .titles import make_title, make_desc

# (city_slug, city_name, gu_slug, gu_name, 대표 생활권)
GYEONGGI_GU = [
    ("suwon", "수원", "jangan-gu", "장안구", "정자·율전·파장"),
    ("suwon", "수원", "gwonseon-gu", "권선구", "권선·세류·호매실"),
    ("suwon", "수원", "paldal-gu", "팔달구", "인계동·매산·행궁동"),
    ("suwon", "수원", "yeongtong-gu", "영통구", "영통·매탄·광교"),
    ("seongnam", "성남", "sujeong-gu", "수정구", "신흥·태평·위례"),
    ("seongnam", "성남", "jungwon-gu", "중원구", "성남·금광·상대원"),
    ("seongnam", "성남", "bundang-gu", "분당구", "서현·정자·판교"),
    ("yongin", "용인", "cheoin-gu", "처인구", "김량장·역북·포곡"),
    ("yongin", "용인", "giheung-gu", "기흥구", "기흥·신갈·동백"),
    ("yongin", "용인", "suji-gu", "수지구", "수지·풍덕천·죽전"),
    ("goyang", "고양", "deogyang-gu", "덕양구", "화정·행신·삼송"),
    ("goyang", "고양", "ilsandong-gu", "일산동구", "정발산·마두·백석"),
    ("goyang", "고양", "ilsanseo-gu", "일산서구", "주엽·대화·킨텍스"),
    ("anyang", "안양", "manan-gu", "만안구", "안양·박달·석수"),
    ("anyang", "안양", "dongan-gu", "동안구", "평촌·범계·관양"),
]

PAGES = [
    P(
        f"gyeonggi/{city_slug}/{gu_slug}/",
        make_title(f"{city_name} {gu_name}", "경기", f"gyeonggi/{city_slug}/{gu_slug}/"),
        make_desc(f"{city_name} {gu_name}", f"gyeonggi/{city_slug}/{gu_slug}/"),
        f"{city_name} {gu_name} 출장마사지·홈타이 안내",
        [("경기", "/gyeonggi/"), (city_name, f"/gyeonggi/{city_slug}/"), (gu_name, "")],
    )
    for city_slug, city_name, gu_slug, gu_name, areas in GYEONGGI_GU
]
