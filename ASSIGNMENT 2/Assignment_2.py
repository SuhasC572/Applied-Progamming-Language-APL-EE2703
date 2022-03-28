"""
        EE2703 Applied Programming Lab - 2022
        Assignment 1
        Name : Suhas C
        Roll Number : EE20B132
        Date : 11th Feb 2022
"""

#Importing req modules
from sys import argv, exit
import numpy as np
import math

#Defining the variables for the initialisation and terminataion
CIRCUIT_START = '.circuit'
CIRCUIT_END = '.end'
CIRCUIT_AC = '.ac'



#Defining the class resistor
class Resistor:
    
    def __init__(self, name, node1, node2, value):
        self.name = name
        self.node1 = node1
        self.node2 = node2
        self.value = value

    #Modified Nodal Analysis entries for resistor
    def MatrixEntries(self, G):
        if(self.node1 == 'GND'):
            b = int(self.node2)-1
            z = np.double(self.value)
        
            ConductanceMatrix[b][b] += 1.0 / z

        if(self.node1 != 'GND' and self.node2 != 'GND'):
            a = int(self.node1)-1
            b = int(self.node2)-1
            z = np.double(self.value)
        
            ConductanceMatrix[a][a] += 1.0 / z
            ConductanceMatrix[a][b] += -1.0 / z
            ConductanceMatrix[b][a] += -1.0 / z
            ConductanceMatrix[b][b] += 1.0 / z

        if(self.node2 == 'GND'):
            a = int(self.node1)-1
            z = np.double(self.value)
        
            ConductanceMatrix[a][a] += 1.0 / z 
        
           

#Defining class capacitor
class Capacitor:
    def __init__(self, name, node1, node2, value):
        self.name = name
        self.node1 = node1
        self.node2 = node2
        self.value = value

    #Modified Nodal Analysis entries for capacitor
    def MatrixEntries(self, G):
        if(self.node1 == 'GND'):
            b = int(self.node2)-1
            z = complex(0,-1/(w*np.double(self.value)))
        
            ConductanceMatrix[b][b] += 1.0 / z

        if(self.node1 != 'GND' and self.node2 != 'GND'):
            a = int(self.node1)-1
            b = int(self.node2)-1
            z = complex(0,-1/(w*np.double(self.value)))
        
            ConductanceMatrix[a][a] += 1.0 / z
            ConductanceMatrix[a][b] += -1.0 / z
            ConductanceMatrix[b][a] += -1.0 / z
            ConductanceMatrix[b][b] += 1.0 / z


        if(self.node2 == 'GND'):
            a = int(self.node1)-1
            z = complex(0,-1/(w*np.double(self.value)))
        
            ConductanceMatrix[a][a] += 1.0 / z 

        
    

#Defining class inductor
class Inductor:
    def __init__(self, name, node1, node2, value):
        self.name = name
        self.node1 = node1
        self.node2 = node2
        self.value = value

    #Modified Nodal Analysis entries for inductor
    def MatrixEntries(self, G):
        if(self.node1 == 'GND'):
            b = int(self.node2)-1
            z = complex(0,(w*np.double(self.value)))
        
            ConductanceMatrix[b][b] += 1.0 / z

        if(self.node1 != 'GND' and self.node2 != 'GND'):
            a = int(self.node1)-1
            b = int(self.node2)-1
            z = complex(0,(w*np.double(self.value)))
        
            ConductanceMatrix[a][a] += 1.0 / z
            ConductanceMatrix[a][b] += -1.0 / z
            ConductanceMatrix[b][a] += -1.0 / z
            ConductanceMatrix[b][b] += 1.0 / z

        if(self.node2 == 'GND'):
            a = int(self.node1)-1
            z = complex(0,(w*np.double(self.value)))
        
            ConductanceMatrix[a][a] += 1.0 / z 

        
         

#Defining class voltage source
class voltageSrc:
    def __init__(self, name, node1, node2, value):
        self.name = name
        self.node1 = node1
        self.node2 = node2
        self.value = value
     

    #Modified Nodal Analysis entries for a independent voltage source
    def MatrixEntries(self,G,I,count,nodecount):
        count += 1
        vkl = nodecount + count -1

        if self.node1 == 'GND' :
            b = int(self.node2)-1
            ConductanceMatrix[vkl][b] = -1
            ConductanceMatrix[b][vkl] = -1

        elif self.node1 != 'GND' and self.node2 != 'GND' :
            a = int(self.node1)-1
            b = int(self.node2)-1
            ConductanceMatrix[a][vkl] = 1
            ConductanceMatrix[b][vkl] = -1
            ConductanceMatrix[vkl][a] = 1
            ConductanceMatrix[vkl][b] = -1

        else :
            a = int(self.node1)-1
            ConductanceMatrix[vkl][a] = -1
            ConductanceMatrix[a][vkl] = -1
        
        CurrentMatrix[vkl][0] = self.value

#Defining class for independent current source
class CurrentSource:
    def __init__(self, name, node1, node2, value):
        self.name = name
        self.node1 = node1
        self.node2 = node2
        self.value = value

    #Modified Nodal Analysis entries for independent current source
    def fillMatrix(self,name, node1, node2,I, value):
        if node1 == "GND":
            b = int(node2)-1
            CurrentMatrix[b] = value

        if node2 == 'GND':
            a = int(node1) -1 
            CurrentMatrix[a] = -value

        if node1 != 'GND' and node2 != 'GND' :
            a = int(node1)-1
            b = int(node2)-1
            CurrentMatrix[a] = -value
            CurrentMatrix[b] = value 

