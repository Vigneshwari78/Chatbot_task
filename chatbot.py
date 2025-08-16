class ChatBot:
    def __init__(self,role):
        self.role=role
        self.context=[]

    def chats(self,name,user_input=None):
        if self.role!="chatbot":
            return "Please provide a role"
        
        if user_input:
            self.context.append(user_input)
            return f"{name}, you said {user_input}.Anything else?"
        else:
            return f"Hello,{name}.How can I help you toda?"
        

chat=ChatBot("chatbot")

name=input("Please tell me your name:")
print(chat.chats(name))

user_input=input()
print(chat.chats(name,user_input))