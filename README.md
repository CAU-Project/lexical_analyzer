# lexical_analyzer
Lexical Analyzer for Simple Java code with Python

# Lexical Specification

![Compiler Project 1, 2022 (1)_1](https://user-images.githubusercontent.com/33647663/162481883-0bba339c-780f-4a6b-b76f-18494e84e3ae.png)

![Compiler Project 1, 2022 (1)_2](https://user-images.githubusercontent.com/33647663/162481877-cce4cfcf-1d23-416d-b5ab-9004277579bf.png)

# 1. Regular Expression

```re
MERGED = Type | Integer | Char | Literal | Bool | Id | Keyword | Operator | SpecialSymbol | WhiteSpace

NZeroDigit = 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 
Digit =  0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 
Letter = a | b | c ... | y | z | A | B ... | Y | Z

Alphabet = Letter | Digit | ! | ' | " | # | $ | % | & | ~ | ( | ) | * | + | , | - | . | / | : | ; | < | = | > | ? | @ | [ | } | ] | ^ | _ | ` | { | | | \t | \n | \r


Arithmetic = + | - | * | /
Assign = =
Compare = < | > | == | != | <= | >=

Type = int | char | boolean | string
Integer = 0 | -NZeroDigit(Digit)* | NZeroDigit(Digit)*
Char = 'Alphabet'
Literal = "(Alphabet)*"
Bool = true | false
Id = (_|Letter)(Letter|Digit|_)*
KeyWord = if | else | while | class | return
Operator = Arithmetic | Assign | Compare
SpecialSymbol = ; | ( | ) | { | } | [ | ] | ,
WhiteSpace = [blank] | \t | \n  
```

# 2. NFA
Draw NFA With Regular Expression

![NFA](https://user-images.githubusercontent.com/33647663/162559648-feedacb0-a2de-4776-9fca-70799ec5a5ec.png)

# 3. DFA & Table
Translate the NFA to DFA in form of Table


# Usage

### Requirements:
- No requirements about python module
- My Python : Python 3.5.3

### Usage:
1. Make Test code in **test_code** Directory which satisfy our Lexical Specification
2. start lex.py with filename in test_code directory
- I have made some test code in test_code directory
```sh
$python3 lex.py test.txt
```

- If an input program has an error, then error report with Line Number
```sh
$python3 lex.py error1.txt
[!] lexical analyzer for tokenizing simple java code.

Line[2] wrong value after ! - f
```
- Otherwise it makes file with a symbol table which stores the information of tokens in **filename_output.txt**

```sh
$python3 lex.py test.txt
[!] lexical analyzer for tokenizing simple java code.

[+] Finish Lexical analyzr
[+] Result Information in test.txt_output.txt
```

# Result Information Table

```
Type                 |	 int
Id                   |	 a
Assign               |	 
Integer              |	 0
ArithmeticOperator   |	 +
Integer              |	 1
SCOLON               |	 
Type                 |	 char
Id                   |	 b
Assign               |	 
Integer              |	 1
ArithmeticOperator   |	 /
Integer              |	 2
SCOLON               |	 
Type                 |	 boolean
Id                   |	 c
Assign               |	 
Integer              |	 22
ArithmeticOperator   |	 *
Integer              |	 3
SCOLON               |	 
Type                 |	 string
Id                   |	 e
Assign               |	 
Integer              |	 -5
ArithmeticOperator   |	 -
Integer              |	 -3
SCOLON               |	 
If                   |	 
LPAREN               |	 
Bool                 |	 true
RPAREN               |	 
LBRACE               |	 
Id                   |	 f
Assign               |	 
Integer              |	 7
ArithmeticOperator   |	 -
Integer              |	 -8
SCOLON               |	 
Return               |	 
SCOLON               |	 
RBRACE               |	 
Else                 |	 
LBRACE               |	 
While                |	 
LPAREN               |	 
Id                   |	 a
Compare              |	 >
Integer              |	 -5
RPAREN               |	 
LBRACE               |	 
RBRACE               |	 
RBRACE               |	 
Type                 |	 int
Id                   |	 k
Assign               |	 
Integer              |	 7
ArithmeticOperator   |	 -
Integer              |	 -8
LPAREN               |	 
Integer              |	 9
RPAREN               |	 
ArithmeticOperator   |	 -
LPAREN               |	 
ArithmeticOperator   |	 -
Integer              |	 5
RPAREN               |	 
Char                 |	 'a'
Char                 |	 '\''
Char                 |	 '\n'
Char                 |	 ' '
Char                 |	 '&'
String               |	 "#@(d2sm^,z."
Type                 |	 int
Id                   |	 test
Assign               |	 
Integer              |	 3
ArithmeticOperator   |	 -
Integer              |	 5
SCOLON               |	 
Type                 |	 int
Id                   |	 test2
Assign               |	 
Integer              |	 3
ArithmeticOperator   |	 -
Integer              |	 -5
SCOLON               |	 

```



