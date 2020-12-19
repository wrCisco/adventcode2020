#!/usr/bin/env python3


def compute(expr, second):
    nums = []
    ops = []
    i = 0
    while i < len(expr):
        c = expr[i]
        i += 1
        if c == '(':
            j, c = compute(expr[i:], second)
            i += j
        elif c == ')':
            if second:
                while len(nums) > 1:
                    nums.append(nums.pop() * nums.pop())
            return i, str(nums[0])
        if c.isdigit():  # c becomes a number if it was '('
            nums.append(int(c))
            if len(nums) > 1:
                if ops[-1] == '+':
                    nums.append(nums.pop() + nums.pop())
                    ops.pop()
                elif not second:
                    nums.append(nums.pop() * nums.pop())
                    ops.pop()
        else:
            ops.append(c)
    return nums[0]


# alternative method: infix to postfix, then evaluate
def compute2(expression, second):
    # translate from infix to postfix
    if second:
        max_prec = '(+'
        min_prec = '*'
    else:
        max_prec = '('
        min_prec = '+*'
    operators = []
    postfixed = []
    for c in expression:
        if c.isdigit():
            postfixed.append(int(c))
        elif c in max_prec:
            operators.append(c)
        elif c in min_prec:
            if operators:
                to_out = operators.pop()
                while to_out not in ('(', None):
                    postfixed.append(to_out)
                    to_out = operators.pop() if operators else None
                if to_out:
                    operators.append(to_out)
            operators.append(c)
        elif c == ')':
            to_out = operators.pop()
            while to_out != '(':
                postfixed.append(to_out)
                to_out = operators.pop()
    while operators:
        postfixed.append(operators.pop())
    # evaluate postfix expression
    operands = []
    for c in postfixed:
        if isinstance(c, int):
            operands.append(c)
        else:
            op2 = operands.pop()
            op1 = operands.pop()
            operands.append(op1 * op2 if c == '*' else op1 + op2)
    return operands.pop()


def run():
    with open('input.txt') as fh:
        lines = ['('+line.strip().replace(' ', '')+')' for line in fh]

    print(sum(compute(line, False) for line in lines))
    print(sum(compute(line, True) for line in lines))


if __name__ == '__main__':
    run()
