#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#!/user/bin/env python3

import copy 
import sys 

class Node:
    def __init__(self,name,cols, rows, nodePlace):
        self.shortPath = {} 
        self.shortNode = {} 
        self.shortPathPast = {} 
        self.shortNodePast = {} 
        self.result = [] 
        self.nearNodes = [] 
        self.name = name 
        self.subChart = [[0 for i in range(cols)] for j in range(rows)]
        for x in range(cols):
            self.subChart[nodePlace][x] = -99
        for x in range(rows):
            self.subChart[x][nodePlace] = -99
        for x in range(rows):
            self.shortPath[x] = -99
            self.shortNode[x] = "Self" 
            
    def usefulValue(self, cols, rows): 
        self.result = [] 
        for x in range(rows):
            for y in range(cols):
                if self.subChart[x][y]!=-99:
                    self.result.append(self.subChart[x][y]) 
                    
    def setInf(self, cols, rows): 
        for x in range(rows):
            for y in range(cols):
                if self.subChart[x][y]==0:
                    self.subChart[x][y] = 100 
                    
    def updateShortPath(self, cols, rows):
        for x in range(rows):
            smallDistance = 99 
            place = 99 
            for y in range(cols):
                if self.subChart[x][y]<smallDistance and self.subChart[x][y]!=-99 and self.subChart[x][y]!=-1:
                    smallDistance = self.subChart[x][y] 
                    place = y 
 
            if smallDistance!=99 and smallDistance>0:
                self.shortPath[x] = smallDistance 
                self.shortNode[x] = place 
 
    def updateShortPathAfterUpdate(self, cols, rows):   
#         self.shortPath = {} 
#         self.shortNode = {} 
        for x in range(rows):
            smallDistance = 99 
            place = 99 
            for y in range(cols):
                if self.subChart[x][y]<smallDistance and self.subChart[x][y]!=-99 and self.subChart[x][y]!=-1:
                    smallDistance = self.subChart[x][y] 
                    place = y 
                    
            if smallDistance!=99:
                self.shortPath[x] = smallDistance 
                self.shortNode[x] = place 
            
            
    def storePastRoute(self): 
        self.shortPathPast =  copy.copy(self.shortPath) 
        self.shortNodePast =  copy.copy(self.shortNode) 
        
    def getFinalResult(self,nodeNames): 
        value = "" 
        for x in self.shortPath:
            if self.shortPath[x]!=-99:
                value = value+ "router "+self.name+": " 
                value = value + nodeNames[x]+" is "+ str(self.shortPath[x])+" routing through "+nodeNames[self.shortNode[x]]+"\n" 
            
        value = value[0:len(value)-1]
        return value 
    def isSend(self):
        sendNodes =[] 
        for x in self.nearNodes:
            if self.shortNode[x]!=self.shortNodePast[x]:
                sendNodes.append(x) 
        return sendNodes 
        
def ReadInput():
    x = []
    lines = 0 
    firstEmpty = 1 
    with open("INPUT") as file:
        for l in file:
            if l.strip() in (None, '') and (firstEmpty==1):
                firstEmpty = 0 
                x.insert(0,lines)
            else:
                lines = lines +1
                x.append(l.strip()) 
    return x 
lastInput = "999" 

def isInputFinished(inputt):

    if len(lastInput)==0 and len(inputt) == 0:
        return 1 
    return 0     

times = 0 
i = 0 
nodes = [] 
nodeNames = [] 
# inputFile = ReadInput() 
inputFile = [] 
inpu = "B" 
number = 0 

# while isInputFinished(inpu)==0:
#     isFirstBlank = 0 
#     lastInput = inpu 
#     inpu = input() 
#     i = i +1 
#     if len(inpu)==0 and number==0:
#         i = i-1 
#         inputFile.insert(0,i)
#         number = -99 
#         isFirstBlank = 1 
#     if  isFirstBlank==0:
#         inputFile.append(inpu)
insertPlace = 0;
lines = 0 
firstEmpty = 1
isQuit = 0;
lineLast = 999
isBreak = 0;
inppu = [];
# try:
#     for line in sys.stdin:
#             inppu.append(line)
#             if line.strip() not in (None, '') or len(inputFile)!=0:
#                 if len(inputFile)!=0 and " " in line: 
#                     raise Exception("Sorry,  "+line)
#                 else:    
#                     if line.strip() in (None, '') and (firstEmpty==1):
#                         firstEmpty = 0 
# #                         inputFile.insert(0,lines)
#                     else:
#                     lines = lines +1
#                     inputFile.append(line.strip())
#                     if lastInput == 0 and len(line.strip()) ==0:
#                             break
#                     if lastInput == 0 and len(line.strip()) ==1:
                            
