import random
import time
import math

fileName =__file__

responses = {
    "hello": ["Hi there!", "Hello!", "Hey!"],
    "how are you": ["I'm doing great!", "Pretty good, thanks for asking!", "All systems go!"],
    "whats your name": ["I'm ApplesChat!", "You can call me AI!",],
    "bye": ["Goodbye!", "See you later!", "Take care!"],
    "help": ["You can ask me: Hello, How are you, whats your name, bye, time, date, timeOffset, i can calculate numbers, and more!"],
    "date": ["Today's date is " + time.strftime("%Y-%m-%d")],
    "time": ["Your time is " + time.strftime("%H:%M:%S")],
    "toffset": ["Your time offset is " + time.strftime("%z")],
    "tamerican": ["Your time in PM/AM is " + time.strftime("%I:%M %p")],
    "ass": ["That is unnacessary! Please be respectful."],
    "nigger": ["That is unnacessary! Please be respectful."],
    "fucking": ["That is unnacessary! Please be respectful."],
    "give me your file location": [f"My file location is {fileName}"],
}

def calculate_the_given_numbers(user_input):
    result = eval(user_input)
    return f"The result is {result}"

def get_response(user_input):
    user_input = user_input.lower()
    
    for keyword, replies in responses.items():
        if keyword in user_input:
            return random.choice(replies)
    
    return "I'm not sure what you mean. Try asking something else!"

print("AI: Hello! Type 'quit' to exit.\n")

while True:
    user_msg = input("You: ")
    if user_msg.lower() == "quit":
        print("AI: Goodbye!")
        break
    
    reply = get_response(user_msg)
    
    if reply == "I'm not sure what you mean. Try asking something else!":
        reply = calculate_the_given_numbers(user_msg)
    
    print(f"AI: {reply}\n")
