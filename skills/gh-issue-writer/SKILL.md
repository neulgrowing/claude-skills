---
name: gh-issue-writer
description: 기능 요구를 입력받아 마일스톤과 서브이슈를 생성하고 gh CLI 명령을 실행한다
---

# 목적

사용자가 기능 요구를 주면 **요청 규모에 따라** 적절한 이슈를 생성한다.

# 요청 규모 판단

| 규모 | 판단 기준 | 생성 결과 |
|------|----------|----------|
| **Large** | 여러 작업 단위로 나눠야 하는 기능 | 마일스톤 + 서브이슈 3~5개 |
| **Small** | 단일 작업으로 완료 가능한 기능/개선 | 단일 이슈 |
| **Bug** | 버그 수정 | 단일 이슈 (label: bug) |

**예시:**
- Large: "OAuth 로그인 시스템 구축", "LLM 통합 파이프라인"
- Small: "로그아웃 버튼 추가", "에러 메시지 개선"
- Bug: "토큰 만료 시 500 에러 발생", "한글 깨짐 현상"

# 프로젝트 설정

## GitHub 저장소
- repo: 현재 프로젝트의 원격 저장소 (`git remote get-url origin`으로 확인)
- organization 멤버: `gh api orgs/{org}/members`로 확인

## 라벨
- `feature`: 새로운 기능
- `bug`: 버그 수정
- `docs`: 문서 작업
- `refactor`: 리팩토링

# 이슈 구조

## Large: 마일스톤 + 서브이슈

### 마일스톤
- 이름: `{PREFIX}-XX 기능명` (예: `RES-01 DB 선정 및 연결`)
- PREFIX는 프로젝트별로 다름 (프로젝트 README 또는 사용자에게 확인)
- 설명: 기능의 Goal 요약

### 서브이슈
- 타이틀: `[{PREFIX}-XX-Y] 작업명` (예: `[RES-01-1] PostgreSQL 연결 설정`)
- 본문 형식:
```markdown
## Context
왜 이 작업이 필요한가

## Goal
이 작업의 목표

## Tasks
- [ ] 체크리스트 항목 1
- [ ] 체크리스트 항목 2
- [ ] 체크리스트 항목 3
```

## Small / Bug: 단일 이슈

- 타이틀: `[{PREFIX}-XX] 작업명` (예: `[RES-15] 로그아웃 버튼 추가`)
- 마일스톤 없이 독립 이슈로 생성
- 본문 형식:
```markdown
## Context
왜 이 작업이 필요한가

## Goal
이 작업의 목표

## Tasks
- [ ] 체크리스트 항목 1
- [ ] 체크리스트 항목 2
```

# 브랜치 네이밍 규칙

- 형식: `{type}/{prefix}-xx`
- 예시: `feature/res-01`, `fix/res-15`

| 요청 내용 | 타입 | 브랜치 prefix |
|----------|------|---------------|
| 새 기능 추가 | feature | `feature/` |
| 버그 수정 | fix | `fix/` |
| 긴급 수정 | hotfix | `hotfix/` |
| 리팩토링 | refactor | `refactor/` |
| 문서 작업 | docs | `docs/` |

# 이슈 생성 시 옵션

- `--assignee`: 담당자 GitHub ID
- `--label`: 라벨 (feature, bug, docs, refactor)
- `--milestone`: 마일스톤 이름 (Large인 경우만)
- 마감기한: 이슈 본문에 `Due: YYYY-MM-DD` 형식으로 추가

# 사용 전 확인사항

1. 현재 레포 확인: `git remote get-url origin`
2. 이슈 PREFIX 확인: 사용자에게 물어보거나 기존 이슈/마일스톤에서 확인
3. 다음 이슈 번호 확인: `gh api repos/{owner}/{repo}/milestones` 또는 `gh issue list`

# 입력 형식

사용자가 간단하게 요청하면 AI가 **규모를 판단**하여 자동으로 생성한다.

예시:
- "Google OAuth 로그인 기능 이슈 만들어줘" → Large
- "로그아웃 버튼 추가해줘" → Small
- "토큰 갱신 안되는 버그 이슈 등록해줘" → Bug

# gh CLI 명령 예시

## Large (마일스톤 + 서브이슈)

```bash
# 0. 현재 레포 확인
REPO=$(gh repo view --json nameWithOwner -q .nameWithOwner)

# 1. 마일스톤 생성
gh api repos/$REPO/milestones -X POST \
  -f title="{PREFIX}-01 기능명" \
  -f description="기능 Goal 요약"

# 2. 서브이슈 생성
gh issue create --repo $REPO \
  --title "[{PREFIX}-01-1] 작업명" \
  --body "## Context
왜 이 작업이 필요한가

## Goal
이 작업의 목표

## Tasks
- [ ] 체크리스트 항목 1
- [ ] 체크리스트 항목 2
- [ ] 체크리스트 항목 3" \
  --label "feature" \
  --milestone "{PREFIX}-01 기능명"
```

## Small (단일 이슈)

```bash
REPO=$(gh repo view --json nameWithOwner -q .nameWithOwner)

gh issue create --repo $REPO \
  --title "[{PREFIX}-15] 로그아웃 버튼 추가" \
  --body "## Context
사용자가 로그아웃할 수 있는 UI가 없음

## Goal
헤더에 로그아웃 버튼 추가

## Tasks
- [ ] 헤더 컴포넌트에 로그아웃 버튼 추가
- [ ] 로그아웃 API 호출 연결" \
  --label "feature"
```

## Bug (버그 이슈)

```bash
REPO=$(gh repo view --json nameWithOwner -q .nameWithOwner)

gh issue create --repo $REPO \
  --title "[{PREFIX}-16] 토큰 만료 시 500 에러 발생" \
  --body "## Context
JWT 토큰 만료 시 500 Internal Server Error 반환됨

## Goal
401 Unauthorized 응답으로 수정

## Tasks
- [ ] 토큰 검증 로직에서 만료 예외 처리
- [ ] 적절한 에러 응답 반환" \
  --label "bug"
```
