import pytest
from progetto.modulo1 import funzione_doppio, funzione_quadrato, ClasseParzialmenteImplementata

def test_funzione_doppio():
    x=2
    assert funzione_doppio(x)== 4 
    #assert funzione_doppio(x) == 87

def test_funzione_quadrato():
    y = 4
    assert funzione_quadrato(y) == 16
    #assert funzione_quadrato(y) == 34

def test_metodo_esistente_classe():
    istanza = ClasseParzialmenteImplementata("Test")
    assert istanza.metodo_esistente() == "Ciao, sono Test!"

def test_metodo_da_completare_classe():
    istanza = ClasseParzialmenteImplementata("Test")
    istanza.metodo_da_completare("Python")
    # TODO: Aggiungere un'asserzione per verificare il comportamento del metodo
    assert istanza.metodo_da_completare("Python") == "TestPython"
    #assert istanza.metodo_da_completare("Python") == "Python"