import re

def calculate_password_score(password):
    """
    Function to calculate the password score based on strength criteria.
    """
    score = 0

    # Criteria 1: Minimum 8 characters
    if len(password) >= 8:
        score += 20

    # Criteria 2: At least one digit
    if any(char.isdigit() for char in password):
        score += 20

    # Criteria 3: At least one uppercase letter
    if any(char.isupper() for char in password):
        score += 20

    # Criteria 4: At least one lowercase letter
    if any(char.islower() for char in password):
        score += 20

    # Criteria 5: At least one special character
    if re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
        score += 20

    return score

def provide_detailed_feedback(password):
    """
    Function to provide detailed feedback on how to improve the password.
    """
    feedback = []

    # Check each criterion and provide specific feedback
    if len(password) < 8:
        feedback.append("- Password is too short. Use at least 8 characters.")

    if not any(char.isdigit() for char in password):
        feedback.append("- Add at least one numeric digit.")

    if not any(char.isupper() for char in password):
        feedback.append("- Include at least one uppercase letter.")

    if not any(char.islower() for char in password):
        feedback.append("- Include at least one lowercase letter.")

    if not re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
        feedback.append("- Add at least one special character (e.g., !, @, #, $).")

    return feedback

def check_password_strength(password):
    """
    Function to check the strength of a password and provide feedback with a percentage score.
    """
    score = calculate_password_score(password)

    if score == 100:
        return f"Strong: Your password is secure! (Strength: {score}%)"
    elif score >= 60:
        return f"Medium: Consider improving your password. (Strength: {score}%)"
    else:
        return f"Weak: Your password needs significant improvement. (Strength: {score}%)"

def password_checker():
    """
    Main function to take user input and check password strength.
    """
    print("Welcome to the Password Strength Checker!")

    while True:
        password = input("\nEnter your password (or type 'exit' to quit): ")

        if password.lower() == "exit":
            print("Thank you for using the Password Strength Checker! Goodbye!")
            break

        result = check_password_strength(password)
        print(result)

        # Provide detailed feedback
        feedback = provide_detailed_feedback(password)
        if feedback:
            print("\nSuggestions to improve your password:")
            for suggestion in feedback:
                print(suggestion)

# Run the password checker
if __name__ == "__main__":
    password_checker()
