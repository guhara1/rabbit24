# 안산 역세권·생활권 허브 페이지 — 2개
# /station/ 와 /area/ 의 인덱스(허브) 페이지. 브레드크럼 상위 링크 대상이며,
# 모든 역세권·생활권 페이지로 내부 링크를 분배한다.


def _page(path, title, desc, h1, breadcrumb, body):
    return {
        "path": path,
        "title": title,
        "desc": desc,
        "h1": h1,
        "breadcrumb": breadcrumb,
        "body": body,
    }


station_hub = _page(
    path="station/",
    title="안산 역세권 출장마사지｜지하철역별 홈타이 예약 안내",
    desc="안산 역세권 출장마사지·홈타이 안내. 상록수·중앙·초지·안산역 등 역별 생활권을 확인하세요.",
    h1="안산 역세권 출장마사지·홈타이 안내",
    breadcrumb=[("안산", "/"), ("역세권 안내", "/station/")],
    body="""
<section>
<h2>안산 지하철역 기준으로 찾기</h2>
<p>안산시는 수도권 전철 4호선과 수인분당선, 서해선이 함께 지나는 도시로, 같은 시 안에서도 역마다 연결되는 생활권과 분위기가 다릅니다. 출장마사지·홈타이를 예약할 때 가장 가까운 역을 기준으로 위치를 안내하면 방문 주소와 이동 시간을 더 정확하게 맞출 수 있습니다.</p>
<p>아래에서 안산 주요 역세권 페이지로 이동해 역별 인접 지역, 이용 장소별 확인사항, 예약 전 체크리스트를 확인하세요. 환승역도 출구·노선별로 페이지를 나누지 않고 역 이름 기준 하나의 안내로 정리했습니다.</p>
</section>

<section>
<h2>상록구 방면 역세권</h2>
<ul>
<li><a href="/station/sangnoksu-station/">상록수역</a> — 본오동 대규모 주거·상권 중심</li>
<li><a href="/station/hanyang-univ-at-ansan-station/">한대앞역</a> — 한양대 에리카·사동 대학가</li>
<li><a href="/station/sari-station/">사리역</a> — 상록구 외곽 생활권</li>
</ul>
</section>

<section>
<h2>단원구 방면 역세권</h2>
<ul>
<li><a href="/station/jungang-station/">중앙역</a> — 안산 최대 번화가·상권</li>
<li><a href="/station/gojan-station/">고잔역</a> — 호수공원·고잔신도시</li>
<li><a href="/station/choji-station/">초지역</a> — 4호선·수인분당선·서해선 환승</li>
<li><a href="/station/ansan-station/">안산역</a> — 원곡동 다문화거리·24시간 상권</li>
<li><a href="/station/seonbu-station/">선부역</a> — 선부동 주거 생활권</li>
<li><a href="/station/wongok-station/">원곡역</a> — 원곡동 서해선 연계</li>
<li><a href="/station/shingiloncheon-station/">신길온천역</a> — 신길동·온천 방면</li>
<li><a href="/station/dalmi-station/">달미역</a> — 선부·와동 인접</li>
<li><a href="/station/wonsi-station/">원시역</a> — 원시·시화공단 외곽권</li>
</ul>
</section>

<section>
<h2>역세권 예약 전 확인</h2>
<p>역 주변은 상가·오피스텔과 주거가 섞여 있어 건물 출입 방식과 주차 가능 여부를 미리 확인하는 것이 좋습니다. 자세한 내용은 <a href="/check/">이용 전 확인사항</a>과 <a href="/reservation/">예약 안내</a>를 참고하시고, 생활권 단위로 보려면 <a href="/area/jungang-gojan/">중앙역·고잔</a>, <a href="/area/sangnoksu-bono/">상록수·본오</a> 등 <a href="/area/">생활권 안내</a>를 확인하세요.</p>
</section>
""",
)


area_hub = _page(
    path="area/",
    title="안산 생활권 출장마사지｜지역·역 통합 생활권 안내",
    desc="안산 생활권 출장마사지·홈타이 안내. 중앙·고잔, 초지, 안산역·원곡 등 생활권을 확인하세요.",
    h1="안산 생활권 출장마사지·홈타이 안내",
    breadcrumb=[("안산", "/"), ("생활권 안내", "/area/")],
    body="""
<section>
<h2>생활권 기준으로 찾기</h2>
<p>행정구역과 지하철역을 함께 묶은 생활권 기준으로 보면, 실제로 사람들이 이동하고 생활하는 범위에 맞춰 방문 주소와 이동 시간을 더 정확하게 안내받을 수 있습니다. 안산은 같은 동이라도 어느 역·상권에 가까운지에 따라 분위기가 달라지므로 생활권 단위 안내가 유용합니다.</p>
<p>아래 생활권 페이지에서 포함 지역, 가까운 역, 이용 장소별 확인사항과 예약 전 체크리스트를 확인하세요.</p>
</section>

<section>
<h2>단원구 중심 생활권</h2>
<ul>
<li><a href="/area/jungang-gojan/">중앙역·고잔</a> — 안산 도심 상권과 호수공원 주거</li>
<li><a href="/area/choji-dong/">초지역·초지동</a> — 트리플 역세권 신도시</li>
<li><a href="/area/ansan-station-wongok/">안산역·원곡동</a> — 다문화거리·24시간 상권</li>
<li><a href="/area/seonbu-station/">선부역·선부동</a> — 선부 주거 생활권</li>
<li><a href="/area/gojan-shinshi/">고잔신도시</a> — 고잔·호수동 신도시 주거</li>
</ul>
</section>

<section>
<h2>상록구·외곽 생활권</h2>
<ul>
<li><a href="/area/sangnoksu-bono/">상록수·본오</a> — 상록구 최대 주거·상권</li>
<li><a href="/area/hanyang-univ-sa-dong/">한대앞·사동</a> — 대학가·신주거</li>
<li><a href="/area/wolpi-seongu/">월피·성포</a> — 상록구 주거 생활권</li>
<li><a href="/area/banwol-gungun/">반월·건건</a> — 외곽 생활권</li>
<li><a href="/area/wonsi-sihwa/">원시·시화</a> — 산업·외곽권</li>
<li><a href="/area/shinggil-neungil/">신길·능길</a> — 신길동 방면</li>
<li><a href="/area/daebu-island/">대부도</a> — 섬·관광권(차량 이동)</li>
</ul>
</section>

<section>
<h2>생활권 예약 전 확인</h2>
<p>생활권별로 주거·상업·산업 비중이 달라 예약 기준도 조금씩 다릅니다. 방문 전 <a href="/check/">이용 전 확인사항</a>을 확인하고, 역 기준으로 보려면 <a href="/station/">역세권 안내</a>를, 구 단위로 보려면 <a href="/danwon-gu/">단원구</a>·<a href="/sangnok-gu/">상록구</a> 안내를 참고하세요.</p>
</section>
""",
)


PAGES = [station_hub, area_hub]
