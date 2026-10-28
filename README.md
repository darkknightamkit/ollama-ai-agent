
# Amit Yadav's Local AI Agent

### A local AI assistant built with Python, Ollama, and tool calling

**Private by default · Runs locally · Built to learn how AI agents
work**

:::👋 About
Hi, I'm Amit Yadav, a Computer Science Engineering student at KIIT
University. I'm learning and building projects in Python, AI/ML,
Generative AI, and software development.

This repository is a hands-on project for exploring how a local AI agent
works: how a model requests tools, how Python executes those tools, and
how their results are returned to the model.
Project status: Update this section to accurately describe what is
implemented in your current version.

🚀 What it does
- Local language model: Uses Ollama to run a supported model on
  your machine.
- Tool calling: Lets the model request registered Python
  functions.
- Conversation history: Sends previous messages back to the model
  for context (if enabled in your implementation).
- Multi-step tool use: Supports a tool-call loop, with a maximum
  step limit (if implemented).
- Debug trace: Can show tool requests and results to help you
  understand the agent's flow (if implemented).
🧰 Example interaction
You: Tell me the current time and the weather in Bengaluru.

Agent:
1. Requests the current-time tool.
2. Requests the weather tool with city="Bengaluru".
3. Receives the tool results.
4. Uses those results to answer.
The example above illustrates the intended flow. Replace it with output
captured from your own running project.
🛠️ Tech stack
  Technology                          Purpose
  Python                              Agent logic and tool execution

  Ollama                              Runs a local language model

  Qwen3:4B                            Example model; use the model
                                      configured in your project

  OpenAI-compatible API               Interface used by the client to
                                      communicate with Ollama
  JSON tool schemas                   Describe tools and their parameters
⚙️ Quick start
1. Prerequisites
Install Python 3.10+ and Ollama. Start Ollama
before running the agent.
2. Clone the repository
git clone YOUR_REPOSITORY_URL
cd YOUR_REPOSITORY_FOLDER
3. Create and activate a virtual environment
python3 -m venv .venv
source .venv/bin/activate
4. Install dependencies
If your repository contains requirements.txt:
python -m pip install -r requirements.txt
If it does not, install the dependencies listed by your project instead.
5. Download a model
ollama pull qwen3:4b
Make sure the model name matches the one configured in your code.
6. Configure environment variables
Create your local .env file from the example file, if your project
provides one:
cp .env.example .env
Edit .env to match the variable names your code actually reads. For a
local Ollama setup, the values might look like:
BASE_URL=http://127.0.0.1:11434/v1
API_KEY=ollama
MODEL=qwen3:4b
DEBUG=True

These are example values; confirm the variable names and expected
settings in your code. Never commit real secrets in .env.
8. Run the project
Use the entry-point filename from your repository. For example:
python simple_ai_assistant.py
🔧 Available tools
Update this table to match the Python functions registered in your
project.


  Tool                 Purpose                                   Parameters
  get_current_time   Returns the current local date and time   None
  get_city_weather   Gets a short weather report for a city    city
  get_user_city      Returns a configured or detected city     None

  
🧠 How tool calling works


1. The model receives context: Your messages, system instructions,
   and tool definitions are sent to the model.
2. The model requests a tool: It returns a tool name and arguments,
   such as get_city_weather({"city": "Bengaluru"}).
3. Python executes the function: Your program validates the request
   and calls the matching registered function.
4. The result goes back to the model: Python adds the tool result
   to the conversation.
5. The model responds: It may request another tool or produce a
   final answer.
   
Important: The model requests tools; your Python program executes
them.
            

Edit the checklist as you complete features.
📚 Learning resources
- Ollama documentation
- Python documentation
- AI Fundamentals playlist
- Advanced AI playlist
Replace the playlist placeholders with the resources you actually use.
👨‍💻 About me
Amit Yadav
B.Tech, Computer Science Engineering --- KIIT University
- GitHub:
  https://github.com/darkknightamkit
- LinkedIn: https://www.linkedin.com/in/amit-yadav-a47501202?utm_source=share_via&utm_content=profile&utm_medium=member_android


SPECIAL THANKS TO CODESTORYWITHMIK BHAIYA 


🤝 Contributing
Suggestions and improvements are welcome. Open an issue to discuss a
change or submit a pull request.
📄 License
This project is licensed under the MIT License if you include an MIT
LICENSE file. Otherwise, update this section to match your chosen
license.
