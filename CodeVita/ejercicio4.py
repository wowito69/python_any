def word_to_number(word):
    digits = {
        'zero': '0', 'one': '1', 'two': '2', 'three': '3', 'four': '4',
        'five': '5', 'six': '6', 'seven': '7', 'eight': '8', 'nine': '9'
    }
    return ''.join(digits.get(char, '') for char in word)

def evaluate_expression(expression):
    words = expression.split()
    numbers = []
    operators = []
    
    for word in words:
        if word in {'add', 'sub', 'mul', 'rem', 'pow'}:
            operators.append(word)
        else:
            number = word_to_number(word)
            if number.isdigit():
                numbers.append(int(number))
            else:
                return "expression evaluation stopped invalid words present"

    if len(operators) != len(numbers) - 1:
        return "expression is not complete or invalid"

    result = numbers[0]
    for i in range(len(operators)):
        if operators[i] == 'add':
            result += numbers[i + 1]
        elif operators[i] == 'sub':
            result -= numbers[i + 1]
        elif operators[i] == 'mul':
            result *= numbers[i + 1]
        elif operators[i] == 'rem':
            if numbers[i + 1] == 0:
                return "expression evaluation stopped division by zero"
            result %= numbers[i + 1]
        elif operators[i] == 'pow':
            result **= numbers[i + 1]

    return result

expression = input("Ingresa la expresión matemática: ").replace('c', 'zero')
output = evaluate_expression(expression)
print(output)
