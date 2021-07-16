#By: Anish (July 5th , 2:00 PM)

def datafileread(datafilename):
    '''
        (datafileread function)
           By: Anish
           Reads a category's text file and returns a nested list
    '''

    file=open(datafilename, mode='r')
    List=file.readlines()
    file.close()
    temp=[]
    data=[]
    s=""
    for i in List:
        for j in i:
            if(j=='#'):
                temp.append(s)
                s=""
            else:
                s+=j
        temp.append(s[:-1])
        s=""
        data.append(temp)
        temp=[]
    return data

def readlog():
    '''
       (readlog function)
          By: Anish
             Reads the log file which contains the Score History (name of player , date & time ,  score)
             and returns the scoreboard dictonary.
    '''

    ScoreBoard={}
    # Read dictionary from file
    log=open("Triple_A_logs.txt", mode='r')
    lines=log.readlines()
    for i in lines:
        ScoreBoard.update({i[:i.index(" #")]: i[i.index("# ")+1:i.rindex(" #")]})
    log.close()
    return ScoreBoard
    

def appendlog(score,name,dt):
    '''
        (appendlog function)
           By:Anish
              Appends the log file to update the scoreboard
    '''
    log=open("Triple_A_logs.txt", mode='a')
    log.write(str(str(score)+' # '+name+' # '+str(dt))+'\n')
    log.close()
