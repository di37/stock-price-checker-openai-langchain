import os, sys
from os.path import dirname as up

sys.path.append(os.path.abspath(os.path.join(up(__file__), os.pardir)))

import openai
from dotenv import load_dotenv

import yfinance as yf

from langchain.tools import BaseTool
from typing import Optional, Type, List
from langchain.agents import initialize_agent, Tool, AgentType
from langchain.chat_models import ChatOpenAI
from langchain.schema import HumanMessage, AIMessage, ChatMessage, FunctionMessage
from langchain.tools import MoveFileTool, format_tool_to_openai_function

from pydantic import BaseModel, Field
from datetime import datetime, timedelta

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

