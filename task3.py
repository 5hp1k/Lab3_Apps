class PasswordError(Exception):
    pass


class LengthError(PasswordError):
    pass


class LetterError(PasswordError):
    pass


class DigitError(PasswordError):
    pass


class SequenceError(PasswordError):
    pass


def check_password(password):
    if len(password) <= 8:
        raise LengthError("Password is too short")

    has_upper = any(char.isupper() for char in password)
    has_lower = any(char.islower() for char in password)

    if not (has_lower and has_upper):
        raise LetterError("Password must contain both upper and lower case letters")

    has_digit = any(char.isdigit() for char in password)

    if not has_digit:
        raise DigitError("Password must contain at least one digit")

    keyboard_layouts = ["qwertyuiop", "asdfghjkl", "zxcvbnm", "йцукенгшщзхъ", "фывапролджэ", "ячсмитьбю"]

    for layout in keyboard_layouts:
        for i in range(len(layout) - 2):
            substring = layout[i:i + 3]
            if substring in password.lower():
                raise SequenceError("Password contains a forbidden sequence")

    return "ok"


def main():
    try:
        password = input("Enter the password: ")
        result = check_password(password)
        print(result)
    except PasswordError as e:
        print(f"Password Error: {e}")
