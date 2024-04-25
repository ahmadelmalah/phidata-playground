from phi.assistant import Assistant
from phi.tools.python import PythonTools
from phi.llm.openai import OpenAIChat

pt = PythonTools()
assistant = Assistant(
    tools=[pt],
    show_tool_calls=True,
    llm=OpenAIChat(model="gpt-3.5-turbo"),
    description="You are a Python assistant that helps with Python programming.",
    instructions=["Please provide clear and concise instructions."],
)
assistant.print_response(
    "Write a python script for fibonacci series and display the result till the 10th number",
    markdown=True,
)
