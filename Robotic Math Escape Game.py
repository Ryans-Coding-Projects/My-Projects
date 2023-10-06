import random

# Constants
QUESTIONS = [
    {'question': '33 + 55 + 189 = ?', 'answer': 277},
    {'question': '1400 / 14 = ?', 'answer': 100},
    {'question': '200 * 50 = ?', 'answer': 10000},
    {'question': '1000 - 333 - 33 - 3 = ?', 'answer': 631},
    {'question': '(900 / 3) * 5 = ?', 'answer': 1500}
]
MAX_LIVES = 3

# Functions
def ask_question(question):
    """Ask the user a question and return True if the answer is correct."""
    answer = input(f"{question['question']} ")
    try:
        answer = int(answer)
        return answer == question['answer']
    except ValueError:
        return False

def display_result(result):
    """Display the result of the game."""
    if result:
        print("You've made it to safety!")
    else:
        print("You couldn't make it out... Robots caught you and turned you to dust.")

# Main game loop
while True:
    lives = MAX_LIVES
    result = True
    print("\nWhile you were asleep, robots broke into your company headquarters\nand were sparing no ones lives.")
    print("\nYour boss was a sadistic man and put automatic locks on every door.")
    print("\nYour boss was also a clever mathematician, who set each door to\nonly unlock when the mathematical equation was solved correctly")
    print("\nI guess your boss never expected robots to break in and cause mayhem....")
    print("\nAmidst the chaotic noises, you got up quickly in a state of panic and\nran to the nearest door")
    print("\n\nYou had this answer memorized after entering it nearly everyday but with\nall the adrenaline you had to think...")
    
    for question in QUESTIONS:
        while lives > 0:
            if ask_question(question):
                print("\nPASSWORD CORRECT\nACCESS GRANTED")
                print("\nYou overcame your fear and got the password correct")
