import sys

def min_val(key_v,mst):
    mi=sys.maxunicode
    l=len(key_v)
    index = 0
    for i in range(l):
        if(mst[i]==False) and (mi>key_v[i]):
                mi=key_v[i]
                index=i
    return index


def all_node(prnt):
    l=len(prnt)
    for i in range(1,l):
        print(prnt[i],i,graph[i][prnt[i]])


def prims_algo(g,v):
    mstset=[False]*v
    key_val=[sys.maxunicode]*v
    key_val[0]=0
    parent=[None]*v
    parent[0]=-1
    n=len(g)
    for i in range(v):
        m=min_val(key_val,mstset)
        mstset[m]=True
        for j in range(v):
            if(g[m][j]<key_val[j] and g[m][j]>0 and mstset[j]==False):
                key_val[j]=g[m][j]
                parent[j]=m

    all_node(parent)    




vrtx=7
edges=[[0,1,2],[1,2,3],[1,4,5],[0,3,6],[2,4,7],[1,3,8],[3,4,9],[5,6,2],[3,5,8],[4,6,10]]
graph=[[sys.maxunicode for i in range(vrtx)] for i in range(vrtx)]

for i in edges:
    graph[i[0]][i[1]]=i[2]
    graph[i[1]][i[0]]=i[2]


prims_algo(graph,vrtx)
