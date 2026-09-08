def add(n1, n2):
    return n1 + n2


def sub(n1, n2):
    return n1 - n2


def multi(n1, n2):
    return n1 * n2


def div(n1, n2):
    if n2 == 0:
        raise ValueError("Cannot divide by 0")
    elif n1 == 0 and n2 == 0:
        raise ValueError("Cannot divide 0 by 0")
    elif n1 == 0:
        return 0
    return n1 / n2


OPERATIONS = {
    "+": add,
    "-": sub,
    "*": multi,
    "/": div,
}

first_num = input("Enter the number: ")

for key in OPERATIONS:
    print(key)
sign_decision = input("Pick an operation from the line above: ")


second_num = input("Enter number: ")

answer = OPERATIONS[sign_decision](int(first_num), int(second_num))
print(f"Result: {first_num} {sign_decision} {second_num} = {answer}")


choose = input("Do you want to continue calculating with the result? (y/n)")


if choose.lower() == "y":
    print(f"Result: {answer}")

    for key in OPERATIONS:
        print(key)
    sign_decision = input("Pick an operation from the line above: ")

    

    second_num = input("Enter the number: ")

    answer = OPERATIONS[sign_decision](int(first_num), int(second_num))
    print(f"Result: {first_num} {sign_decision} {second_num} = {answer}")

    choose = input("DO you want to continue calculating with the result? (y/n)")










# elif choose.lower == "n":
#     break