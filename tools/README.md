# 색인(인덱싱) 도구

빌드(`python3 build.py`) 시 루트에 다음이 함께 생성됩니다.

- `sitemap.xml` — 색인 대상 URL(우선순위·lastmod 포함)
- `feed.xml` — RSS 2.0 피드(검색엔진 콘텐츠 발견 가속)
- `robots.txt` — `Sitemap:` 지시 포함
- `<INDEXNOW_KEY>.txt` — IndexNow 키 검증 파일

## 1) 가장 빠른 색인 통보 흐름

1. **배포**: 변경 후 푸시 → Cloudflare Pages 배포(루트에 키 파일이 라이브여야 함).
2. **빙·네이버 즉시 통보(IndexNow)**:
   ```bash
   python tools/indexnow.py
   ```
   sitemap.xml의 모든 URL을 IndexNow(빙·네이버 등)로 즉시 통보합니다.
3. **구글**(IndexNow 미참여):
   - 표준 경로: **Google Search Console**에 `sitemap.xml` 제출 + URL 검사로 색인 요청.
   - 자동화(선택): `tools/google_index.py` (서비스 계정 필요, 파일 상단 안내 참고).

## 2) 검색엔진 등록(최초 1회)

- **네이버 서치어드바이저**: 사이트 등록 → 소유확인은 `<head>`의
  `naver-site-verification` 메타로 자동 처리됨(이미 적용) → `sitemap.xml`/`feed.xml` 제출.
- **구글 Search Console**: 속성 추가 → 소유확인(HTML 태그 발급 시
  `content/site.py`의 `GOOGLE_SITE_VERIFICATION`에 입력 후 재빌드) → `sitemap.xml` 제출.

## 3) 글/페이지 추가할 때마다

1. `python3 build.py` → 2. 푸시·배포 → 3. `python tools/indexnow.py`
   (구글은 Search Console에서 해당 URL '색인 요청').

> 참고: 과거의 sitemap ping(google.com/ping, bing.com/ping)은 두 엔진 모두
> 폐기했습니다. 현재 가장 빠른 경로는 **IndexNow(빙·네이버)** + **GSC 제출/요청(구글)** 입니다.
