if __name__ == "__main__":
    position = input()
    # . 빈칸
    # @ 로봇
    # # 박스
    # ! 목적지

    for idx, char in enumerate(position):
        if char == "@":
            robot_idx = idx
        elif char == "#":
            box_idx = idx
        elif char == "!":
            dest_idx = idx
    
    if (robot_idx < box_idx < dest_idx) or (dest_idx < box_idx < robot_idx):
        print(abs(robot_idx - dest_idx) - 1)
    else:
        print("-1")