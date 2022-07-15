import math

digits = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
signs = ['+', '-', '*', '/', '(', ')']


def vision(expression):
    def NumberConvertor(expression, i):
        result = ''
        for j in range(i, len(expression)):
            if expression[j] in digits:
                result = result + expression[j]
            else:
                break
        return (int(result))

    format_expression = []
    for i in range(len(expression)):
        if expression[i] != ' ':
            if expression[i] in digits:
                if ((expression[i - 1] in digits) == False) or i == 0:
                    format_expression.append(NumberConvertor(expression, i))

            elif expression[i] in signs:
                format_expression.append(expression[i])
    return (format_expression)


def brackets(format_expression, begin, end):
    i = 0
    s_point = 0
    e_point = len(format_expression)
    while i < end:
        if format_expression[i] == '(':
            s_point = i + 1
        i += 1

    i = s_point

    while i < end:
        if format_expression[i] == ')':
            e_point = i - 1
            break
        i += 1

    return (s_point, e_point)


def deBrackets(format_expression, begin, end):
    print(begin, end)
    if len(format_expression) == 1:
        return (format_expression)

    if end - begin <= 2:
        print(format_expression)
        format_expression.pop(end + 1)
        print(format_expression)
        format_expression.pop(begin - 1)
        print(format_expression)

        return (format_expression)


def calc(format_expression):
    def PlusAndMinus(begin, end):

        i = begin

        while i < end:
            if format_expression[i] == '+' or format_expression[i] == '-':

                if format_expression[i] == '+':

                    format_expression[i] = format_expression[i - 1] + format_expression[i + 1]
                    format_expression.pop(i - 1)
                    format_expression.pop(i)
                    print(format_expression)
                    i -= 1
                    end -= 2

                elif format_expression[i] == '-':

                    format_expression[i] = format_expression[i - 1] - format_expression[i + 1]
                    format_expression.pop(i - 1)
                    format_expression.pop(i)
                    print(format_expression)
                    i -= 1
                    end -= 2

            i += 1
        return (begin, end)

    def MultiplyAndDivision(begin, end):

        i = begin

        while i < end:
            if format_expression[i] == '*' or format_expression[i] == '/':

                if format_expression[i] == '*':

                    format_expression[i] = format_expression[i - 1] * format_expression[i + 1]
                    format_expression.pop(i - 1)
                    format_expression.pop(i)
                    print(format_expression)
                    i -= 1
                    end -= 2

                elif format_expression[i] == '/':

                    format_expression[i] = format_expression[i - 1] / format_expression[i + 1]
                    format_expression.pop(i - 1)
                    format_expression.pop(i)
                    print(format_expression)
                    i -= 1
                    end -= 2

            i += 1
        return (begin, end)

    if len(format_expression) > 1:
        begin, end = brackets(format_expression, 0, len(format_expression))
        begin, end = MultiplyAndDivision(begin, end)
        begin, end = PlusAndMinus(begin, end)
        begin, end = brackets(format_expression, 0, len(format_expression))
        deBrackets(format_expression, begin, end)

        print(format_expression)
    else:
        return (format_expression)
    calc(format_expression)


y = str(input())
format_expression = vision(y)
print(format_expression)
breckout = calc(format_expression)
print(breckout)
