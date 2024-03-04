# Example: reuse your existing OpenAI setup
from openai import OpenAI


# Point to the local server
def generate_score(symbol):
    client = OpenAI(base_url="http://localhost:1234/v1", api_key="not-needed")
    completion = client.chat.completions.create(
    model="local-model", # this field is currently unused
    response_format={ "type": "json_object" },
    messages=[
        {"role": "system", "content": "you are a referee in charge of explaining to players of Magic The Gathering what the rules are and how things interact in the game"},
        {"role": "user", "content": f"Generate an ESG score for {symbol}, if you aren't sure give your best guess, only respond with JSON"}
    ],
    temperature=0.7,
    )
    return completion.choices[0].message.content



print(generate_score("NVIDIA"))