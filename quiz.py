score = 0
print("General Knowledge Quiz")
answer = input("1. What is the capital of France? ")
if answer.lower() == "paris":    
    score += 1
answer = input("2. What is 2 + 2? ")
if answer == "4":
    score += 1
answer = input("3. Which planet is known as the Red Planet? ")
if answer.lower() == "mars":
    score += 1
print("\nQuiz Completed!")
print("Your Final Score:", score, "/ 3")