def greet():
    print("Welcome to College Admission Bot!")
    print("How can I assist you today?")

def ask_question():
    question = input("What question do you have? ")
    return question.lower()

def respond(question):
    if "deadline" in question:
        print("The application deadline for this year is May 31st.")
    elif "requirements" in question:
        print("To apply, you need to submit your high school transcript, standardized test scores, letters of recommendation, and a personal statement.")
    elif "tuition" in question:
        print("Tuition for the upcoming academic year is $20,000.")
    elif "scholarships" in question:
        print("We offer various scholarships based on academic merit, financial need, and extracurricular achievements.")
    else:
        print("I'm sorry, I don't understand that question.")

def main():
    greet()
    while True:
        question = ask_question()
        if question == "exit":
            print("Thank you for using College Admission Bot. Goodbye!")
            break
        respond(question)

if __name__ == "__main__":
    main()
