# -*- coding: utf-8 -*-
"""
Created on Tue Oct  4 14:44:53 2022

@author: SAMSUNG
"""

"""
Created on Wed Sep 21 16:17:22 2022

@author: SAMSUNG
"""

# In[3] final ! 

import pandas as pd 
import random
import numpy as np
import datetime as dt
import string

def selectTeam(teams):
    team = random.choice(teams)
    return team

def selectTeamP(teamsP):
    team = random.choice(teamsP)
    teamsP.remove(team)
    return team

def teamDistribution(fileName,groupNum,proNum=1):
    
    emptyData = {'담당교수':np.nan,
                 'classcificationNo': np.nan,
                 '이름':np.nan,
                 '조':np.nan}
    
    # 빈 데이터 추가하기
    
        
    # 인원만큼 selectTeam method 호출 
    while True:
        df = pd.read_csv(fileName)
        
        # teams, teamsP 만듦 
        stringList = list(string.ascii_uppercase)
        teams = stringList[0:groupNum]
        teamsP = stringList[0:groupNum]
        
        lenDf = len(df['이름'])
        lenTeams = len(teams)
        
        quot = lenDf // lenTeams
        remains = lenDf % lenTeams
        
        # null data 추가
        for i in range(len(teams)-remains):
            df= df.append(emptyData,ignore_index=True)
        print('>> empty data가 '+str(i)+'만큼 추가되었음.')
        
        # 인원만큼 selectTeams() 
        for i in range(len(df['이름'])):       
            if proNum==1 and df['classcificationNo'][i]==1: # 팀 당 교수 1인 배치 
                team = selectTeamP(teamsP) # 교수이면
            else:
                team = selectTeam(teams) # 아니면
            
            df['조'][i] = team
            
            # 인원이 가득 찬 팀은 리스트에서 제거 
            count = df[df['조']==team]['조'].count()
            if count == quot+1:
                teams.remove(team)
                
        # 임의로 추가한 null 인원 제거            
        df=df.dropna(axis=0)
        
        # 기준 인원 미달/초과일 경우 while loop으로 반복 
        series = df.groupby('조').count()
        if (series['classcificationNo'].isin(range(0,quot))).any():
            continue
        else:
            break
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

def getResults(result):
    print("\n-----------------------------------")
    print("조편성 결과:\n"+getDay())
    print("-----------------------------------")
    result.to_csv("Results\조편성 결과_"+getDay()+".csv",encoding='cp949',index = False)
    print("완료 !")
    print("-----------------------------------")


def startGroupRandom(fileName):
    print("-----------------------------------")
    try:
        groupNum = int(input("group 수: "))
        professorDis = int(input("각 그룹 당 교수를 1인 분배할까요? [Y=1, N=0]: "))
    except:
        print('잘못된 값을 입력하였습니다.')
    
    result = teamDistribution(fileName,groupNum,professorDis)
    result = result.sort_values(by='조', ascending=True)
    getResults(result)
    
    
 # In[3] final !  
  
startGroupRandom("DATA\야유회참여자명단_ver2.csv")
