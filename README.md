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

![NFA drawio](https://user-images.githubusercontent.com/33647663/162576571-467b6261-00bd-41ba-a764-cc08bdaf675a.png)


# 3. DFA & Table
Translate the NFA to DFA in form of Table



## Transition Table

Token|lexeme|state|+|-|*|/|=|<|>|!|(|)|{|}|[|]|;|,|\t|\n|blank|'|"|_|0|NZeroDigit|Letter|Alphabet|$
--|--|--|--|--|--|--|--|--|--|--|--|--|--|--|--|--|--|--|--|--|--|--|--|--|--|--|--|--|--
|||0|1|2|3|4|5|6|7|8|9|10|11|12|13|14|15|16|17|18|19|20|21|22|23|24|25|37|-
Arithmetic operator|+|1|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-
Arithmetic operator|-|2|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|26|-|-|-
Arithmetic operator|*|3|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-
Arithmetic operator|/|4|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-
Assign|=|5|-|-|-|-|27|28|29|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-
Compare Operator|<|6|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-
Compare Operator|>|7|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-
!ERR|!|8|-|-|-|-|30|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-
LPAREN|(|9|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-
RPAREN|)|10|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-
LBRACE|{|11|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-
RBRACE|}|12|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-
LBRAKET|[|13|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-
RBRAKET|]|14|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-
SCOLON|;|15|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-
COMMA|,|16|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-
WHITESPACE|\t|17|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-
WHITESPACE|\n|18|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-
WHITESPACE|blank|19|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-
!ERR|'|20|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|35|-|-|-|-|-|31|-
!ERR|"|21|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|33|-
ID|_(_|digit|letter)*|22|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|22|22|22|22|-|-
INT|0|23|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|36|36|-|-|-
INT|[1-9][0-9]*|24|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|24|24|-|-|-
ID|letter(_|digit|letter)*|25|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|25|25|25|25|-|-
INT|-[1-9][0-9]*|26|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|26|26|-|-|-
Compare Operator|==|27|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-
Compare Operator|=<|28|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-
Compare Operator|=>|29|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-
Compare Operator|!=|30|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-
!ERR|'alphabet|31|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|32|-|-|-|-|-|-|-
CHAR|'alphabet'|32|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-
!ERR|"(alphabet)+|33|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|34|-|-|-|-|33|-
STRING|"(alphabet)+"|34|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-
!ERR|''|35|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-
!ERR|00,001,0123123 ….|36|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|36|36|-|-|-
!ERR|alphabet|37|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-

 

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

### test.txt
```java
int a = 0 + 1;
char b = 1 / 2 ;
boolean c =22 * 3;
string e = -5 - -3;
if(true){
    f = 7 - -8;
    return;
}else{
    while(a > -5){


    }
}

int k = 7 - -8
(9) - (-5)

'a'
'\''
'\n'
' '
'&'



"#@(d2sm^,z."

int test = 3 - 5;
int test2 = 3 - -5;

```

### Result Information Table

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



