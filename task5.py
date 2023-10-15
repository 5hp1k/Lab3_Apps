class FormatError(Exception):
    pass


class DigitCountError(Exception):
    pass


class CountryCodeError(Exception):
    pass


class OperatorError(Exception):
    pass


def remove_spaces(s):
    return "".join(s.split())


def has_single_closed_bracket_pair(number):
    stack = []
    for char in number:
        if char == '(':
            stack.append(char)
        elif char == ')':
            if not stack:
                return False
            stack.pop()
    return not stack


def has_valid_hyphens(number):
    for i in range(1, len(number) - 1):
        if number[i] == '-':
            if number[i - 1] == '-' or number[i + 1] == '-':
                return False
    return True


def has_letters(number):
    return any(char.isalpha() for char in number)


def format_phone_number(number):
    if (not has_single_closed_bracket_pair(number) or not has_valid_hyphens(number) or has_letters(number)
            or len(number) == 0):
        raise FormatError("неверный формат")

    cleaned_number = ''.join(filter(str.isdigit, number))

    operator_codes = {
        'МТС': ['910', '911', '912', '913', '914', '915', '916', '917', '918', '919', '980', '981', '982', '983', '984', '985', '986', '987', '988', '989'],
        'МегаФон': ['920', '921', '922', '923', '924', '925', '926', '927', '928', '929', '930', '931', '932', '933', '934', '935', '936', '937', '938', '939'],
        'Билайн': ['902', '903', '904', '905', '906', '960', '961', '962', '963', '964', '965', '966', '967', '968', '969']
    }

    operator_code = cleaned_number[1:4]

    operator_name = None
    for operator, codes in operator_codes.items():
        if operator_code in codes:
            operator_name = operator
            break

    if len(cleaned_number) != 11:
        raise DigitCountError("неверное количество цифр")

    if number.startswith('+7'):
        number = '+7' + number[2:]
    elif number.startswith('8'):
        number = '+7' + number[1:]
    else:
        raise CountryCodeError("неверный код страны")

    if operator_name is None:
        raise OperatorError("не определяется оператор сотовой связи")

    return cleaned_number


def main():
    try:
        phone_number = input("Введите номер телефона: ")
        formatted_number = format_phone_number(phone_number)
        print(formatted_number)
    except (CountryCodeError, DigitCountError, OperatorError, FormatError) as e:
        print(e)
