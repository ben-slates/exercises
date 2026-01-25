questions = [
    {
        "question": "What is the capital of Pakistan?",
        "options": ["A. Islamabad", "B. Karachi", "C. Lahore", "D. Peshawar"],
        "correct_answer": "A"
    },
    {
        "question": "What is the capital of India?",
        "options": ["A. Delhi", "B. Mumbai", "C. Bangalore", "D. Gujarat"],
        "correct_answer": "A"
    },
    {
        "question": "What is the capital of Germany?",
        "options": ["A. Cologne", "B. Hamburg", "C. Berlin", "D. Munich"],
        "correct_answer": "C"
    },
    {
        "question": "What is the capital of Afghanistan?",
        "options": ["A. Kandahar", "B. Kabul", "C. Herat", "D. Mazar-i-Sharif"],
        "correct_answer": "B"
    },
    {
        "question": "What is the capital of China?",
        "options": ["A. Shanghai", "B. Beijing", "C. Guangzhou", "D. Shenzhen"],
        "correct_answer": "B"
    },
    {
        "question": "What is the capital of France?",
        "options": ["A. Lyon", "B. Marseille", "C. Paris", "D. Nice"],
        "correct_answer": "C"
    },
    {
        "question": "What is the capital of Japan?",
        "options": ["A. Osaka", "B. Tokyo", "C. Kyoto", "D. Hiroshima"],
        "correct_answer": "B"
    },
    {
        "question": "What is the capital of Brazil?",
        "options": ["A. Rio de Janeiro", "B. Salvador", "C. Brasília", "D. São Paulo"],
        "correct_answer": "C"
    }
]
prize_money = [
    10000,
    20000,
    50000,
    100000,
    500000,
    1000000,
    5000000,
    10000000
]

def play_KBC():
    print("WELCOME TO KBC QUIZ GAME!")
    current_prize = 0
    
    for level, q_data in enumerate(questions):
        print(f"\nQUESTION {level + 1}: Prize Amount - Rs. {prize_money[level]:,}")
        print(f"\n{q_data['question']}\n")
        for option in q_data['options']:
            print(f"  {option}")
        print()
        user = input("Your answer (A/B/C/D) or 'Q' to quit: ")
        if user == 'Q':
            print(f"\nYou quit the game!")
            print(f"Your final prize: Rs. {current_prize:,}")
            break
        if user not in ['A', 'B', 'C', 'D']:
            print("Invalid input! Please enter A, B, C, or D.")
            print(f"\nYour final prize: Rs. {current_prize:,}")
            break
        if user == q_data['correct_answer']:
            current_prize = prize_money[level]
            print(f"\n CORRECT ANSWER!")
            print(f"You have won Rs. {current_prize:,}")
        else:
            print(f"\n WRONG ANSWER! The correct answer was {q_data['correct_answer']}")
            print(f"\nYour final prize: Rs. {current_prize:,}")
            break
    else:
        print(" CONGRATULATIONS! YOU HAVE WON THE GAME")
        print(f"Your final prize: Rs. {current_prize:,}")
    print("Thanks for playing.")

if __name__ == "__main__":
    play_KBC()