# Test Analysis and Test Fixing Instruction

## Objective
Automate the initial triage of test failures, focusing exclusively on identifying and fixing issues in the test suite itself.

## Prerequisites/Assumptions
- Access to a test execution environment (e.g., Playwright runner).
- Ability to parse test reports (e.g., JUnit XML, console output).
- Ability to understand and modify code, especially test scripts.

## Step-by-Step Instructions

### 1. Obtain Jira Task Number
- Prompt the user to input the Jira task identifier (e.g., `AG-123`) relevant to the current testing session.

### 2. Find Relevant Test Files
- Identify all test files in the `playwright/tests/` directory whose filenames start with the provided Jira Task prefix (e.g., `AG-123.spec.ts`).

### 3. Run Tests from Matching Files
- Switch to the `playwright` directory:
  ```sh
  cd playwright
  ```
- Execute tests from all files in the `tests/` directory that contain the Jira Task as a prefix in their filename.
- Add the `--reporter=list` flag to the test command for human-readable output:
  ```sh
  npx playwright test tests/AG-123.spec.ts --reporter=list
  ```
  **Note:** Wait for the test command to finish and ensure the full output is displayed before proceeding to the next step. This prevents missing or incomplete test results due to premature analysis.

### 4. Analyze Test Results
- Parse the output produced by the `list` reporter to understand test results, including pass/fail status, error messages, and stack traces.
- Identify and log all failing test cases with details (name, error, stack trace, location).
- Categorize failures using initial heuristics:
  - **Potential Test Issue Indicators:**
    - Assertion errors due to calculation errors in the test
    - FileNotFoundError or similar setup issues
    - Errors in setup/teardown hooks
    - Timeouts in usually fast tests
    - Errors related to mocks, test data, or environment
    - Missing/incorrect test dependencies
    - Explicit notes that the product behavior is correct

### 5. Take Action Based on Analysis
- For each failed test, diagnose the specific line(s) and reason for failure.
- Propose a concrete code change to the test file.
- Present the proposed changes as a code diff or modified code block, with an explanation.

## Example Output

**Test Failure Fix Example:**
```diff
--- a/path/to/your_test_file.py
+++ b/path/to/your_test_file.py
@@ -10,7 +10,7 @@
def test_user_creation_success():
    # ... setup
-    assert created_user.status == "pending"
+    assert created_user.status == "active" # Updated assertion based on new API spec
    # ... more assertions
```
_This test was failing because the status field for newly created users is now 'active' instead of 'pending' according to the latest API documentation. The assertion has been updated accordingly._

## Output/Result
- All test results are analyzed and categorized.
- If a test issue is found, a fix is proposed.
- If unclear, the user is prompted for further analysis.

