# two sum problem multiple solutions


def two_sum_hash(ar, target):
    hash = {}
    all_solutions = []
    for idx, num in enumerate(ar):
        complement = target - num
        if complement in hash:
            all_solutions.append([hash[complement], idx])
        hash[num] = idx
    if len(all_solutions) > 0:
        return all_solutions
    else:
        return []


if __name__ == "__main__":
    ar = [10, 5, 2, 12, 7, 95, 90]
    target = 100
    print(two_sum_hash(ar, target))
    # output: [[1, 5], [0, 6]]
