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

1. Make Test code in **test_code** Directory which satisfy our Lexical Specification
2. start lex.py with filename in test_code directory

```sh
python3 lex.py test.txt
```

- If an input program has an error, then error report with Line Number
- Otherwise it makes file with a symbol table which stores the information of tokens in **filename_output.txt**
- I have made some test code in test_code directory



