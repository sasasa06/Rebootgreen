import random
from colorama import Fore

questions = [
    {
        "question": "Which of the following items is recyclable?",
        "options": ["a. Banana peels", "b. Plastic bottles", "c. Styrofoam cups", "d. Used napkins"],
        "answer": "b",
    },
    {
        "question": "Which of the following items should not be put in the recycling bin?",
        "options": ["a. Aluminum cans", "b. Glass bottles", "c. Food scraps", "d. Paper"],
        "answer": "c",
    },
    {
        "question": "Which of the following items should be recycled separately from other materials?",
        "options": ["a. Tissue paper", "b. Cardboard boxes", "c. Plastic bags", "d. All of the above"],
        "answer": "c",
    },
    {
        "question": "What is the correct way to prepare a cardboard box for recycling?",
        "options": ["a. Leave it as is", "b. Flatten it and remove any plastic or metal parts", "c. Cut it into small pieces", "d. Paint it first"],
        "answer": "b",
    },
    {
        "question": "What is the best way to dispose of an old mobile phone?",
        "options": ["a. Throw it in the trash", "b. Give it to a friend", "c. Recycle it at an e-waste collection centre", "d. Bury it in the backyard"],
        "answer": "c",
    },
    {
        "question": "Which of the following is an example of upcycling?",
        "options": ["a. Recycling a plastic bottle", "b. Composting food scraps", "c. Turning an old T-shirt into a bag", "d. Buying a new item instead of repairing an old one"],
        "answer": "c",
    },
]

def play_game():
    score = 0
    random.shuffle(questions)
    for question in questions:
        print(Fore.GREEN + "\n" + question["question"])
        for option in question["options"]:
            print(option)
        guess = input(Fore.YELLOW + "\nEnter your answer (a, b, c, or d): ").lower()
        if guess == question["answer"]:
            print(Fore.BLUE + "\nGreat job! You got it right.")
            score += 1
        else:
            print(Fore.RED + "\nSorry, that's incorrect.")
    print(Fore.GREEN + "\nYour final score is:", score, "out of", len(questions))
    
    if score == len(questions):
        print(Fore.YELLOW + "Congratulations! You got a perfect score. Thanks for playing!")
    else:
        print(Fore.YELLOW + "Thanks for playing!")

print(Fore.GREEN + "Welcome to Saachi's fun & learn Recycling Game!\n")
play_game()
import random
from colorama import Fore

story = "Once upon a time, there was a __noun__ named __name__. __name__ lived in a world that was __adjective__ due to __noun2__ and __noun3__. But __name__ was a __adjective2__ person who wanted to make a difference. One day, __name__ found a __noun4__ that could __verb__ the air and __verb2__ the water. __name__ knew that this could help the world become more __adjective3__. So, __name__ gathered a team of __pluralnoun__ and together, they went on a mission to __verb3__ the __noun5__ and bring __adjective4__ back to the world. In the end, __name__ and the team succeeded and the world was a much __adjective5__ place thanks to their hard work!"

word_bank = {
    "__noun__": ["tree", "flower", "ocean", "mountain"],
    "__name__": ["Lily", "Max", "Oliver", "Ava"],
    "__adjective__": ["polluted", "overpopulated", "chaotic", "unpredictable"],
    "__noun2__": ["deforestation", "global warming", "plastic pollution", "ozone depletion"],
    "__noun3__": ["extinction", "droughts", "floods", "wildfires"],
    "__adjective2__": ["caring", "determined", "brave", "intelligent"],
    "__noun4__": ["seed", "machine", "robot", "formula"],
    "__verb__": ["clean", "filter", "absorb", "purify"],
    "__verb2__": ["cleanse", "sanitize", "hydrate", "irrigate"],
    "__adjective3__": ["sustainable", "healthy", "beautiful", "livable"],
    "__pluralnoun__": ["scientists", "environmentalists", "volunteers", "activists"],
    "__verb3__": ["explore", "discover", "restore", "protect"],
  
    "__noun5__": ["forest", "ocean", "atmosphere", "ecosystem"],
    "__adjective4__": ["hope", "life", "peace", "prosperity"],
    "__adjective5__": ["better", "greener", "cleaner", "safer"],
}

def play_game():
    blanks = list(word_bank.keys())
    random.shuffle(blanks)
    inputs = {}
    for blank in blanks:
        options = word_bank[blank]
        print(Fore.GREEN + f"\nPlease choose an option for '{blank}':")
        for i, option in enumerate(options):
            print(Fore.BLUE + f"{chr(97 + i)}. {option}")
        guess = input(Fore.YELLOW + "Enter your answer (a, b, c, or d): ").lower()
        while guess not in ["a", "b", "c", "d"]:
            guess = input(Fore.YELLOW + "Please enter a valid answer (a, b, c, or d): ").lower()
        inputs[blank] = options[ord(guess) - 97]
    print(Fore.GREEN + "\nYour story:")
    filled_story = story
    for blank, value in inputs.items():
        filled_story = filled_story.replace(blank, value)
    print(Fore.BLUE + filled_story)

print(Fore.RED + "Welcome to another interesting story game which is the Climate Change Warrior Mad Libs Game!\n")
play_game()
