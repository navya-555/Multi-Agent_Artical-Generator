# Multi-Agent_Artical-Generator

A multi-agent system designed to automate the creation of high-quality articles using advanced AI agents. This project leverages [CrewaAI](https://crewa.ai/), [Streamlit](https://streamlit.io/), and Google GenAI for seamless content generation. The system features specialized agents for planning, writing, and editing articles, ensuring accurate, engaging, and polished output.

## Features

- **Content Planner**: Researches and outlines the article's structure and key points.
- **Content Writer**: Converts the outline into a well-written draft.
- **Editor**: Refines the content for tone, style, and audience appropriateness.
- **Streamlit UI**: Easy-to-use interface for generating articles with a few clicks.

## Usage
1. Open the application in your browser after running the command `Streamlit run app.py`.
2. Enter the topic, word limit, article style, and tone in the UI.
3. Click "Generate" to create an article. The system will research, write, and edit the article automatically.
4. View and copy the final polished article from the UI.

## File Structure
- `agent.py`: Defines the planner, writer, and editor agents and their tasks.
- `crew_handler.py`: Manages the interaction between agents and tasks.
- `app.py`: Streamlit application to interact with the system.
- `pyproject.toml`: Project dependencies and metadata.

## Requirements
- Python 3.12+
- Poetry for dependency management
- API keys for Serper tool and Google GenAI

## Technologies Used
- CrewaAI: Multi-agent orchestration.
- Streamlit: Frontend for the application.
- Google GenAI: Generative AI for natural language tasks.

## License
This project is licensed under the MIT License.
