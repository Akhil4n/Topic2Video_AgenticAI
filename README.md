# Multi-Agent Workflow AI Project

## Overview
This project demonstrates a user-initiated AI workflow built with four distinct AI agents sequenced to process user prompts: planning, researching, drafting, and editing. Using OpenAI's API, each agent performs a specific task to transform the input progressively. The system includes a graphical web interface built with Flask and JavaScript for users to enter prompt and view each agents action.

## Features
- Four distinct AI agents forming a sequential workflow (planner → researcher → writer → editor)
- User submits prompts via a web GUI; results display step-by-step outputs dynamically
- Backend built on Flask serving API endpoints and the web interface
- OpenAI GPT-4.1-mini model integration for AI agent tasks
- Easy API key management via a `.env` file and python-dotenv

### Setup
1. Clone or download the repository.
2. Create a `.env` file in the root directory with your OpenAI API key:
OPENAI_API_KEY=your-real-api-key-here
3. Install Python dependencies:
pip install -r requirements.txt

## Running

Start the Flask server:

python app.py


Open your browser and go to:

http://127.0.0.1:5000/


Enter a prompt and click **Run Workflow** to see how the AI agents process your input step-by-step.

## Project Structure

| Path               | Purpose                                     |
|--------------------|---------------------------------------------|
| `app.py`           | Flask backend and AI agent orchestration    |
| `.env`             | Stores your OpenAI API key                   |
| `requirements.txt`  | Python packages required                      |
| `templates/index.html` | Frontend GUI (HTML + vanilla JS)          |

## Output Formatting

- Agents A and B produce markdown-style bullet lists, rendered in `<pre>` blocks for readability.
- Agents C and D output formatted paragraphs with line breaks preserved via innerHTML rendering on the frontend.

## Troubleshooting

- Ensure `.env` is properly configured with a valid API key.
- Confirm dependencies are installed with compatible versions.
- Check console logs for error details if the workflow fails.
- Verify network connectivity to OpenAI API endpoints.
