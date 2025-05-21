import random
import time
from Bubblesort import Bubblesort, Bubblesort_with_steps
from Bogosort import Bogosort, Bogosort_with_steps
from TwoPointSort import TwoPointSort
from MergeSort import MergeSort, MergeSort_WithSteps
from SelectionSort import SelectionSort

from Utilities import run_sort, run_step_by_step_demo, clear_console

def get_sorting_algorithms():
    return {
        "1": {
            "name": "Bubble Sort",
            "function": Bubblesort,
            "with_steps": Bubblesort_with_steps
        },
        "2": {
            "name": "Bogo Sort",
            "function": Bogosort,
            "with_steps": Bogosort_with_steps
        },
        "3": {
            "name": "Merge Sort",
            "function": MergeSort,
            "with_steps": MergeSort_WithSteps
        },
        "4": {
            "name": "Selection Sort",
            "function": SelectionSort,
            "with_steps": None
        },
        "5": {
            "name": "Two-Point Sort",
            "function": TwoPointSort,
            "with_steps": None
        },
    }

def choose_algorithm():
    algorithms = get_sorting_algorithms()

    print("\nChoose sorting algorithm:")
    for key, value in algorithms.items():
        print(f"[{key}] {value['name']}")

    choice = input("Input: ").strip()
    clear_console()

    if choice in algorithms:
        return algorithms[choice]
    else:
        print("Invalid choice.")
        return None

def run_speed_test():
    algo = choose_algorithm()
    if algo:
        run_sort(algo["name"], algo["function"])

def run_visual_demo():
    algo = choose_algorithm()
    if algo and algo["with_steps"]:
        run_step_by_step_demo(algo["name"], algo["with_steps"])
    elif algo:
        print(f"\n{algo['name']} does not support step-by-step visualization yet.\n")
        input("Press Enter to continue...")

def main():
    while True:
        clear_console()
        print("\n--- Sorting Program Menu ---")
        print("[1] Test Sorting Speed")
        print("[2] Step-by-Step Showcase")
        print("[3] Sorting Race (not implemented)")
        print("[4] Exit")

        choice = input("Input: ").strip()
        clear_console()

        if choice == "1":
            run_speed_test()
        elif choice == "2":
            run_visual_demo()
        elif choice == "3":
            print("Sorting race is not implemented yet.")
            input("Press Enter to continue...")
        elif choice == "4":
            print("Exiting program.")
            break
        else:
            print("Invalid option.")
            time.sleep(1)

if __name__ == "__main__":
    main()
