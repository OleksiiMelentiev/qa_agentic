# Test Analysis, Bug Creation, and Test Fixing Instruction

## Objective
Automate the triage of test failures: run tests, analyze results, and create Jira bugs for failed tests using MCP, focusing on capturing all relevant failure details.

## Prerequisites/Assumptions
- Access to a test execution environment (e.g., Playwright runner).
- Ability to parse test reports (e.g., JUnit XML, console output).
- Ability to understand and modify code, especially test scripts.
- Access to Jira via MCP (Machine Control Platform) for automated bug creation.

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
- **Important:**  
  - **Wait for Completion:** The test command may take some time to run. Do not proceed, analyze, or interact with the output until you see the Playwright summary line with `X failed` and `Y passed` (where X and Y are numbers).  
  - **Do Not Interrupt:** Ensure the process is not interrupted and allow it to finish naturally, even if there are delays or other messages in the output.
  - **Ignore Non-Test Errors:** If you encounter any errors or warnings related to PSReadLine or PowerShell (such as initialization errors, module load failures, or similar), ignore these messages. They are not related to the Playwright test results.  
  - **Proceed Only After Summary:** Only after the summary line appears should you continue to the next step.

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

### 5. Create Jira Bugs for Failed Tests (via MCP)
- For each failed test case, automatically create a Jira bug using MCP with the following details:
  - Test case name
  - Error message and stack trace
  - Test file and location
  - Steps to reproduce (if available)
  - Any relevant logs or screenshots
- Ensure the bug summary and description are clear and actionable.
- Link the bug to the relevant Jira task identifier.
- Log the created Jira issue key for each failure.

### 6. Take Action Based on Analysis
- For each failed test, diagnose the specific line(s) and reason for failure.
- Propose a concrete code change to the test file if the issue is in the test itself.
- Present the proposed changes as a code diff or modified code block, with an explanation.

## Example Output

**Jira Bug Creation Example:**
```
Jira Bug Created: AG-1234
Summary: Test 'test_user_creation_success' failed due to assertion error
Description:
Test case: test_user_creation_success
File: tests/AG-123.spec.ts
Error: AssertionError: expected 'pending' but got 'active'
Stack trace: ...
Steps to reproduce: Run the test suite with ...
Linked to: AG-123
```

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
- For each failed test, a Jira bug is created via MCP with full details.
- If a test issue is found, a fix is proposed.
- If unclear, the user is prompted for further analysis. 