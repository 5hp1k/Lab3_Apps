with open('data/top 10000 passwd.txt', 'r') as file:
    global passwords
    passwords = file.read().splitlines()

with open('data/top-9999-words.txt', 'r') as file:
    global english_words
    english_words = set(file.read().splitlines())


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


class WordError(PasswordError):
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

    if password.lower() in english_words:
        raise WordError("Password contains a dictionary word")

    return "ok"


error_counts = {
    'LengthError': 0,
    'LetterError': 0,
    'DigitError': 0,
    'SequenceError': 0,
    'WordError': 0,
}

for password in passwords:
    try:
        check_password(password)
    except PasswordError as error:
        error_counts[error] += 1
        pass

print(error_counts)
