# Playwright Test Generator Instruction

## Objective
Generate a single Playwright TypeScript test file for each Jira task, containing all test cases as separate test blocks.

## Prerequisites/Assumptions
- The `test_cases/` directory exists and contains the specified JSON file named `<Jira-Ticket>.json`.
- The browser output `.json` files in `browser_use_output/` are provided only as additional context for the AI and must NOT be included, imported, or referenced in the generated test files.
- The structure of the `test_cases/<Jira-Ticket>.json` file is an array of objects, each with a `name` property.
- The structure of the `<test_case_name>.json` browser output files is consistent and understandable for mapping to Playwright actions, but again, these files are for AI context only.
- The AI has access to a Playwright-specific knowledge base to correctly translate different types of browser interactions into appropriate Playwright API calls (e.g., `click()`, `fill()`, `goto()`, `expect()`, `locator()`).

## Step-by-Step Instructions

### 1. Obtain Jira Ticket Number
- Prompt the user to enter the Jira ticket (e.g., `AG-1`) that corresponds to the set of test cases.

### 2. Locate Test Cases File
- Construct the full path to the test cases file: `test_cases/<jira_ticket>.json` (e.g., `test_cases/AG-1.json`).

### 3. Read Test Cases
- Open and read the JSON file specified by `test_cases/<jira_ticket>.json`.
- Parse the JSON content. Assume the file contains an array of test case objects. Each test case object should have a `name` property (e.g., `{ "name": "test_case_1" }`).

### 4. Generate Playwright Test File
- Create a new Playwright TypeScript test file for the current Jira ticket: `playwright/tests/<jira_ticket>.spec.ts` (e.g., `playwright/tests/AG-1.spec.ts`).
- Standard Playwright Setup: Include necessary imports: `import { test, expect } from '@playwright/test';`
- For each test case in the list:
  - (Optional Context) The `browser_use_output/<test_case_name>.json` file may be provided as context to help the AI understand the intended browser actions for each test case. However, this file is NOT to be included, imported, or referenced in the generated Playwright test file in any way.
  - Generate a `test()` block for the current test case inside the `<jira_ticket>.spec.ts` file: `test('<test_case_name>', async ({ page }) => { ... });`
  - Translate the intended browser actions (as understood from the context or description) into Playwright code within the `test()` block.
  - Example Mappings:
    - Navigation: `await page.goto('<url>');`
    - Click: `await page.locator('<selector>').click();`
    - Fill: `await page.locator('<selector>').fill('<value>');`
    - Assertion: `await expect(page.locator('<selector>')).toHaveText('<expected_text>');`
  - Add comments to the generated code for clarity, especially for complex actions or assertions.
- Save the generated Playwright TypeScript code to `playwright/tests/<jira_ticket>.spec.ts`.

## Example Workflow

Suppose the user provides the Jira ticket number `AG-1`:
- The file `test_cases/AG-1.json` is read and parsed.
- For each test case, a Playwright test block is generated in `playwright/tests/AG-1.spec.ts`.
- The resulting file contains all test cases as separate test blocks.

## Error Handling/Edge Cases
- Handle cases where `<Jira-Ticket>.json` does not exist in `test_cases/`.
- Provide informative feedback to the user in case of errors.

## Output/Result
- A Playwright TypeScript test file named `<jira_ticket>.spec.ts` in the `playwright/tests/` directory, containing all test cases as separate test blocks.
