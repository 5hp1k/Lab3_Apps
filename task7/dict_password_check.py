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


def dict_password_check(password, word_dict):
    errors = []

    try:
        if len(password) <= 8:
            errors.append(LengthError("Password is too short"))

        has_upper = any(char.isupper() for char in password)
        has_lower = any(char.islower() for char in password)

        if not (has_lower and has_upper):
            errors.append(LetterError("Password must contain both upper and lower case letters"))

        has_digit = any(char.isdigit() for char in password)

        if not has_digit:
            errors.append(DigitError("Password must contain at least one digit"))

        keyboard_layouts = ["qwertyuiop", "asdfghjkl", "zxcvbnm", "йцукенгшщзхъ", "фывапролджэ", "ячсмитьбю"]

        for layout in keyboard_layouts:
            for i in range(len(layout) - 2):
                substring = layout[i:i + 3]
                if substring in password.lower():
                    errors.append(SequenceError("Password contains a forbidden sequence"))

        if any(word in password.lower() for word in word_dict):
            errors.append(WordError("Password contains a dictionary word"))

    except PasswordError as e:
        errors.append(e)

    return errors
