import string

'''
[Regular Expression]
MERGED = Type | Integer | Char | String | Bool | Id | Keyword |
         Operator | SpecialSymbol | WhiteSpace

NZeroDigit = 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 
Digit =  0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 
Letter = a|b|c|d ...|x|y|z|A|B|C ...|X|Y|Z

AlphabetC = Letter | Digit | ! | " | # | $ | % | & | ~ | ( | ) | * | + | 
            , | - | . | / | : | ; | < | = | > | ? | @ | [ | } | ] | ^ | _ | ` |
            { | | | \\ | \' | \t | \n | \r
AlphabetS = Letter | Digit | ! | ~ | # | $ | % | & | ' | ( | ) | * | + | 
            , | - | . | / | : | ; | < | = | > | ? | @ | [ | } | ] | ^ | _ | ` |
            { | | | \\ | \" | \t | \n | \r

Arithmetic = + | - | * | /
Assign = =
Compare = < | > | == | != | <= | >=

Type = int | char | boolean | string
Integer = 0 | -NZeroDigit(Digit)* | NZeroDigit(Digit)*
Char = 'AlphabetC'
String = "(AlphabetS)*"
Bool = true | false
Id = (_|Letter)(Letter|Digit|_)*
KeyWord = if | else | while | class | return
Operator = Arithmetic | Assign | Compare
SpecialSymbol = ; | ( | ) | { | } | [ | ] | ,
WhiteSpace = [blank] | \t | \n  
'''


text = """
boolean d = 1;
int b = true;
char c = 'a'    
string my_word = "good choice";"""

# Define
Digit = [x for x in string.digits] # [0-9]
NZeroDigit = Digit[1:] # [1-9]
Letter = [x for x in string.ascii_letters] # [a-z,A-Z]
Alphabetc = [x for x in string.printable.replace('\'','')]
Alphabetc
test = "'"
test in Alphabetc
Type = [
    'int',
    'char',
    'boolean',
    'string'
]

Bool = [
    'true',
    'false'
]


Keyword =[
    'if',
    'else',
    'while',
    'class',
    'return'
]



# 몇번째 토큰에서 오류가 나는지 디버깅 용
token_number = 0
token_result = []
i = 0
text = text + '\0'


