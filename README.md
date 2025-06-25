# Browser-Use Test Case Execution

This project automates the execution of test cases using the browser-use agent. The test cases are parsed from a markdown file and executed using the `main.py` script.

## Requirements

- Python 3.8 or higher
- Required Python packages (install via `pip install -r requirements.txt`)
- Environment variables setup in a `.env` file (see below)

## Setup

1. Make sure the required environment variables are set in a `.env` file:
   ```
   PERSONAL_OPENAI_API_KEY=your_openai_api_key
   ```

2. Make the execution script executable:
   ```bash
   chmod +x browser_use/execute_tests.sh
   ```

## Usage

You can run the test cases using either the shell script or directly using Python:

### Using the shell script

```bash
./browser_use/execute_tests.sh test-cases-AG-1.md
```

### Using Python directly

```bash
python browser_use/run_test_cases.py test-cases-AG-1.md
```

## Test Case Format

The script expects test cases in markdown format with the following structure:

```markdown
## Test Case N: Test Case Name

**Test Steps:**
1. Step one description
2. Step two description
3. ...

**Expected Results:**
...
```

The script will extract the test case name and steps, then execute each test case using the browser-use agent.

## Output

For each test case, a history file will be saved with the test case name.
