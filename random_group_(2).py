"""
Created on Wed Sep 21 16:17:22 2022

@author: SAMSUNG
"""

# In[3] final ! 

import pandas as pd 
import random
import numpy as np
import datetime as dt

def selectTeam(teams):
    team = random.choice(teams)
    return team

def dataAppendForDistribution(fileName,teams):
    df = pd.read_csv(fileName)
    quot = len(df['이름']) // len(teams)
    remains = len(df['이름']) % len(teams)
    df= df.append([0,0,0])
    print('추가')
    return df

def teamDistribution(fileName,teams):
    
    df = pd.read_csv(fileName)
    quot = len(df['이름']) // len(teams)
    remains = len(df['이름']) % len(teams)

    emptyData = {'담당교수':np.nan,
                 '이름':np.nan,
                 '조':np.nan}
    
    for i in range(len(teams)-remains):
        df= df.append(emptyData,ignore_index=True)
    print('추가되었음')
        
    for i in range(len(df['이름'])):
        print(len(df['이름']))
        while True:
            team = selectTeam(teams)
            df['조'][i] = team
            count = df[df['조']==team]['조'].count()
            if count == quot+1:
                teams.remove(team)
            break
    df=df.dropna(axis=0)
    return df

def getDay():
    today = dt.datetime.now()
    m = today.month
    d = today.day
    h = today.hour
    mn = today.minute
    if m<10:
        m = '0'+str(m)
    return str(m)+"월"+str(d)+"일"+str(h)+"시"+str(mn)+"분"


# team info
teams = ['A','B','C','D','E']
teamsNumber = [1,2,3,4,5]

# result
result = teamDistribution("DATA\야유회참여자명단.csv",teams)
result=result.sort_values(by='조', ascending=True)

# result 출력 및 저장
print("\n-----------------------------------")
print("조편성 결과:\n"+getDay())
print("-----------------------------------")
print(result)
result.to_csv("Results\조편성 결과_"+getDay()+".csv",encoding='cp949',index = False)