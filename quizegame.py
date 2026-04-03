# Quiz Game

def run_quiz():
    score = 0

    questions = [
        {
            "question": "What is the capital of India?",
            "answer": "delhi"
        },
        {
            "question": "What is 5 + 3?",
            "answer": "8"
        },
        {
            "question": "Which language is used for web apps? (python/java/javascript)",
            "answer": "javascript"
        },
        {
            "question": " Who developed Python Programming Language?",
            "answer": "Guido van Rossum"
        },
         {
            "question": "Which type of Programming does Python support?",
            "answer": "object-oriented programming"
        },


    ]

    for q in questions:
        user_answer = input(q["question"] + " ").lower()

        if user_answer == q["answer"]:
            print("✅ Correct!")
            score += 1
        else:
            print("❌ Wrong!")

    print("\nYour final score is:", score, "/", len(questions))


        # Pass/Fail condition
    if score >= 3:
        print("🎉 You Passed!")
    else:
        print("😢 You Failed!")


# Run game
run_quiz()