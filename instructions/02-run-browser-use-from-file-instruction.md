# Test Case Processing Instruction

## Objective
Process all test cases for a given Jira ticket by running a single command that takes the ticket number as input.

## Prerequisites/Assumptions
- The `test_cases/` directory exists and contains the relevant JSON file.
- The Python environment is located at `./browser_use/.venv/bin/python` (do not use any other environment or `python3`).

## Step-by-Step Instructions

### 1. Obtain Jira Ticket Number
- Request the user to provide the Jira ticket number (e.g., `AG-1`) if not already given.
- The process cannot proceed without this input.

### 2. Construct Test Case File Name
- Build the file name as `<jira_ticket>.json` (e.g., `AG-1.json`).
- The file should be located in the `test_cases/` directory.
- Example: `test_cases/AG-1.json`

### 3. Execute main.py
- Run the following command, replacing `<file_full_name>` with the full path to the constructed file:

```sh
./browser_use/.venv/bin/python browser_use/main.py <file_full_name>
```

- **Important:**
  - Use only `./browser_use/.venv/bin/python` as the environment.
  - Do not use `python3` or any other Python environment.

## Example Workflow

Suppose the user provides the Jira ticket number `AG-1`:

- The constructed file name is: `test_cases/AG-1.json`
- The command to run is:

```sh
./browser_use/.venv/bin/python browser_use/main.py /User/full/path/test_cases/AG-1.json
```

This approach ensures all test cases for the specified Jira ticket are processed in a single execution, using the constructed filename.

## Output/Result
- All test cases for the specified Jira ticket are processed by the script, using the provided JSON file as input.