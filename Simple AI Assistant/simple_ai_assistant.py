# standard library imports
import os
from types import SimpleNamespace

# Third-party imports
from httpcore import stream
from openai import OpenAI
from dotenv import load_dotenv

# Local modules
from tools import TOOLS, run_tool
from Utilites.utilites import log


load_dotenv() #by default looks for .env file

client = OpenAI(
    base_url=os.getenv("BASE_URL"),
    api_key=os.getenv("API_KEY")
)

messages = []

# Safety limit: the max number of model rounds for ONE user question
MAX_STEPS = 5

messages.append(
    {
        "role" : "system",
        "content": "Act like a very humble agent Answer general questions(programming,math,sciience,history,advice)"
        "from you own knowledge use a tool only when the user ask current time,weather ,city keep the answer under 100 words"
    }
)

def stream_chat(history):
    response_stream = client.chat.completions.create(
        model=os.getenv("MODEL"),
        messages=history,
        tools=TOOLS,
        stream=True,
    )
    full_response = ""
    calls = {}
    label_printed = False

    try:
        for chunk in response_stream:
            if not chunk.choices:
                continue

            delta = chunk.choices[0].delta

            if delta.content:
                if not label_printed:
                    print("🤖 Assistant: ", end="", flush=True)
                    label_printed = True
                print(delta.content, end="", flush=True)
                full_response += delta.content

            for tc in (delta.tool_calls or []):
                obj = calls.setdefault(
                    tc.index,
                    SimpleNamespace(
                        id=None,
                        function=SimpleNamespace(name="", arguments=""),
                    ),
                )
                if tc.id:
                    obj.id = tc.id
                if tc.function and tc.function.name:
                    obj.function.name += tc.function.name
                if tc.function and tc.function.arguments:
                    obj.function.arguments += tc.function.arguments

    except KeyboardInterrupt:
        print("\n{the streaming is stooped by the user}")

    if label_printed:
        print()  # Print a newline after the assistant's response

    calls_list = []
    for key in sorted(calls):
            calls_list.append(calls[key])
    return full_response, calls_list   


def build_tool_calls_payload(tool_calls):
  


    payload = []
    for tool_call in tool_calls:
                tool_call_dict = {
                    "id" : tool_call.id,
                    "type" : "function",
                    "function" : {
                        "name" : tool_call.function.name,
                        "arguments" :tool_call.function.arguments,
                    }
                }    
                payload.append(tool_call_dict)

    return payload  

            


# Chat loop starts from here
while True:

    user_input = input("\n👦🏻 Amit: ")
    
    if user_input.lower() in ["exit", "quit", "bye", "goodbye"]:
        break

    messages.append(
        {
            "role": "user",
            "content": user_input
        }
    )

    # Chained Tool Calling
    for step in range(MAX_STEPS):
        full_response,tool_calls = stream_chat(messages)

       # msg = response.choices[0].message
       
        if not tool_calls:
            break

        log(f"Step {step + 1}: model requested {len(tool_calls)} tool calls")

        messages.append({
           "role" :"assistant",
           "content" : full_response,
           "tool_calls" : build_tool_calls_payload(tool_calls)
       })

        for tool_call in tool_calls:
            result = run_tool(tool_call)
            messages.append({
                "role": "tool",
                "tool_call_id" : tool_call.id,
                "content" : str(result),
            })

    else:
        # Ran out of steps: The model never gave the final answer
        fallback = "Sorry, I could not finish this within the step limit."
        messages.append({
            "role": "assistant",
            "content": fallback
        })
        print("🤖 Assistant: " + fallback)
        continue