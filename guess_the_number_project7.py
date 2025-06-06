import random
easy_level_attempts=10
hard_level_attempts=5
def set_difficulty(level_choosen):
    if level_choosen=='easy':
         return easy_level_attempts
    else:
        return hard_level_attempts
def check_answer(guessed_number,answer,attempts):
    if guessed_number>answer:
        print("your guess too high.")
        return attempts-1
    elif guessed_number<answer:
         print("your guess too low")
         return attempts-1
    else:
         print(f"your guess the number {guessed_number} is right")

print("let me think of a number between 1 to 50.")
answer=random.randint(1,50)
#print(answer)
level=input("choose level of difficulty....type 'easy' or 'hard':").lower()
attempts=set_difficulty(level)
guessed_number=0
while guessed_number!=answer:
  print(f"you have {attempts} attempts remaining to guess the number.")
  guessed_number=int(input("guess a number:"))
  attempts=check_answer(guessed_number,answer,attempts)
  if attempts==0:
      exit()
  else:
      print("guess again")

print("game over")
