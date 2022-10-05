# -*- coding: utf-8 -*-
"""
Created on Wed Sep 21 15:48:45 2022

@author: SAMSUNG
"""

import random
# import pandas as pd
nameList = ['조인호','오세영','최영민','박진희',
            '안영호','김은주','이시은','천인영','오선영','박지혜',
            '박영미','조원경','Eman Taha','박진아','권소연',
            '김희선','박진선','박정은','김도연','박재민',
            '오세관','김미진']
len(nameList)
result=[]
teamList = [1,2,3,4,5]
teamList_count = [0,0,0,0,0]


for i in range(22):
    teamNumber = random.randrange(1,6)
    result.append(teamNumber)
    # [teamNumber-1] = teamList_count[teamNumber-1] +1
    # print(nameList[i]+"은(는) team "+str(teamNumber)+"입니다.")

for i in range(22):
    if result[i]==1:
        print("team 1: "+nameList[i])
    elif result[i]==2:
        print("team 2: "+nameList[i])
    elif result[i]==2:
        print("team 3: "+nameList[i])
    elif result[i]==2:
        print("team 4: "+nameList[i])
    else:
        print("team 5: "+nameList[i])




import random

nameList = ['조인호','오세영','최영민','박진희',
            '안영호','김은주','이시은','천인영','오선영','박지혜',
            '박영미','조원경','Eman Taha','박진아','권소연',
            '김희선','박진선','박정은','김도연','박재민',
            '오세관','김미진']

team1=[]
team2=[]
team3=[]
team4=[]
team5=[]
teamList = [team1,team2,team3,team4,team5]

for i in range(len(nameList)):
    while True:
        teamNumber = random.randrange(1,6)
        if len(teamList[teamNumber])<=5: break
    teamList[teamNumber].append(nameList[i])
    
for i in range(len(teamList)):
    print(teamList[i])

# In[0]
import pandas as pd 
import random

data_raw = pd.read_csv("야유회참여자명단.csv")
#data_raw.info()
#data_raw.describe()
teamList = [1,2,3,4,5]

def team_distribution(data_raw, teamList):
    
    nameSeries = data_raw['이름']
    
    for i in range(len(nameSeries)):
        while True:   
            teamNumber = random.choice(teamList)
            data_raw['조'][i] = teamNumber 
            #print(type(data_raw['조']==teamNumber))
            #data_raw[data_raw['조']==teamNumber]
            if data_raw[data_raw['조']==teamNumber]['조'].count()<6:
                break
            else:
                teamList.remove(teamNumber)
            
def team_count_distribution(data_raw):
    while True:
        if data_raw.groupby('조').count()>=4:
            break
        
team_distribution(data_raw, teamList)
team_count_distribution(data_raw)

# In[1]

import pandas as pd 
import random

df = pd.read_csv("야유회참여자명단.csv")
teamList = [1,2,3,4,5]

def team_distribution(df, teamList):
    while True:
        result = select_team(df, teamList)
        if result == True:
            break
        
        
def select_team(df, teamList):
    nameSeries = df['이름']
    
    for i in range(len(nameSeries)):
        while True:   
            teamNumber = random.choice(teamList)
            df['조'][i] = teamNumber 
            #print(type(data_raw['조']==teamNumber))
            #data_raw[data_raw['조']==teamNumber]
            if df[df['조']==teamNumber]['조'].count()<6:
                break
            else:
                teamList.remove(teamNumber)
                
    result = ""
    return result
    
team_distribution(df, teamList)

# In[2]

import pandas as pd 
import random

def randomTeams(teamList):
    teamNumber = random.choice(teamList)
    return teamNumber

def teamDistribution(fileName,teamList):
    df = pd.read_csv(fileName)
    quot = len(df['이름'])//len(teamList)
    teamCount = len(teamList)
    
    for i in range(len(df['이름'])):
        while True:
            teamNumber = randomTeams(teamList)
            df['조'][i] = teamNumber
            count = df[df['조']==teamNumber]['조'].count()
            if count==quot+1:
                teamList.remove(teamNumber)
            else:
                if len(teamList)==0:
                    teamNumber = random.randrange(0,teamCount+1)
                    df['조'][i] = teamNumber
                    break 
                else:
                    break
            
teamList = [1,2,3,4,5]       
teamDistribution("야유회참여자명단.csv",teamList)
       