from openai import OpenAI
from secret import API_DEEPSEEK as DEEP

client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key=DEEP,
)

completion = client.chat.completions.create(
    extra_body={},
    model="deepseek/deepseek-r1:free",
    messages=[{"role": "user", "content": "Cual es la capital de Peru?"}],
)

print(completion.choices[0].message.content)
