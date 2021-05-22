def all_different_variants(matrix, answer, used_place):
    for place in range(len(matrix[0])):
        if place not in used_place and matrix[len(used_place)][place] != 1:
            if len(used_place) != len(matrix) - 1:
                used_place.add(place)
                all_different_variants(matrix, answer, used_place)
                used_place.remove(place)
            if len(used_place) == len(matrix) - 1:
                answer.append(1)
    return


matrix_size, M, ans = int(input()), [], []

for string in range(matrix_size):
    M.append(list(map(int, input().split())))

all_different_variants(M, ans, set())

print(sum(ans))
