codes = {
    "identifier": 0,
    "constant": 1,
    "array": 2,
    "if": 3,
    "haha_unless": 4,
    "while": 5,
    "+": 6,
    "-": 7,
    "*": 8,
    "/": 9,
    "=": 10,
    "<": 11,
    "<=": 12,
    ">": 13,
    ">=": 14,
    "==": 15,
    "(": 16,
    ")": 17,
    "int": 18,
    "char": 19,
    "bool": 20,
    "and": 21,
    "or": 22,
    "[": 23,
    "]": 24,
    "{": 25,
    "}": 26,
    ";": 27,
    ":": 28,
    " ": 29,
    ",": 30,
    "write": 31,
    "read": 32,
    "true": 33,
    "false": 34,
    "&&": 35
}

operators = ['+', '-', '*', '/', '=', '<', '<=', '>', '>=', '&&']

separators = ['[', ']', '{', '}', ';', ':', ' ', '(', ')', ',', "'"]

reserved_words = ["array", "if", "haha_unless", "while", "write", "read", "true", "false"]

operators_separator_words = operators + separators + reserved_words
