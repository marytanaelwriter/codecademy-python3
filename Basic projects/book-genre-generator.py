import random

print("""

Are you in the mood for reading but not sure what to read?

I get the struggle.

This simple program, a guessing game and a book genre generator rolled into one, might help you decide.

The idea is simple: you have to guess a random number. Upon guessing correctly, you'll get your first genre.

For the second genre, you have to enter your favorite number.

The final result? You'll get two genres, and you can decide which book falls into those categories.

Hopefully, this will help narrow down your options.

Ready?

Let's get started!
      """)

guess = int(input("Choose a number between 1 and 25. What's your first guess?: "))
correct_number = random.randint(1, 25)

guess_count = 1

while guess != correct_number:
    guess_count += 1
    if guess < correct_number:
        guess = int(
            input(
                "Wrong. You need to guess higher. What's your guess?: "
            ))
    else:
        guess = int(
            input(
                "Wrong. You need to guess lower. What's your guess?: "
            ))

genre_1 = ""

if correct_number <= 5:
  genre_1 = "romance"
elif correct_number > 5 and correct_number <= 10:
  genre_1 = "science fiction"
elif correct_number > 10 and correct_number <= 15:
  genre_1 = "thriller"
elif correct_number > 15 and correct_number <= 20:
  genre_1 = "magical realism"
else:
  genre_1 = "horror"

print(
    f"""Congrats! You got it.

  The correct number is {correct_number} and it took you {guess_count} guess(es) to get it right.

  Your first genre is {genre_1}.

  Take note of it!"""
)

user_input = input(
    "Press enter to proceed to the next step! ")

print("On to the second genre... Simply choose a number between 1 and 100.")

fave_number = int(input("Enter your favorite number: "))

if fave_number <= 10:
  genre_2 = "children's lit"
elif fave_number > 10 and fave_number <= 20:
  genre_2 = "middle grade fiction"
elif fave_number > 20 and fave_number <= 30:
  genre_2 = "adult"
elif fave_number > 30 and fave_number <= 40:
  genre_2 = "young adult"
elif fave_number > 40 and fave_number <= 50:
  genre_2 = "chick lit"
elif fave_number > 50 and fave_number <= 60:
  genre_2 = "slice of life"
elif fave_number > 60 and fave_number <= 70:
  genre_2 = "literary fiction"
elif fave_number > 70 and fave_number <= 80:
  genre_2 = "cultural fiction"
elif fave_number > 80 and fave_number <= 90:
  genre_2 = "myths and legends"
else:
  genre_2 = "LGBTQ"

print(
    f"""You chose {fave_number} — {genre_2}.

  Now, all you have to do is choose a book that's both {genre_1} and {genre_2}.

  I hope that helps, and I hope you had fun! <3

  -Anne"""
)
