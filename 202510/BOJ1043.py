if __name__ == "__main__":
    import sys
    input = sys.stdin.readline

    N, M = map(int, input().split())
    
    n_true, *knows = map(int, input().split())

    parent = [i for i in range(N + 1)]
    rank = [0 for _ in range(N + 1)]

    def union(a, b):
        anc_a = find(a)
        anc_b = find(b)

        if anc_a == anc_b:
            return False
        
        if rank[anc_a] > rank[anc_b]:
            parent[anc_b] = anc_a
        elif rank[anc_a] < rank[anc_b]:
            parent[anc_a] = anc_b
        else:
            parent[anc_b] = anc_a
            rank[anc_a] += 1
    
    def find(a):
        if parent[a] == a:
            return a
        else:
            anc_a = find(parent[a])
            parent[a] = anc_a
            return anc_a
    
    if knows:
        for know in knows:
            union(0, know)
    
    attend_list = []
    for _ in range(M):
        N_attend, *attends = list(map(int, input().split()))
        attend_list.append(attends)

        for attend in attends[1:]:
            union(attends[0], attend)
    
    count = 0
    for attends in attend_list:
        for attend in attends:
            if find(attend) == find(0):
                break
        else:
            count += 1

    print(count)