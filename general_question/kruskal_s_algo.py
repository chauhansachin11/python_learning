def add_visit(v_ar,edge):
    l=len(v_ar)
    for i in range(l):
        if(edge[0] in v_ar[i]):
            if(edge[1] in v_ar[i]):
                return(0,v_ar)
            else:
                for j in range(l):
                    if(edge[1] in v_ar[j]):
                         v_ar=[v_ar[i]+v_ar[j]]+list(filter(lambda x:x!=v_ar[i] and x!=v_ar[j],v_ar))
                         return(1,v_ar)
                v_ar[i]+=[edge[1]]
                return(1,v_ar)
        elif(edge[1] in v_ar[i]):
             for j in range(l):
                 if(edge[0] in v_ar[j]):
                     v_ar=[v_ar[i]+v_ar[j]]+list(filter(lambda x:x!=v_ar[i] and x!=v_ar[j],v_ar))
                     return(1,v_ar)
             v_ar[i]+=[edge[0]]
             return(1,v_ar)            
    v_ar+=[[edge[0],edge[1]]]
    return(1,v_ar)



def kruskal_s_algo(ed):
    ed.sort(key=lambda x:x[2])
    v_arr=[]
    for i in ed:
        is_add,v_arr=add_visit(v_arr,i)
        if(is_add==1):
            print(i[0],i[1])


edges=[[1,4,5],[5,6,2],[3,5,8],[0,3,6],[0,1,2],[1,2,3],[4,6,10],[1,3,8],[2,4,7],[4,3,9]]
kruskal_s_algo(edges)

