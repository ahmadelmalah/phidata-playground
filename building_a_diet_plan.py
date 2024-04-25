from phi.assistant import Assistant
from phi.llm.openai import OpenAIChat

assistant = Assistant(
    llm=OpenAIChat(model="gpt-3.5-turbo"),
    description="You help people with their health and fitness goals.",
    instructions=["Plans should be simple and easy to follow."],
)

# -*- Print the response in markdown format
assistant.print_response(
    "I wanna get back to diet, help me with a basic plan", markdown=True
)
