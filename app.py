from flask import Flask, request, jsonify, render_template
from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()

app = Flask(__name__)
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def call_openai_agent(instructions: str, user_input: str) -> str:
    response = client.responses.create(
        model="gpt-4.1-mini",
        instructions=instructions,
        input=user_input
    )
    return response.output_text

def agent_a_planner(user_prompt: str) -> str:
    instructions = (
        "You are Agent A, a planning assistant. "
        "Given a user prompt, produce a clear, bullet-point style plan to write a detailed essay about the prompt "
        "with main steps and substeps, formatted as markdown bullets."
    )
    return call_openai_agent(instructions, user_prompt)

def agent_b_researcher(plan_text: str) -> str:
    instructions = (
        "You are Agent B, a researcher. "
        "Given a plan in bullet point format, do detailed research and expand each step with key points "
        "and brief explanations as nested bullet points in markdown."
    )
    return call_openai_agent(instructions, plan_text)

def agent_c_writer(research_text: str) -> str:
    instructions = (
        "You are Agent C, a writer. "
        "Turn the structured notes into a coherent draft in paragraph form."
    )
    return call_openai_agent(instructions, research_text)

def agent_d_editor(draft_text: str) -> str:
    instructions = (
        "You are Agent D, an editor. "
        "Improve the clarity, flow, and tone of the draft you are given. "
        "Format the text in readable paragraphs separated with blank lines."
        "Return a polished final version that is ready for submission."
    )
    return call_openai_agent(instructions, draft_text)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/run_workflow", methods=["POST"])
def run_workflow():
    data = request.get_json()
    user_prompt = data.get("prompt", "")

    a_out = agent_a_planner(user_prompt)
    b_out = agent_b_researcher(a_out)
    c_out = agent_c_writer(b_out)
    d_out = agent_d_editor(c_out)

    return jsonify({
        "agent_outputs": {
            "A": a_out,
            "B": b_out,
            "C": c_out,
            "D": d_out
        },
        "final": d_out
    })

if __name__ == "__main__":
    app.run(debug=True)
