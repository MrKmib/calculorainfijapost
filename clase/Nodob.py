
import sys

class TNodo:
	'''
	title: clase Nodo w
	'''
	def __init__(self,value):
		self.__dato=value
		self.__izq=None
		self.__der=None

	def getData(self):
		return self.__dato
	def setData(self,d):
		self.__dato=d


	def getIzq(self):
		return self.__izq
	def setIzq(self,nodo):
		self.__izq=nodo


	def getDer(self):
		return self.__der
	
	def setDer(self,nodo):
		self.__der=nodo

def main():
	print("clase nodo")
	#creando un objeto de la clase TNodo
	n1=TNodo("hello")
	n1.setData("Donde")
	print(n1.getData())

if __name__== "__main__":
	main()


	
