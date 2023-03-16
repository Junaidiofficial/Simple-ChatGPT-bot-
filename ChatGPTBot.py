#Install API package --> pip install openai 

import openai

# Enter OpenAI API Key
openai.api_key = ''

# Environment Variable
default = "text-davinci-003"
tokensamount = 1200


userprompt = "What question do you have for ChatGPT?"
print(userprompt)


#Take question from user
userresponse = input("Type your question here: ")

# Generate response using API
query = openai.Completion.create(
    model=default,
    prompt=userresponse,
    temperature=0.5,
    max_tokens=tokensamount
)


botresponse = query.choices[0].text
print(botresponse)
