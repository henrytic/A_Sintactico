# Analizador Sintactico
Analizador sintáctico en python de un gramatica:

programa --> bloque
bloque --> {decls instr}
decls --> decls decl | ε
decl --> tipo id;
tipo --> tipo [ num ] | basico
instrs --> instrs stmt | ε
instr --> loc = bool ;
 | if ( bool ) instr
 | if ( bool ) instr else instr
 | while ( bool ) instr
 | do instr while ( bool ) ;
 | break ;
 | bloque
loc --> loc [ bool ] | id
bool --> bool || comb | comb
comb --> comb && igualdad | igualdad
igualdad --> igualdad == rel | igualdad != rel | rel
rel --> expr < expr | expr <= expr | expr >= expr | expr > expr | expr
expr --> expr + term | expr - term | term
term --> term * unario | term / unario | unario
unario --> ! unario | - unario | factor
factor --> ( bool ) | loc | num | real | true | false

#para este bloque de codigo
 { 
  int i; int j; float v; float x; float[100] a;
  while( true ) {
  do i = i+1; while( a[i] < v);
  do j = j−1; while( a[j] > v);
  if( i >= j ) break;
  x = a[i]; a[i] = a[j]; a[j] = x;
  }
  }
