import ply.lex as lex
tokens = (
	'LANGLE', # <
	'LANGLESLASH', # </
	'RANGLE', # >
	'EQUAL', # =
	'STRING', # "hello"
	'WORD', # Welcome!
	)
t_ignore = ' '

states = (
	('htmlcomment', 'exclusive'),
)
def t_htmlcomment(token):
	r'<!--'
	token.lexer.begin('htmlcomment')
def t_htmlcomment_end(token):
	r'-->'
	token.lexer.lineno += token.value.count('\n')
	token.lexer.begin('INITIAL')
def t_htmlcomment_error(token):
	token.lexer.skip(1) # pass

def t_newline(token):
	r'\n'
	token.lexer.lineno += 1
	pass
def t_LANGLESLASH(token):
	r'</'
	return token
def t_LANGLE(token):
	r'<'
	return token
def t_RANGLE(token):
	r'>'
	return token
def t_EQUAL(token):
	r'='
	return token
def t_STRING(token):
	r'"[^"]+"'
	return token
def t_WORD(token):
	r'[^<> \n]+'
	return token

webpage = "Hello <!-- comment\nlala --> all"
htmllexer = lex.lex()
htmllexer.input(webpage)
while True:
	tok = htmllexer.token()
	if not tok: break
	print(tok)