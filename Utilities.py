import random
import time
import os

def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')

def Get_Random_List(amount):
    return [random.randint(1, 9) for _ in range(amount)]

def Reverse_List(nums):
    return sorted(nums, reverse=True)

def createsortinglists():
    print("\nChoose Length(s) (e.g., '1' for 10, '123' for 10, 100, 1000):")
    options = {
        "1": 10,
        "2": 20,
        "3": 100,
        "4": 1000,
        "5": 10000,
        "6": 100000,
        "7": 1000000
    }
    # printing all values
    for key, val in options.items():
        print(f"[{key}] {val}")
        
    choice = input("Your choice: ").strip()
    clear_console()

    lists_to_return = []

    # foreach char in input add list to lists_to_return
    for char in choice:
        if char in options:
            size = options[char]
            lists_to_return.append(Get_Random_List(size))

    return lists_to_return

def run_sort(sort_name, sort_function):
    lists = createsortinglists()
    for unsortedlist in lists:
        # loop over all unsortedlists and benchmark all sorts
        print(f"\nRunning {sort_name}...")
        print (f"Length: {len(unsortedlist)}")
        start = time.time()
        sort_function(unsortedlist)  # call function of selected sort
        end = time.time()
        print(f"{sort_name} finished in {end - start:.6f} seconds")
    print("press enter to continue")
    input()

def run_step_by_step_demo(sort_name, sort_with_steps_function):
    clear_console()
    print(f"Running step-by-step demo for {sort_name}...\n")
    nums = Get_Random_List(10)  # Small size for clarity
    steps = sort_with_steps_function(nums)
    visualize_sorting_steps(steps)
    input("Press Enter to continue...")


def visualize_sorting_steps(steps):
    import time

    def render_horizontal_chart(data, i, j, step_number):
        clear_console()
        max_height = max(data)
        bar_char = "█"
        width = len(data)
        column_width = 3

        print(f"Step {step_number + 1} of {len(steps)} | Comparing indices {i} and {j}\n")

        for level in range(max_height, 0, -1):
            row = ""
            for idx, val in enumerate(data):
                if val >= level:
                    if idx == i:
                        row += f"\033[91m{bar_char.center(column_width)}\033[0m"
                    elif idx == j:
                        row += f"\033[92m{bar_char.center(column_width)}\033[0m"
                    else:
                        row += bar_char.center(column_width)
                else:
                    row += " " * column_width
            print(row)

        # Print index numbers below bars, centered
        value_row = ""
        for val in data:
            value_row += f"{str(val).center(column_width)}"
        print(value_row)


    # Step by step loop
    step_index = 0
    while True:
        current_state, i, j = steps[step_index]
        render_horizontal_chart(current_state, i, j, step_index)

        print("\n[1] Next | [2] Previous | [q] Quit")
        choice = input("Choice: ").strip()

        if choice == "1":
            if step_index < len(steps) - 1:
                step_index += 1
            else:
                print("Already at last step.")
                time.sleep(0.5)
        elif choice == "2":
            if step_index > 0:
                step_index -= 1
            else:
                print("Already at first step.")
                time.sleep(0.5)
        elif choice.lower() == "q":
            break
        else:
            print("Invalid input.")
            time.sleep(0.5)

    print("\nVisualization ended.")
