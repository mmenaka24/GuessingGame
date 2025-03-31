import random


def get_positive_int(prompt):
    while True:
        try:
            num = int(input(prompt))
            if num < 1:
                raise ValueError
        except ValueError:
            pass
        else:
            return num


def main():
    n = get_positive_int("Level: ")
    ans = random.randint(1, n)

    while True:
        guess = get_positive_int("Guess: ")
        if guess < ans:
            print("Too small!")
        elif guess > ans:
            print("Too large!")
        else:
            print("Just right!")
            return


if __name__ == "__main__":
    main()
