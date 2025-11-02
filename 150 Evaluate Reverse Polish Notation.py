def evalRPN(tokens):
    """
    :type tokens: List[str]
    :rtype: int
    """
    stash = []
    operators = ["+","-","*","/"]
    for i in tokens:
        if i not in operators:
            stash.append(float(i))
        else:
            num2 = stash.pop()
            num1 = stash.pop()
            if i == "+":
                stash.append(int(num1 + num2))
            elif i == "*":
                stash.append(int(num1 * num2))
            elif i == "-":
                stash.append(int(num1 - num2))
            else:
                stash.append(int(num1 / num2))
    return int(stash[0])



tokens = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]
print(evalRPN(tokens))