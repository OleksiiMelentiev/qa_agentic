AI Instructions: Test Case Processing

This document outlines the steps for an AI to process test cases from a user-provided Jira ticket number.
Main Goal:

To process all test cases for a given Jira ticket by running a single command that takes the ticket number as input. The AI should only ask the user for the Jira ticket number (e.g., AG-1), construct the filename, and then execute the script with that filename as the argument.



Instructions:

    1. Obtain Jira Ticket Number:
        Action: Request the user to provide the Jira ticket number (e.g., AG-1) if not.
        Context: The process cannot proceed unless the user provides a Jira ticket number. Always prompt the user to supply the ticket number if it is not given.
        * jira_ticket: The Jira ticket number (e.g., AG-1) that identifies the test case file.

    2. Construct Test Case File Name:
        Action: Build the file name as <jira_ticket>.json (e.g., AG-1.json).
        Context: The file should be located in the test_cases/ directory.
        * file_path: test_cases/<jira_ticket>.json

    3. Execute main.py:
        Action: Run the following command, replacing <file_full_name> with the full path of the file constructed from the Jira ticket number.
        ./browser_use/.venv/bin/python browser_use/main.py <file_full_name>
        ** crucial: use ./browser_use/.venv/bin/python as env to run. Don't try to use any other env
        ** crucial: don't use python3
        

Example Workflow:

Let's assume the user provides a Jira ticket number AG-1:

The constructed file name is: test_cases/AG-1.json

The command to run is:

./browser_use/.venv/bin/python browser_use/main.py User/full/path/test_cases/AG-1.json

This approach ensures all test cases for the specified Jira ticket are processed in a single execution, using the constructed filename.