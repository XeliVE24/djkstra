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


#ES LO MISMO SOLO Q POR SEPARADO 
"""diccRel ['A'] = {'B':5, 'C':3}
diccRel ['B'] = {'A':5, 'C':2, 'D':4}
diccRel ['C'] = {'A':3, 'B':2, 'D':6, 'E':7}
diccRel ['D'] = {'B':4, 'C':6, 'E':8}
diccRel ['E'] = {'C':7, 'D':8}  """

grafoTest = grafo()
grafoTest.addArista('A', 'B', 5)
grafoTest.addArista('A', 'C', 3)

grafoTest.addArista('B', 'A', 5)
grafoTest.addArista('B', 'C', 2)
grafoTest.addArista('B', 'D', 4)

grafoTest.addArista('C', 'A', 3)
grafoTest.addArista('C', 'B', 2)
grafoTest.addArista('C', 'D', 6)
grafoTest.addArista('C', 'E', 7)

grafoTest.addArista('D', 'B', 4)
grafoTest.addArista('D', 'C', 6)
grafoTest.addArista('D', 'E', 8)

grafoTest.addArista('E', 'C', 7)
grafoTest.addArista('E', 'D', 8)

origenG = 'A'
destinoG = 'E'
path ={}
visitados=[]
visitados.append(origenG)
path[origenG] = {'-':0}
llaves = grafoTest.aristas[origenG].keys()
print(llaves)

for i in llaves:
    path[i]={origenG: grafoTest.aristas[origenG][i]}

print("primer iter")
print(path)
print(visitados)



verticeAct = 'B'
llaves = grafoTest.aristas[origenG].keys()
print(llaves)

for i in llaves:
    if i not in visitados:
     #   self.aristas[origen].update((destino.peso))
        if i not in path: path[i]={}
        llave=list(path[verticeAct].keys())
        acumulado=path[verticeAct][llave[0]]
        path[i].update({verticeAct: grafoTest.aristas[verticeAct][i]+acumulado})

#revisa si hay mas de dos llaves en una llave del path
        if len(path[i]==2):
            kiss=list(path[i].keys())
            if kiss[0]>kiss[1]:
                del (path[i][kiss[0]])
            elif kiss[0]< kiss[1]:
                del(path[i][kiss[1]])
            pass
    
print(path)

