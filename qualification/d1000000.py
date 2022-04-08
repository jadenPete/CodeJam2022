for i in range(int(input())):
    input()

    j = 0

    for n in sorted(map(int, input().split())):
        if j < n:
            j += 1

    print(f"Case #{i + 1}: {j}")

# O(N) Solution
# def solution(dice):
#     i = 0

#     for j, die in enumerate(dice):
#         if j >= die:
#             while i < j and j >= dice[i]:
#                 i += 1

#             if i == j:
#                 return j + 1

#             dice[i], dice[j] = dice[j], dice[i]

#     return j + 1

# for i in range(int(input())):
#     input()

#     dice = list(map(int, input().split()))

#     print(f"Case #{i + 1}: {solution(dice)}")
