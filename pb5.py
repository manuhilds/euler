
check_list = [11, 12, 13, 14, 15, 16, 17, 18, 19, 20]


def find_solution(step):
    for num in range(step, 9999999999, step):
        if all(num % n == 0 for n in check_list):
            return num
    return None


if __name__ == '__main__':
    solution = find_solution(2520)
    if solution is None:
        print("No answer found")
    else:
        print("found an answer:", solution)
