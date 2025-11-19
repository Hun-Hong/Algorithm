if __name__ == "__main__":
    fomula = input()
    stack = []
    icp = {
        "+": 1,
        "-": 1,
        "*": 2,
        "/": 2,
        "(": 3,
        ")": "",
    }
    isp = {
        "+": 1,
        "-": 1,
        "*": 2,
        "/": 2,
        "(": 0,
        ")": "",
    }
    postorder = ""
    for char in fomula:
        # print(stack, postorder)
        if icp.get(char) == None:
            postorder += char
            continue

        if not stack:
            stack.append(char)
        else:
            if char == ")":
                while stack[-1] != "(":
                    postorder += stack.pop()
                else:
                    stack.pop()
                continue
            
            while stack and (icp.get(char) <= isp.get(stack[-1])):
                postorder += stack.pop()

            stack.append(char)
    else:
        while stack:
            postorder += stack.pop()

    print(postorder)
    