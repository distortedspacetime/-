import random
import csv

primarly = []
f = open("VVP.csv",'r',encoding='utf-8-sig')
rea = csv.reader(f)
for row in rea:
    primarly.append([row[0],row[1],row[2],row[3]])
f.close
        
WordList = []
for i in range(0,len(primarly)-1):
    WordList.append(i)

correct = 0
WordListIncorrect = []

def rem(num):
    if num == 11:
        for i in range(0,50):
            WordList.remove(i)
    if num == 12:
        for i in range(50,100):
            WordList.remove(i)
    if num == 13:
        for i in range(100,150):
            WordList.remove(i)    
    if num == 14:
        for i in range(150,200):
            WordList.remove(i)    
    if num == 15:
        for i in range(200,250):
            WordList.remove(i)        
                
def yes_or_no(question):
    while "the answer is invalid":
        reply = str(input(question+' (y/n): ')).lower().strip()
        if reply[0] == 'y':
            break
        if reply[0] == 'n':
            rem(int(question[0:2]))
            break
            
yes_or_no('11차시?')
yes_or_no('12차시?')
yes_or_no('13차시?')
yes_or_no('14차시?')
yes_or_no('15차시?')

count = len(WordList)

for i in range(10):
    j = random.choice(WordList)
    print(f'{i}/10' + '\n' + primarly[j+1][3])
    WordList.remove(j)
    a = input('답: ')
    if a == primarly[j+1][2].rstrip():
        correct += 1
        print('정답')
    else:
        WordListIncorrect.append(primarly[j+1][2] + ' ' + primarly[j+1][3])
        print(f'오답(정답: {primarly[j+1][2].rstrip()})\n')
        
        
print(f"score: {correct}/10")
print("Incorrect words:")
for i in range(len(WordListIncorrect)):
    print(WordListIncorrect[i])


