import ply.lex as lex
import ply.yacc as yacc

tokens = [
    'ID', 'NUMBER', 'REAL', 'PLUS', 'MINUS', 'TIMES', 'DIVIDE', 'LPAREN',
    'RPAREN', 'LBRACE', 'RBRACE', 'LBRACKET', 'RBRACKET', 'EQUALS',
    'SEMICOLON', 'LESS', 'LESSEQUAL', 'GREATER', 'GREATEREQUAL',
    'NOTEQUAL', 'EQUALITY', 'AND', 'OR', 'NOT', 'IF', 'ELSE', 'WHILE',
    'DO', 'BREAK', 'TRUE', 'FALSE', 'INT', 'FLOAT', 'COMMA'
]

t_PLUS       = r'\+'
t_MINUS      = r'-'
t_TIMES      = r'\*'
t_DIVIDE     = r'/'
t_LPAREN     = r'\('
t_RPAREN     = r'\)'
t_LBRACE     = r'\{'
t_RBRACE     = r'\}'
t_LBRACKET   = r'\['
t_RBRACKET   = r'\]'
t_EQUALS     = r'='
t_SEMICOLON  = r';'
t_COMMA      = r','
t_LESS       = r'<'
t_LESSEQUAL  = r'<='
t_GREATER    = r'>'
t_GREATEREQUAL = r'>='
t_NOTEQUAL     = r'!='
t_EQUALITY     = r'=='
t_AND          = r'&&'
t_OR           = r'\|\|'
t_NOT          = r'!'

reserved = {
    'if': 'IF', 'else': 'ELSE', 'while': 'WHILE', 'do': 'DO', 'break': 'BREAK',
    'true': 'TRUE', 'false': 'FALSE', 'int': 'INT', 'float': 'FLOAT'
}

def t_ID(t):
    r'[a-zA-Z_][a-zA-Z_0-9]*'
    t.type = reserved.get(t.value, 'ID')  # Check for reserved words
    return t

def t_REAL(t):
    r'\d+\.\d+'
    t.value = float(t.value)
    return t

def t_NUMBER(t):
    r'\d+'
    t.value = int(t.value)
    return t

def t_error(t):
    print(f"Illegal character '{t.value[0]}'")
    t.lexer.skip(1)

t_ignore = ' \t\n'

lexer = lex.lex()

errores_encontrados = False

def p_programa(p):
    'programa : bloque'
    if not errores_encontrados:
        print("Código analizado correctamente.")

def p_bloque(p):
    'bloque : LBRACE decls stmts RBRACE'

def p_decls_empty(p):
    'decls : '
    pass

def p_decls(p):
    'decls : decls decl'

def p_decl(p):
    'decl : tipo ID SEMICOLON'

def p_tipo(p):
    '''tipo : tipo LBRACKET NUMBER RBRACKET
            | basico'''

def p_basico(p):
    '''basico : INT
              | FLOAT'''

def p_stmts_empty(p):
    'stmts : '
    pass

def p_stmts(p):
    'stmts : stmts stmt'

def p_stmt(p):
    '''stmt : loc EQUALS bool SEMICOLON
            | IF LPAREN bool RPAREN stmt
            | IF LPAREN bool RPAREN stmt ELSE stmt
            | WHILE LPAREN bool RPAREN stmt
            | DO stmt WHILE LPAREN bool RPAREN SEMICOLON
            | BREAK SEMICOLON
            | bloque'''

def p_loc(p):
    '''loc : loc LBRACKET bool RBRACKET
           | ID'''

def p_bool(p):
    '''bool : bool OR comb
            | comb'''

def p_comb(p):
    '''comb : comb AND igualdad
            | igualdad'''

def p_igualdad(p):
    '''igualdad : igualdad EQUALITY rel
                | igualdad NOTEQUAL rel
                | rel'''

def p_rel(p):
    '''rel : expr LESS expr
           | expr LESSEQUAL expr
           | expr GREATEREQUAL expr
           | expr GREATER expr
           | expr'''

def p_expr(p):
    '''expr : expr PLUS term
            | expr MINUS term
            | term'''

def p_term(p):
    '''term : term TIMES unario
            | term DIVIDE unario
            | unario'''

def p_unario(p):
    '''unario : NOT unario
              | MINUS unario
              | factor'''

def p_factor(p):
    '''factor : LPAREN bool RPAREN
              | loc
              | NUMBER
              | REAL
              | TRUE
              | FALSE'''

def p_error(p):

    global errores_encontrados
    errores_encontrados = True

    if p:
        print(f"Error de sintaxis en '{p.value}', línea {p.lineno}")
    else:
        print("Error de sintaxis en EOF")

parser = yacc.yacc()
def leer_archivo(nombre_archivo):
    with open(nombre_archivo, 'r') as file:
        return file.read()

contenido_archivo = leer_archivo('input.txt')
# Probar el analizador sintáctico con una entrada
#data = '''{
 # int i; int j; float v; float x; float[100] a;
  #while( true ) {
  #do i = i+1; while( a[i] < v);
  #do j = j-1; while( a[j] > v);
  #if( i >= j ) break;
  #x = a[i]; a[i] = a[j]; a[j] = x;
  #}}
  #'''
parser.parse(contenido_archivo)
