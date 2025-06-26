# Jira Test Case Generation Instruction

## Objective
Automate the generation, formatting, and saving of test cases from Jira task details.

## Prerequisites/Assumptions
- Access to a pre-configured Jira MCP API endpoint (e.g., GET /api/jira/task/{jiraTaskNumber}).
- Authentication tokens are handled or available.
- The `test_cases/` directory exists or can be created.

## Step-by-Step Instructions

### 1. Obtain Jira Task Number
- **Check Initial Prompt:** Inspect the user's prompt for a Jira task number (format: `[PROJECT_KEY]-[NUMBER]`, e.g., `ABC-1234`).
- **If Missing:**
  - Prompt the user: _"Please provide the Jira task number (e.g., ABC-1234) for which you'd like to generate test cases."_
  - Wait for user input.

### 2. Fetch Jira Task Details
- Use the Jira MCP API to fetch details for the provided Jira task number.
- **Error Handling:**
  - If the API call fails or the task number is invalid, inform the user and return to Step 1.

### 3. Analyze Task Details and Generate Test Cases
- **Parse Acceptance Criteria/Requirements:**
  - Identify fields like Description, Acceptance Criteria, or custom fields.
  - Decompose into individual, actionable test cases using:
    - Bullet points, numbered lists, or distinct sentences.
    - Keywords (e.g., "User can", "System should", "When X then Y").
    - Logical implications and edge cases.
- **Define Test Case Components:**
  - **Summary/Title:** Concise, descriptive title.
  - **Preconditions:** (If applicable) Conditions required before execution.
  - **Test Steps:** Numbered sequence of actions. _Always add 'navigate to URL' as the first step, with the specific URL._
  - **Expected Result:** Anticipated outcome.
  - **Priority:** High, Medium, or Low.
  - **Type:** Functional, UI, Performance, Security, etc.
  - **Jira Task Link:** Store the original Jira task number.

### 4. Format Test Cases for Output
- Map components to a clear, human-readable format:
  - **summary:** Title
  - **description:** Detailed explanation or preconditions
  - **steps:** Array of strings (first step: 'navigate to URL' with the full URL)
  - **expected_result:** Anticipated outcome
  - **priority:** High/Medium/Low
  - **type:** Functional/UI/Performance/Security
  - **jira_task:** Jira task number
  - **(Other relevant metadata as needed)**
- **If URL is unclear:** Ask the user to provide the full page URL.

### 5. Save Generated Test Cases to JSON File
- Serialize test cases as a JSON array (each test case is a JSON object with the above fields).
- **File Naming:** Use only the Jira task number (e.g., `test_cases/ABC-1234.json`).
- **Ensure Directory:** Create `test_cases/` if it does not exist.
- **Save File:** Place the JSON file in the `test_cases/` directory.

## Example Workflow

**User:**
> Generate test cases for ABC-1234.

**AI:**
- Identifies `ABC-1234`.
- Calls Jira API.
- Parses Description/Acceptance Criteria.
- Creates Test Case 1, Test Case 2, ...
- Formats as a JSON array.
- Saves as `test_cases/ABC-1234.json`.
- _"Test cases for ABC-1234 have been successfully generated and saved as ABC-1234.json."_

**User:**
> Generate test cases for login.

**AI:**
- No Jira task number found.
- _"Please provide the Jira task number (e.g., ABC-1234) for which you'd like to generate test cases."_

**User:**
> Sorry, it's DEF-5678.

**AI:**
- Identifies `DEF-5678` and continues from Step 2.

## Output/Result
- A JSON file named `[JiraTaskNumber].json` in the `test_cases/` directory, containing an array of test case objects with all required fields.