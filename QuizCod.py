def ask_question(question, options, correct_answer):
    print(question)
    for idx, option in enumerate(options, 1):
        print(f"{idx}. {option}")
    user_answer = int(input("Your answer: "))
    if user_answer == correct_answer:
        print("Your answer is correct.")
        return 1
    else:
        print(f"Your answer is incorrect. The correct answer is option {correct_answer}.")
        return 0

def calculate_score(score):
    print(f"\nYour total score is {score} out of 4 questions!")
    print(f"You got {(score / 4) * 100}%")
    if score == 4:
        print("Congratulations! You got all the answers correct. Well done!")
    elif score >= 2:
        print("Good job! You answered most of the questions correctly.")
    else:
        print("You can try again to improve your score. Keep learning!")

print("WELCOME TO THE QUIZ GAME\n"
      "\nGuidelines:"
      "\n1. Give an answer in the integer form (1 to 4)."
      "\n2. Answer the questions to the best of your knowledge."
      "\n3. The quiz consists of 4 questions related to the Russia-Ukraine war."
      "\n4. Each correct answer will earn you one point."
      "\n5. There is no negative marking for incorrect answers."
      "\n\nOrganized by Vidhan and CodSoft")

def play_quiz():
    score = 0

    # Question 1
    question1 = "Q1. What is India's stance on the Russia-Ukraine war?"
    options1 = [
        "Condemning Russia's actions and supporting Ukraine",
        "Supporting Russia's actions in the region",
        "Maintaining a neutral stance",
        "Urging both countries to find a peaceful resolution"
    ]
    correct_answer1 = 1
    score += ask_question(question1, options1, correct_answer1)

    # Question 2
    question2 = "Q2. How has India reacted to the imposition of international sanctions on Russia during the conflict?"
    options2 = [
        "India has fully supported the sanctions",
        "India has opposed the sanctions",
        "India has imposed its own sanctions on Russia",
        "India has expressed concerns about the impact on bilateral relations"
    ]
    correct_answer2 = 4
    score += ask_question(question2, options2, correct_answer2)

    # Question 3
    question3 = "Q3. What measures has India taken to evacuate its citizens from the conflict zone?"
    options3 = [
        "India has conducted air evacuations using military aircraft",
        "India has used diplomatic channels to facilitate evacuations",
        "India has asked its citizens to leave the region on their own",
        "India has not initiated any evacuation measures"
    ]
    correct_answer3 = 2
    score += ask_question(question3, options3, correct_answer3)

    # Question 4
    question4 = "Q4. How has India engaged with other countries to find a resolution to the Russia-Ukraine conflict?"
    options4 = [
        "India has taken a leading role in mediating peace talks",
        "India has participated in international forums to address the conflict",
        "India has not actively engaged in the conflict",
        "India has provided military support to Ukraine"
    ]
    correct_answer4 = 2
    score += ask_question(question4, options4, correct_answer4)

    calculate_score(score)

    play_again = input("Do you want to play again? (yes/no): ")
    if play_again.lower() == "yes":
        play_quiz()
    else:
        print("Okay, have a nice day! If you change your mind, come back to play the quiz later.")

play_quiz()
