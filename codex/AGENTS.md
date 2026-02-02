# GitHub Issue Writer Agent

GitHub 이슈를 마일스톤 + 서브이슈 구조로 자동 생성하는 에이전트

## 트리거

사용자가 다음과 같이 요청할 때 활성화:
- "이슈 만들어줘"
- "기능 이슈 생성해줘"
- "마일스톤 생성해줘"

## 이슈 구조

### 마일스톤 (기능 단위)
- 이름: `{PREFIX}-XX 기능명`
- PREFIX는 프로젝트별로 다름 (사용자에게 확인)

### 서브이슈 (작업 단위)
- 타이틀: `[{PREFIX}-XX-Y] 작업명`
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

## 브랜치 네이밍

- `feature/{prefix}-xx` - 새 기능
- `fix/{prefix}-xx` - 버그 수정
- `hotfix/{prefix}-xx` - 긴급 수정
- `refactor/{prefix}-xx` - 리팩토링
- `docs/{prefix}-xx` - 문서 작업

## 라벨

- `feature`: 새로운 기능
- `fix`: 버그 수정
- `docs`: 문서 작업
- `refactor`: 리팩토링

## 사용 전 확인

1. 현재 레포: `git remote get-url origin`
2. 이슈 PREFIX: 사용자에게 확인
3. 마일스톤 번호: `gh api repos/{owner}/{repo}/milestones`