while True:
    ch = text[i]
    # White Spaces
    if(ch == '\0'):
        break
    if(ch == ' '):
        i += 1
        print("\nSPACE REMOVED")
    elif(ch == '\t'):
        i += 1
        print("\nTAB REMOVED")
    elif(ch == '\n'):
        i += 1
        print("\nNEW LINE REMOVED")
    # Special Symbols 
    elif(ch == ';'):
        i += 1
        token_result.append({'token' : 'SpecialSymbol' ,'lexeme' : ';'})
    elif(ch == '('):
        i += 1
        token_result.append({'token' : 'SpecialSymbol' ,'lexeme' : '('})
    elif(ch == ')'):
        i += 1
        token_result.append({'token' : 'SpecialSymbol' ,'lexeme' : ')'})
    elif(ch == '{'):
        i += 1
        token_result.append({'token' : 'SpecialSymbol' ,'lexeme' : '{'})
    elif(ch == '}'):
        i += 1
        token_result.append({'token' : 'SpecialSymbol' ,'lexeme' : '}'})
    elif(ch == '['):
        i += 1
        token_result.append({'token' : 'SpecialSymbol' ,'lexeme' : '['})
    elif(ch == ']'):
        i += 1
        token_result.append({'token' : 'SpecialSymbol' ,'lexeme' : ']'})
    elif(ch == ','):
        i += 1
        token_result.append({'token' : 'SpecialSymbol' ,'lexeme' : ','})
    # Operator
    elif(ch == '+'):
        i += 1
        token_result.append({'token' : 'ArithmeticOperator', 'lexeme' : '+'})
    elif(ch == '-'):
        # - operator는 정수형 Int와 구분해야 한다.
        # 마지막 토큰이 operator 혹은 '(' 인 경우 Int 형으로 판단
        last_token = token_result[-1]
        ch = ' '

        if(last_token['token'] in ['ArithmeticOperator','Compare','Assign'] or last_token['lexeme'] == ')'):
            number = '-'
            i += 1
            ch = text[i]
            if(ch in NZeroDigit):
                while(ch in Digit):
                    number = number + ch
                    i += 1
                    ch = text[i]
                token_result.append({'token' : 'Integer', 'lexeme' : number})
            else:
                raise Exception("wrong value after - : %".format(ch))
        else:
            i +=1
            token_result.append({'token' : 'ArithmeticOperator', 'lexeme' : '-'})
    elif(ch == '*'):
        i +=1
        token_result.append({'token' : 'ArithmeticOperator', 'lexeme' : '*'})
    elif(ch == '/'):
        i +=1
        token_result.append({'token' : 'ArithmeticOperator', 'lexeme' : '/'})
    elif(ch == '='):
        next = text[i+1]
        if(next == '='):
            i += 2
            token_result.append({'token' : 'Compare', 'lexeme' : '=='})
        else:
            i += 1
            token_result.append({'token' : 'Assign', 'lexeme' : '='})
    elif(ch == '<'):
        next = text[i+1]
        if(next == '='):
            i += 2
            token_result.append({'token' : 'Compare','lexeme' : '<='})
        else:
            i += 1
            token_result.append({'token' : 'Compare', 'lexeme' : '<'})
    elif(ch == '>'):
        next = text[i+1]
        if(next == '='):
            i += 2
            token_result.append({'token' : 'Compare', 'lexeme' : '>='})
        else:
            i += 1
            token_result.append({'token' : 'Compare', 'lexeme' : '>'})
    elif(ch == '!'):
        next = text[i+1]
        if(next == '='):
            i += 2
            token_result.append({'token' : 'Compare', 'lexeme' : '!='})
        else:
                raise Exception("wrong value after ! - {}".format(ch))
    # Char
    elif(ch == "'"):
        character = "'"
        i += 1
        ch = text[i]
        character = character + ch
        if(ch == "'"):
            raise Exception("Wrong value after ' - [blank is not permitted]")
        if(ch == "\\"):
            i += 1
            ch = text[i]
            if(ch in ['t','n','r',"'","\\"]):
                character = character + ch
            else:
                raise Exception("Wrong value '\\{} - only{t,n,r,',\\} is permitted after \\".format(ch))
        i += 1
        ch = text[i]
        if(ch == "'"):
            character = character + ch
            i += 1
            token_result.append({'token' : 'Char', 'lexeme' : character})
        else:
            raise Exception("Wrong value in single character {} - only 1 symbol is permitted".format(character))        
    # String
    elif(ch == '"'):
        String = '"'
        i += 1
        ch = text[i]
        while(ch != '"'):
            if(ch == '\\'):
                String = String + ch
                i += 1
                ch = text[i]
            String = String + ch
            i += 1
            ch = text[i]
            if(ch == '\0'):
                raise Exception("String is not Closed.")
        String = String + ch
        i += 1
        token_result.append({'token' : 'String', 'lexeme' : String})
    # Integer
    elif(ch in Digit):
        number = ''
        number = number + ch
        next = text[i+1]
        if(ch == '0'):
            if(next in Digit):
                raise Exception("Integer Start with 0 is not permitted - {}".format(number))
        else:
            while(next in Digit):
                number = number + next
                i += 1
                next = text[i+1]
        i += 1
        token_result.append({'token' : 'Integer', 'lexeme' : number})

    # Id    // Type, Bool, Keyword 체크
    elif(ch == '_' or ch in  Letter):
        Identifier = ''
        Identifier = Identifier + ch
        next = text[i+1]
        while(next in Letter or next in Digit or next =='_'):
            Identifier = Identifier + next
            i += 1
            next = text[i+1]
        i += 1
        if(Identifier in Type):
            token_result.append({'token' : 'Type','lexeme' : Identifier})
        elif(Identifier in Bool):
            token_result.append({'token' : 'Bool', 'lexeme' : Identifier})
        elif(Identifier in Keyword):
            Identifier = Identifier[0].upper() + Identifier[1:]
            token_result.append({'token' : Identifier,'lexeme' : ''})
        else:
            token_result.append({'token' : 'Id','lexeme' : Identifier})
    # 그 이외에 정의되지 않은 값이 들어오면 종료
    else:
        raise Exception("Invalid Input. Check character number {}".format(i))

print(token_result)