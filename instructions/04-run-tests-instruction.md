# AI Test Analysis and Bug Reporting Instruction

This document outlines the process for the AI to run tests, analyze their results, and determine the appropriate subsequent action: fixing tests, reporting bugs, or seeking user clarification.

## Goal
The primary goal is to automate the initial triage of test failures, distinguishing between issues originating from the test suite itself and those indicating a product defect.

## Prerequisites and Setup (Assumed Capabilities)
For this process, the AI is assumed to have access to and the capability to use the following:

Test Execution Environment: A method to execute test files provided as context (e.g., an integrated test runner, the ability to invoke language-specific testing frameworks).

Test Result Parser: The ability to parse test reports (e.g., JUnit XML, console output) to extract:

Overall pass/fail status

Individual test case pass/fail status

Error messages and stack traces for failures

Duration of tests (for potential flakiness detection)

Atlassian MCP Integration: Access to Atlassian Jira via a pre-configured API (e.g., atlassian_mcp_api.create_issue) with the necessary authentication and permissions to create bug tickets.

Code Editing/Analysis Capabilities: The ability to understand and modify code, especially test scripts.

## Core Process
Follow these steps sequentially upon receiving a request to run and analyze tests:

Step 0: Prompt for Jira Task
Prompt the user to input the Jira task identifier (e.g., AG-123) that is relevant to the current testing session.

Step 1: Find Relevant Test Files
Identify all test files in the 'playwright/tests/' directory whose filenames start with the provided Jira Task prefix (e.g., AG-123.spec.ts).

Step 2: Run Tests from Matching Files
Execute tests from all files in the 'playwright/tests/' directory that contain the Jira Task as a prefix in their filename.

Step 3: Analyze Test Results
Parse Results: Process the captured output and test reports.

Action: Parse test results.

Identify Failures: List all failing test cases. For each failure, extract:

Test case name/identifier

Full error message

Stack trace

File and line number of the failure point.

Action: Identify and log all failing test cases with details (name, error, stack trace, location).

Categorize Failures (Initial Heuristics): Based on error messages and stack traces, attempt a preliminary categorization.

Potential Test Issue Indicators:

Assertion errors where the expected/actual values are clearly mismatched due to obvious calculation errors in the test.

FileNotFoundError or similar issues pointing to test setup resources.

Errors within setUp/tearDown or beforeEach/afterEach methods.

Timeouts in tests that are usually fast, suggesting test flakiness or environmental issues rather than a core product bug.

Errors related to mock objects, test data generation, or test environment configuration.

Errors indicating a missing or incorrect test dependency.

Errors explicitly stating "Test failed due to X, but product behavior seems correct" (if such details are in the test output).

Potential Product Bug Indicators:

Errors originating deep within product code (not test framework or test utility code).

Unhandled exceptions (e.g., NullPointerException, IndexOutOfBoundsException, TypeError) from product logic.

Logical failures where the product's output directly contradicts a clear requirement (e.g., "Expected status to be 'active' but got 'inactive'").

Crashes or unexpected termination of the application under test.

Step 4: Decision Logic
For each failed test:

Determine Problem Origin: Based on the analysis in Step 3, decide if the problem is primarily:

Problem is in the Test: Clear evidence points to a fault in the test script (e.g., incorrect assertion, setup, data).

Problem is in the Product (Bug): Clear evidence points to a defect in the application code.

Unclear: Cannot definitively determine if the issue is with the test or the product, or if both are contributing.

Step 5: Action: Fix Test (If Problem is in Test)
If the decision for a failed test is "Problem is in the Test":

Diagnose Test Issue: Pinpoint the specific line(s) and reason for the test failure. Common reasons include:

Incorrect assertion logic.

Invalid test data or setup.

Flaky test due to race conditions or timing issues.

Outdated expected values.

Missing test environment configuration.

Suggest Fix: Propose a concrete code change to the test file.

Action: Suggesting a fix for test: [test_name] in [file_path].

Output: Present the proposed changes as a code diff or directly modified code block, along with an explanation of why the fix is being applied.

Example Output:

```diff
--- a/path/to/your_test_file.py
+++ b/path/to/your_test_file.py
@@ -10,7 +10,7 @@
 def test_user_creation_success():
     # ... setup
-    assert created_user.status == "pending"
+    assert created_user.status == "active" # Updated assertion based on new API spec
     # ... more assertions

This test was failing because the status field for newly created users is now 'active' instead of 'pending' according to the latest API documentation. The assertion has been updated accordingly.
```

Step 6: Action: Create Bug Report (If Problem is in the Product)
If the decision for a failed test is "Problem is in the Product (Bug)":

Create Bug Report: Use Playwright MCP to create a bug report in Jira, including all relevant details from the test failure (test name, error message, stack trace, and any other context).

Action: Create a Jira bug report using Playwright MCP for the product issue.

Step 7: Action: User Analysis Required (If Problem is Unclear)
If the decision for a failed test is "Unclear":

Ask User for Input: Present the analysis and results to the user, and request that the user analyze the results and choose the next steps (e.g., whether to treat as a test issue, a product bug, or provide more information).

Action: Ask the user to analyze the results and choose the next steps if the problem origin is unclear.