#                             del inputFile[len(inputFile)-2:len(inputFile)-1]
#                     lastInput = len(line.strip())
# except:
#     print("An exception occurred")
#     print(inppu)

# for pla in inputFile:
#     if len(pla) ==1:
#         insertPlace = insertPlace+1;
        
# inputFile.insert(0,insertPlace)
# print(sys.stdin)


try:
    while True:
        line = raw_input()
        inppu.append(line)
        singleLine = "";
        inputFile.append(line)
        if not line and len(inputFile)==1:
            del inputFile[0:1]
        if lineLast == 0 and len(line.strip()) ==0:
            break
        lineLast = len(line.strip());

except:
    print("An exception occurred")
#     print(inppu)
    exit(1)
    
for inp in inputFile:
    eachLine = inp.split(" ")
    if len(eachLine)==1 and inp.strip() not in (None, ''):
        insertPlace = insertPlace+1;
        

del inputFile[insertPlace:insertPlace+1]
inputFile.insert(0,insertPlace)
# print(inputFile)
i = 0  

nodeNumber = inputFile[0] 
del inputFile[0:1]

for x in range(int(nodeNumber)):
    nodes.append(Node(inputFile[x],int(nodeNumber),int(nodeNumber), x)) 
    nodeNames.append(inputFile[x]) 

del inputFile[0:nodeNumber]

while i<len(inputFile):
    if inputFile[i] not in (None, ''):
        eachLine = inputFile[i].split(" ") 
#         route table
        nodes[nodeNames.index(eachLine[0])].subChart[nodeNames.index(eachLine[1])][nodeNames.index(eachLine[1])] = int(eachLine[2]) 
        nodes[nodeNames.index(eachLine[1])].subChart[nodeNames.index(eachLine[0])][nodeNames.index(eachLine[0])] = int(eachLine[2])  
#         short path
        nodes[nodeNames.index(eachLine[0])].shortPath[nodeNames.index(eachLine[1])] = int(eachLine[2]) 
        nodes[nodeNames.index(eachLine[1])].shortPath[nodeNames.index(eachLine[0])] = int(eachLine[2]) 
#         near node
        nodes[nodeNames.index(eachLine[0])].nearNodes.append(nodeNames.index(eachLine[1])) 
        nodes[nodeNames.index(eachLine[1])].nearNodes.append(nodeNames.index(eachLine[0])) 

        i=i+1 
    else:
        break 
        
del inputFile[0:i+1]   

for node in nodes:    
    node.setInf(len(nodeNames),len(nodeNames))   
    
# print process
def printProcess(x):
    nodes[x].usefulValue(len(nodeNames),len(nodeNames)) 
    print("router "+ nodeNames[x]+" at t="+str(times)) 
    names = "\t";
#     names = names+"\t";
#     print("\t", end = '') 
    for y in range(len(nodeNames)):
        if nodeNames[y]!=nodeNames[x]:
            names = names+nodeNames[y]
#             print(nodeNames[y], end = '')
            if y!=len(nodeNames)-1:
                names = names+"\t";
#                 print("\t", end = '')
    print(names)
#     print() 
    for y in range(len(nodeNames)):
        if nodeNames[y]!=nodeNames[x]:
            values = "" 
            singleValue = "" 
            for z in range(len(nodeNames)-1):
                if nodes[x].result[0]==100:
                    singleValue = "INF"
                    if z!=len(nodeNames)-2:
                        singleValue = singleValue+"\t";
                elif nodes[x].result[0]== -1:
                    singleValue = "-"
                    if z!=len(nodeNames)-2:
                        singleValue = singleValue+"\t";
                else:
                    singleValue = str(nodes[x].result[0])
                    if z!=len(nodeNames)-2:
                        singleValue = singleValue+"\t";
                values = values+singleValue 
                del nodes[x].result[0:1]
            print(nodeNames[y]+"\t"+values) 
    print() 

# print result
def printResult(): 
    for node in nodes:
        print(node.getFinalResult(nodeNames)) 
    print()     
    
for x in range(int(nodeNumber)):
    printProcess(x) 
    


# init process
def cauculate(fromNode, midNode):
    for path in midNode.shortPath:
        if midNode.shortPath[path]!=-99 and path!=nodeNames.index(fromNode.name):
            if fromNode.subChart[nodeNames.index(midNode.name)][nodeNames.index(midNode.name)]!=-99:
                compare = fromNode.subChart[nodeNames.index(midNode.name)][nodeNames.index(midNode.name)]+ midNode.shortPath[path] 
                if fromNode.subChart[nodeNames.index(midNode.name)][nodeNames.index(midNode.name)]==-1:
                    fromNode.subChart[path][nodeNames.index(midNode.name)] = -1
                elif compare>0 and compare<fromNode.subChart[path][nodeNames.index(midNode.name)]:
                    fromNode.subChart[path][nodeNames.index(midNode.name)] = compare          
            
            
