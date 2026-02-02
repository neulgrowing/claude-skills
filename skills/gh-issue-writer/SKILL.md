---
name: gh-issue-writer
description: 기능 요구를 입력받아 마일스톤과 서브이슈를 생성하고 gh CLI 명령을 실행한다
---

# 목적

사용자가 기능 요구를 주면 다음을 생성한다:
1. 마일스톤 1개 (기능 단위)
2. 서브이슈 3~5개 (각 이슈는 Context/Goal/Tasks 포함)
3. gh CLI 명령으로 실제 이슈 생성

# 프로젝트 설정

## GitHub 저장소
- repo: 현재 프로젝트의 원격 저장소 (`git remote get-url origin`으로 확인)
- organization 멤버: `gh api orgs/{org}/members`로 확인

## 라벨
- `feature`: 새로운 기능
- `fix`: 버그 수정
- `docs`: 문서 작업
- `refactor`: 리팩토링

# 이슈 구조

## 마일스톤 (기능 단위)
- 이름: `{PREFIX}-XX 기능명` (예: `RES-01 DB 선정 및 연결`)
- PREFIX는 프로젝트별로 다름 (프로젝트 README 또는 사용자에게 확인)
- 설명: 기능의 Goal 요약

## 서브이슈 (작업 단위)
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

# 브랜치 네이밍 규칙

- 형식: `{type}/{prefix}-xx`
- 예시: `feature/res-01`, `fix/res-02`

| 요청 내용 | 타입 | 브랜치 prefix |
|----------|------|---------------|
| 새 기능 추가 | feature | `feature/` |
| 버그 수정 | fix | `fix/` |
| 긴급 수정 | hotfix | `hotfix/` |
| 리팩토링 | refactor | `refactor/` |
| 문서 작업 | docs | `docs/` |

# 이슈 생성 시 옵션

- `--assignee`: 담당자 GitHub ID
- `--label`: 라벨 (feature, fix, docs, refactor)
- `--milestone`: 마일스톤 이름
- 마감기한: 이슈 본문에 `Due: YYYY-MM-DD` 형식으로 추가

# 사용 전 확인사항

1. 현재 레포 확인: `git remote get-url origin`
2. 이슈 PREFIX 확인: 사용자에게 물어보거나 기존 이슈/마일스톤에서 확인
3. 다음 마일스톤 번호 확인: `gh api repos/{owner}/{repo}/milestones`

# 입력 형식

사용자가 간단하게 요청하면 AI가 프로젝트 컨텍스트를 파악하여 자동으로 생성한다.

예시:
- "Google OAuth 로그인 기능 이슈 만들어줘"
- "LLM 통합 시스템 필요해, 마일스톤이랑 서브이슈 생성해줘"

# gh CLI 명령 예시

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
