import sys
import yaml
import random

def parse_feature_spec(spec_text):
    # feature_spec 블록을 YAML로 파싱
    try:
        spec = yaml.safe_load(spec_text)
        return spec
    except yaml.YAMLError as e:
        return {"error": str(e)}

def generate_main_issue(spec):
    title = spec.get('title', 'Untitled Feature')
    body = f"""# {title}

## Context
{spec.get('context', 'N/A')}

## Goal
{spec.get('goal', 'N/A')}

## Non-Goal
{spec.get('non_goal', 'N/A')}

## Scope In
{spec.get('scope_in', 'N/A')}

## Scope Out
{spec.get('scope_out', 'N/A')}

## Acceptance Criteria
{spec.get('acceptance_criteria', 'N/A')}

## Risk
{spec.get('risk', 'N/A')}

## Data I/O
{spec.get('data_io', 'N/A')}

## API Changes
{spec.get('api_changes', 'N/A')}

## Testing Expectations
{spec.get('testing_expectations', 'N/A')}

## Notes
{spec.get('notes', 'N/A')}

## Assignee
{spec.get('assignee', 'N/A')}

## Labels
{spec.get('labels', 'N/A')}
"""
    return title, body

def generate_sub_issues(spec, num_sub_issues=8):
    acceptance = spec.get('acceptance_criteria', '')
    # 간단히 acceptance_criteria를 줄로 나누어 서브 이슈 생성
    criteria_lines = [line.strip() for line in acceptance.split('\n') if line.strip()]
    if not criteria_lines:
        criteria_lines = ['Implement feature part 1', 'Implement feature part 2', 'Test implementation', 'Deploy and verify']

    sub_issues = []
    for i in range(min(num_sub_issues, len(criteria_lines))):
        sub_title = f"Sub-task {i+1}: {criteria_lines[i][:50]}..."
        num_checkboxes = random.randint(3, 8)
        checkboxes = '\n'.join([f"- [ ] Task {j+1}" for j in range(num_checkboxes)])
        sub_body = f"""## Description
{criteria_lines[i]}

## Checklist
{checkboxes}

## Definition of Done
- [ ] Code reviewed
- [ ] Tests passed
- [ ] Documentation updated
"""
        sub_issues.append((sub_title, sub_body))
    return sub_issues

def generate_gh_commands(repo, assignee, labels, main_title, main_body, sub_issues):
    commands = []
    # 메인 이슈
    assignee_str = f"--assignee {assignee}" if assignee else ""
    labels_str = f"--label {labels}" if labels else ""
    body_escaped = main_body.replace('"', '\\"').replace('\n', '\\n')
    cmd = f'gh issue create --title "{main_title}" --body "{body_escaped}" {assignee_str} {labels_str} --repo {repo}'
    commands.append(cmd)
    
    # 서브 이슈들
    for sub_title, sub_body in sub_issues:
        body_escaped = sub_body.replace('"', '\\"').replace('\n', '\\n')
        cmd = f'gh issue create --title "{sub_title}" --body "{body_escaped}" {assignee_str} {labels_str} --repo {repo}'
        commands.append(cmd)
    
    return commands

def main():
    # 입력은 feature_spec 블록
    input_text = sys.stdin.read()
    # ```feature_spec ... ``` 추출
    start = input_text.find('```feature_spec')
    end = input_text.find('```', start + 1)
    if start == -1 or end == -1:
        print("Error: feature_spec block not found")
        return
    spec_text = input_text[start:end].replace('```feature_spec', '').strip()
    
    spec = parse_feature_spec(spec_text)
    if 'error' in spec:
        print(f"Error parsing spec: {spec['error']}")
        return
    
    repo = spec.get('repo', 'owner/repo')
    assignee = spec.get('assignee', '')
    labels = spec.get('labels', '')
    
    # 메인 이슈 생성
    main_title, main_body = generate_main_issue(spec)
    print("### Main Issue")
    print(main_body)
    print()
    
    # 서브 이슈 생성
    num_sub = random.randint(5, 12)
    sub_issues = generate_sub_issues(spec, num_sub)
    for i, (sub_title, sub_body) in enumerate(sub_issues):
        print(f"### Sub Issue {i+1}")
        print(f"**Title:** {sub_title}")
        print(sub_body)
        print()
    
    # gh 명령 생성
    commands = generate_gh_commands(repo, assignee, labels, main_title, main_body, sub_issues)
    print("### GH CLI Commands")
    for cmd in commands:
        print(cmd)
        print()

if __name__ == "__main__":
    main()