def updateNodeAttributes():
    for x in range(int(nodeNumber)):
        nodes[x].usefulValue(len(nodeNames),len(nodeNames)) 
        nodes[x].updateShortPath(len(nodeNames),len(nodeNames)) 
        
def storePast():
    for x in range(int(nodeNumber)):
        nodes[x].storePastRoute() 
    
def isIterationStop():
    for x in range(int(nodeNumber)):
        if nodes[x].shortPath!=nodes[x].shortPathPast:
            return 1 
        
    return 0 

updateNodeAttributes() 

while isIterationStop()==1:
    storePast() 
    for node in nodes:
        for near in node.nearNodes:
            cauculate(node,nodes[near])

    updateNodeAttributes() 
    times = times+1 
    for x in range(int(nodeNumber)):
        printProcess(x)   

printResult()   

# update
i = 0 

while i>=0:
    if i>=len(inputFile):
        break 
    if inputFile[i] not in (None, ''):
        distance = 0 
        eachLine = inputFile[i].split(" ") 
        if int(eachLine[2])<0:
            distance = -1 
        else:
            distance = int(eachLine[2]) 
#       route table
        nodes[nodeNames.index(eachLine[0])].subChart[nodeNames.index(eachLine[1])][nodeNames.index(eachLine[1])] = distance 
        nodes[nodeNames.index(eachLine[1])].subChart[nodeNames.index(eachLine[0])][nodeNames.index(eachLine[0])] = distance 
        if distance==-1:
            for x in range(int(nodeNumber)):
                if nodes[nodeNames.index(eachLine[1])].subChart[x][nodeNames.index(eachLine[0])]!=-99:
                    nodes[nodeNames.index(eachLine[1])].subChart[x][nodeNames.index(eachLine[0])] = distance 
                if nodes[nodeNames.index(eachLine[0])].subChart[x][nodeNames.index(eachLine[1])]!=-99:    
                    nodes[nodeNames.index(eachLine[0])].subChart[x][nodeNames.index(eachLine[1])] = distance 
        
        if nodeNames.index(eachLine[1]) in nodes[nodeNames.index(eachLine[0])].nearNodes:            
            if distance==-1:
        #       near node
                nodes[nodeNames.index(eachLine[0])].nearNodes.remove(nodeNames.index(eachLine[1])) 
                
        else:
            if distance!=-1:
                nodes[nodeNames.index(eachLine[0])].nearNodes.append(nodeNames.index(eachLine[1])) 
                
        if nodeNames.index(eachLine[0]) in nodes[nodeNames.index(eachLine[1])].nearNodes:
            
            if distance==-1:
        #       near node
                nodes[nodeNames.index(eachLine[1])].nearNodes.remove(nodeNames.index(eachLine[0])) 
                
        else:
            if distance!=-1:
                nodes[nodeNames.index(eachLine[1])].nearNodes.append(nodeNames.index(eachLine[0])) 
        
        i=i+1 
    else:
        break 
    
# for node in nodes:
#     node.updateShortPathAfterUpdate(len(nodeNames),len(nodeNames)) 
def cauculateUpdate(fromNode, midNode):
    for path in midNode.shortPath:
        if midNode.shortPath[path]!=-99 and path!=nodeNames.index(fromNode.name):
            if fromNode.subChart[nodeNames.index(midNode.name)][nodeNames.index(midNode.name)]!=-99:
                compare = fromNode.subChart[nodeNames.index(midNode.name)][nodeNames.index(midNode.name)]+ midNode.shortPath[path] 
                if fromNode.subChart[nodeNames.index(midNode.name)][nodeNames.index(midNode.name)]==-1:
                    fromNode.subChart[path][nodeNames.index(midNode.name)] = -1
                elif compare>0 :
                    fromNode.subChart[path][nodeNames.index(midNode.name)] = compare          
                    
for node in nodes:
        for near in node.nearNodes:
            cauculate(node,nodes[near]) 
            
times = times+1 
for x in range(int(nodeNumber)):
    printProcess(x) 
storePast() 
updateNodeAttributes() 

# for node in nodes:
#         for near in node.nearNodes:
#             cauculateUpdate(node,nodes[near])             
# times = times+1 
# for x in range(int(nodeNumber)):
#     printProcess(x)   
# storePast() 
# updateNodeAttributes() 

while isIterationStop()==1:
    
    for node in nodes:
        for near in node.nearNodes:
            cauculateUpdate(node,nodes[near])
    storePast() 
    updateNodeAttributes() 
    i = i+1
    times = times+1 
    for x in range(int(nodeNumber)):
        printProcess(x)   

printResult()   


# In[ ]:


qwe


# In[ ]:




