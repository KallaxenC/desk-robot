from openai import OpenAI
import os
client = OpenAI(
  base_url="https://openrouter.ai/api/v1",
  api_key=os.getenv("DESK_ROBOT_API_KEY"),
)
user_Input = input("Message: ")
while True:
  if user_Input.lower() == "exit":
    break
  user_Input = user_Input.lower()
  response = client.chat.completions.create(
    model="openai/gpt-4o-mini",
    messages=[
      {
        "role": "user",
        "content": user_Input
      }
    ]
  )
  print(response.choices[0].message.content)
  user_Input = input("Message: ")
  