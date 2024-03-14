from libs import *
"""diccRel={
    'A':'B':5,'C':3
    'B':'A':5,'C':2,'D':4
    'C':'A':3,'B':2,'D':6,'E':7
    'D':'B':4,'C':6,'E':8
    'E':'C':7,'D':8
}
#diccRel={'A':'B'}
#diccRel={'B':'D'}
#diccRel.update({'C':'D'})

diccRel['A']={'B':5,'C':3}
diccRel['B']={'A':5,'C':2,'D':4}
diccRel['C']={'A':3,'B':2,'D':6,'E':7}
diccRel['D']={'B':4,'C':6,'E':8}
diccRel['E']={'C':7,'D':8}

printDicc(diccRel)"""

grafoTest=grafo()

grafoTest.addArista('A','B',5)
grafoTest.addArista('A','C',3)

grafoTest.addArista('B','A',5)
grafoTest.addArista('B','D',4)
grafoTest.addArista('B','C',2)

grafoTest.addArista('C','A',3)
grafoTest.addArista('C','B',2)
grafoTest.addArista('C','D',6)

grafoTest.addArista('D','C',7)
grafoTest.addArista('D','B',4)
grafoTest.addArista('D','E',8)

grafoTest.addArista('E','D',7)
grafoTest.addArista('E','C',8)
origenG ='A'
destinoG='E'
path={}
path['-']=0
print(grafoTest.Arista['A']['B'])
print(grafoTest.Arista[origenG])
print (path)
print(grafoTest)