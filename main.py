from nlp import detect_intent
from memory import save_memory, get_memory


print("Bot: Hello! I am your assistant")


while True:


    user = input("You: ").lower()



    # remember user information

    if "student" in user:

        save_memory("occupation", "student")

        print("Bot: Okay, I will remember that you are a student.")
        continue

    elif "i am " in user:

        name = user.replace("i am ", "").strip()

        save_memory("name", name)

        print(f"Bot: Nice to meet you {name}. I will remember your name.")

        continue



    elif "my name is" in user:

        name = user.replace("my name is", "").strip()

        save_memory("name", name)

        print(f"Bot: Nice to meet you {name}. I will remember your name.")

        continue



    intent = detect_intent(user)



    if intent == "greeting":

        print("Bot: Hi, how can I help you?")

    elif intent == "account_opening":

        print("Bot: We provide Savings, FD, RD and Current accounts.")

    elif intent == "account_recommendation":

        occupation = get_memory("occupation")

        if occupation == "student":

            print("Bot: Since you are a student, Savings Account is suitable for you.")

        else:

            print("Bot: Savings Account is good for daily use. FD/RD is good for investment.")

    elif intent == "goodbye":

        print("Bot: Goodbye!")
        break

    else:

        print("Bot: Sorry, I did not understand.")