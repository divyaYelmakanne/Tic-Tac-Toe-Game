from nltk.chat.util import Chat, reflections

pairs=[
    [r'hi', ['hii']],
    [r'hii|hey|hello', ['hii i am there']],
    [r'how are you', ['i am fine and hoping you good']],
    [r'what is your name', ['My name is chatbot']],
    [r'who invented you', ['i am invented by divya yelmakanne']],
    [r'who is your boss', ['my boss is divya yelmakanne']],
    [r'what can you tell for viewers', ['Hello, lets connect with DIVA YELMAKANNE']],
    [r'are you mad', ['nice joke']],
    [r'sorry', ['machine can have feelings at all its ok.']],
    [r'what is python', ['it is a programming language']],
    [r'can you help me', ['Of course! What do you need help with?']],
    [r'will you be my friend', ["I’d love to be your friend! I’m here to chat, help with questions, and support you however I can."]],
    [r'thank you', ["You’re welcome! Anytime you need to talk or have questions, just let me know. What’s up?"]]
]

chat=Chat(pairs, reflections)
chat.converse()

def quit1():
    print("hii i am chatbot ask me something")

if __name__ == "__main__":
    quit1()
