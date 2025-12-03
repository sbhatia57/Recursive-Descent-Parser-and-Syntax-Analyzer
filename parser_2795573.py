import sys

#global variables
symbol_table = {}
charClass = 0
lexeme = [''] * 100
nextChar = ''
lexLen = 0
token = 0
nextToken = 0
file = open(sys.argv[1], 'r')
curr_pos = 0


#Character Classes
LETTER = 0
DIGIT = 1
UNKNOWN = 99
LET = 2
INT_CLASS = 3
REAL_CLASS = 4
FLOAT_CLASS = 5
IN_CLASS = 6
END_CLASS = 7
IF_CLASS = 8
GREATER_THAN_EQUAL_CLASS = 9
LESS_THAN_EQUAL_CLASS = 40
EQUAL_TO_CLASS = 41
NOT_EQUAL_TO_CLASS = 42
THEN_CLASS = 43
ELSE_CLASS = 44

# Token codes
INT_LIT = 10
IDENT = 11
ASSIGN_OP = 20
ADD_OP = 21
SUB_OP = 22
MUL_OP = 23
DIV_OP = 24
LEFT_PAREN = 25
RIGHT_PAREN = 26
EOF = -1
LET_TOKEN = 12
COLON = 13
INT_TOKEN = 14
SEMICOLON = 15
REAL_TOKEN = 16
FLOAT_LIT = 17
DOT_TOKEN = 18
IN_TOKEN = 19
END_TOKEN = 27
IF_TOKEN = 28
GREATER_THAN_OP = 29
LESS_THAN_OP = 30
GREATER_THAN_EQUAL_OP = 31
LESS_THAN_EQUAL_OP = 32
EQUAL_TO_OP = 33
NOT_EQUAL_TO_OP = 34
THEN_TOKEN = 35
ELSE_TOKEN = 36


def addChar():
    global lexLen, lexeme, nextChar
    if lexLen <= 98:
        lexeme[lexLen] = nextChar
        lexLen += 1
        lexeme[lexLen] = '!'
    else:
        print("Error - lexeme is too long! \n")

def addMultipleChar(str, num):
    global lexLen, lexeme, nextChar
    for i in range(num):
        if lexLen <= 98:
            lexeme[lexLen] = str[i]
            lexLen += 1
            lexeme[lexLen] = '!'
        else:
            print("Error - lexeme is too long! \n")
            break

def getChar():
    global charClass, nextChar, file, curr_pos
    curr_pos = file.tell()
    nextChar = file.read(1)
    curr_pos += 1
    tmp_str_let = nextChar + file.read(2)
    file.seek(curr_pos)
    tmp_str_int = nextChar + file.read(2)
    file.seek(curr_pos)
    tmp_str_real = nextChar + file.read(3)
    file.seek(curr_pos)
    tmp_str_in = nextChar + file.read(1)
    file.seek(curr_pos)
    tmp_str_end = nextChar + file.read(2)
    file.seek(curr_pos)
    tmp_str_if = nextChar + file.read(1)
    file.seek(curr_pos)
    tmp_str_less_than_equal = nextChar + file.read(1)
    file.seek(curr_pos)
    tmp_str_greater_than_equal = nextChar + file.read(1)
    file.seek(curr_pos)
    tmp_str_equal_to = nextChar + file.read(1)
    file.seek(curr_pos)
    tmp_str_not_equal = nextChar + file.read(1)
    file.seek(curr_pos)
    tmp_str_then = nextChar + file.read(3)
    file.seek(curr_pos)
    tmp_str_else = nextChar + file.read(3)
    file.seek(curr_pos)
    if nextChar != '':
        if nextChar == 'r' and tmp_str_real == "real":
            curr_pos += 3
            charClass = REAL_CLASS
            file.seek(curr_pos)
        elif nextChar == 't' and tmp_str_then == "then":
            curr_pos += 3
            charClass = THEN_CLASS
            file.seek(curr_pos)
        elif nextChar == 'e' and tmp_str_else == "else":
            curr_pos += 3
            charClass = ELSE_CLASS
            file.seek(curr_pos)
        elif nextChar == 'e' and tmp_str_end == "end":
            curr_pos += 2
            charClass = END_CLASS
            file.seek(curr_pos)
        elif nextChar == 'l' and tmp_str_let == "let":
            curr_pos += 2
            charClass = LET
            file.seek(curr_pos)
        elif nextChar == 'i' and tmp_str_int == "int":
            curr_pos += 2
            charClass = INT_CLASS
            file.seek(curr_pos)
        elif nextChar == 'i' and tmp_str_in == "in":
            curr_pos += 1
            charClass = IN_CLASS
            file.seek(curr_pos)
        elif nextChar == 'i' and tmp_str_if == "if":
            curr_pos += 1
            charClass = IF_CLASS
            file.seek(curr_pos)
        elif nextChar == '=' and tmp_str_equal_to == "==":
            curr_pos += 1
            charClass = EQUAL_TO_CLASS
            file.seek(curr_pos)
        elif nextChar == '>' and tmp_str_greater_than_equal == ">=":
            curr_pos += 1
            charClass = GREATER_THAN_EQUAL_CLASS
            file.seek(curr_pos)
        elif nextChar == '<' and tmp_str_less_than_equal == "<=":
            curr_pos += 1
            charClass = LESS_THAN_EQUAL_CLASS
            file.seek(curr_pos)
        elif nextChar == '<' and tmp_str_not_equal == "<>":
            curr_pos += 1
            charClass = NOT_EQUAL_TO_CLASS
            file.seek(curr_pos)
        elif nextChar.isalpha():
            charClass = LETTER
        elif nextChar.isdigit():
            charClass = DIGIT
        elif nextChar == '.':
            charClass = FLOAT_CLASS
        else:
            charClass = UNKNOWN
    else:
        charClass = EOF

