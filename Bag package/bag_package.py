def right_distribution():
    number_of_goods = int(input())
    weights_lst = sorted(list(map(int, input().split())), reverse=True)
    if number_of_goods == 1:
        return "NO"
    else:
        max_weight = weights_lst[0]
        rest_weight = sum(weights_lst) - max_weight
        if max_weight > 2 * rest_weight:
            return "NO"
        elif 0.5 <= max_weight / rest_weight <= 2:
            return "YES"
        else:
            for i in range(2, number_of_goods):
                max_weight += weights_lst[i]
                rest_weight -= weights_lst[i]
                if 0.5 <= max_weight / rest_weight <= 2:
                    return "YES"


print(right_distribution())
