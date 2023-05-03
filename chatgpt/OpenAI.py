import os
import openai 

openai.api_key = "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"

def main(a):
  messages=[
    {"role": "user", "content": f"{a}"}
  ]
  completion = openai.ChatCompletion.create(
  model="gpt-3.5-turbo",
  messages=messages
  ) 
  answer = completion.choices[0].message.content
  # messages.append({"role": "assistant", "content": answer})
  # print(messages)
  return answer