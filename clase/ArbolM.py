
from clase.Nodob import TNodo

#clase arbol----------------------------
class Arbol:
	'''
	title: clase arbol modificado
	'''
	raiz = TNodo
	c=""
	p=""
	def __init__(self):
	 	self.__raiz=None

	def setRaiz(self,link):
		self.__raiz=link
	def getRaiz(self):
		return self.__raiz
	
	def getHDer(self,node):
		return node.getDer()
	def getHIzq(self,node):
		return node.getIzq()
	
	#def setHder(self,node,value):
	def setHder(self,node,value):
		if(node is not None):
			node.setDer(value)

	def setHIzq(self,node,value):
		if(node is not None):
			node.setIzq(value)
		


	 	
##metodos de la clase Arbol
	def Insertar(self,node,value):
		'''
		title: inserta un nodo al arbol
		'''
		if node is None:
			self.setRaiz(TNodo(value))
		else:
			if (value < node.getData()):
				if (node.getIzq() is None):
					node.setIzq(TNodo(value))
				else:
					self.Insertar(node.getIzq(),value)
			else:
				if (node.getDer() is None):
					node.setDer(TNodo(value))
				else:
					self.Insertar(node.getDer(),value)

	def InOrden(self,node):
		'''
		recorrido InOrden del arbol
		'''
		if (node is not None):
			self.InOrden(node.getIzq())
			self.acumular(node.getData())
			self.InOrden(node.getDer())

	#@staticmethod
	def acumular(self,value):
		self.c=self.c+str(value)
	
	def postOrden(self,node):
		'''
		title: recorrido postOrden del Arbol
		'''
		if (node is not None):
			self.postOrden(node.getIzq())
			self.postOrden(node.getDer())
			self.acumular2(node.getData())

	def acumular2(self,value):
		self.p=self.p+str(value)



		

		
#------------------------------------


def main():
	n=TNodo(90)
	n1=Arbol()
	n1.Insertar(n1.getRaiz(),50)
	#n1.setHIzq(n1.getRaiz(),n)
	n1.Insertar(n1.getRaiz(),90)
	n1.Insertar(n1.getRaiz(),21)
	n1.Insertar(n1.getRaiz(),70)
	n1.InOrden(n1.getRaiz())
	print(n1.c)

	
    

if __name__=="__main__":
	main()
