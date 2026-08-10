from dotenv import load_dotenv
from pydantic import BaseModel
from langchain_openai import ChatOpenAI
from langchain_core.output_parsers import PydanticOutputParser
from langchain_core.prompts import ChatPromptTemplate
from langchain.agents import create_tool_calling_agent, AgentExecutor
from langchain.agents import create_agent

load_dotenv()

class ResearchResponse(BaseModel):
    topic: str
    summary: str
    sources: list[str]
    tools_used: list[str]

llm = ChatOpenAI(model ="gpt-5.4-mini")
# response = llm.invoke("What is the meaning of life?")
# print(response)

parser = PydanticOutputParser(pydantic_object = ResearchResponse)

prompt = ChatPromptTemplate.from_messages(
    [
        (
            "system",
            """
            You are a research assistant that will help generate a reasearch paper.Answer the user query and use necessary tools.Wrap the ouptut in this format and provide no other text\n{format_instructions}
            """
            ,

        ),
        ("placeholder","{chat_history}"),
        ("human","{query}"),
        ("placeholder","{agent_scratchpad}"),
    ]
).partial(format_instruction=parser.get_format_instructions())

agent = create_tool_calling_agent(
    llm = llm,
    prompt = prompt,
    tools = []
)

agent_executor = AgentExecutor(agent=agent,tools=[],verbose=True)

raw_response = agent_executor.invoke({"query":"Whati is the capital of Romania?"})

print(raw_response)

structured_response = parser.parse(raw_response)