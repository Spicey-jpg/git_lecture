def password_guessing_game():
    """A simple password guessing game."""
    # Ask the user to set a secret password
    secret_password = input("Set your secret password: ")
    
    print("Alright! Now it's time for someone to guess the password.")
    
    playing = True

    while playing:
        # Ask for a password guess
        guess = input("Enter your guess for the secret password: ")
        
        if guess == secret_password:
            print("Congratulations! You've guessed the correct password.")
            play_again = input("Do you want to set a new secret password and play again? (yes/no): ").lower()
            if play_again == 'yes':
                secret_password = input("Set your new secret password: ")
            else:
                playing = False
                print("Thanks for playing!")
        else:
            print("Incorrect! Try again.")
    
if __name__ == "__main__":
    password_guessing_game()
