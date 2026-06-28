#!/usr/bin/env python3
"""Google Indexing API 색인 통보 (구글은 IndexNow 미참여).

사전 준비:
  1) Google Cloud 콘솔에서 'Indexing API' 사용 설정
  2) 서비스 계정 생성 → JSON 키 다운로드 (tools/google-sa.json 로 저장)
  3) Google Search Console 속성에 그 서비스 계정 이메일을 '소유자'로 추가
  4) pip install google-auth

사용:
  python tools/google_index.py
  (또는 GOOGLE_SA_JSON 환경변수로 키 파일 경로 지정)

참고:
  - Indexing API 공식 지원 타입은 JobPosting/BroadcastEvent 이지만 일반 URL도
    널리 사용됩니다. 구글의 표준 권장 경로는 Search Console 사이트맵 제출 +
    URL 검사(색인 요청)입니다.
  - 일일 쿼터(기본 200건)가 있으니 핵심 URL 위주로 통보하세요.
"""
import os
import sys
import xml.etree.ElementTree as ET

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, ROOT)
from content.site import BASE_URL  # noqa: E402

BASE = BASE_URL.rstrip("/")
SA_FILE = os.environ.get("GOOGLE_SA_JSON",
                         os.path.join(os.path.dirname(__file__), "google-sa.json"))
ENDPOINT = "https://indexing.googleapis.com/v3/urlNotifications:publish"
_SM = "{http://www.sitemaps.org/schemas/sitemap/0.9}loc"


def urls_from_sitemap(limit=200):
    local = os.path.join(ROOT, "sitemap.xml")
    root = ET.parse(local).getroot() if os.path.exists(local) else None
    if root is None:
        import urllib.request
        with urllib.request.urlopen(f"{BASE}/sitemap.xml", timeout=30) as r:
            root = ET.fromstring(r.read())
    return [e.text for e in root.iter(_SM)][:limit]


def main():
    if not os.path.exists(SA_FILE):
        print(f"서비스 계정 JSON 필요: {SA_FILE}")
        print("위 '사전 준비' 1~3단계를 먼저 진행하세요.")
        return
    try:
        from google.oauth2 import service_account
        from google.auth.transport.requests import AuthorizedSession
    except ImportError:
        print("pip install google-auth 가 필요합니다.")
        return

    creds = service_account.Credentials.from_service_account_file(
        SA_FILE, scopes=["https://www.googleapis.com/auth/indexing"])
    sess = AuthorizedSession(creds)
    urls = urls_from_sitemap()
    print(f"Google Indexing API: {len(urls)} URLs")
    ok = 0
    for u in urls:
        r = sess.post(ENDPOINT, json={"url": u, "type": "URL_UPDATED"}, timeout=30)
        if r.status_code == 200:
            ok += 1
        else:
            print(f"  {r.status_code} {u} {r.text[:120]}")
    print(f"done: {ok}/{len(urls)} 통보 성공")


if __name__ == "__main__":
    main()
