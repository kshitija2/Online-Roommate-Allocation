import numpy as np
import pandas as pd
from random import *
import copy
n=int(input('Enter number of rooms:'))

Matching = []
for i in range(n):
    Matching.append([])
    
newMatching = []
for i in range(n):
    newMatching.append([])

    
Assignment={}
roomsNotAvailable=[]



def recursive(h,initialMatching,dict2,unassignedRooms,edges):
#     print('h,initialMatching,dict2,unassignedRooms')
#     print(h,initialMatching,dict2,unassignedRooms)
    unassignedRooms=[]
    for v in range(n):
        if v not in initialMatching.values():
            unassignedRooms.append(v)
        
    for key, value in initialMatching.items():
        if value==h:
            for k in edges:
                if k[0]==key and k[1]!=value:
                    if k[1] in dict2.values():
                        continue
                    dict2.update({k[0]:k[1]})
                    if k[1] in unassignedRooms:
                        unassignedRooms.remove(k[1])
                        return (1,dict2,unassignedRooms)
                    r,dict2,unassignedRooms=recursive(k[1],initialMatching,dict2,unassignedRooms,edges)
#                     print('r,dict2,unassignedRooms')
#                     print(r,dict2,unassignedRooms)
                    if r==1:
                        return (1,dict2,unassignedRooms)
                    if r==0:
                        del dict2[k[0]]
                        continue
            return (0,dict2,unassignedRooms)
    return(0,dict2,unassignedRooms)
            

def offlineMatching(Matching):
    success=0
    
    while(success==0):
        assignedRooms=[]
        unassignedPeople=[]
        unassignedRooms=[]
        initialMatching={}
        Assignment={}

    
        edges=[]
        for i in range(n):
            for j in range(n):
                if Matching[i][j]==0:
                    edges.append([i,j])


        for i in range(n):
            flag=0
            for j in range(n):
                if Matching[i][j]==0 and j not in initialMatching.values() :
                    initialMatching.update({i:j})
                    flag=1
                    break
            if flag==0:
                unassignedPeople.append(i)

        for j in range(n):
            if j not in initialMatching.values():
                unassignedRooms.append(j)

        for each in unassignedPeople:
            continueFlag=0
            listEdges=[]
            for i in edges:
                if i[0]==each:
                    listEdges.append(i)

            for j in listEdges:
                if j[1] not in initialMatching.values():
                    initialMatching.update({j[0]:j[1]})
                    continueFlag=1
                    break

                else:    
                    dict2={}
                    dict2.update({j[0]:j[1]})
                    result,dict3,unassignedRooms=recursive(j[1],initialMatching,dict2,unassignedRooms,edges)

                    if result==1:
                        for key in dict3.keys():
                            if key in initialMatching:
                                del initialMatching[key]
                        initialMatching.update(dict3)
                        break
            if continueFlag==1:
                continue


        Assignment=initialMatching
        tempArray=[]
        for each in unassignedPeople:
            if each in initialMatching.keys():
                tempArray.append(each)
        for t in tempArray:
            unassignedPeople.remove(t)


        if bool(unassignedPeople):
            
            for j in range(n):
                minimum=100
                for i in range(n):
                    if Matching[i][j]<minimum:
                        minimum=Matching[i][j]
                for i in range(n):
                    Matching[i][j]=Matching[i][j]-minimum
            assignedRooms=[]
            unassignedPeople=[]
            unassignedRooms=[]
            initialMatching={}
            edges=[]
            for i in range(n):
                for j in range(n):
                    if Matching[i][j]==0:
                        edges.append([i,j])


            for i in range(n):
                flag=0
                for j in range(n):
                    if Matching[i][j]==0 and j not in initialMatching.values() :
                        initialMatching.update({i:j})
                        flag=1
                        break
                if flag==0:
                    unassignedPeople.append(i)

            for j in range(n):
                if j not in initialMatching.values():
                    unassignedRooms.append(j)

            for each in unassignedPeople:
                continueFlag=0
                listEdges=[]
                for i in edges:
                    if i[0]==each:
                        listEdges.append(i)

                for j in listEdges:
                    if j[1] not in initialMatching.values():
                        initialMatching.update({j[0]:j[1]})
                        continueFlag=1
                        break

                    else:    
                        dict2={}
                        dict2.update({j[0]:j[1]})
                        result,dict3,unassignedRooms=recursive(j[1],initialMatching,dict2,unassignedRooms,edges)

                        if result==1:
                            for key in dict3.keys():
                                if key in initialMatching:
                                    del initialMatching[key]
                            initialMatching.update(dict3)
                            break
                if continueFlag==1:
                    continue


        Assignment=initialMatching
        tempArray=[]
        for each in unassignedPeople:
            if each in initialMatching.keys():
                tempArray.append(each)
        for t in tempArray:
            unassignedPeople.remove(t)

        
        if len(Assignment)==n:
            success=1
            break

        if bool(unassignedPeople):
