
def run_hitting_set_algorithm(conflict_sets):
    """
    Algorithm that handles the entire process from conflict sets to hitting sets

    :param conflict_sets: list of conflict sets as list
    :return: the hitting sets and minimal hitting sets as list of lists
    """
        
    #-------------------finding the hit set ----------------------

    con_set = list (conflict_sets)
    con_set_reversed = con_set.reverse()
    print ("sorted" ,con_set_reversed)
    
    def Ishit(selection):
            # return the first conflict set not yet hit by ' selection' , else none
            for subset in con_set:
                hit = False
                for element in subset:
                    if element in selection:
                        hit = True
                        break   # only stop checking this set
                if not hit:
                    return subset   # return first unhit set
            return None         # all sets were hit


    all_hits = []
    stack = [[]]
    counter = 0

    while stack:
        counter = counter + 1
        path = stack.pop()
        #print (counter, "path =", path)

        unhit = Ishit(path)
        #print (counter, "unhit =", unhit)

        if unhit is None: 
            all_hits.append(path)
            #print(counter, "all_hits =", all_hits)
            continue

        for u in unhit:
            if u not in path:
                stack.append(path+[u])
                #print(counter, "path+u =", stack)

    #print("all_hits:", all_hits)



    # -------------------finding the minimal hitting sets ----------------------

    min_hit_sets = set()
    hitting_sets = set()

    hitting_sets.update(frozenset(set) for set in all_hits) #converting the lists to sets
    min_hit_sets.update(frozenset(set) for set in all_hits) #converting the lists to sets

    for hit_set in hitting_sets:
        for hit_set_compare in hitting_sets:
            if hit_set_compare != hit_set:
                if hit_set.issuperset(hit_set_compare):
                    #print("set", hit_set, "is a superset of", hit_set_compare)
                    min_hit_sets.remove(hit_set)

    min_hit_sets_list = [list(fs) for fs in min_hit_sets] #converting the sets back to lists
    #print("the minimal hitting sets are:", min_hit_sets_list)

    return all_hits, min_hit_sets_list