def getNonBlank():
    while nextChar.isspace():
        getChar()

def lex():
    global lexLen, lexeme, nextChar, nextToken
    lexLen = 0
    getNonBlank()

    if charClass == LET:
        addMultipleChar("let", 3)
        getChar()
        nextToken = LET_TOKEN
    elif charClass == END_CLASS:
        addMultipleChar("end", 3)
        getChar()
        nextToken = END_TOKEN
    elif charClass == IN_CLASS:
        addMultipleChar("in", 2)
        getChar()
        nextToken = IN_TOKEN
    elif charClass == IF_CLASS:
        addMultipleChar("if", 2)
        getChar()
        nextToken = IF_TOKEN
    elif charClass == REAL_CLASS:
        addMultipleChar("real", 4)
        getChar()
        nextToken = REAL_TOKEN
    elif charClass == THEN_CLASS:
        addMultipleChar("then", 4)
        getChar()
        nextToken = THEN_TOKEN
    elif charClass == ELSE_CLASS:
        addMultipleChar("else", 4)
        getChar()
        nextToken = ELSE_TOKEN
    elif charClass == INT_CLASS:
        addMultipleChar("int", 3)
        getChar()
        nextToken = INT_TOKEN
    elif charClass == LESS_THAN_EQUAL_CLASS:
        addMultipleChar("<=", 2)
        getChar()
        nextToken = LESS_THAN_EQUAL_OP
    elif charClass == GREATER_THAN_EQUAL_CLASS:
        addMultipleChar(">=", 2)
        getChar()
        nextToken = GREATER_THAN_EQUAL_OP
    elif charClass == EQUAL_TO_CLASS:
        addMultipleChar("==", 2)
        getChar()
        nextToken = EQUAL_TO_OP
    elif charClass == NOT_EQUAL_TO_CLASS:
        addMultipleChar("<>", 2)
        getChar()
        nextToken = NOT_EQUAL_TO_OP
    elif charClass == LETTER:
        addChar()
        getChar()
        while (charClass == LETTER or charClass == DIGIT):
            addChar()
            getChar()
        nextToken = IDENT
    elif charClass == DIGIT:
        addChar()
        getChar()
        while (charClass == DIGIT):
            addChar()
            getChar()
        if (charClass == FLOAT_CLASS):
            addChar()
            getChar()
            while (charClass == DIGIT):
                addChar()
                getChar()
            nextToken = FLOAT_LIT
        else:
            while (charClass == DIGIT):
                addChar()
                getChar()
            nextToken = INT_LIT

    elif charClass == UNKNOWN:
        lookup(nextChar)
        getChar()
    elif charClass == EOF:
        nextToken = EOF
        lexeme[0] = 'E'
        lexeme[1] = 'O'
        lexeme[2] = 'F'
        lexeme[3] = 0

    #print("Next token is {}, Next lexeme is {}".format(nextToken, lexeme))

    return nextToken

def lookup(ch):
    global nextToken
    if ch == '(':
        addChar()
        nextToken = LEFT_PAREN
    elif ch == ')':
        addChar()
        nextToken = RIGHT_PAREN
    elif ch == '+':
        addChar()
        nextToken = ADD_OP
    elif ch == '-':
        addChar()
        nextToken = SUB_OP
    elif ch == '*':
        addChar()
        nextToken = MUL_OP
    elif ch == '/':
        addChar()
        nextToken = DIV_OP
    elif ch == ':':
        addChar()
        nextToken = COLON
    elif ch == ';':
        addChar()
        nextToken = SEMICOLON
    elif ch == '=':
        addChar()
        nextToken = ASSIGN_OP
    elif ch == '>':
        addChar()
        nextToken = GREATER_THAN_OP
    elif ch == '<':
        addChar()
        nextToken = LESS_THAN_OP
    else:
        addChar()
        nextToken = EOF

    return nextToken

