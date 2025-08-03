import random

def get_user_choice():
    print("\nChoose one:")
    print("1. Rock 🪨")
    print("2. Paper 📄")
    print("3. Scissors ✂️")
    choice = input("Enter 1, 2, or 3: ")

    if choice == '1':
        return "rock"
    elif choice == '2':
        return "paper"
    elif choice == '3':
        return "scissors"
    else:
        print("❌ Invalid choice. Try again.")
        return get_user_choice()

def get_computer_choice():
    return random.choice(["rock", "paper", "scissors"])

def determine_winner(user, computer):
    if user == computer:
        return "It's a tie!"
    elif (user == "rock" and computer == "scissors") or \
         (user == "paper" and computer == "rock") or \
         (user == "scissors" and computer == "paper"):
        return "✅ You win!"
    else:
        return "💻 Computer wins!"

def play_game():
    print("\n🎮 Welcome to Rock-Paper-Scissors Game!")

    while True:
        user_choice = get_user_choice()
        computer_choice = get_computer_choice()

        print(f"\n🧑 You chose: {user_choice}")
        print(f"🤖 Computer chose: {computer_choice}")

        result = determine_winner(user_choice, computer_choice)
        print(f"\n📢 Result: {result}")

        play_again = input("\nWanna play again? (y/n): ").lower()
        if play_again != 'y':
            print("\nThanks for playing, Dhanya! 💖")
            break

if __name__ == "__main__":
    play_game()