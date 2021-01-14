class Pila:
	'''Representa una pila con operaciones de apilar, desapilar y
        verificar si está vacía.'''
   
	def __init__(self):
		""" Crea una pila vacía. """
		# La pila vacía se representa con una lista vacía
		self.items=[]
		self.tope= -1

	def apilar(self,value):
		""" Agrega el elemento x a la pila. """
		# Apilar es agregar al final de la lista.
		self.items.append(value)
		self.tope=self.tope+1
		


	def desapilar(self):
		""" Devuelve el elemento tope y lo elimina de la pila.
        Si la pila está vacía levanta una excepción. """

		try:
			t=self.items.pop()
			self.tope=self.tope-1
			return t
			
		except IndexError:
			raise ValueError("La pila esta vacia")

	def estaVacia(self):
		""" Devuelve True si la lista está vacía, False si no. """
		return self.tope==-1#self.items == []
	
	def getTope(self):
		return self.items[self.tope]

	def mostrar(self):
		#print(self.items[2])
		for n in self.items:
			print(n)

		#for i in range(self.cont,0,-1):
		#	print(self.items[i])


#------------------------
def main():
	p=Pila()

	p.estaVacia()

	p.apilar(1)
	p.apilar('+')
	p.apilar(3)
	

	p.mostrar()
	p.desapilar()
	p.mostrar()

	print("el elemto tope es: "+str(p.getTope()))
	


if __name__=='__main__':
	main()