import string


def calculate_password_score(password):
    score = 0
    has_upper = any(char.isupper() for char in password)
    has_digit = any(char.isdigit() for char in password)
    has_special = any(char in string.punctuation for char in password)
    has_normal = any(char.islower() for char in password)

    if len(password) > 8 and has_normal:
        score += 10
    if has_upper:
        score += 10
    if has_digit:
        score += 20
    if has_special:
        score += 30
    if len(password) > 8 and has_upper and has_digit and has_special and has_normal:
        score += 30

    return score


def get_security_rank(score):
    if score < 30:
        return "Poor"
    elif score < 70:
        return "Weak"
    else:
        return "Strong"


password = input("Enter your password: ")
score = calculate_password_score(password)
rank = get_security_rank(score)
print(f"Your password security score is: {score}")
print(f"Security rank: {rank}")