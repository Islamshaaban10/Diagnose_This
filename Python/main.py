from circuitplotter import plot_circuit
from guesscomponentsgame import choose_components, score_function
from conflictsets import ConflictSetRetriever
from hittingsets import run_hitting_set_algorithm
from os.path import join
import time 

if __name__ == '__main__':
    start_time = time.time()
    proces_time = time.process_time()
    document = "circuit7.txt"

    game = False

    # It only makes sense to play the game if you have the hitting set algorithm implemented.
    if game:
        # If you play the game, choose conflict sets, compute hitting sets:
        plot_circuit(document)
        chosen_conflict_sets = choose_components()
        print("Your chosen conflict sets:", chosen_conflict_sets)
        chosen_hitting_sets, chosen_minimal_hitting_sets = run_hitting_set_algorithm(chosen_conflict_sets)
        print("Your hitting sets:", chosen_hitting_sets)
        print("Your minimal hitting sets:", chosen_minimal_hitting_sets, "\n")

    # Collect conflict sets:
    csr = ConflictSetRetriever(join("circuits", document))
    conflict_sets = csr.retrieve_conflict_sets()
    print("Actual conflict sets:", conflict_sets)

    # Collect minimal hitting sets:
    if len(conflict_sets) == 0:
        print("This circuit works correctly, there are no faulty components!")
    else:
        hitting_sets, minimal_hitting_sets = run_hitting_set_algorithm(conflict_sets)
        print("Hitting sets:", hitting_sets)
        print("Minimal hitting sets:", minimal_hitting_sets, "\n")

    # Give score on similarity between the two sets:
    if game:
        score = score_function(conflict_sets, chosen_conflict_sets)
        print(f"Your score: {score:.2f}%")

    # printing the timestamps
    end_time = time.time()
    total_time = end_time-start_time
    print(f'start time: {start_time:.2f}, end time: {end_time:.2f}, total literal elapsed time: {total_time:.2f}seconds')
    print("proces time:", proces_time)
