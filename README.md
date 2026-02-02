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

GitHub 이슈를 마일스톤 + 서브이슈 구조로 자동 생성

**사용법:**
```
/gh-issue-writer
```

**기능:**
- 마일스톤 생성 (기능 단위)
- 서브이슈 3~5개 생성 (Context/Goal/Tasks 형식)
- 브랜치 네이밍 규칙 적용

## 프로젝트별 커스텀

프로젝트별 설정이 필요하면 해당 프로젝트의 `.claude/skills/`에 추가하세요.
로컬 스킬이 전역 스킬보다 우선 적용됩니다.

## 기여

1. 이 레포를 포크
2. 스킬 추가/수정
3. PR 생성
