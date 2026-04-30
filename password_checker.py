import string

def check_password_strength(password):
    length = len(password)

    
    has_upper = any(char.isupper() for char in password)
    has_lower = any(char.islower() for char in password)
    has_digit = any(char.isdigit() for char in password)
    has_symbol = any(char in string.punctuation for char in password)

    score = 0

    
    if length >= 8:
        score += 1
    if length >= 12:
        score += 1

    
    if has_upper:
        score += 1
    if has_lower:
        score += 1
    if has_digit:
        score += 1
    if has_symbol:
        score += 1

    
    if score <= 2:
        return "Weak "
    elif score <= 4:
        return "Medium "
    else:
        return "Strong "


password = input("Enter your password: ")
strength = check_password_strength(password)

print(f"Password Strength: {strength}")
