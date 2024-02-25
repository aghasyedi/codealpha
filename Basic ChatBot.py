import random
import spacy

nlp = spacy.load("en_core_web_sm")
responses = {
    "hi": ["Hello!", "Hi there!", "Hey!", "Hi, how can I assist you?", "Greetings!", "Hey, what's up?", "Hi! Nice to see you.", "Hello, how are you doing?", "Hey, how's it going?", "Hi! How may I help you today?"],
    "how_are_you": ["I'm good, thank you!", "I'm doing well, thanks for asking.", "All good!", "I'm great, how about you?", "Pretty good, thanks!", "Doing fine, how about yourself?", "I'm alright, thank you!", "Not too bad, thanks for asking.", "I'm doing well, how can I assist you?", "I'm good, what can I do for you?"],
    "name": ["I'm just a chatbot.", "I don't really have a name.", "You can call me Chatbot.", "I go by Chatbot.", "I'm your friendly neighborhood chatbot.", "I'm a nameless AI assistant.", "Names aren't really my thing.", "You can call me whatever you like.", "I'm your virtual assistant, without a name.", "You can refer to me as Chatbot."],
    "bye": ["Goodbye!", "See you later!", "Bye! Take care!", "Farewell!", "Until next time!", "Catch you later!", "Bye bye!", "Have a great day!", "Goodbye! Come back soon.", "Take care!"],
    "thanks": ["You're welcome!", "No problem!", "My pleasure!", "Glad I could assist!", "Anytime!", "Happy to help!", "Don't mention it!", "No worries!", "It was nothing!", "You got it!"],
    "about_chatbot": ["I'm a chatbot designed to assist you.", "I'm here to help with your queries.", "I'm an AI designed to chat with you.", "I'm your virtual assistant.", "I'm programmed to respond to your messages.", "I'm a conversational agent.", "I'm an artificial intelligence designed to engage in conversation.", "I'm a chatbot built to assist users like you.", "I'm here to provide support and answer your questions.", "I'm an AI chatbot created to interact with users."],
    "thanks_response": ["You're welcome!", "Glad I could assist!", "No problem!", "Anytime!", "You're welcome! Is there anything else I can help with?", "My pleasure! Let me know if there's anything else I can assist you with.", "Don't mention it! If you have any more questions, feel free to ask.", "No worries! If you need further assistance, just let me know.", "Happy to help! If you have any more inquiries, feel free to ask.", "It was nothing! Let me know if there's anything else I can do for you."],
    "about_user": ["Tell me about yourself.", "What do you like to do?", "What are your hobbies?", "What's your favorite thing to do?", "Describe yourself.", "What are your interests?", "Can you tell me more about yourself?", "What makes you unique?", "What do you enjoy doing?", "Tell me something about you."],
    "about_weather": ["What's the weather like today?", "Can you give me the weather forecast?", "How's the weather outside?", "Is it going to rain today?", "What's the temperature right now?", "Tell me about the weather conditions.", "Can you provide me with the weather update?", "Is it sunny outside?", "What's the weather forecast for tomorrow?", "How's the weather been lately?"],
    "joke": ["Why don't scientists trust atoms? Because they make up everything!", "I told my wife she was drawing her eyebrows too high. She looked surprised.", "Parallel lines have so much in common. It’s a shame they’ll never meet.", "What's orange and sounds like a parrot? A carrot!", "Why did the scarecrow win an award? Because he was outstanding in his field!", "I'm reading a book on anti-gravity. It's impossible to put down!", "Why couldn't the bicycle stand up by itself? It was two-tired!", "I'm on a whiskey diet. I've lost three days already.", "What do you get when you cross a snowman and a vampire? Frostbite!", "I used to play piano by ear, but now I use my hands."],
    "compliment": ["You're very smart!", "You're doing great!", "You're awesome!", "You're fantastic!", "You're brilliant!", "You're outstanding!", "You're amazing!", "You're exceptional!", "You're remarkable!", "You're a star!"],
    "encouragement": ["Keep going!", "You can do it!", "Don't give up!", "Believe in yourself!", "Keep pushing forward!", "You've got this!", "Stay strong!", "You're doing great!", "Keep up the good work!", "You're making progress!"],
    "apology": ["I apologize for any inconvenience.", "I'm sorry if I caused any confusion.", "I'm sorry for the misunderstanding.", "I apologize for the mistake.", "I'm sorry if I wasn't clear.", "I'm sorry for any trouble I may have caused.", "Please accept my apologies.", "I'm sorry for any frustration this may have caused.", "I apologize for any errors.", "I'm sorry for any inconvenience this may have caused."],
    "about_ai": ["What is artificial intelligence?", "Can you explain artificial intelligence?", "How does AI work?", "What are the applications of AI?", "Tell me about the history of artificial intelligence.", "What are the types of AI?", "Can AI replace humans?", "What are the benefits of artificial intelligence?", "What are the limitations of AI?", "How is AI changing the world?"],
    "favorite_food": ["What's your favorite food?", "Do you have a favorite dish?", "What food do you like the most?", "Tell me about your favorite cuisine.", "What's the most delicious food you've tasted?", "What's your go-to meal?", "Do you enjoy eating?", "What's your preferred food?", "Describe your favorite meal.", "What's your favorite snack?"],
    "current_events": ["What's happening in the world?", "Can you tell me about the latest news?", "What are the current events?", "What's going on in the news?", "Can you update me on current affairs?", "Tell me about the recent developments.", "What's making headlines?", "Do you know any recent news stories?", "What's the latest buzz?", "What's happening around the globe?"],
    "about_technology": ["What is the latest in technology?", "Can you tell me about recent technological advancements?", "How is technology shaping the future?", "What are the trends in technology?", "Tell me about innovations in technology.", "How is technology impacting society?", "What are the emerging technologies?", "Can you explain cutting-edge technology?", "What's new in the world of tech?", "How is technology changing our lives?"],
    "about_science": ["What are some interesting scientific facts?", "Can you tell me about recent scientific discoveries?", "What is happening in the world of science?", "Tell me about scientific breakthroughs.", "How is science advancing?", "What are the major fields of science?", "Can you explain complex scientific concepts?", "What are some cool experiments in science?", "Tell me about famous scientists.", "What are the mysteries of the universe?"],
}

