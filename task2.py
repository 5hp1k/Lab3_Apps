def is_length_valid(password):
    return len(password) > 8


def has_upper_and_lower(password):
    has_upper = any(char.isupper() for char in password)
    has_lower = any(char.islower() for char in password)
    return has_upper and has_lower


def has_digit(password):
    return any(char.isdigit() for char in password)


def no_keyboard_patterns(password):
    keyboard_layouts = ["qwertyuiop", "asdfghjkl", "zxcvbnm", "йцукенгшщзхъ", "фывапролджэ", "ячсмитьбю"]

    for layout in keyboard_layouts:
        for i in range(len(layout) - 2):
            substring = layout[i:i + 3]
            if substring in password.lower():
                return False

    return True


def check_password(password):
    assert is_length_valid(password), "error"
    assert has_upper_and_lower(password), "error"
    assert has_digit(password), "error"
    assert no_keyboard_patterns(password), "error"

    return "ok"


password = input("Enter your password: ")
check_password(password)
