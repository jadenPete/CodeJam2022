def print_row(width, first=False, last=False):
    if first:
        print("..", end="")

        width -= 1

    print("+-" * width + "+")

    if first:
        print("..", end="")

    print("|." * width + "|")

    if last:
        print("+-" * width + "+")

for i in range(int(input())):
    height, width = map(int, input().split())

    print(f"Case #{i + 1}:")

    for j in range(height):
        print_row(width, first=j == 0, last=j == height - 1)
