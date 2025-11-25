def kiir(matrix):
    i=0
    while i < len(matrix):
        #print(matrix[i])
        j=0
        
        while j < len(matrix[i]):
            print(f"{matrix[i][j]:>3}",end=" ")
            j+=1
        i+=1
        print("\n")


def szorzotabla_generator():
    szorzotabla=[]
    tabla=[]
    elso=1
    while elso <= 10:
        masodik=1
        tabla=[]
        while masodik <= 10:
            eredmeny=elso*masodik
            tabla.append(eredmeny)
            eredmeny=0
            masodik+=1
        szorzotabla.append(tabla)
        elso+=1
   
    return szorzotabla

    

def szorzotabla_generator_for():
    tablaszorzo=[]
    tabla=[]
    for a in range(1,11,1):
        for b in range(1,11,1):
            eredmeny=a*b
            tabla.append(eredmeny)
        tablaszorzo.append(tabla)
        tabla=[]
        b=1
    return tablaszorzo

szorzotabla_generator_for()