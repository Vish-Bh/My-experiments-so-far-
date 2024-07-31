import os

def print_diamond(n):
    if n % 2 == 0:
        n += 1
    mid_point = n // 2
    for i in range(mid_point):
        print(" " * (mid_point - i) + "*" * (2 * i + 1))
    for i in range(mid_point - 1, -1, -1):
        print(" " * (mid_point - i) + "*" * (2 * i + 1))

def clear_screen():
    if os.name == "nt":  # for windows
        _ = os.system("cls")
    else:  # for mac and linux(here, os.name is 'posix')
        _ = os.system("clear")

def main():
    clear_screen()
    n = int(input("Enter the size of the diamond (odd number): "))
    while n % 2 == 0:
        print("Please enter an odd number.")
        n = int(input("Enter the size of the diamond (odd number): "))
    print_diamond(n)

if __name__ == "__main__":
    main()