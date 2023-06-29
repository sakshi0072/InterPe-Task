import re

# Define patterns and corresponding responses
patterns = [
    (r"hi|hello|hey", "Hello! How can I assist you?"),
    (r"what is your name", "My name is ChatBot."),
    (r"how are you", "I'm doing well, thank you! How about you?"),
    (r"(.*) (weather|temperature) (.*)", "I'm sorry, I cannot provide weather information."),
    (r"quit|bye|goodbye", "Goodbye! Have a great day!")
]

def chatbot_response(message):
    for pattern, response in patterns:
        match = re.search(pattern, message, re.IGNORECASE)
        if match:
            return response
    return "I'm sorry, I didn't understand. Can you please rephrase?"

# Start the conversation
print("ChatBot: Hello! How can I assist you?")

while True:
    user_input = input("User: ")
    if user_input.lower() == "quit":
        break
    response = chatbot_response(user_input)
    print("ChatBot:", response)
