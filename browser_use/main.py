import os
import sys
import asyncio

from browser_use import Agent
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

from src.history_helper import save_history
from src.files_helper import read_test_cases_from_file

load_dotenv()


async def execute_browser_script_async(test_name, test_scenario):
    # url = os.environ.get("AZURE_OPENAI_ENDPOINT")
    key = os.environ.get("PERSONAL_OPENAI_API_KEY")
    agent = Agent(
        task=test_scenario,
        llm=ChatOpenAI(
            model="gpt-4o",
            api_key=key,
        )
    )

    history = await agent.run()
    filename = save_history(history, test_name)
    await agent.close()
    print(f"browser-use task completed. Results saved to {filename}")


async def main():
    file_name = sys.argv[1]
    tests = read_test_cases_from_file(file_name)

    for test in tests:
        test_scenario = "\n".join(test.steps) + "\n" + test.expected_result
        await execute_browser_script_async(test.summary, test_scenario)


if __name__ == "__main__":
    asyncio.run(main())
