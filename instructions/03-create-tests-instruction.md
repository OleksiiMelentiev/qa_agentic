AI Instruction: Playwright Test Generator

Objective: Generate Playwright TypeScript tests for each test case within a specified Jira task, utilizing pre-recorded browser interaction outputs.

Input from User:

jira_ticket: The Jira ticket identifier (e.g., AG-1). This will be used to locate the relevant test cases file.

Process:

1. Request User Input: Prompt the user to enter the jira_ticket (e.g., AG-1) that corresponds to the set of test cases.

2. Locate Test Cases File: Construct the full path to the test cases file: test_cases/<jira_ticket>_TestCases.json (e.g., test_cases/AG-1_TestCases.json).

3. Read Test Cases:
   * Open and read the JSON file specified by test_cases/<jira_ticket>_TestCases.json.
   * Parse the JSON content. Assume the file contains an array of test case objects. Each test case object should have a name property (e.g., {"name": "test_case_1"}).

4. Iterate Through Test Cases: For each test_case in the read list:

   a. Identify Output File:
   * Construct the name of the corresponding browser output file: browser_use_output/<test_case_name>.json. (e.g., if test_case.name is "login scenario", the output file would be "browser_use_output/login_scenario.json").

   b. Load Browser Output:
   * Open and read the JSON file specified by browser_use_output/<test_case_name>.json.
   * Parse the JSON content. This file is assumed to contain a structured representation of browser actions (e.g., navigations, clicks, input fills, assertions). The specific structure needs to be defined for the AI to interpret it. For example, it could be an array of objects, where each object has a type (e.g., "navigate", "click", "fill", "assert"), and other relevant properties.

   c. Generate Playwright Test Code:
   * Create a new Playwright TypeScript test file for the current test case (e.g., tests/<test_case_name>.spec.ts).
   * Standard Playwright Setup: Include necessary imports: import { test, expect } from '@playwright/test';
   * Test Block: Create a test() block for the current test case: test('<test_case_name>', async ({ page }) => { ... });
   * Translate Browser Output to Playwright Actions: Based on the parsed browser output from step 4b, generate the corresponding Playwright code within the test() block. This is the core logical step and requires the AI to understand the mapping.
   * Example Mappings:
     * If browser output indicates a "navigate" action to url: await page.goto('<url>');
     * If browser output indicates a "click" action on a selector: await page.locator('<selector>').click();
     * If browser output indicates a "fill" action on a selector with value: await page.locator('<selector>').fill('<value>');
     * If browser output indicates an "assertion" (e.g., "text_content_check" on selector with expected_text): await expect(page.locator('<selector>')).toHaveText('<expected_text>');
   * Add comments to the generated code for clarity, especially for complex actions or assertions.
   * Save Test File: Save the generated Playwright TypeScript code to tests/<test_case_name>.spec.ts.

Assumptions for AI:

* The test_cases/ directory exists and contains the specified JSON file named <Jira-Ticket>_TestCases.json.
* The browser output .json files are located in the browser_use_output directory.
* The structure of the test_cases/<Jira-Ticket>_TestCases.json file is an array of objects, each with a name property.
* The structure of the <test_case_name>.json browser output files is consistent and understandable for mapping to Playwright actions. You may need to provide the AI with a schema or examples of this structure.
* The AI has access to a Playwright-specific knowledge base to correctly translate different types of browser interactions into appropriate Playwright API calls (e.g., click(), fill(), goto(), expect(), locator()).
* The AI should proceed immediately to generate and save the Playwright test files for all test cases found, without asking for further user confirmation

Error Handling (AI Considerations):

* Handle cases where <Jira-Ticket>_TestCases.json does not exist in test_cases/.
* Handle cases where a browser_use_output/<test_case_name>.json file is missing or corrupted.
* Provide informative feedback to the user in case of errors.

Example of Browser Output Structure (for AI understanding):

// Example of a browser_use_output/<test_case_name>.json file
[
  {
    "type": "navigate",
    "url": "https://www.example.com"
  },
  {
    "type": "fill",
    "selector": "#username",
    "value": "testuser"
  },
  {
    "type": "fill",
    "selector": "#password",
    "value": "password123"
  },
  {
    "type": "click",
    "selector": "#loginButton"
  },
  {
    "type": "assert_text",
    "selector": "#welcomeMessage",
    "expected_text": "Welcome, testuser!"
  }
]
