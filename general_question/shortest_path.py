def find_min_path(A,S,x,y,p,q):
    if x==p and y==q:
        return A[x][y]
    if x>p or y>q:
        return 0
    if S[x][y] is not None:
        return S[x][y]
    else:
        if x+1 > p or y+1 > q:
            S[x][y] = A[x][y] + max(find_min_path(A,S,x+1,y,p,q),find_min_path(A,S,x,y+1,p,q))
        else:
            S[x][y] = A[x][y] + min(find_min_path(A,S,x+1,y,p,q),find_min_path(A,S,x,y+1,p,q))
        return S[x][y]

def main():
    A = [[2,1,1,6,2],[9,3,4,5,8],[2,8,3,6,9],[4,2,6,5,6]]
    S = [[None]*5]*4
    a = find_min_path(A,S,0,0,3,4)
    print(a)

main()
