import random

def compareNumber(number, answer):
    if (number > answer):
        print("Too big")
        return False
    elif (number < answer):
        print("Too small")
        return False
    else:
        print("You guessed the number!")
        return True

print("Welcome to number guesser!")

score_table = []

while True:
    answer = random.randint(1, 5)
    isGuessed = False
    numberOfTries = 0
    provided_numbers = []
    

    while(not isGuessed):
        try:
            number = int(input("Guess the number: "))

            provided_numbers.append(number)

            isGuessed = compareNumber(number, answer)

            numberOfTries += 1

        except ValueError:
            print("That's not a number!")

    print(f"You finished in {numberOfTries} tries.")

    print("You provided the following numbers: ", end='')
    for index, number in enumerate(provided_numbers):
        if index < len(provided_numbers) - 1:
            print(number, end=', ')
        else:
            print(number)

    print("\nStatystyki:")
    print(f"Biggest provided number: {max(provided_numbers)}")
    print(f"Smallset provided number: {min(provided_numbers)}")
    print(f"Average of provided number: {sum(provided_numbers)/len(provided_numbers)}")

    name = input("Provide your name: ")

    result = {
        "name" : name,
        "tries" : numberOfTries
    }

    score_table.append(result)

    while (True):
        next_game = input("Do you want to play another game? (Y/N): ")
        if next_game == 'Y' or next_game == 'y' or next_game == 'N' or next_game == 'n':
            break

    if next_game == 'N' or next_game == 'n':
        break

score_table.sort(key=lambda x: x['tries'])

print("Scoreboard:")

for result in score_table:
    print(f"{result['name']} finished in {result['tries']} tries")