import keyboard
running_count = 0

def reset_count():
    global running_count
    running_count = 0

def increment_count():
    global running_count
    running_count += 1

def get_count():
    return running_count

def decrease_count():
    global running_count
    running_count -= 1

def calculate_running_count(cards):
    for card in cards:
        if card in [2, 3, 4, 5, 6]:
            increment_count()
        elif card in [10, 11, 12, 13, 1]:
            decrease_count()

while True:
    print("Reminder! Cards are as follows from high to low: 2, 3, 4, 5, 6 | 7, 8, 9 | 10, 11, 12, 13, 1")
    cards_input = input("Enter the cards dealt (comma-separated): ")
    cards = [int(card) for card in cards_input.split(",")]

    calculate_running_count(cards)

    print("Running count:", get_count())

    if get_count() > 0:
        print("Bet high!")
    else:
        print("Bet low!")

    if keyboard.is_pressed('r'):
        reset_count()
        print("Count reset!")
    
    