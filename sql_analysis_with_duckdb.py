from phi.assistant import Assistant
from phi.tools.duckdb import DuckDbTools
from phi.llm.openai import OpenAIChat


assistant = Assistant(
    llm=OpenAIChat(model="gpt-3.5-turbo"),
    tools=[DuckDbTools()],
    show_tool_calls=True,
    system_prompt="Use this file for Movies data: https://phidata-public.s3.amazonaws.com/demo_data/IMDB-Movie-Data.csv",
)
assistant.print_response(
    "What is the average rating of movies?", markdown=True, stream=False
)

pip_install_package = "duckdb"
