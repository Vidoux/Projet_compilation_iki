```Ohm
Iki {
  Program     =  Block
  Block       =  (Stmt ";")+
  Stmt        =  var id ":" Type             -- declaration
              |  VarExp "=" Exp              -- assignment
              |  read VarExp ("," VarExp)*   -- read
              |  write Exp ("," Exp)*        -- write
              |  while Exp loop Block endw   -- while
  Type        =  int | bool
  Exp         =  Exp or Exp1                 -- binary
              |  Exp1
  Exp1        =  Exp1 and Exp2               -- binary
              |  Exp2
  Exp2        =  Exp3 relop Exp3             -- binary
              |  Exp3
  Exp3        =  Exp3 addop Exp4             -- binary
              |  Exp4
  Exp4        =  Exp4 mulop Exp5             -- binary
              |  Exp5
  Exp5        =  prefixop Exp6               -- unary
              |  Exp6
  Exp6        =  boollit
              |  intlit
              |  VarExp
              |  "(" Exp ")"                 -- parens
  VarExp      =  id

  var         =  "var" ~idrest
  read        =  "read" ~idrest
  write       =  "write" ~idrest
  while       =  "while" ~idrest
  loop        =  "loop" ~idrest
  endw        =  "end" ~idrest
  int         =  "int" ~idrest
  bool        =  "bool" ~idrest
  true        =  "true" ~idrest
  false       =  "false" ~idrest
  or          =  "or" ~idrest
  and         =  "and" ~idrest
  not         =  "not" ~idrest

  keyword     =  var | int | bool
              |  read | write | while | loop | endw
              |  true | false | or | and | not
  id          =  ~keyword letter idrest*
  idrest      =  "_" | alnum
  intlit      =  digit+
  boollit     =  true | false
  addop       =  "+" | "-"
  relop       =  "<=" | "<" | "==" | "!=" | ">=" | ">"
  mulop       =  "*" | "/" | "%"
  prefixop    =  ~"--" "-" | not

  space      +=  comment
  comment     =  "--" (~"\n" any)* "\n"
}
```