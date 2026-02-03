# Claude Skills

팀 공유용 AI 어시스턴트 스킬 모음

## 지원 도구

| 도구 | 전역 경로 | 상태 |
|------|----------|------|
| Claude Code | `~/.claude/skills/` | ✅ 지원 |
| Codex (OpenAI) | `~/.codex/` | ✅ 지원 |
| Cursor | `~/.cursorrules` | ✅ 지원 |

## 설치

### Claude Code 사용자

```bash
# 기존 ~/.claude 백업 (있는 경우)
mv ~/.claude ~/.claude.bak

# 클론
git clone https://github.com/neulgrowing/claude-skills.git ~/.claude

# 업데이트
cd ~/.claude && git pull
```

### Codex 사용자

```bash
# ~/.codex에 심볼릭 링크 생성
ln -s ~/.claude/codex ~/.codex
```

### Cursor 사용자

```bash
# ~/.cursorrules에 심볼릭 링크 생성
ln -s ~/.claude/.cursorrules ~/.cursorrules
```

## 스킬 목록

### gh-issue-writer

GitHub 이슈를 **요청 규모에 따라** 자동 생성

**사용법:**
```
/gh-issue-writer
```

**요청 규모 판단:**

| 규모 | 판단 기준 | 생성 결과 |
|------|----------|----------|
| **Large** | 여러 작업 단위로 나눠야 하는 기능 | 마일스톤 + 서브이슈 3~5개 |
| **Small** | 단일 작업으로 완료 가능한 기능/개선 | 단일 이슈 |
| **Bug** | 버그 수정 | 단일 이슈 (label: bug) |

**예시:**
- Large: "OAuth 로그인 시스템 구축" → 마일스톤 + 서브이슈
- Small: "로그아웃 버튼 추가" → 단일 이슈
- Bug: "토큰 만료 시 500 에러" → 단일 이슈 (bug 라벨)

**기능:**
- 요청 규모에 따라 마일스톤 + 서브이슈 또는 단일 이슈 생성
- Context/Goal/Tasks 형식의 이슈 본문
- 브랜치 네이밍 규칙: `{type}/{prefix}-xx`
- 프로젝트별 PREFIX 자동 감지 (예: RES, PRJ 등)

## 프로젝트별 커스텀

프로젝트별 설정이 필요하면 해당 프로젝트의 `.claude/skills/`에 추가하세요.
로컬 스킬이 전역 스킬보다 우선 적용됩니다.

**프로젝트별 설정 예시:**
- GitHub 저장소 이름
- 이슈 PREFIX (예: RES, PRJ)
- 조직 멤버 목록
- 라벨 목록

## 기여

1. 이 레포를 포크
2. 스킬 추가/수정
3. PR 생성
