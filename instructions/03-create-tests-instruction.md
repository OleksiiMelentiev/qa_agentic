# AI Instruction: Playwright Test Generator

## Objective: Generate a single Playwright TypeScript test file for each Jira task, containing all test cases as separate test blocks. The browser_use_output files are provided solely as additional context for the AI to understand the intended browser interactions, but they should NOT be included, imported, or referenced in any way in the final generated Playwright test files.

## Input from User:

jira_ticket: The Jira ticket identifier (e.g., AG-1). This will be used to locate the relevant test cases file.

## Process:

1. Request User Input: Prompt the user to enter the jira_ticket (e.g., AG-1) that corresponds to the set of test cases.

2. Locate Test Cases File: Construct the full path to the test cases file: test_cases/<jira_ticket>.json (e.g., test_cases/AG-1.json).

3. Read Test Cases:
   * Open and read the JSON file specified by test_cases/<jira_ticket>.json.
   * Parse the JSON content. Assume the file contains an array of test case objects. Each test case object should have a name property (e.g., {"name": "test_case_1"}).

4. Generate Playwright Test File:
   * Create a new Playwright TypeScript test file for the current Jira ticket: playwright/tests/<jira_ticket>.spec.ts (e.g., playwright/tests/AG-1.spec.ts).
   * Standard Playwright Setup: Include necessary imports: import { test, expect } from '@playwright/test';
   * For each test_case in the read list, do the following:

     a. (Optional Context for AI) The browser_use_output/<test_case_name>.json file may be provided as context to help the AI understand the intended browser actions for each test case. However, this file is NOT to be included, imported, or referenced in the generated Playwright test file in any way.

     b. Generate Playwright Test Block:
     * Create a test() block for the current test case inside the <jira_ticket>.spec.ts file: test('<test_case_name>', async ({ page }) => { ... });
     * Translate the intended browser actions (as understood from the context or description) into Playwright code within the test() block. This is the core logical step and requires the AI to understand the mapping.
     * Example Mappings:
       * If the intended action is a navigation to a URL: await page.goto('<url>');
       * If the intended action is a click on a selector: await page.locator('<selector>').click();
       * If the intended action is a fill on a selector with value: await page.locator('<selector>').fill('<value>');
       * If the intended action is an assertion (e.g., text content check on selector with expected_text): await expect(page.locator('<selector>')).toHaveText('<expected_text>');
     * Add comments to the generated code for clarity, especially for complex actions or assertions.

   * Save Test File: Save the generated Playwright TypeScript code to playwright/tests/<jira_ticket>.spec.ts.

## Assumptions for AI:

* The test_cases/ directory exists and contains the specified JSON file named <Jira-Ticket>.json.
* The browser output .json files in browser_use_output/ are provided only as additional context for the AI and must NOT be included, imported, or referenced in the generated test files.
* The structure of the test_cases/<Jira-Ticket>.json file is an array of objects, each with a name property.
* The structure of the <test_case_name>.json browser output files is consistent and understandable for mapping to Playwright actions, but again, these files are for AI context only.
* The AI has access to a Playwright-specific knowledge base to correctly translate different types of browser interactions into appropriate Playwright API calls (e.g., click(), fill(), goto(), expect(), locator()).
* The AI should proceed immediately to generate and save the Playwright test file for all test cases found, without asking for further user confirmation

## Error Handling (AI Considerations):

* Handle cases where <Jira-Ticket>.json does not exist in test_cases/.
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

// Note: The above is for AI context only and should not be referenced in the generated test files.
