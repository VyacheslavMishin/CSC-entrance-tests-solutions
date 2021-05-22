csc_expr = input()


def csc_calculator(expression):
    if expression == "":
        return "ERROR"
    braces_balance, operators_balance = 0, 0
    set_of_accepted_symbols = {'+', '-', '*', '/', '^', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '(', ')', " "}
    operators_set = {'+', '-', '*', '/', '^'}
    for item in expression:
        if item == '(':
            braces_balance += 1
            operators_balance += 1
        elif item == ')':
            braces_balance -= 1
        elif item not in set_of_accepted_symbols:
            return "ERROR"
        elif item in operators_set:
            operators_balance -= 1
        if braces_balance < 0 or braces_balance > 1:
            return "ERROR"
        if operators_balance < 0:
            return "ERROR"

    if braces_balance:
        return "ERROR"

    common_stack, parsed_string = [], ""
    for item in expression:
        if item == '(' or item == ')':
            parsed_string += " " + item + " "
        else:
            parsed_string += item

    parsed_string = parsed_string.split()

    for item in parsed_string:
        if item == '(':
            continue
        if item in operators_set:
            common_stack.append(item)
        elif item != ')':
            common_stack.append([item])
        elif len(common_stack):
            temp_lst, elem = [], ""
            while True:
                try:
                    elem = common_stack.pop(len(common_stack) - 1)
                except IndexError:
                    return "ERROR"
                if type(elem) != list:
                    if elem in operators_set:
                        break
                else:
                    temp_lst.append([int(it) for it in elem])
            if elem == '+':
                if len(temp_lst) == 2:
                    common_stack.append([temp_lst[0][0] + temp_lst[1][0], 1])
                else:
                    return "ERROR"
            elif elem == '-':
                if len(temp_lst) == 2:
                    common_stack.append([temp_lst[1][0] - temp_lst[0][0], 1])
                elif len(temp_lst) == 1:
                    common_stack.append([-temp_lst[0][0], 1])
                else:
                    return "ERROR"
            elif elem == '*':
                if len(temp_lst) == 2:
                    common_stack.append([temp_lst[0][0] * temp_lst[1][0], 1])
                else:
                    return "ERROR"
            elif elem == '/':
                if len(temp_lst) == 2:
                    if temp_lst[0][0] != 0:
                        common_stack.append([temp_lst[1][0] // temp_lst[0][0], 1])
                    else:
                        return "ERROR"
                else:
                    return "ERROR"
            elif elem == "^":
                if len(temp_lst) == 2:
                    if len(temp_lst[0]) == 1 and temp_lst[0][0] >= 0:
                        common_stack.append([temp_lst[1][0] ** temp_lst[0][0], 1])
                    else:
                        return "ERROR"
                else:
                    return "ERROR"
        else:
            return "ERROR"

    return common_stack[0][0]


print(csc_calculator(csc_expr))
