
# Final Project: Python Quiz Engine

import random

class PythonQuiz:
    def __init__(self):

        self.questions = {
            "Basics": [
                {"q": "Which keyword is used to define a function?", "options": ["A) func", "B) def", "C) function"], "ans": "B", "difficulty": "Easy"},
                {"q": "What symbol is used for comments in Python?", "options": ["A) //", "B) #", "C) <!--"], "ans": "B", "difficulty": "Easy"}
            ],
            "Data Types": [
                {"q": "Which of these is immutable?", "options": ["A) List", "B) Tuple", "C) Dictionary"], "ans": "B", "difficulty": "Medium"},
                {"q": "Which data type stores True or False?", "options": ["A) String", "B) Boolean", "C) Integer"], "ans": "B", "difficulty": "Easy"}
            ],
            "OOP": [
                {"q": "What refers to the instance itself inside a class?", "options": ["A) self", "B) this", "C) me"], "ans": "A", "difficulty": "Medium"},
                {"q": "Which method is called when an object is created?", "options": ["A) __start__", "B) __init__", "C) __create__"], "ans": "B", "difficulty": "Medium"}
            ]
        }
        self.score = 0
        self.past_scores = []

  
    def choose_category(self):
        print("\nAvailable Python categories:")
        for idx, cat in enumerate(self.questions.keys(), 1):
            print(f"{idx}. {cat}")
        while True:
            choice = input("Choose category number: ")
            if choice.isdigit() and 1 <= int(choice) <= len(self.questions):
                self.category = list(self.questions.keys())[int(choice)-1]
                break
            else:
                print("Invalid choice! Enter a valid number.")

    def ask_questions(self):
        self.score = 0
        self.choose_category()
        qlist = self.questions[self.category].copy()
        random.shuffle(qlist)

        print(f"\nStarting Python Quiz in category: {self.category}!\n")
        question_number = 1
        while qlist:
            q = qlist.pop()
            print(f"Question {question_number}: {q['q']} (Difficulty: {q['difficulty']})")
            for opt in q['options']:
                print(opt)
            while True:
                ans = input("Your answer (A/B/C): ").upper()
                if ans in ["A","B","C"]:
                    break
                else:
                    print("Invalid choice! Enter A, B, or C.")

            if ans == q['ans']:
                print("✅ Correct!")
                self.score += 1
            else:
                print(f" Wrong! Correct answer: {q['ans']}")
            question_number += 1

        self.past_scores.append({"category": self.category, "score": self.score})

    def show_result(self):
        total_q = len(self.questions[self.category])
        percent = (self.score / total_q) * 100
        print("\n🎯 Quiz Finished!")
        print(f"Score: {self.score}/{total_q} ({percent:.2f}%)")
        if percent == 100:
            print("🏆 Perfect! Python Master!")
        elif percent >= 50:
            print("👍 Good job!")
        else:
            print("📚 Study more! Keep practicing.")


    def replay(self):
        while True:
            choice = input("\nDo you want to play again? (Y/N): ").upper()
            if choice == "Y":
                self.ask_questions()
                self.show_result()
            elif choice == "N":
                print("\nThanks for playing Python Quiz!")
                print("Your past scores:", self.past_scores)
                break
            else:
                print("Invalid input! Enter Y or N.")

def main():
    quiz = PythonQuiz()
    quiz.ask_questions()
    quiz.show_result()
    quiz.replay()

if __name__ == "__main__":
    main()