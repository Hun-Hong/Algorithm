candidates = {str(i) for i in range(1000, 10000) if '0' not in str(i)}

def validate(number, answer):
    strike = 0
    ball = 0
    for i in range(4):
        if number[i] == answer[i]:
            strike += 1
        else:
            if number[i] in answer:
                ball += 1
    return (strike, ball)
        
def solution(n, submit):
    global candidates
    
    n_try = 0
    
    while n_try < n:
        if len(candidates) > 0:
            cand_list = list(candidates)
            cand_pr = [(len(set(cand)), cand)for cand in cand_list]
            cand_pr.sort(reverse=True)
            number = cand_pr[0][1]
        else:
            return 0
        result = submit(int(number))
        n_try += 1

        strike, ball = result.split()
        strike = int(strike[0])
        ball = int(ball[0])
        
        if strike == 4:
            print(n_try)
            return int(number)
        
        remove_list=[]
        
        for candidate in candidates:
            valid = validate(number, candidate)
            if valid != (strike, ball):
                remove_list.append(candidate)
                
        for remove_number in remove_list:
            candidates.remove(remove_number)
    else:
        return 0
            