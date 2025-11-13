
def run_hitting_set_algorithm(conflict_sets):
    """
    Algorithm that handles the entire process from conflict sets to hitting sets

    :param conflict_sets: list of conflict sets as list
    :return: hit_sets_list: list of hitting sets as a list
             min_hitting_sets_list: list of minimal hitting sets as a list
    """

    conflict_sets_list = list(conflict_sets)

    print("Heuristic = 0", conflict_sets_list)
    print('Enter Heuristic :')
    heuristic = int(input())
    
    if heuristic == 1:      # sort the conflict set with the smallest set first
        con_set = list(sorted(conflict_sets_list, key=len))
        print("Heuristic = 1", con_set)
    elif heuristic ==2:     # sort the conflict set with the Largest set first
        con_set = list(sorted(conflict_sets_list, key=len, reverse=True))
        print("Heuristic = 2", con_set)
    elif heuristic == 3:     # containing the most common elements
        print("Heuristic = 3", conflict_sets_list)
        element_dic = {}
        for subset in conflict_sets_list:   # create dictionary with element counts
            for e in subset:
                if e in element_dic:
                    element_dic[e] += 1
                else:
                    element_dic[e] = 1
        weights = []    # get the element Weight for the supset
        for s in conflict_sets_list:
            weight = 0
            for e in s:
                weight = element_dic[e]+1
            weights.append((s, weight))
        conflict_sets_list = sorted(weights, key=lambda x: x[1], reverse=True)
        print("Heuristic = 3", conflict_sets_list)
        
    def first_unhit_set(selection):
        # return the first conflict set not yet hit by 'selection', if all sets are hit return none
        for subset in conflict_sets_list:
            hit = False
            for element in subset:
                if element in selection:
                    hit = True
                    break   # only stop checking this set
            if not hit:
                return subset   # return first unhit set
        return None         # all sets were hit

    hitting_sets_list = []
    stack = [[]]
    counter = 0

    while stack:
        counter = counter + 1
        path = stack.pop()
        print(counter, "path =", path)

        unhit_set = first_unhit_set(path)
        print(counter, "unhit_set =", unhit_set)

        if unhit_set is None:
            hitting_sets_list.append(path)
            print(counter, "hitting sets list =", hitting_sets_list)
            continue

        for item in unhit_set:
            if item not in path:
                stack.append(path + [item])
                print(counter, "path+item =", stack)

    hitting_sets = set()    # creating an empty set for the hitting sets
    hitting_sets.update(frozenset(sets) for sets in hitting_sets_list)  # converting the lists to sets
    min_hitting_sets = hitting_sets.copy()

    for hit_set in hitting_sets:
        for hit_set_compare in hitting_sets:
            if hit_set_compare != hit_set and hit_set.issuperset(hit_set_compare):
                min_hitting_sets.remove(hit_set)

    min_hitting_sets_list = [list(sets) for sets in min_hitting_sets]   # converting the sets back to lists

    return hitting_sets_list, min_hitting_sets_list
