import os
from dotenv import load_dotenv
from crewai import Agent, Task, Crew, Process
from crewai.task import TaskOutput
from langchain_community.tools import DuckDuckGoSearchRun
from langchain.agents import load_tools
from langchain_community.tools.wikidata.tool import WikidataAPIWrapper, WikidataQueryRun
from langchain.tools import WikipediaQueryRun
from langchain_community.utilities import WikipediaAPIWrapper

load_dotenv()
openai_key = os.getenv("OPENAI_API_KEY")
openai_model = os.getenv("OPENAI_MODEL_NAME")
os.environ["OPENAI_MODEL_NAME"]= openai_model
os.environ["OPENAI_API_KEY"]= openai_key

search_tool = DuckDuckGoSearchRun()
wikipedia_tool = WikipediaQueryRun(api_wrapper=WikipediaAPIWrapper())
wikidata_tool = WikidataQueryRun(api_wrapper=WikidataAPIWrapper())

# Political advisor Role
# domain expert

# use agent to search for queries





researcher = Agent(
  role='Political Researcher',
  goal="""Collect a large number of facts on the city""",
  backstory="""You are political researcher that gathers facts about areas to help campaigns create a plan of attack.""",
  verbose=True,
  allow_delegation=False,
)


manager = Agent(
  role='Campaign Manager',
  goal="""Receive all the information and create a detailed report on the city of Gainesville, Florida from a political standpoint with hard facts."
    """,
  backstory="""You are a renowned campaign manager. You can analyze an election and come up with a path to victory, creating reports to help others understand the area and the population.""",
  verbose=True,
  allow_delegation=False,
)

def callback_function(output: TaskOutput):
    # Do something after a task is completed
    print(f"""
        Task completed!
        Task: {output.description}
        Output: {output.raw_output}
    """)


task1 = Task(
  description="""Search the web to gather information on Gainesville, Florida.
    It's important for us to consider facts about Gainesville that will help us understand the political climate of the city
""",
  expected_output="A list of facts",
  callback=callback_function,
  agent= researcher,
  tools=[search_tool, wikidata_tool, wikipedia_tool]
)

task2 = Task(
  description="""Take the data provided and write a detailed report to help an election campaign come up with a plan to win.  
    """,
  agent=manager,
  expected_output="A report on the city",
  tools=[],
  callback=callback_function,
  context=[task1]
)


# Instantiate your crew with a sequential process
crew = Crew(
  agents=[researcher, manager],
  tasks=[task1, task2],
  process=Process.sequential,
  verbose=2
)
result = crew.kickoff()

print("######################")
print(result)
