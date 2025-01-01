#Combine the code into single file to integrate with Phidata Platform
from phi.agent import Agent
import phi.api
from phi.model.groq import Groq
from phi.tools.yfinance import YFinanceTools
from phi.tools.duckduckgo import DuckDuckGo #Enables Agent to search the web for information