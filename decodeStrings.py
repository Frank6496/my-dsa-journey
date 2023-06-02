def decodeStr(str):
    stack = []
    for i in range(len(str)):
        if str[i] != "]":
            stack.append(str[i])
        else:

            currChar = ""
            while stack[-1] != "[":
                currChar = stack.pop() + currChar
            stack.pop()

            k = ""
            while stack and stack[-1].isdigit():
                k = stack.pop() + k
            stack.append(int(k) * currChar)

    return "".join(stack)

