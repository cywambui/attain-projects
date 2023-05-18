import openai
#openai is a package that is neccesary for the use of api's

openai.api_key = "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"

# defines the first system message
system_message = "You are an AI."


messages = [
    {"role": "system", "content": system_message}
]

# iterate to have a conversation until an interruption is encountered
while True:
    # gets users prompt
    user_input = input("User: ")

    # checks if the user wants to exit from the conversation and exits even if the words are in uppercase and exits
    if user_input.lower() == "exit":
        break

    # adds user inut message to the conversation
    messages.append({"role": "user", "content": user_input})

    # responsible for making request to the ai api and receiving response
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=messages
    )#gpt 3.5 turbo is an api model 

    # gets the assistant's reply to the user according the prompt given
    ai_reply = response.choices[0].message.content

    # prints the assistant's reply
    print("AI:", ai_reply)

    # add assistant's reply to the conversation
    messages.append({"role": "assistant", "content": ai_reply})
