# 지역 페이지 타이틀/디스크립션 헬퍼.
# 규칙: 타이틀은 항상 "<지역명> 출장마사지"로 시작하고 지역명은 1회만.
# 페이지 경로를 키로 다양한 변형을 결정적으로 배정한다(중복 줄이고 다양성 확보).
import hashlib

# 타이틀 접미(지역명 뒤). {scope}=상위 지역(시/도·구) — 같은 지역명을 반복하지 않는다.
_TITLE_SUFFIXES = [
    "｜{scope} 홈타이 방문 예약 안내",
    "｜{scope} 자택·호텔 출장 홈타이",
    "｜{scope} 오피스텔·자택 방문 관리",
    "｜{scope} 24시간 출장 홈타이 안내",
    "｜{scope} 생활권별 방문 안내",
    "｜{scope} 예약 전 확인·요금 안내",
    "｜{scope} 전문 관리사 방문 홈타이",
    "｜{scope} 야간 예약 가능 홈타이",
]

# 디스크립션 본문(지역명 뒤, 80자 이내 유지). 지역명을 반복하지 않는다.
_DESC_SUFFIXES = [
    "출장마사지·홈타이 예약 전 방문 주소와 이용 기준을 확인하세요.",
    "자택·호텔·오피스텔 방문 홈타이를 예약 전 확인하세요.",
    "24시간 출장 홈타이, 예약 가능 시간과 요금을 확인하세요.",
    "방문 마사지·홈타이 생활권별 이용 안내를 확인하세요.",
    "출장 홈타이 예약 전 건물 출입·추가 이동비를 확인하세요.",
    "홈타이 코스 60·90·120분 요금과 방문 예약을 안내합니다.",
    "전문 관리사 방문 출장마사지·홈타이를 예약 전 확인하세요.",
    "야간 예약 가능 출장 홈타이, 이용 기준을 확인하세요.",
]


def _idx(key, n):
    return int(hashlib.md5(key.encode("utf-8")).hexdigest(), 16) % n


def make_title(primary, scope, key):
    """'<primary> 출장마사지' + 변형 접미. primary=지역명(1회), scope=상위 지역."""
    suf = _TITLE_SUFFIXES[_idx("t:" + key, len(_TITLE_SUFFIXES))]
    return f"{primary} 출장마사지" + suf.format(scope=scope)


def make_desc(region, key):
    """'<region> ' + 변형 본문. region=문맥 포함 지역 표기(중복 없이)."""
    suf = _DESC_SUFFIXES[_idx("d:" + key, len(_DESC_SUFFIXES))]
    return f"{region} {suf}"
