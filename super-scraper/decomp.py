import datetime
from typing import Literal, Optional, Tuple
from langchain.output_parsers import PydanticToolsParser
from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI
from langchain_core.pydantic_v1 import BaseModel, Field

# Get question
question = ""

# create base class  that will define our query
#
class ParaphrasedQuery(BaseModel):
    """You have performed query expansion to generate a paraphrasing of a question."""

    paraphrased_query: str = Field(
        ...,
        description="A unique paraphrasing of the original question.",
    )
# define the system propmpt to guide the llm
system = """
###Add system prompt for generating focused question on elections 
"""
prompt = ChatPromptTemplate.from_messages(
    [
        ("system", system),
        ("human", "{question}"),
    ]
)
# set the llm model
llm = ChatOpenAI(model="gpt-3.5-turbo-0125", temperature=0)

llm_with_tools = llm.bind_tools([ParaphrasedQuery])
# setup the chain
queries = prompt | llm_with_tools | PydanticToolsParser(tools=[ParaphrasedQuery])
# Run
questions = queries.invoke({"question":question})
print(  questions)