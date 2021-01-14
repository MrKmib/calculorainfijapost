'''
clases importadas:

'''
from clase.pila import Pila
from clase.Eexpresiones import Evaluador
from clase.ArbolM import Arbol
from clase.Nodob import TNodo
#----------class Save-----------------------
class Save():
    '''
    title: clase para guardar posdija en arbol
    '''

    @staticmethod
    def saveInTree(posfija):
        pila=Pila()
        tree=Arbol()
        for c in posfija:
            if not(Evaluador.esOperador(c)):
                arbol=Arbol()
                arbol.Insertar(arbol.getRaiz(),c)
                pila.apilar(arbol)
            else:
                hd=pila.desapilar()
                hi=pila.desapilar()
                arbol2=Arbol()
                arbol2.Insertar(arbol2.getRaiz(),c)
                arbol2.setHder(arbol2.getRaiz(),hd)
                arbol2.setHIzq(arbol2.getRaiz(),hi)
                pila.apilar(arbol2)
                tree=arbol2
        return tree
    @staticmethod
    def saveInTree2(posfija):
        '''
        title: metodo 2 de guardar en arbol
        '''
        pila=Pila()
        tree=Arbol()
        for c in posfija:
            if not(Evaluador.esOperador(c)):
                node=TNodo(c)
                pila.apilar(node)
            else:
                hd=pila.desapilar()
                hi=pila.desapilar()
                node2=TNodo(c)
                node2.setDer(hd)
                node2.setIzq(hi)
                pila.apilar(node2)
                tree.setRaiz(node2)
        return tree






