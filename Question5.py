# given function
def processString(input_str):
    output_str = ""
    for char in input_str:
        if char.isupper():
            output_str += char.lower()
        elif char.isnumeric():
            output_str += char * 2
        else:
            output_str += char.upper()

    return output_str


# test special signs
result = processString("+=-_@#$%^&*!()<>?:|")
print(result)
# test alphabet
result = processString("abcdefghijklmnopqrstuvwxyz")
print(result)

result = processString("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
print(result)

# test numbers
result = processString("CCDDEExy")
print(result)


# delta-debugging:
# since we already found the bug, which will change the length of inputs in some cases
# therefore, we check the length of input and output to find the problem in inputs.

def DeltaDebugging(input):
    # base case, when to end the recursion
    if len(input) <= 1:
        if len(processString(input)) == len(input):
            return ""
        else:
            return input
    output = processString(input)
    # check if the input will cause the bug
    if len(input) == len(output):
        return ""
    else:
        # binary search implemented by recursion
        left = DeltaDebugging(input[:(len(input) // 2)])
        right = DeltaDebugging(input[(len(input) // 2):])
        return left + right


# test cases

print(DeltaDebugging("abcdefG1"))
print(DeltaDebugging("CCDDEExy"))
print(DeltaDebugging("1234567b"))
print(DeltaDebugging("8665"))
