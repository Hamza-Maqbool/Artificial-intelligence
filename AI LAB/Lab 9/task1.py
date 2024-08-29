import random

# Pre-defined responses
responses = {
    "hello": "Hi there! How can I help you today?",
    "traffic": "I'm sorry, I don't have access to real-time map information.",
    "joke": "Why did the scarecrow win an award? Because he was outstanding in his field!",
    "story": "Once upon a time, in a land far, far away..."
}

# Function to handle user input
def chatbot_response(user_input):
    user_input = user_input.lower()  # Convert user input to lowercase for case insensitivity
    response = responses.get(user_input, "I'm not sure how to respond to that.")

    return response

# Main chat loop
print("Chatbot: Hello! Type 'exit' to end the conversation.")
while True:
    user_input = input("You: ")
    if user_input.lower() == "exit":
        print("Chatbot: Goodbye!")
        break
    response = chatbot_response(user_input)
    print("Chatbot:", response)
