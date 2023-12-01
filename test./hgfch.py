import random  
  
def guess_number():  
    secret_number = random.randint(1, 100)  
    attempts = 0  
      
    print("Welcome to Guess the Number!")  
    print("You have 10 attempts to guess a number between 1 and 100.")  
      
    while attempts < 10:  
        guess = int(input("Enter your guess: "))  
        attempts += 1  
          
        if guess < secret_number:  
            print("Too low.")  
        elif guess > secret_number:  
            print("Too high.")  
        else:  
            print(f"Congratulations! You guessed the number {secret_number} in {attempts} attempts.")  
            return  
      
    print(f"Sorry, you ran out of attempts. The secret number was {secret_number}.")  
  
guess_number()