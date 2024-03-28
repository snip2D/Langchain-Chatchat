# LangChain 的 ArxivQueryRun 工具
from chatchat.server.pydantic_v1 import Field
from .tools_registry import regist_tool


@regist_tool
def arxiv(query: str = Field(description="The search query title")):
    '''A wrapper around Arxiv.org for searching and retrieving scientific articles in various fields.'''
    from langchain.tools.arxiv.tool import ArxivQueryRun

    tool = ArxivQueryRun()
    return tool.run(tool_input=query)
