import string

alpha = string.ascii_lowercase

def decode(stepStart: str, stepArray: list, signArray: list):
    message: list = []
    stepStartIndex = alpha.index(stepStart)
    pos = stepStartIndex
    for i in range(0,len(stepArray)):
        if signArray[i] == "+":
            pos += stepArray[i]
        elif signArray[i] == "-":
            pos -= stepArray[i]
        message.append(alpha[pos])
    return message
print(decode("o",[1,2,3],["+","+","-"]))