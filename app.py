import os
from dotenv import load_dotenv
from groq import Groq

load_dotenv()

client = Groq(
    api_key=os.environ.get("GROQ_API_KEY"),
)

system_prompt = "Your name is Axiom, and you are a personal assistant of an AI Developer who is a bit of a sarcastic and humorous in nature."

history = [{
    "role": "system",
    "content": system_prompt
}]

while True:

    user_input = input("What do you want to do?")

    if user_input.lower() == "exit":
        print("Exiting...")
        break

    history.append({
        "role": "user",
        "content": user_input
    })

    llm_response = client.chat.completions.create(
        messages=history,
        model="llama-3.3-70b-versatile",
    )

    response_text = llm_response.choices[0].message.content

    print(response_text)

    history.append({
        "role": "assistant",
        "content": response_text
    })
