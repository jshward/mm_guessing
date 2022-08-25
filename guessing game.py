import random

print('-----------------------------------------------------------')
print('              M & M Guessing Game!')
print('-----------------------------------------------------------')


attempt_limit = 5
attempts = 0

mm_count = random.randint(1, 100)

print("Guess How many M & M's in the jar and won a free lunch")
print("You've 5 tries!")
print()

while attempts < attempt_limit:
    guess_text = input("How many M & M's are in the jar? ")
    guess = int(guess_text)
    attempts += 1
    if mm_count == guess:
        print(f'Congrats on your free lunch. It was {guess}')
        break
    elif mm_count > guess:
        print('Too low')
    else:
        print('That is too high')


print(f'Bye! You guessed it in {attempts} tries')
