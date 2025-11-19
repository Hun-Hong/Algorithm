if __name__ == "__main__":
    T = int(input())

    for _ in range(T):
        p_string = input()
        stack = []
        idx = 0
        while idx < len(p_string):
            if not stack:
                stack.append(p_string[idx])
                idx += 1
            else:
                if p_string[idx] == ")":
                    if stack[-1] == "(":
                        stack.pop()
                        idx += 1
                        continue
                    else:
                        print("NO")
                        break
                else:
                    stack.append(p_string[idx])
                    idx += 1
        else:
            if stack:
                print("NO")
            else:
                print("YES")


