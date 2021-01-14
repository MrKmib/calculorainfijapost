from clase.pila import Pila

class Evaluador:
    '''
    type: clase de metodos estaticos
    evaluar,getPos, convertir, 
    '''

    @staticmethod
    def evaluar(value):
        '''
        evalua la expresion pos
        '''
        infija=value
        posfija =Evaluador.convertir(infija)
        return Evaluador.evaluarPosfija(posfija)
    
    @staticmethod
    def getPos(infija):
        """
        devuelve la expresion posfija
        """
        posfija = Evaluador.convertir(infija)
        return posfija


    @staticmethod
    def convertir(infija):
        posfija= ""
        pila= Pila()
        for n in infija:
            if(Evaluador.esOperador(n)):
                if(pila.estaVacia()):
                    pila.apilar(n)
                else:
                    if(Evaluador.prioridadExp(n)==0):
                        b=True
                        while ((b is True) and (pila.getTope()!='(')):
                            posfija = posfija + str(pila.desapilar()) 
                            if(Evaluador.prioridadPila(pila.getTope())==0):
                                pila.desapilar()
                                b=False
                    else:
                        if(Evaluador.prioridadExp(n)>Evaluador.prioridadPila(pila.getTope())):
                            pila.apilar(n)                         
                        else:
                             while((pila.tope > -1) and (Evaluador.prioridadExp(n)<=Evaluador.prioridadPila(pila.getTope()))):
                                posfija = posfija + str(pila.desapilar())                                             
                             pila.apilar(n)

                        
                    '''
                    if(Evaluador.prioridadExp(n)>Evaluador.prioridadPila(pila.getTope())):
                        pila.apilar(n)
                    else:
                        while((pila.tope > -1) and (Evaluador.prioridadExp(n)<=Evaluador.prioridadPila(pila.getTope()))):
                            posfija = posfija + str(pila.desapilar())                              
                        pila.apilar(n)                     
                    '''    
            else:
                posfija=posfija+str(n)
        
        while(not(pila.estaVacia()) and (pila.getTope()!=')')):
            posfija = posfija + str(pila.desapilar())
            
        return posfija

    @staticmethod
    def prioridadExp(operador):
        '''
        retorna int prioridad en la expresion
        '''
        if(operador=='^'): return 4
        if(operador=='*' or operador=='/'): return 2
        if(operador=='+' or operador=='-'): return 1
        if(operador=='('): return 5
        return 0

    @staticmethod
    def prioridadPila(operador):
        '''
        retorna int prioridad en la pila
        '''
        if(operador=='^'): return 3
        if(operador=='*' or operador=='/'): return 2
        if(operador=='+' or operador=='-'): return 1
        if(operador=='('): return 0
        return -1

    @staticmethod
    def evaluarPosfija(posfija):
        '''
        evaluacion de posfija 
        '''
        pila=Pila()
        for c in posfija:
            if not(Evaluador.esOperador(c)):
                x=float(c)
                pila.apilar(x)
            else:
                op2 = pila.desapilar()
                op1 = pila.desapilar()
                resul= Evaluador.operacion(c,op1,op2)
                pila.apilar(resul) 
        return pila.desapilar()
    
        


    @staticmethod
    def esOperador(a):
        '''
        verfica si un operador, retorna True o False
        '''
        if(a=='*' or a=='/' or a=='+' or a=='-' or a=='(' or a==')' or a=='^'):
            return True
        else:
            return False
    
    @staticmethod
    def operacion(c,op1,op2):
        """
        operacion de los datos
        """
        if(c=='*'): return op1*op2
        if(c=='/'): return op1/op2
        if(c=='+'): return op1+op2
        if(c=='-'): return op1-op2
        if(c=='^'): return pow(op1,op2)
        return 0




       

        