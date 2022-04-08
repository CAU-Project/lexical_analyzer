import argparse
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
Literal = "(AlphabetS)*"
Bool = true | false
Id = (_|Letter)(Letter|Digit|_)*
KeyWord = if | else | while | class | return
Operator = Arithmetic | Assign | Compare
SpecialSymbol = ; | ( | ) | { | } | [ | ] | ,
WhiteSpace = [blank] | \t | \n  
'''


# Define
Digit = [x for x in string.digits] # [0-9]
NZeroDigit = Digit[1:] # [1-9]
Letter = [x for x in string.ascii_letters] # [a-z,A-Z]
Alphabetc = [x for x in string.printable.replace('\'','')]

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



def lexical(text) -> list:
    text = text + '\0'
    i=0
    token_result = []
    line_num = 1

    while True:
        ch = text[i]
        # White Spaces
        if(ch == '\0'):
            break
        if(ch == ' '):
            i += 1
#            print("\nSPACE REMOVED")
        elif(ch == '\t'):
            i += 1
#            print("\nTAB REMOVED")
        elif(ch == '\n'):
            i += 1
            line_num +=1
#            print("\nNEW LINE REMOVED")
        # Special Symbols 
        elif(ch == ';'):
            i += 1
            token_result.append({'token' : 'SCOLON' ,'lexeme' : ''})
        elif(ch == '('):
            i += 1
            token_result.append({'token' : 'LPAREN' ,'lexeme' : ''})
        elif(ch == ')'):
            i += 1
            token_result.append({'token' : 'RPAREN' ,'lexeme' : ''})
        elif(ch == '{'):
            i += 1
            token_result.append({'token' : 'LBRACE' ,'lexeme' : ''})
        elif(ch == '}'):
            i += 1
            token_result.append({'token' : 'RBRACE' ,'lexeme' : ''})
        elif(ch == '['):
            i += 1
            token_result.append({'token' : 'LBRAKET' ,'lexeme' : ''})
        elif(ch == ']'):
            i += 1
            token_result.append({'token' : 'RBRAKET' ,'lexeme' : ''})
        elif(ch == ','):
            i += 1
            token_result.append({'token' : 'COMMA' ,'lexeme' : ''})
        # Operator
        elif(ch == '+'):
            i += 1
            token_result.append({'token' : 'ArithmeticOperator', 'lexeme' : '+'})
        elif(ch == '-'):
            # - operator는 정수형 Int와 구분해야 한다.
            # 마지막 토큰이 operator 혹은 '(' 인 경우 Int 형으로 판단
            last_token = token_result[-1]
            if(last_token['token'] in ['ArithmeticOperator','Compare','Assign'] or last_token['lexeme'] == '('):
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
                    raise Exception("Line[{}] wrong value after - : {}".format(line_num,ch))
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
                token_result.append({'token' : 'Assign', 'lexeme' : ''})
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
                    raise Exception("Line[{}] wrong value after ! - {}".format(line_num,next))
        # Char
        elif(ch == "'"):
            character = "'"
            i += 1
            ch = text[i]
            character = character + ch
            if(ch == "'"):
                raise Exception("Line[{}] Wrong value after ' - [blank is not permitted]".format(line_num))
            if(ch == "\\"):
                i += 1
                ch = text[i]
                if(ch in ['t','n','r',"'","\\"]):
                    character = character + ch
                else:
                    raise Exception("Line[{}] Wrong value '\\{} - only{t,n,r,',\\} is permitted after \\".format(line_num,ch))
            i += 1
            ch = text[i]
            if(ch == "'"):
                character = character + ch
                i += 1
                token_result.append({'token' : 'Char', 'lexeme' : character})
            else:
                raise Exception("Line[{}] Wrong value in single character {} - only 1 symbol is permitted".format(line_num,character))        
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
                    raise Exception("Line[{}] String is not Closed.".format(line_num))
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
                    raise Exception("Line[{}] Integer Start with 0 is not permitted - {}".format(line_num,number))
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
            raise Exception("Line[{}] Invalid Input. Check character {}".format(line_num,ch))
    return token_result

def main() -> None:
    print("lexical analyzer for tokenizing simple java code.\n")
    parser = argparse.ArgumentParser(description='Lexical Analyzer')
    parser.add_argument('input',
                    metavar='filename',
                    type=str,
                    help='Enter file name')

    args = parser.parse_args()
    filename = 'test_code/' + args.input

    text = []
    with open(filename,"r") as fr:
        text = fr.read()
    
    # 어휘 분석 결과 반환
    token_list = lexical(text)
    

    with open(args.input+'_output.txt',"w") as fw:
        
        for token in token_list:
            fw.write('%-20s |\t %s\n'%(token['token'],token['lexeme']))

#    print(token_list)

    

if __name__ == "__main__":
    main()