from libs import *
import sys

#dicc = {
 #   'nom' :'xeli',
#    'edad':18
#    'tel':{
#        'cel':5,
 #       'fij':6
 #   }
           
#}

#print (dicc["edad"])

diccRel={
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

printDicc(diccRel)
verticeA = vertice ('A')
arista1=arista ('A':'B')