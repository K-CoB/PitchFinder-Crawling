import re


def validate_data(data):
    if type(data) == int:
        return data
    pattern = r'\s*\[.*?\]'
    data = re.sub(pattern=pattern, repl="", string=data)
    return data