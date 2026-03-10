def jaccard_similarity(set_a, set_b):
    set_un=set()
    set_int=set()
    
    for i in set_a:
        if i in set_b:
            set_int.add(i)
            
    for i in set_a:
        set_un.add(i)
        
    for i in set_b:
        set_un.add(i)
            
    l=len(set_int)
    p=len(set_un)

    if p == 0:
        return 0
    
    return l/p