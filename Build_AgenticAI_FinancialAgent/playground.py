#Combine the code into single file to integrate with Phidata Platform
from phi.agent import Agent
import phi.api
from phi.model.groq import Groq
from phi.tools.yfinance import YFinanceTools
from phi.tools.duckduckgo import DuckDuckGo #Enables Agent to search the web for information

import os
from dotenv import load_dotenv
load_dotenv()
import pathlib
from phi.playground import Playground,serve_playground_app

#Import API Keys for PHIDATA and GROQ
#if using google colab
#from google.colab import userdata
#GROQ_API_KEY=userdata.get('GROQ_API_KEY')
#PHI_API_KEY=userdata.get('PHI_API_KEY')

#os.environ["GROQ_API_KEY"] = GROQ_API_KEY # Setting the Groq API key as an environment variable
#os.environ["PHI_API_KEY"] = PHI_API_KEY # Setting the Groq API key as an environment variable

phi.api = os.getenv('PHI_API_KEY')
GROQ_API_KEY = os.getenv('GROQ_API_KEY')


## Web search Agent 
web_search_agent = Agent(
    name ="Web Search Agent",
    role = "Search the web for the information",
    model = Groq(id='llama3-groq-70b-8192-tool-use-preview'),
    tools = [DuckDuckGo()],
    instructions = ['Always include sources'],
    show_tool_calls = True,
    markdown = True
)

## Financial Agent
finance_agent = Agent(
    name = "Finance AI Agent",
    model =Groq(id='llama3-groq-70b-8192-tool-use-preview'),
    tools = [
        YFinanceTools( stock_price=True,analyst_recommendations=True, stock_fundamentals = True,company_news = True)
        ],
    instructions = ['Use Tables to display the datasources'],
    show_tool_calls = True,
    markdown = True
)



## Create App

app = Playground(agents = [finance_agent,web_search_agent]).get_app()

if __name__ == "__main__":
    serve_playground_app("playground:app",reload=True)

