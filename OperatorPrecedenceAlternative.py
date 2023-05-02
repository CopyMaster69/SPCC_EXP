class OperatorPrecedenceParser:
    def __init__(self):
        self.operators = {'+': 0, '-': 0, '*': 1, '/': 1, '^': 2}
        self.stack = []
        self.output = []

    def parse(self, expr):
        tokens = expr.split()
        for token in tokens:
            if token.isdigit():
                self.output.append(token)
            elif token in self.operators:
                while self.stack and self.stack[-1] in self.operators and self.operators[self.stack[-1]] >= self.operators[token]:
                    self.output.append(self.stack.pop())
                self.stack.append(token)
            elif token == '(':
                self.stack.append(token)
            elif token == ')':
                while self.stack and self.stack[-1] != '(':
                    self.output.append(self.stack.pop())
                if self.stack and self.stack[-1] == '(':
                    self.stack.pop()
                else:
                    raise Exception("Invalid expression")
            else:
                raise Exception("Invalid expression")

        while self.stack:
            if self.stack[-1] in self.operators:
                self.output.append(self.stack.pop())
            else:
                raise Exception("Invalid expression")

        return ' '.join(self.output)


if __name__ == '__main__':
    parser = OperatorPrecedenceParser()
    expr = input("Enter an infix expression: ")
    try:
        postfix = parser.parse(expr)
        print("Postfix notation:", postfix)
    except Exception as e:
        print("Error:", str(e))
