from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer
import random


bot = ChatBot('AdmissionBot')


trainer = ChatterBotCorpusTrainer(bot)


trainer.train('chatterbot.corpus.english')


admission_responses = {
    'requirements': 'The admission requirements typically include a completed application form, transcripts, standardized test scores, letters of recommendation, and a personal statement.',
    'deadline': 'The admission deadline varies depending on the college and program. It's important to check the college website for specific deadline information.',
    'procedure': 'The admission procedure usually involves completing an application form, submitting required documents, and possibly attending an interview.',
    'financial_aid': 'Yes, many colleges offer financial aid to eligible students. You can find information about financial aid options on the college website or by contacting the financial aid office.'
}


print("AdmissionBot: Hi! I'm AdmissionBot. How can I assist you today?")


previous_intent = None


while True:
    
    user_input = input("User: ").lower()

    
    if user_input == 'bye':
        print("AdmissionBot: Goodbye! Have a great day!")
        break

    
    elif any(keyword in user_input for keyword in ['admission', 'apply', 'requirement', 'deadline', 'procedure', 'financial aid']):
       
        if 'requirement' in user_input:
            intent = 'requirements'
        elif 'deadline' in user_input:
            intent = 'deadline'
        elif 'procedure' in user_input:
            intent = 'procedure'
        elif 'financial aid' in user_input:
            intent = 'financial_aid'
        else:
            intent = None

        
        if intent:
            if previous_intent == intent:
                print("AdmissionBot: You've already asked about that. Is there anything else I can help you with?")
            else:
                print(f"AdmissionBot: {admission_responses[intent]}")
                previous_intent = intent
        else:
            print("AdmissionBot: I'm sorry, I didn't quite catch that. Could you please rephrase your question?")
    
    
    else:
        print("AdmissionBot: I'm sorry, I'm not sure how to answer that. Could you please ask another question?")

