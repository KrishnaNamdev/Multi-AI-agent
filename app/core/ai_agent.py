from langchain_groq import ChatGroq
from langchain_community.tools.tavily_search import TavilySearchResults

from langchain_core.messages import AIMessage
from langchain.agents import create_agent

from app.config.setting import settings

def get_response_from_ai_agents(llm_id : str, query: str, allow_search: bool = False, system_prompt: str = "") -> str:
    
    llm = ChatGroq(model=llm_id, temperature=0)

    tools = [TavilySearchResults(max_results=3)] if allow_search else []


    agent = create_agent(
        model=llm,
        tools=tools,
        system_prompt=system_prompt
        )

    state = {"messages": query}

    response = agent.invoke(state)

    messages = response.get("messages", [])

    ai_messages = [message for message in messages if isinstance(message, AIMessage)]

    return ai_messages[-1].content if ai_messages else ""