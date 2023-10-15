def check_password(password):
    if len(password) <= 8:
        return "error"

    has_upper = False
    has_lower = False
    for char in password:
        if char.islower():
            has_lower = True
        if char.isupper():
            has_upper = True
    if not (has_lower and has_upper):
        return "error"

    has_digit = any(char.isdigit() for char in password)
    if not has_digit:
        return "error"

    keyboard_layouts = ["qwertyuiop", "asdfghjkl", "zxcvbnm", "йцукенгшщзхъ", "фывапролджэ", "ячсмитьбю"]

    for layout in keyboard_layouts:
        for i in range(len(layout) - 2):
            substring = layout[i:i + 3]
            if substring in password.lower():
                return "error"

    return "ok"


password = input("Enter the password: ")
result = check_password(password)
print(result)
