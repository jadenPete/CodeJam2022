import math

limit = 10 ** 6

for i in range(int(input())):
    units = [math.inf] * 4

    for _ in range(3):
        new_units = map(int, input().split())

        for j, new_unit in enumerate(new_units):
            units[j] = min(units[j], new_unit)

    total = 0

    print(f"Case #{i + 1}: ", end="")

    if sum(units) < limit:
        print("IMPOSSIBLE")
    else:
        for i, unit in enumerate(units):
            if total + unit > limit:
                print(limit - total, end="")

                total = limit
            else:
                print(unit, end="")

                total += unit

            if i < 3:
                print(" ", end="")

        print()
