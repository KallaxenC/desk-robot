from openai import OpenAI
import os
import tiktoken
import actions
import json

client = OpenAI(
  base_url="https://openrouter.ai/api/v1",
  api_key=os.getenv("DESK_ROBOT_API_KEY"),
)
#VARIABLES
callCount = 0
messages =[]
ai_config = """
You are a robot controller.
Return ONLY valid JSON in this format:
{
  "action": "led_on | led_off | none",
  "response": "a short helpful message to the user"
}
Rules:
- action is for robot control only
- response is for speaking to the user
- do not include any extra text outside JSON
User question: 
"""
encoding = tiktoken.get_encoding("cl100k_base")

def send_message():
  user_Input = input("Message: ")

  if user_Input.lower() == "exit":
    return("abort")

  tokens = len(encoding.encode(user_Input))

  print(f"INPUT Token Count: {tokens}")
  confirm = input("Send message? (y/n): ")
  if confirm.lower() == "y":
    response = client.chat.completions.create(
    model="openai/gpt-4o-mini",
    messages=[
      {
        "role": "user",
        "content": ai_config + user_Input
      }
    ])
    output =response.choices[0].message.content
    cmd = json.loads(output)
    if cmd["action"] == "led_on":
      actions.led_on()
    elif cmd["action"] == "led_off":
      actions.led_off()
    print(f"AI Response: {cmd['response']}")


while True:
  result = send_message()
  if result == "abort":
    break
  callCount +=1
  if callCount >= 10:
    print("Max calls reached. Exiting.")
    break
