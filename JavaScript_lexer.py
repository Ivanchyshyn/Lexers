# JavaScript: Comments & Keywords

import ply.lex as lex
  
tokens = (
        'ANDAND',       # &&
        'COMMA',        # ,
        'DIVIDE',       # /
        'ELSE',         # else
        'EQUAL',        # =
        'EQUALEQUAL',   # ==
        'FALSE',        # false
        'FUNCTION',     # function
        'GE',           # >=
        'GT',           # >
        'IDENTIFIER',   
        'NUMBER',       
        'STRING', 
        'IF',           # if
        'LBRACE',       # {
        'LE',           # <=
        'LPAREN',       # (
        'LT',           # <
        'MINUS',        # -
        'NOT',          # !
        'OROR',         # ||
        'PLUS',         # +
        'RBRACE',       # }
        'RETURN',       # return
        'RPAREN',       # )
        'SEMICOLON',    # ;
        'TIMES',        # *
        'TRUE',         # true
        'VAR',          # var
)

t_ignore = ' \t\v\r' # whitespace
t_comments_ignore = ' '
states = (
    ('comments','exclusive'),
)

def t_endline(token):
    r'//[^\n]+'
    pass
def t_comments(token):
    r'/\*'
    token.lexer.begin('comments')
def t_comments_end(token):
    r'\*/'
    token.lexer.begin('INITIAL')
def t_comments_error(token):
    token.lexer.skip(1)

def t_ANDAND(token):
    r'&&'
    return token
def t_COMMA(token):
    r','
    return token
def t_DIVIDE(token):
    r'/'
    return token
def t_ELSE(token):
    r'else'
    return token
def t_GE(token):
    r'>='
    return token
def t_GT(token):
    r'>'
    return token
def t_LE(token):
    r'<='
    return token
def t_LT(token):
    r'<'
    return token
def t_EQUALEQUAL(token):
    r'=='
    return token
def t_EQUAL(token):
    r'='
    return token
def t_FALSE(token):
    r'false'
    return token
def t_FUNCTION(token):
    r'function'
    return token
def t_IF(token):
    r'if'
    return token
def t_LBRACE(token):
    r'\{'
    return token
def t_LPAREN(token):
    r'\('
    return token
def t_NOT(token):
    r'!'
    return token
def t_OROR(token):
    r'\|\|'
    return token
def t_PLUS(token):
    r'\+'
    return token
def t_RBRACE(token):
    r'\}'
    return token
def t_RETURN(token):
    r'return'
    return token
def t_RPAREN(token):
    r'\)'
    return token
def t_SEMICOLON(token):
    r';'
    return token
def t_TIMES(token):
    r'\*'
    return token
def t_TRUE(token):
    r'true'
    return token
def t_VAR(token):
    r'var'
    return token

def t_NUMBER(token):
    r'-?\d+(?:\.\d*)?'
    token.value = float(token.value)
    return token

def t_STRING(token):
    r'"(?:[^"\\]|(?:\\"))*"'
    token.value = token.value[1:-1]
    return token

def t_IDENTIFIER(token):
    r'[a-zA-Z][a-zA-Z_]*'
    return token
 
def t_MINUS(token):
    r'-'
    return token

def t_newline(t):
        r'\n'
        t.lexer.lineno += 1

def t_error(t):
        print("JavaScript Lexer: Illegal character " + t.value[0])
        t.lexer.skip(1)

# Test cases

lexer = lex.lex() 
def test_lexer_specials(input_string):
  lexer.input(input_string)
  result = [ ] 
  while True:
    tok = lexer.token()
    if not tok: break
    result = result + [tok.type]
  return result

def test_lexer(input_string):
  lexer.input(input_string)
  result = [ ] 
  while True:
    tok = lexer.token()
    if not tok: break
    result = result + [tok.type, tok.value]
  return result

input1 = """ - !  && () * , / ; { || } + < <= = == > >= else false function
if return true var """

output1 = ['MINUS', 'NOT', 'ANDAND', 'LPAREN', 'RPAREN', 'TIMES', 'COMMA',
'DIVIDE', 'SEMICOLON', 'LBRACE', 'OROR', 'RBRACE', 'PLUS', 'LT', 'LE',
'EQUAL', 'EQUALEQUAL', 'GT', 'GE', 'ELSE', 'FALSE', 'FUNCTION', 'IF',
'RETURN', 'TRUE', 'VAR']

print(test_lexer_specials(input1) == output1)

input2 = """
if // else mystery  
=/*=*/= 
true /* false 
*/ return"""

output2 = ['IF', 'EQUAL', 'EQUAL', 'TRUE', 'RETURN']

print(test_lexer_specials(input2) == output2)

input3 = 'some_identifier -12.34 "a \\"escape\\" b""a \\"escape\\" b"'
output3 = ['IDENTIFIER', 'some_identifier', 'NUMBER', -12.34, 'STRING', 
'a \\"escape\\" b']
print(test_lexer(input3))


input4 = '-12x34' 
output4 = ['NUMBER', -12.0, 'IDENTIFIER', 'x', 'NUMBER', 34.0]
print(test_lexer(input4) == output4)