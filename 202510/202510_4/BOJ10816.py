if __name__ == "__main__":
    N = int(input())

    cards = list(map(int, input().split()))
    card_dict = {}
    for card in cards:
        if card_dict.get(card):
            card_dict[card] += 1
        else:
            card_dict[card] = 1

    M = int(input())
    find_nums = list(map(int, input().split()))
    result = []
    for num in find_nums:
        if card_dict.get(num):
            result.append(card_dict.get(num))
        else:
            result.append(0)
    
    print(" ".join(map(str, result)))

