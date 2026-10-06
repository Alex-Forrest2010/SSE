import codes.decode
import codes.encode
import sys
import string
def getData():
    stepFileName = ""
    signFileName = ""
    startingCharacter = ""
    if len(sys.argv) == 3:
        stepFileName = sys.argv[1]
        signFileName = sys.argv[2]
    else:
        print("Enter exactly 2 arguments")
        return
    try:
        with open(stepFileName,"r") as stepFile:
            stepData = stepFile.read()
        with open(signFileName,"r") as signFile:
            signData = signFile.read()
    except FileNotFoundError:
        print("File(s) not found")
        return 
    if stepData[0] not in string.ascii_lowercase:
        startingCharacter = stepData[0]
    else:
        startingCharacter = "a"
    return (startingCharacter,stepData,signData)

if len(sys.argv) > 1:
    codeInfo = getData()
    if codeInfo == None:
        print("Some error occurred")
    else:
        print(codes.decode.decode(codeInfo[0],codeInfo[1],codeInfo[2]))