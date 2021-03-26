def revword(word:str) -> str:
    sizeword=len(word)
    result=""
    for i in range(sizeword):
        result=result+word[sizeword-i-1]
    return result.lower()

def countword()-> int:
    counter=1
    fhand=open('text.txt')
    word=fhand.readline()
    word=word.lower()
    for line in fhand:  
        words1=line.split() 
        numberofwords=len(words1)
        for i in range(numberofwords):        
            a=line.split()
            b=revword(a[i])
            if(word.strip()==b.strip()):
                counter=counter+1      
    return counter
    

