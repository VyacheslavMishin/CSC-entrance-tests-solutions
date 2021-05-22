def rooms_to_check_short(rooms_number, minimal_digit, maximal_digit):
    ctrl_set = {minimal_digit, maximal_digit}
    return sum([set(str(n)).issubset(ctrl_set) for n in range(1, rooms_number + 1)])


'''rooms_amount, x, y = input().split()
rooms_amount, control_set = int(rooms_amount), {x, y}

print(rooms_to_check_short(rooms_amount, x, y))
'''