def parse():
    getChar()
    lex()
    prog()
    if nextToken != EOF:
        error("Unexpected input after end of program")

def error(msg):
    print(f"Syntax error: {msg}")
    sys.exit(1)


def match(expected_token):
    global nextToken
    if nextToken == expected_token:
        lex()
    else:
        error(f"Expected token {expected_token}, got {nextToken}")

def get_identifier_value():
    name = ''
    for ch in lexeme:
        if ch == '!':
            break
        name += ch
    if name not in symbol_table:
        error(f"Undefined variable {name}")
    return symbol_table[name]

def get_literal_value():
    value_str = ''
    for ch in lexeme:
        if ch == '!':
            break
        value_str += ch
    if '.' in value_str:
        return float(value_str)
    else:
        return int(value_str)

def prog():
    result = let_in_end()
    print("Result: {}".format(result))
    while nextToken == LET_TOKEN:
        result = let_in_end()
        print("Result: {}".format(result))
    return result

def let_in_end():
    match(LET_TOKEN)
    decl_list()
    match(IN_TOKEN)
    type_rule()
    match(LEFT_PAREN)
    val = expr()
    match(RIGHT_PAREN)
    match(END_TOKEN)
    match(SEMICOLON)
    return val
def decl_list():
    decl()
    while nextToken == IDENT:
        decl()

def decl():
    global symbol_table
    id_name = ''.join(lexeme[:lexeme.index('!')])
    match(IDENT)
    match(COLON)
    type_rule()
    match(ASSIGN_OP)
    val = expr()
    symbol_table[id_name] = val
    match(SEMICOLON)

def type_rule():
    if nextToken == INT_TOKEN:
        match(INT_TOKEN)
    elif nextToken == REAL_TOKEN:
        match(REAL_TOKEN)
    else:
        error("Expected type 'int' or 'real'")


def expr():
    if nextToken == IF_TOKEN:
        match(IF_TOKEN)
        condition = cond()
        match(THEN_TOKEN)
        then_val = expr()
        match(ELSE_TOKEN)
        else_val = expr()
        return then_val if condition else else_val
    else:
        val = term()
        while nextToken in (ADD_OP, SUB_OP):
            op = nextToken
            lex()
            rhs = term()
            if op == ADD_OP:
                val += rhs
            else:
                val -= rhs
        return val

def term():
    val = factor()
    while nextToken in (MUL_OP, DIV_OP):
        op = nextToken
        lex()
        rhs = factor()
        if op == MUL_OP:
            val *= rhs
        else:
            val /= rhs
    return val

def factor():
    global nextToken
    if nextToken == LEFT_PAREN:
        match(LEFT_PAREN)
        val = expr()
        match(RIGHT_PAREN)
        return val
    elif nextToken == IDENT:
        val = get_identifier_value()
        match(IDENT)
        return val
    elif nextToken in (INT_LIT, FLOAT_LIT):
        val = get_literal_value()
        lex()
        return val
    elif nextToken in (INT_TOKEN, REAL_TOKEN):
        type_rule()  # match INT_TOKEN / REAL_TOKEN
        match(LEFT_PAREN)  # match '('
        val = expr()  # evaluate expression inside parentheses
        match(RIGHT_PAREN)  # match ')'
        return val
    else:
        error("Unexpected token in <factor>")

def cond():
    lhs = oprnd()
    if nextToken in (LESS_THAN_OP, LESS_THAN_EQUAL_OP, GREATER_THAN_OP, GREATER_THAN_EQUAL_OP, EQUAL_TO_OP, NOT_EQUAL_TO_OP):
        op = nextToken
        lex()
        rhs = oprnd()
        if op == LESS_THAN_OP:
            return lhs < rhs
        elif op == LESS_THAN_EQUAL_OP:
            return lhs <= rhs
        elif op == GREATER_THAN_OP:
            return  lhs > rhs
        elif op == GREATER_THAN_EQUAL_OP:
            return lhs >= rhs
        elif op == EQUAL_TO_OP:
            return lhs == rhs
        elif op == NOT_EQUAL_TO_OP:
            return lhs != rhs
        else:
            error("Expected comparison operator in <cond>")
    else:
        error("Expected comparison operator in <cond>")

def oprnd():
    if nextToken == IDENT:
        val = get_identifier_value()
        match(IDENT)
        return val
    elif nextToken == INT_LIT:
        val = get_literal_value()
        lex()
        return val
    else:
        error("Expected identifier or integer literal in <oprnd>")
def main():
    parse()
    print("Parsing complete")

if __name__ == '__main__':
    main()