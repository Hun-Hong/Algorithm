if __name__ == "__main__":
    N = int(input())

    nums = list(map(int, input().split()))

    sorted_nums = sorted(list(set(nums)))

    num_dict = {}

    for idx, num in enumerate(sorted_nums):
        num_dict[num] = idx

    result = [num_dict[num] for num in nums]

    print(" ".join(map(str, result)))

