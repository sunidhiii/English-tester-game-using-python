def countVowels(words):
    vowels=0
    for i in words:
        if(i=='a' or i=='e' or i=='i' or i=='o' or i=='u' or i=='A' or i=='E' or i=='I' or i=='O' or i=='U'):
            vowels=vowels+1
    return vowels


def countConsonants(words):
    cons=0
    for i in words:
        if(i=='a' or i=='e' or i=='i' or i=='o' or i=='u' or i=='A' or i=='E' or i=='I' or i=='O' or i=='U'):
            cons=cons
        else:
            cons=cons+1
    return cons

def wordLength(words):
    length=len(words)
    return length

def letter(words,r):
    return words[r-1]

    
       
score=0
import random
candidateWords=['Cat','Dog','Car','Pen','Man','Hello','Bye','Eat','Ear','Nose','Study','Read','Write','Roam','Hand','Pen','Goodbye']
a=random.sample(candidateWords,5)
print('Welcome to English Tester Pro!')
for index,words in enumerate(a):
    print("\nWord {}/{}: {}".format(index+1,len(a),words))
    questionNumber=random.randint(1,4)
 
    if questionNumber==1:
        ans1=int(input("How many vowels does the word contain?\n>"))
        
    
        vowels =countVowels(words);
        if vowels==ans1:
            print("Correct!")
            score=score+1
        else:
            print("Incorrect! Correct answer was",vowels)
            
    
    elif questionNumber==2:
         ans2=int(input("How many consonants does the word contain?\n>"))
        

         cons =countConsonants(words)
         if cons==ans2:
             print("Correct!")
             score=score+1
         else:
            print("Incorrect! Correct answer was",cons)
            
    elif questionNumber==3:
         r=random.randint(1,3)
         ans3=input("What is letter {} of the word?\n>".format(r))
         let=letter(words,r)
         if let==ans3:
             print("Correct!")
             score=score+1
                  
         else:
             print("Incorrect! Correct answer was",let)                 
        

    else:
         ans4=int(input("How many letters does the word contain?\n>"))
        

         length = wordLength(words)
         if length==ans4:
             print("Correct!")
             score=score+1
         else:
             print("Incorrect! Correct answer was", length)



print("\nGame Over. Your score is {}/5".format(score))



 
        
