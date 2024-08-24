import nltk
from nltk.chat.util import Chat, reflections
# Define pairs of patterns and responses
pairs=[
    [
        r"my name is(.*)",
        ["Hello %1, How are you today?",]
    ],
    [
        r"hi|hey|hello",
        ["Hello!","Hey there!",]
    ],
    [
        r"what is your name?",
        ["I am a chatbot",]
    ],
    [
        r"how are you",
        ["I am good. How are you?",]
    ],
    [
        r"sorry(.*)",
        ["It's alright.","No problem.",]
    ],
    [
        r"I am(.*) (good|well|okay|ok)",
        ["Good to know that you're 1%", "How can I help you today?",]
    ],
    [
        r"quit",
        ["Goodbye! Take care.", "See you soon!"]
    ],
    [
        r"(.*)",
        ["I'm not sure how to respond to that. Could you please rephrase?",]
    ],
]
# Create chatbot
def chatbot():
    print("Hi! I am a chatbot, Type 'quit to exit.")
    chat=Chat(pairs, reflections)
    chat.converse()

# Run the chatbot
if __name__=="__main__":
    chatbot()