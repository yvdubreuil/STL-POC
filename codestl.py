import matplotlib.pyplot as plt
import string
"""
Created on Fri Oct  6 14:26:28 2023

@author: yvand
"""



class Vertex:
    def __init__(self): 
        self.x =0
        self.y =0
        self.z =0
    def add_point(self,Point):
        self.x=Point[0]
        self.y =Point[1]
        self.z =Point[2]

    pass

class facet:
    def __init__(self):
        self.vertex=[]
        self.normal=[]
    def add_vertex(self,Vertex):
        self.vertex.append(Vertex)
        
    def add_normal(self,Normal):
        self.normal= Normal
        
    pass

class Solid:
    def __init__(self, name):
        self.name = name 
        self.facet=[]
        
    def add_facet(self, Facet):
        self.facet.append(Facet)
        
    pass

"""
On cherche à générer un cube en STL de coté 1x1

a=0
for i in range(0,1) :
    for k in range(0,1):
        for w in range(0,1):
            string.ascii_uppercase[a]
            a=a+1

on souhaite 
"""
stl = open("sphere_poly12.txt", "r")
a=stl.read()
stl.close()



# on recupére le nom du solide 

i=0
Nom_solid=''
while a[i] != "\n":
    Nom_solid= Nom_solid+a[i]
    i=i+1

liste_vertex=[]
listefacet=[]
nvert=0
Type=''
x=''
y=''
z=''
while  i<len(a)-1:
    print(Type)
    Type=Type+a[i]
    if Type==' vertex':
        i=i+2
        while a[i]!=' ':
            x=x+a[i]
            i=i+1
        i=i+1
        while a[i]!=' ':
            y=y+a[i]
            i=i+1
        i=i+1
        while a[i]!=' ':
            z=z+a[i]
            i=i+1
        i=i+1
        while a[i]!='\n':
            i=i+1
        Type=[]
        v=Vertex()
        v.x=float(x)
        v.y=float(y)
        v.z=float(z)
        x=''
        y=''
        z=''
        liste_vertex.append(v)
        Type=''
        nvert=nvert+1
        if nvert==3:
            nvert=0
            f=facet()
            f.vertex=(liste_vertex[-3],liste_vertex[-2],liste_vertex[-1])
            listefacet.append(f)
            
    i=i+1    
    if a[i]==' ':
        Type=''
        i=i+1
        
        
ax = plt.figure().add_subplot(projection='3d')

for i in range(0,len(liste_vertex)-1):
    ax.plot(liste_vertex[i].x,liste_vertex[i].y,liste_vertex[i].z, marker=10)
plt.show()
        


