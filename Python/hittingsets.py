
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

    return None, None
