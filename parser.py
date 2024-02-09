from lark import Lark

grammar = '''
start       : program

program     : line+

line        : INT? _statement _NEWLINE

_statement  : print_statement
            | if_statement
            | goto_statement
            | input_statement
            | let_statement
            | gosub_statement
            | return_statement
            | clear_statement
            | list_statement
            | run_statement
            | end_statement

print_statement   : "PRINT" exprlist
if_statement      : "IF" expression relop expression "THEN" _statement
goto_statement    : "GOTO" expression
input_statement   : "INPUT" string "," varlist
let_statement     : "LET" var "=" expression
gosub_statement   : "GOSUB" expression
return_statement  : "RETURN"
clear_statement   : "CLEAR"
list_statement    : "LIST"
run_statement     : "RUN"
end_statement     : "END"

string      : ESCAPED_STRING

?exprlist    : (string | expression) ("," (string | expression))*

?expression  : (PLUS | MINUS)? term ((PLUS | MINUS) term)*

?term        : factor ((TIMES | DIV) factor)*

?factor      : var
            | INT
            | expression

var         : UCASE_LETTER

?varlist     : var ("," var)*

op          : PLUS
            | MINUS
            | TIMES
            | DIV

PLUS        : "+"
MINUS       : "-"
TIMES       : "*"
DIV         : "/"

relop       : EQ
            | GT
            | LT
            | GEQ
            | LEQ
            | NEQ

EQ          : "="
GT          : ">"
LT          : "<"
GEQ         : ">="
LEQ         : "<="
NEQ         : "<>"

%import common.ESCAPED_STRING
%import common.INT
%import common.UCASE_LETTER
%import common.WS_INLINE
%import common.NEWLINE          -> _NEWLINE

%ignore WS_INLINE
'''

example_program = '''
50 INPUT "GUESS A NUMBER?", G
60 LET C = C+1
70 IF G=N THEN GOTO 110
80 IF G>N THEN PRINT "LOWER"
90 IF G<N THEN PRINT "HIGHER"
100 GOTO 50
110 PRINT "YOU GUESSED IT IN", C, " TRIES!"
'''.lstrip()

compiled = Lark(grammar, ambiguity='explicit')
parser = compiled.parser

