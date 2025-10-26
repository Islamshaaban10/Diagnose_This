
def run_hitting_set_algorithm(conflict_sets):
    """
    Algorithm that handles the entire process from conflict sets to hitting sets

    :param conflict_sets: list of conflict sets as list
    :return: the hitting sets and minimal hitting sets as list of lists
    """

    #--------------- here is what I wrote: ------------------
    

    #stack = [] #create an empty stack
    visited_nodes = []

    stack = conflict_sets.copy()
    print("not visited nodes:", stack)

    #root_node = conflict_sets[0]  # get the root node

    print("the stack before popping is:", stack)

    while len(stack) > 0: #while the stack is not empty
        visited_nodes.append(stack[0]) #add the top node to the list of visited nodes
        print("visited nodes is:", visited_nodes)

        stack.pop(0) #remove the top node from the stack
        print("the stack after popping:", stack)

        #set its label to a set S ∈ F not yet hit by the set of edge labels on the path from the root to this node, or to ✓ otherwise

        
    #-------------------finding the hit set ----------------------
    '''
    for subset in conflict_sets :
        for e in subset :
        print (e)
    '''

    con_set = conflict_sets.copy()

    def first_unhit (selection):
            # return the frist conflict set not yet hit by ' selection' , else none 
            for subset in con_set:
                hit = False
                for element in subset:
                    if element in selection:
                        hit = True
                        break   # only stop checking this set
                if not hit:
                    return subset   # return first unhit set
            return None         # all sets were hit


    all_hits =[]
    stack =[[]]      
    counter =0
    while stack:
        counter = counter+1
        path = stack.pop()
        print (counter,"path =" ,path)
        unhit = first_unhit(path)
        print (counter,"unhit =" ,unhit)

        if unhit is None: 
            all_hits.append(path)
            print (counter,"all_hits =" ,all_hits)
            continue
        for u in unhit :
            if u not in path : 
                stack.append(path+[u])
                print (counter,"path+u =" ,stack)

    return all_hits, None
    #return None, None
