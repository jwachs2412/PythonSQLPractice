quiz_data = [
    {
        "question": "In which city were the 2008 Summer Olympics held?",
        "options": ["A. London", "B. Tokyo", "C. Rome", "D. Beijing"],
        "answer": "D"
    },
    {
        "question": "In which sport is the ""Super Bowl"" played?",
        "options": ["A. Baseball", "B. Football", "C. Soccer", "D. Hockey"],
        "answer": "B"
    },
    {
        "question": "What is the largest ocean on Earth?",
        "options": ["A. Atlantic Ocean", "B. Indian Ocean", "C. Arctic Ocean", "D. Pacific Ocean"],
        "answer": "D"
    },
    {
        "question": "Who wrote the play 'Romeo and Juliet'?",
        "options": ["A. Charles Dickens", "B. Mark Twain", "C. William Shakespeare", "D. Jane Austen"],
        "answer": "C"
    },
    {
        "question": "What is the capital of Japan?",
        "options": ["A. Beijing", "B. Seoul", "C. Tokyo", "D. Bangkok"],
        "answer": "C"
    },
    {
        "question": "Which planet is known as the Red Planet?",
        "options": ["A. Earth", "B. Mars", "C. Jupiter", "D. Venus"],
        "answer": "B"
    },
    {
        "question": "What is the smallest prime number?",
        "options": ["A. 0", "B. 1", "C. 2", "D. 3"],
        "answer": "C"
    },
    {
        "question": "Who painted the Mona Lisa?",
        "options": ["A. Vincent van Gogh", "B. Pablo Picasso", "C. Leonardo da Vinci", "D. Claude Monet"],
        "answer": "C"
    },
    {
        "question": "What is the hardest natural substance on Earth?",
        "options": ["A. Gold", "B. Iron", "C. Diamond", "D. Silver"],
        "answer": "C"
    },
    {
        "question": "Which element has the chemical symbol 'O'?",
        "options": ["A. Gold", "B. Oxygen", "C. Osmium", "D. Hydrogen"],
        "answer": "B"
    }
]

score = 0
question_number = 1

for item in quiz_data:
    print(f"Question {question_number}: {item['question']}")
    for option in item['options']:
        print(option)

    user_answer = input("Your answer (A/B/C/D): ").upper()

    if user_answer == item['answer']:
        print("Correct!\n")
        score += 1
    else:
        print(f"Wrong! The correct answer was {item['answer']}.\n")

    question_number += 1

print(f"Your final score is {score} out of {len(quiz_data)}.")
