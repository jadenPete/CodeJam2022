import collections
import math

for i in range(int(input())):
    input()

    fun = [0] + list(map(int, input().split()))

    nodes = collections.defaultdict(list)

    for j, parent in enumerate(map(int, input().split()), 1):
        nodes[parent].append(j)

    def node_result_max(j):
        if len(nodes[j]) == 0:
            return fun[j], fun[j]

        result_sum = 0

        final_delta = -math.inf
        final_max = 0

        for k in nodes[j]:
            result, old_max = node_result_max(k)

            result_sum += result

            new_max = max(old_max, fun[j])

            if new_max - old_max > final_delta:
                final_delta = new_max - old_max
                final_max = new_max

        return result_sum + final_delta, final_max

    print(f"Case #{i + 1}: {node_result_max(0)[0]}")
