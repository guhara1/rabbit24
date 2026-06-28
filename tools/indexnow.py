#!/usr/bin/env python3
"""IndexNow 즉시 색인 통보 (Bing·Naver 등 IndexNow 참여 엔진).

사용:
  1) 사이트를 먼저 배포한다(루트에 <KEY>.txt 키 파일이 라이브여야 함).
  2) python tools/indexnow.py

동작:
  - 로컬 sitemap.xml(빌드 결과) 또는 라이브 sitemap.xml 의 URL 전체를
    IndexNow 엔드포인트로 제출한다. 한 번 호출로 빙·네이버에 즉시 통보된다.
  - api.indexnow.org 는 참여 엔진 전체로 전파한다(네이버·빙 포함).
"""
import json
import os
import sys
import urllib.error
import urllib.request
import xml.etree.ElementTree as ET

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, ROOT)
from content.site import BASE_URL, INDEXNOW_KEY  # noqa: E402

BASE = BASE_URL.rstrip("/")
HOST = BASE.split("//", 1)[-1]
KEY_LOCATION = f"{BASE}/{INDEXNOW_KEY}.txt"
ENDPOINTS = [
    "https://api.indexnow.org/indexnow",       # 참여 엔진 전체로 전파
    "https://searchadvisor.naver.com/indexnow",  # 네이버
    "https://www.bing.com/indexnow",            # 빙
]
_SM = "{http://www.sitemaps.org/schemas/sitemap/0.9}loc"


def urls_from_sitemap():
    local = os.path.join(ROOT, "sitemap.xml")
    if os.path.exists(local):
        root = ET.parse(local).getroot()
    else:
        with urllib.request.urlopen(f"{BASE}/sitemap.xml", timeout=30) as r:
            root = ET.fromstring(r.read())
    return [e.text for e in root.iter(_SM)]


def submit(urls):
    payload = {"host": HOST, "key": INDEXNOW_KEY,
               "keyLocation": KEY_LOCATION, "urlList": urls}
    body = json.dumps(payload).encode("utf-8")
    for ep in ENDPOINTS:
        try:
            req = urllib.request.Request(
                ep, data=body,
                headers={"Content-Type": "application/json; charset=utf-8"},
                method="POST")
            with urllib.request.urlopen(req, timeout=30) as r:
                print(f"  {ep} -> {r.status}")
        except urllib.error.HTTPError as e:
            print(f"  {ep} -> HTTP {e.code}")
        except Exception as e:  # noqa: BLE001
            print(f"  {ep} -> ERR {e}")


def main():
    urls = urls_from_sitemap()
    print(f"IndexNow: {len(urls)} URLs (host={HOST}, key={INDEXNOW_KEY})")
    for i in range(0, len(urls), 10000):  # IndexNow 요청당 최대 10,000
        submit(urls[i:i + 10000])
    print("done")


if __name__ == "__main__":
    main()
