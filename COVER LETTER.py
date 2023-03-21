import json
import os
import openai
openai.api_key = "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"
#user information
name= "My name is "+ input("Your name is:")
user_job="I want to apply for the position of "+input("What job do you want to apply for?:")
years_of_experience="I have "+input("How many years of experience do you have?:")+" years of experience"
company="The company I am applying at is "+input("What company are you applying at?:")
bsc_degree="I have a Bachelor's degree in"+input("What do you have a Bachelor's degree in?:")
personal_achievements=input("What are your personal achievements in relation to this profession?: ")
university="I graduated from "+input("What university did you graduate from?:")
extra_info=input("Is there any other information you would like to be included?")
response = openai.Completion.create(
  model="text-davinci-003",
  prompt="Create a cover letter using "+name+"+ "+user_job+" + "+years_of_experience+"+"+company+"+"+bsc_degree+"+"+personal_achievements+"+"+university,
#prompt="Generate a cover letter using this text:\n\ntext:" + name + "\n\ntext:" + user_job + " \n\ntext:" + years_of_experience +" \n\ntext:" + bsc_degree+"\n\nCover Letter:",
  temperature=0,
  max_tokens=1024,
  top_p=1.0,
  frequency_penalty=0.0,
  presence_penalty=0.0,
  stop=None
)
#to print the prompt only
data = json.loads(str(response))
text = data['choices'][0]['text']
print(text)
