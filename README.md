# Browser-Use Test Case Execution

This project automates the execution of test cases using the browser-use agent. The test cases are parsed from a markdown file and executed using the `main.py` script.

## Requirements

### Python

- Python 3.8 or higher
- Install dependencies:
  ```bash
  pip install -r requirements.txt
  ```

## TypeScript/Node.js Requirements

- Node.js (v16 or higher recommended)
- npm (comes with Node.js)
- Install dependencies for Playwright:
  ```bash
  cd playwright
  npm install
  ```

## Setup

### MCPs:
1. Atlassian mcp https://github.com/sooperset/mcp-atlassian

### Browser Use
1. Make sure the required environment variables are set in a `.env` file:
   ```
   PERSONAL_OPENAI_API_KEY=your_openai_api_key
   ```

2. Make the execution script executable:
   ```bash
   chmod +x browser_use/execute_tests.sh
   ```