def get_intent(sentence):
    doc = nlp(sentence)
    intent = None
    for token in doc:
        if token.text.lower() == "hi" or token.text.lower() == "hello":
            intent = "hi"
        elif token.text.lower() == "how" and token.nbor().text.lower() == "are" and token.nbor(2).text.lower() == "you":
            intent = "how_are_you"
        elif token.text.lower() == "name":
            intent = "name"
        elif token.text.lower() == "bye":
            intent = "bye"
        elif token.text.lower() == "thanks" or token.text.lower() == "thank":
            intent = "thanks"
        elif token.text.lower() == "about":
            intent = "about_chatbot"
        elif token.text.lower() == "thank" and (token.nbor().text.lower() == "you" or token.nbor().text.lower() == "u"):
            intent = "thanks_response"
        elif token.text.lower() == "about":
            intent = "about_user"
        elif token.text.lower() == "weather":
            intent = "about_weather"
        elif token.text.lower() == "joke":
            intent = "joke"
        elif token.text.lower() == "compliment":
            intent = "compliment"
        elif token.text.lower() == "encouragement":
            intent = "encouragement"
        elif token.text.lower() == "apology":
            intent = "apology"
        elif token.text.lower() == "ai" or token.text.lower() == "artificial" and token.nbor().text.lower() == "intelligence":
            intent = "about_ai"
        elif token.text.lower() == "food":
            intent = "favorite_food"
        elif token.text.lower() == "events" or token.text.lower() == "news":
            intent = "current_events"
        elif token.text.lower() == "technology" or token.text.lower() == "tech":
            intent = "about_technology"
        elif token.text.lower() == "science":
            intent = "about_science"
    return intent

def chat():
    print("Hello! I'm a basic chatbot. You can start chatting with me. Type 'bye' to end the conversation.")
    while True:
        user_input = input("You: ")
        intent = get_intent(user_input)
        if intent == 'bye':
            print(random.choice(responses['bye']))
            break
        elif intent:
            print(random.choice(responses[intent]))
        else:
            print("I'm not sure how to respond to that.")

chat()
