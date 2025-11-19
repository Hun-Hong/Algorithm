if __name__ == "__main__":
    import sys
    input = sys.stdin.readline
    
    N, M = map(int, input().split())

    parent = [i for i in range(N + 1)]

    def union(a, b):
        global parent

        anc_a = find(a)
        anc_b = find(b)
        
        if anc_a != anc_b:
            parent[anc_b] = anc_a
        
    
    def find(a):
        global parent

        if parent[a] == a:
            return a
        else:
            anc_a = find(parent[a])
            parent[a] = anc_a
            return anc_a
            
    for _ in range(M):
        a, b = map(int, input().split())

        union(a, b)
    
    for i in range(N + 1):
        find(i)

    print(len(set(parent)) - 1)