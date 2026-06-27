# 경기 핵심 시·군 페이지 (1차-B). 안산은 /gyeonggi/ansan/ 로 별도 운영.
from .sudogwon import P

GYEONGGI_CITIES = [
    ("suwon", "수원", "수원역·광교·영통"),
    ("seongnam", "성남", "분당·판교·서현"),
    ("yongin", "용인", "수지·기흥·죽전"),
    ("goyang", "고양", "일산·화정·삼송"),
    ("hwaseong", "화성", "동탄·병점·봉담"),
    ("bucheon", "부천", "부천역·상동·중동"),
    ("anyang", "안양", "평촌·범계·안양역"),
    ("pyeongtaek", "평택", "평택역·소사벌·송탄"),
    ("siheung", "시흥", "정왕·배곧·시흥시청"),
    ("gimpo", "김포", "김포·구래·장기"),
    ("namyangju", "남양주", "다산·별내·평내"),
    ("paju", "파주", "운정·금촌"),
    ("uijeongbu", "의정부", "의정부역·민락"),
    ("hanam", "하남", "미사·하남시청"),
    ("gwangmyeong", "광명", "철산·하안·광명역"),
    ("guri", "구리", "구리·갈매"),
    ("gunpo", "군포", "산본·금정"),
    ("osan", "오산", "오산역·세교"),
    ("uiwang", "의왕", "내손·오전"),
    ("gwacheon", "과천", "과천·정부청사"),
    ("gwangju-si", "광주", "태전·경기광주역"),
    ("icheon", "이천", "이천·부발"),
    ("yangpyeong", "양평", "양평·용문"),
]

PAGES = [
    P(
        f"gyeonggi/{slug}/",
        f"{name} 출장마사지｜{name} {areas} 생활권 안내",
        f"{name} 출장마사지·홈타이 예약 전 {areas} 생활권과 이용 기준을 확인하세요.",
        f"{name} 출장마사지·홈타이 안내",
        [("경기", "/gyeonggi/"), (name, "")],
    )
    for slug, name, areas in GYEONGGI_CITIES
]
