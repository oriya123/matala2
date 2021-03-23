def revword (word:str)-> str:
    sizeword=len(word)
    result=''
    for i in range (sizeword):
        result=result +word[sizeword-i-1]
    return result.lower()

def countword()->int:
    fhand=open('text.txt')
    word=fhand.readline()
    counter=1
    for line in fhand:
        words=line.split()
        numberofwordsinline=len(words)
        for i in range(numberofwordsinline):
            a=line.split()
            b=revword(a[i])
            if (word.strip()==b.strip()):
                counter=counter+1    
    return counter





        
    
   



    




    
