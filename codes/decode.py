import string

alpha = string.ascii_lowercase

def decode(stepStart: str, stepArray: list, signArray: list):
    message: list = []
    stepStartIndex = alpha.index(stepStart)
    pos = stepStartIndex
    for i in range(1,len(stepArray)):
        if signArray[i - 1] == "+":
            pos += int(stepArray[i])
        elif signArray[i - 1] == "-":
            pos -= int(stepArray[i])
        message.append(alpha[pos])
    return message

if __name__ == "__main__":
    print(decode("o",[1,2,3],["+","+","-"]))