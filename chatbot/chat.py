from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer

# Create a new chatbot
chatbot = ChatBot('SimpleBot')

# Create a new Trainer for the chatbot
trainer = ChatterBotCorpusTrainer(chatbot)

# Train the chatbot on the English language data
trainer.train('chatterbot.corpus.english')

# Simple interaction loop
print("SimpleBot: Hello! Type 'bye' to exit.")
while True:
    user_input = input("You: ")
    
    # Exit if the user types 'bye'
    if user_input.lower() == 'bye':
        print("SimpleBot: Goodbye!")
        break

    # Get the chatbot's response
    response = chatbot.get_response(user_input)
    
    print(f"SimpleBot: {response}")
