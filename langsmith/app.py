import openai
from langsmith.wrappers import wrap_openai
from langsmith import traceable

client = wrap_openai(openai.Client())

@traceable
def pipeline(user_input: str):
        result = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "user", "content": user_input}
            ]
        )
        print(result.choices[0].message.content)
        return result.choices[0].message.content

pipeline("What is the capital of France?")