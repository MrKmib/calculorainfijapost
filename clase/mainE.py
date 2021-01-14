'''
clases importadas: Arbolb,Eexpresiones
Arbol,Evaluador
'''
from clase.Eexpresiones import Evaluador
from clase.ArbolM import Arbol
from clase.guardarExpre import Save


def main():
	infija=input("escriba la expresion aqui: ")
	posfija=Evaluador.getPos(infija)
	print("expresion posfija:"+str(posfija))
	tree=Save.saveInTree2(posfija)
	print(tree.InOrden(tree.getRaiz()))
	print(tree.c)
	print("el resultado es: "+str(Evaluador.evaluar(infija)))
	


		
		

	

if __name__== "__main__":
	main()