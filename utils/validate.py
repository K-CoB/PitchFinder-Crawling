import re


def validate_data(datas):
    for i in range(len(datas)):
        for j in range(len(datas[i])):
            if type(datas[i][j]) == int:
                continue
            pattern = r'\s*\[.*?\]'
            datas[i][j] = re.sub(pattern=pattern, repl="", string=datas[i][j])
    return datas