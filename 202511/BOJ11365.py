if __name__ == "__main__":
    while True:
        code = input()
        if code == "END":
            break

        print(code[::-1])