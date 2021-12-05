#Create a program that check if password is valid
#The password is valid if all criteria are met:
#a. Greater than 15 letters
#b. Have at least one capital letter
#c. Have at least one number
#d. Have at least one special char (!@#$%^&*()_+ etc)
#ex. input: P@ssw0rd+P@ssw0rd, ouput: Valid

passw = input("Password : ")
lower = 0
capital_case = 0
number = 0
Special_char = 0

if len(passw)>=15:
    for p in passw:
        
        if (p == 'a'or p == 'b' or p == 'c' or p == 'd' or p == 'f' or p == 'g' or p == 'h' or p == 'j' or p == 'k' or p == 'l' or 
        p == 'm' or p == 'n' or p == 'p' or p == 'q' or p == 'r' or p == 's' or p == 't' or p == 'v' or p == 'w' or 
        p == 'x' or p == 'y' or p == 'z'):
            lower = lower +1

        if (p == 'A' or p == 'B' or p == 'C' or p == 'D' or p=='E' or p == 'F' or p == 'G' or p == 'H' or p =='I' or p == 'J' or p == 'K' or p == 'L' or 
        p == 'M' or p == 'N' or p =='O' or p == 'P' or p == 'Q' or p == 'R' or p == 'S' or p == 'T' or p=='U' or p == 'V' or p == 'W' or 
        p == 'X' or p == 'Y' or p == 'Z'):
            capital_case = capital_case +1
        
        if (p =='!' or p=='@' or p =='#' or p==' ' or p =='%' or p =='&' or p =='*' or p ==',' or p =='.'or p =='-'or p =='_'):
            Special_char = Special_char +1
        
        if (p =='0' or p=='1' or p=='2' or p=='3' or p=='4' or p=='5' or p=='6' or p=='7' or p=='8' or p=='9'):
            number = number +1

if (lower>=1 and capital_case >=1 and number>=1 and Special_char >=1 and lower+capital_case +number+Special_char==len(passw)):
    print(" \t Valid Password")
else: 
    print("\t Invalid Password")
