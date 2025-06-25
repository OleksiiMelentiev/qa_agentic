from dataclasses import dataclass


@dataclass
class TestCase:
    summary: str
    description: str
    steps: list
    expected_result: str
    priority: str
    type: str
    jira_task: str
