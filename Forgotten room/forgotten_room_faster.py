def rooms_to_check(rooms_amount, minimal_digit, maximal_digit):
    if minimal_digit == '0' and maximal_digit == '0':
        return 0

    if minimal_digit == maximal_digit:
        for digit in rooms_amount:
            if digit > maximal_digit:
                return len(rooms_amount)
            if digit < minimal_digit:
                return len(rooms_amount) - 1
        return len(rooms_amount)

    if minimal_digit == '0':
        if rooms_amount[0] < maximal_digit:
            return 2 ** (len(rooms_amount) - 1) - 1
        elif rooms_amount[0] > maximal_digit:
            return 2 ** len(rooms_amount) - 1
        else:
            result = 2 ** (len(rooms_amount) - 1) - 1
            for index in range(1, len(rooms_amount)):
                if rooms_amount[index] > maximal_digit:
                    return result + 2 ** (len(rooms_amount) - index)
                if rooms_amount[index] == maximal_digit:
                    result += 2 ** (len(rooms_amount) - index - 1)
                    continue
                if rooms_amount[index] > minimal_digit:
                    return result + 2 ** (len(rooms_amount) - index - 1)

            return result + 1

    if rooms_amount[0] > maximal_digit:
        return 2 ** (len(rooms_amount) + 1) - 2

    result = 2 ** len(rooms_amount) - 2
    last_max_digit_index = -1

    for index in range(len(rooms_amount)):
        if rooms_amount[index] > maximal_digit:
            return result + 2 ** (len(rooms_amount) - index)
        if rooms_amount[index] == maximal_digit:
            result += 2 ** (len(rooms_amount) - index - 1)
            last_max_digit_index = index
            continue
        if rooms_amount[index] > minimal_digit:
            return result + 2 ** (len(rooms_amount) - index - 1)
        if rooms_amount[index] < minimal_digit:
            if last_max_digit_index == -1:
                return 2 ** len(rooms_amount) - 2
            else:
                return result

    return result + 1


rooms_number, x, y = input().split()

if x < y:
    print(rooms_to_check(rooms_number, x, y))
else:
    print(rooms_to_check(rooms_number, y, x))
