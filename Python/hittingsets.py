import dictionary as dct

def run_hitting_set_algorithm(conflict_sets):
    """
    Algorithm that handles the entire process from conflict sets to hitting sets

    :param conflict_sets: list of conflict sets as list
    :return: the hitting sets and minimal hitting sets as list of lists
    """

    #--------------- here is what I wrote: ------------------

    root_node = conflict_sets[0] #get the root node
    stack = [] #create an empty stack
    stack.append(root_node) #place the root node on the stack
    print("the stack is:", stack)

    while len(stack) > 0: #while the stack is not empty
        stack.pop() #remove the rootnode

        #next_node = conflict_sets[i]

        print("after popping the stack is", stack)


    return None, None