#             print('hi')
            linescount=0
            unmarkedRows=[]
            markedColumns= []
            markedRows=[]
            for f in unassignedPeople:
                if f not in unmarkedRows:
                    unmarkedRows.append(f)
                for f in unmarkedRows:
                    for j in range(n):
                        if Matching[f][j]==0:
                            if j not in markedColumns:
                                markedColumns.append(j)
                                for key,value in Assignment.items():
                                    if value==j:
                                        if key not in unmarkedRows:
                                            unmarkedRows.append(key)



            for b in range(n):
                if b not in unmarkedRows:
                    markedRows.append(b)


            linesCount=len(markedRows)+len(markedColumns)
            if linesCount==n:
                print(linesCount)

            if linesCount < n:
                minimum=100
                for c in range(n):
                    if c in unmarkedRows:
                        for d in range(n):
                            if d not in markedColumns:
                                if Matching[c][d]<minimum:
                                    minimum=Matching[c][d]
                for c in range(n):
                    if c in unmarkedRows:
                        for d in range(n):
                            if d not in markedColumns:
                                Matching[c][d]=Matching[c][d]-minimum

                for c in markedRows:
                    for d in markedColumns:
                        Matching[c][d]=Matching[c][d]+minimum



#     print(Assignment)
    return (Assignment)
#     print(Assignment.values())


finalAssignment={}
u=0
print('First', str(n), 'people with their utilities for rooms')

for i in range(n):
    u=u+1
    print(u)
    val=np.random.randint(n, size=n)
    print(val)
    
    Matching[i].clear()

    for a in range(n):
        Matching[i].insert(a,val[a])
        

    max=0
    for b in range(n):
        if val[b]>max:
            max=val[b]


    for c in range(n):
        Matching[i][c]=-Matching[i][c] + max



    for d in range(i+1,n):
        Matching[d].clear()
        for e in range(n):
            Matching[d].insert(e,0)
            
#     print(Matching)
    if i<5:
        while True:
            room=randint(0,n-1)
            if room not in roomsNotAvailable:
                roomsNotAvailable.append(room)
                finalAssignment.update({i:room})
                break
    else:
        assgn=offlineMatching(Matching)
        r=assgn.get(i)
        if r not in roomsNotAvailable:
            roomsNotAvailable.append(r)
            finalAssignment.update({i:r})
        else:
            while True:
                room=randint(0,n-1)
                if room not in roomsNotAvailable:
                    roomsNotAvailable.append(room)
                    finalAssignment.update({i:room})
                    break

print(finalAssignment)
print('Next', str(n), 'people with','Utilities for rooms, for already existing people and utilities assigned to them by first',str(n),'people.')
secondAssignment={}
roomsNotAvailable=[]

u=0
for j in range(n):
    u=u+1
    print(u)
    val1=np.random.randint(n, size=n)
    print(val1)
    val2=np.random.randint(n, size=n)
    print(val2)
    val3=np.random.randint(n, size=n)
    print(val3)
    
    val=[]
    for i in range(n):
        v=val1[i]+val2[i]+val3[i]
        val.append(v)

    
    newMatching[j].clear()

    for a in range(n):
        newMatching[j].insert(a,val[a])
        

    max=0
    for b in range(n):
        if val[b]>max:
            max=val[b]


    for c in range(n):
        newMatching[j][c]=-newMatching[j][c] + max


    for d in range(j+1,n):
        newMatching[d].clear()
        for e in range(n):
            newMatching[d].insert(e,0)
            
#     print(newMatching)
    if j<5:
        while True:
            room=randint(0,n-1)
            if room not in roomsNotAvailable:
                roomsNotAvailable.append(room)
                secondAssignment.update({j:room})
                break
    else:
        assgn=offlineMatching(newMatching)
        r=assgn.get(j)
        if r not in roomsNotAvailable:
            roomsNotAvailable.append(r)
            secondAssignment.update({j:r})
        else:
            while True:
                room=randint(0,n-1)
                if room not in roomsNotAvailable:
                    roomsNotAvailable.append(room)
                    secondAssignment.update({j:room})
                    break

    
print(secondAssignment)
print('Combination of Room, First Roommate and Second Roommate:')
for i in range(n):
    first=0
    second=0
    for key,value in finalAssignment.items():
        if value==i:
            first=key
    for key,value in secondAssignment.items():
        if value==i:
            second=key+n

    print(i,first,second)
