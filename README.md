# lexical_analyzer
Lexical Analyzer for Simple Java code with Python

# Lexical Specification

![Compiler Project 1, 2022 (1)_1](https://user-images.githubusercontent.com/33647663/162481883-0bba339c-780f-4a6b-b76f-18494e84e3ae.png)

![Compiler Project 1, 2022 (1)_2](https://user-images.githubusercontent.com/33647663/162481877-cce4cfcf-1d23-416d-b5ab-9004277579bf.png)

# 1. Regular Expression

```
MERGED = Type | Integer | Char | String | Bool | Id | Keyword | Operator | SpecialSymbol | WhiteSpace

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