#counting the number of voltage sources   
def volcount(lines):
    count_vol=0
    for line in lines:
        element_token = line.split('#')[0].split()

        if(element_token[0][0] == "V"):
            count_vol += 1
    return count_vol
    
        
def nodecount(lines):
    count=0
    for line in lines:
        element_token = line.split('#')[0].split()
        
        if(element_token[1] != 'GND'):
            if(int(element_token[1]) > count):
                count = int(element_token[1])
        if(element_token[2] != 'GND'):
            if(int(element_token[2]) > count):
                count = int(element_token[2])        
    return count

#initialising a list called element_token with null
element_token = [] 
count =0 # To count the index of voltage source
ValueOfPI = 3.14

#Making sure the Arguments are 2
if len(argv) != 2:
    print('INVALID INPUT ARGUMENT')
    exit()


try:
    with open(argv[1]) as f:
        lines = f.readlines()
        start = -1; end = -2

        for line in lines:              # extracting circuit definition start and end lines
            if  CIRCUIT_START== line[:len(CIRCUIT_START)]:
                start = lines.index(line)
               
            elif CIRCUIT_END== line[:len(CIRCUIT_END)]:
                end = lines.index(line)

            elif CIRCUIT_AC == line[:len(CIRCUIT_AC)]:
                ac = lines.index(line)  
                ac_element_token = line.split()
                w=2*ValueOfPI*np.double(ac_element_token[-1]) #angular frequency of the ac circuit

#validating circuit block,i.e. '.circuit' should always ahead of '.end'
        if start >= end:
            print("Invalid circuit definition")
        else :
            for i in range(start+1, end):
                temp = ((lines[i].split('#')[0].split()))
                element_token.append(temp)
               

        m = nodecount(lines[start+1 : end]) #m = no. of nodes in circuit
        n = volcount(lines[start+1 : end])  #n = no. of voltage sources in the circuit
        unit = 1
        OrderOfMatrix = m+n # m+n gives the order of the G matrix

        ConductanceMatrix = np.zeros((OrderOfMatrix,OrderOfMatrix), dtype="complex")  # Conductance matrix
        UnknownMatrix = np.zeros((OrderOfMatrix,unit), dtype="complex")  # Variable vector
        CurrentMatrix = np.zeros((OrderOfMatrix,unit), dtype="complex")  # Vector of independent sources

        for line in element_token:
            #Ind Voltage source
            if(line[0][0] == 'V'):
                if(line[3] != 'ac'):
                    line[3] = np.double(line[3])
                    object = voltageSrc(line[0],line[1],line[2],line[3])
                    object.MatrixEntries(ConductanceMatrix,CurrentMatrix,count, m)


                else:
                    realPart = np.double(line[-2])*math.cos(np.double(line[-1]))
                    imgPart = np.double(line[-2])*math.sin(np.double(line[-1]))
                    line[4] = complex(realPart/2,imgPart/2)
                    object = voltageSrc(line[0],line[1],line[2],line[4])
                    object.MatrixEntries(ConductanceMatrix,CurrentMatrix,count, m)

            #Ind current source
            if(line[0][0] == 'I'):
                if(line[3] != 'ac'):
                    object = voltageSrc(line[0],line[1],line[2],line[3])
                    object.MatrixEntries(line[0],line[1],line[2],line[3],CurrentMatrix)
                    
                else:
                    realPart = np.double(line[-2])*math.cos(np.double(line[-1]))
                    imgPart = np.double(line[-2])*math.sin(np.double(line[-1]))
                    line[4] = complex(realPart/2,imgPart/2)
                    object = voltageSrc(line[0],line[1],line[2],line[4])
                    object.MatrixEntries(line[0],line[1],line[2],line[4],CurrentMatrix)


            #Capacitor    
            if(line[0][0] == 'C'):
                object = Capacitor(line[0],line[1],line[2],line[3])
                object.MatrixEntries( ConductanceMatrix)
                
            #Inductor
            if(line[0][0] == 'L'):
                object = Inductor(line[0],line[1],line[2],line[3])
                object.MatrixEntries( ConductanceMatrix)

            #Resistor 
            if(line[0][0] == 'R'):
                object = Resistor(line[0],line[1],line[2],line[3])
                object.MatrixEntries( ConductanceMatrix)
                    
        #Solving for V matrix GV = I; V = inv(G)I
        UnknownMatrix = np.linalg.solve(ConductanceMatrix, CurrentMatrix)

        #Printinng the Matrixes
        print('The Conductance Matrix is : \n')
        print(ConductanceMatrix)
        print('The Current Matrix is :\n')
        print(CurrentMatrix)
        print('The Unknown Matrix  is : \n')
        print(UnknownMatrix)

    for i in range(OrderOfMatrix - 1):
        print("THE VALUE OF THE VOLTAGE AT  NODE V", i + 1, "=", UnknownMatrix[i], "\n")

    for j in range(n):
        print("THE VALUE OF THE CURRENT I", j + 1, "=", UnknownMatrix[j + OrderOfMatrix - 1], "\n")

        
except IOError:
     print('Invalid file. Make sure you entered correct file name')
     exit()               
        
