#  Rock-Paper-Scissors 
import  random,pyttsx3,os
engine = pyttsx3.init()
print('###############Rock-Paper-Scissors##########################')
def wingame(you,comp):
    if comp==you:
        return None
    elif comp=='r':
        if you=='s':
            return False
        elif you=='p':
            return True,
    elif comp=='p':
        if you=='r':
            return False
        elif you=='s':
            return True
    elif comp=='s':
        if you=='p':
            return False
        elif you=='r':
            return True

# Directory 
directory = "ScoreBoard"

# Parent Directory path 
parent_dir = "C:\\"

# Path 
path1 = os.path.join(parent_dir, directory) 

# Create the directory 
# 'GeeksForGeeks' in 
# '/home / User / Documents' 
# Path  
path = 'C:\\ScoreBoard'
    
# Check whether the   
# specified path is an  
# existing directory or not  
isdir = os.path.isdir(path)  
if isdir==False: 

    os.mkdir(path1)
    with open('C:\\ScoreBoard\\score.txt','a+') as f:
        d=f.readline()





i=0
score=0
rate=engine.getProperty('rate')
engine.setProperty('rate',150)
voices=engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)


engine.say('Welcome To Rock Paper Scissors Game  ')
engine.runAndWait()
while(i==0):

    ra= random.randint(1,3)
    if ra == 1:
        comp='r'
    elif ra == 2:
        comp='p'
    elif ra == 3:
        comp='s'

    print('Computer Turn: Rock(r) Paper(p) Scissors(s)?')
    engine.say('choose one of the')
    engine.runAndWait()
    you=input('Your Turn: Rock(r) Paper(p) Scissors(s)?')
    print(f'Computer Choose {comp}')
    print(f'You Choose {you}')

    if wingame(you, comp)== None:
        engine.say('Tie')
        engine.runAndWait()
        print('Tie')
        
    elif wingame(you,comp):
        print('You Win!!')
        engine.say('You Win')
        engine.runAndWait()
        score=5+score
        engine.say(f'Your Score is {score}')
        engine.runAndWait()
        print(score)
        with open('C:\\ScoreBoard\\score.txt','r') as f:
                d=f.readline()
        if d=='':
            with open('C:\\ScoreBoard\\score.txt','w') as f:
                f.write(str(score))
        elif int(d)<int(score):
            with open('C:\\ScoreBoard\\score.txt','w') as f:
                f.write(str(score))

    else:
        engine.say('You Lose')
        engine.runAndWait()
        print('You Lose!!')
    engine.say('For Continue Press 0 Exit Press 1')
    engine.runAndWait()
    i=int(input('Continue(0) Exit(1)?'))
    if i==1:
        engine.say(f'Exiting and Your Score is {score}')
        engine.runAndWait()


print(f'Check Your High Score [path:  {path1}\score.txt')

engine.say(f'Check Your  High Score. path is  :  {path1}\score.txt')
engine.runAndWait()
engine.say('Thanks For Play the game')
engine.runAndWait()


##############################################################################
