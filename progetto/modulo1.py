def funzione_doppio(x):
    """Questa funzione restituisce il doppio del argomento passato alla funzione"""
    return x*2

def funzione_quadrato(y):
    """
    Questa funzione dovrebbe prendere un numero e restituire il suo quadrato.
    Completa l'implementazione.
    """
    return y**2

class ClasseParzialmenteImplementata:
    def __init__(self, nome):
        self.nome = nome

    def metodo_esistente(self):
        return f"Ciao, sono {self.nome}!"

    def metodo_da_completare(self, valore:str):
        """
        Questo metodo dovrebbe aggiungere il 'valore' a un attributo interno
        e restituire il nuovo valore.
        """
        return self.nome + valore