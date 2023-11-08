import re

# Step 2: Create a Lexer
def lexer(input_text):
    tokens = re.findall(r'\d+|\+|-|\*|/|\(|\)', input_text)
    return tokens

# Step 3: Implement a Parser
def parse_expression(tokens):
    if not tokens:
        return None

    def parse_term():
        term = parse_factor()
        while tokens and tokens[0] in ('*', '/'):
            operator = tokens.pop(0)
            right = parse_factor()
            term = (operator, term, right)
        return term

    def parse_factor():
        if tokens[0] == '(':
            tokens.pop(0)  # Consume the opening parenthesis
            expression = parse_expression(tokens)
            if tokens.pop(0) != ')':
                raise SyntaxError("Expected closing parenthesis")
            return expression
        else:
            return int(tokens.pop(0))

    expression = parse_term()
    while tokens and tokens[0] in ('+', '-'):
        operator = tokens.pop(0)
        right = parse_term()
        expression = (operator, expression, right)
    return expression

# Step 5: Evaluate the AST
def evaluate(ast):
    if isinstance(ast, int):
        return ast
    operator, left, right = ast
    if operator == '+':
        return evaluate(left) + evaluate(right)
    elif operator == '-':
        return evaluate(left) - evaluate(right)
    elif operator == '*':
        return evaluate(left) * evaluate(right)
    elif operator == '/':
        return evaluate(left) / evaluate(right)
    else:
        raise ValueError(f"Invalid operator: {operator}")

# Main function
def main():
    input_text = input("Enter an arithmetic expression: ")
    tokens = lexer(input_text)
    ast = parse_expression(tokens)
    result = evaluate(ast)
    print(f"Result: {result}")

if __name__ == "__main__":
    main()
