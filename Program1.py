#Program 1:
#Create a program that ask for a sentence as input.
#Display the number of words, vowels and consonants in the input 
#input: Bahala kayo dyan, #output:, #words: 3, #vowels: 6, #consonants: 

#Create a program that ask for a sentence as input.
Given_sentence =input("Give a sentence you have in mind : \t ")
#Display the number of words, vowels and consonants in the input 
vowels=0
consonants=0
words = 1

for Gs in Given_sentence:
        if Gs == ' ' :
            words = words + 1

        if (Gs == 'a' or Gs == 'e' or Gs == 'i' or Gs == 'o' or Gs == 'u' or 
        Gs == 'A' or Gs == 'E' or Gs == 'I' or Gs == 'O' or Gs == 'U' ):
            vowels = vowels +1

        if (Gs == 'b' or Gs == 'c' or Gs == 'd' or Gs == 'f' or Gs == 'g' or Gs == 'h' or Gs == 'j' or Gs == 'k' or Gs == 'l' or 
        Gs == 'm' or Gs == 'n' or Gs == 'p' or Gs == 'q' or Gs == 'r' or Gs == 's' or Gs == 't' or Gs == 'v' or Gs == 'w' or 
        Gs == 'x' or Gs == 'y' or Gs == 'z' or
        Gs == 'B' or Gs == 'C' or Gs == 'D' or Gs == 'F' or Gs == 'G' or Gs == 'H' or Gs == 'J' or Gs == 'K' or Gs == 'L' or 
        Gs == 'M' or Gs == 'N' or Gs == 'P' or Gs == 'Q' or Gs == 'R' or Gs == 'S' or Gs == 'T' or Gs == 'V' or Gs == 'W' or 
        Gs == 'X' or Gs == 'Y' or Gs == 'Z'):
            consonants=consonants+1

 #input: Bahala kayo dyan, #output:, #words: 3, #vowels: 6, #consonants:    
print(f"Given sentence: {Given_sentence} ")
print(f"How many words are there in the given sentence? : \t {words} word(s) .")
print(f"How many vowels are present in the given sentence? : \t {vowels} vowels.")
print(f"How many consonants are present in the given sente? : \t {consonants} consonants.")

print("Done")