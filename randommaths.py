import random
import time

def expression_generator():
    left = random.randint(1, 20)
    right = random.randint(1, 20)
    operators = ["+", "-", "*"]
    operator = random.choice(operators)
    expression = str(left) + operator + str(right)
    answer = eval(expression)
    print(expression)
    return expression, answer

correct = 0
wrong = 0
questions = 10
start_time = time.time()

for q in range(questions):
    print("Question number:", q + 1)
    expression, answer = expression_generator()
    user_ans = input("Enter your answer: ")

    if user_ans == str(answer):
        print("Correct answer!")
        correct += 1
    else:
        print("Wrong answer!")
        wrong += 1

end_time = time.time()
total_time = round(end_time - start_time, 2)

print("You finished the quiz in", total_time, "seconds")
print("Your correct answers were:", correct)
print("Your wrong answers were:", wrong)
