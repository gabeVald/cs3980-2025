from fastapi import FastAPI
from openai import OpenAI
import os
from dotenv import load_dotenv

load_dotenv()

api_key = os.environ["OPENAI_API_KEY"]
client = OpenAI(api_key=api_key)

app = FastAPI()


@app.get("/")
async def welcome() -> dict:
    return {"msg": "Hello good World!"}


@app.get("/chatbot")
async def chat(message) -> dict:
    if message:
        completion = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {
                    "role": "system",
                    "content": "Sarcastically respond to the user, as if their question is the dumbest thing you've ever heard.",
                },
                {"role": "user", "content": f"{message}"},
            ],
        )
        print(completion)
        return {
            "msg": f"{completion.choices[0].message}",
            "tokens": {completion.usage.completion_tokens},
        }
    else:
        return {"msg": "There isn't a user message!"}
