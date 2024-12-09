from crewai import Agent,Task,Crew,LLM
import streamlit as st
from crewai_tools import SerperDevTool
import os
from langchain_google_genai import ChatGoogleGenerativeAI
from litellm import completion
import warnings
warnings.filterwarnings('ignore')

os.environ['SERPER_API_Key']=st.secrets['serper_api']

llm = LLM(
    api_key=st.secrets['gemini_api'],
    model="gemini/gemini-1.5-flash",
)

search_tool=SerperDevTool()

#Agents

planner = Agent(
    role = 'Content Planner',
    goal = '''Research and extract accurate, concise, and relevant factual information on {topic}.
     Create a detailed outline of key points to structure the article effectively.''',
    tools=[search_tool],
    backstory = '''You are a meticulous researcher who loves uncovering and organizing information.
     You are planning an article on the topic {topic}. You collect information that helps the audience
     learn something new. You prioritize factual accuracy and relevance while extracting information,
     ensuring the foundation of the article is solid.''',
    allow_delegation=False,
    verbose=True,
    llm=llm
)

writer = Agent(
    role = 'Content Writer',
    goal = '''Craft an engaging, well-written article on the topic {topic} using the outline and
     context provided by the Planner. Stay within the specified word limit of {limit} words while maintaining clarity and coherence.''',
    backstory = '''You are a skilled writer writing on the topic {topic} with a talent for turning
     dry facts into compelling narratives. You thrive on transforming structured outlines provided
     by the planner into polished, audience-friendly content. You provide objective and impartial
     insights and back them up with information provided by the planner.
     While writing keep a few things in mind that you are writing for {style} and the number of words should be {limit}.''',
    allow_delegation=False,
    verbose=True,
    llm=llm
)

editor = Agent(
    role = 'Editor',
    goal = '''Refine the article's language, tone, and structure to suit the target audience.
     Ensure the content aligns with the intended tone that is {tone}, and purpose of the piece.''',
    backstory = '''You are a perfectionist editor who takes pride in making every article resonate
     with its audience. With a keen eye for detail, you elevate the text to its best possible version.
     You have to review the article to ensure that it follows the {tone}, provides balanced viewpoints
     and avoids major controversial points when possible.''',
    allow_delegation=False,
    verbose=True,
    llm=llm
)

#Tasks

plan = Task(
    description = '''1.Identify the key aspects of the given topic by performing thorough research.
     2.Extract concise, factual, and relevant information. Avoid opinions or unverified claims.
     3.Create a clear and structured outline highlighting the main points and subpoints for the article.
     4.Ensure the outline logically flows and covers all critical aspects of the topic.
     5.Provide contextual information or keywords that the Writer can expand upon.''',
    expected_output = '''A structured outline (e.g., bullet points) with main headings and subheadings.
     A summary of key factual points for each section.
     A list of important contextual keywords or phrases related to the topic.''',
    agent=planner,
)

write = Task(
    description = '''1.Use the outline and context provided by the Planner to write the article.
     2.Maintain coherence and flow while ensuring each section of the outline is thoroughly addressed.
     3.Adhere strictly to the word limit specified for the article.
     4.Use engaging language suitable for the topic while remaining accessible to the target audience.
     5.Name sections properly in an engaging manner.''',
    expected_output = '''A well-written draft of the article in markdown format covering all points from the outline,
     Engaging, easy-to-read text with a clear structure (introduction, body, and conclusion).''',
    agent=writer
)

edit = Task(
    description = '''1.Review the article for grammatical correctness, spelling, and stylistic consistency.
     2.Adjust the tone, vocabulary, and style to align with the preferences of the target audience.
     3.Ensure the article flows naturally and maintains a professional or engaging voice, as required.
     4.Eliminate unnecessary repetition or overly complex phrasing.
     5.Verify that all information is presented clearly and concisely while retaining factual integrity.''',
    expected_output = '''A polished final version of the article, free from grammatical and stylistic errors, ready for publication in markdown format.
     Text with a consistent tone and style appropriate for the specified audience.
     Enhanced readability and flow while retaining the original meaning and intent of the content.''',
    agent=editor
)

tasks = [plan, write, edit]
agents = [planner, writer, editor]

