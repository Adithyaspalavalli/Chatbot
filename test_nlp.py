from nlp import detect_intent
from memory import save_memory, get_memory



print("\n========== CHATBOT COMPLETE TEST ==========\n")



# -----------------------------
# 1. Greeting Tests
# -----------------------------

greeting_tests = [

    "hello",
    "hi",
    "hey assistant"

]


print("1. GREETING TEST\n")


for msg in greeting_tests:

    result = detect_intent(msg)

    print(
        f"Input: {msg}"
        f"\nExpected: greeting"
        f"\nActual: {result}"
    )

    print("PASS\n" if result == "greeting" else "FAIL\n")





# -----------------------------
# 2. Account Opening Tests
# -----------------------------


opening_tests = [

    "I want to open account",
    "create a bank account",
    "I need a new account"

]


print("2. ACCOUNT OPENING TEST\n")


for msg in opening_tests:


    result = detect_intent(msg)


    print(
        f"Input: {msg}"
        f"\nExpected: account_opening"
        f"\nActual: {result}"
    )


    print(
        "PASS\n" 
        if result == "account_opening"
        else "FAIL\n"
    )





# -----------------------------
# 3. Account Recommendation Tests
# -----------------------------


recommendation_tests = [

    "which account is best",
    "help me choose account",
    "which one should I take",
    "what account suits me"

]


print("3. ACCOUNT RECOMMENDATION TEST\n")


for msg in recommendation_tests:


    result = detect_intent(msg)


    print(
        f"Input: {msg}"
        f"\nExpected: account_recommendation"
        f"\nActual: {result}"
    )


    print(
        "PASS\n"
        if result == "account_recommendation"
        else "FAIL\n"
    )





# -----------------------------
# 4. Goodbye Tests
# -----------------------------


goodbye_tests = [

    "bye",
    "exit",
    "quit"

]


print("4. GOODBYE TEST\n")


for msg in goodbye_tests:


    result = detect_intent(msg)


    print(
        f"Input: {msg}"
        f"\nExpected: goodbye"
        f"\nActual: {result}"
    )


    print(
        "PASS\n"
        if result == "goodbye"
        else "FAIL\n"
    )






# -----------------------------
# 5. Unknown Tests
# -----------------------------


unknown_tests = [

    "tell me weather",
    "play music",
    "who is president"

]


print("5. UNKNOWN TEST\n")


for msg in unknown_tests:


    result = detect_intent(msg)


    print(
        f"Input: {msg}"
        f"\nExpected: unknown"
        f"\nActual: {result}"
    )


    print(
        "PASS\n"
        if result == "unknown"
        else "FAIL\n"
    )






# -----------------------------
# 6. Memory Test
# -----------------------------


print("6. MEMORY TEST\n")



save_memory(
    "name",
    "Adithya"
)


save_memory(
    "occupation",
    "student"
)



print(
    "Saved Name:",
    get_memory("name")
)


print(
    "Saved Occupation:",
    get_memory("occupation")
)



if (
    get_memory("name") == "Adithya"
    and
    get_memory("occupation") == "student"
):

    print("PASS\n")

else:

    print("FAIL\n")







# -----------------------------
# 7. Personalized Response Test
# -----------------------------


print("7. PERSONALIZATION TEST\n")



intent = detect_intent(
    "which account is best for me"
)



occupation = get_memory("occupation")



if (
    intent == "account_recommendation"
    and
    occupation == "student"
):

    print(
    "PASS: Student recommendation working"
    )


else:

    print(
    "FAIL"
    )




print(
"\n========== ALL TESTS COMPLETED =========="
)