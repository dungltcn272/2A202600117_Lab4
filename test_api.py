from dotenv import load_dotenv
load_dotenv()
from langchain_openai import ChatOpenAI


llm = ChatOpenAI(model="gpt-4o-mini")
print(llm.invoke("xin chào").content)