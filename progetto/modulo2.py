import json

def leggi_da_file(filepath):
    """Questa funzione legge dati JSON da un file."""
    try:
        with open(filepath, 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        return None

def processa_dati(dati:list): 
    """
    Questa funzione dovrebbe processare una lista di dizionari.
    Implementa la logica per filtrare i dizionari che hanno una chiave 'attivo'
    con valore True e restituire una nuova lista contenente solo i valori
    della chiave 'id' di questi dizionari.
    """
    # TODO: Implementare la logica di processamento dei dati
    lista_attivi = []

    for diz in dati:
        if diz["attivo"] == True:
            lista_attivi.append(diz["id"])

    return lista_attivi

if __name__ == "__main__":
    lista_test = [
        {
      "id": 1,
      "nome": "Prodotto A",
      "prezzo": 25.99,
      "attivo": True
    },
    {
      "id": 2,
      "nome": "Prodotto B",
      "prezzo": 12.50,
      "attivo": False
    },
    {
      "id": 3,
      "nome": "Servizio X",
      "durata": "1 ora",
      "attivo": True
    },
    {
      "id": 4,
      "nome": "Prodotto C",
      "prezzo": 55.00,
      "attivo": True,
      "in_offerta": True
    },
    {
      "id": 5,
      "nome": "Servizio Y",
      "durata": "30 minuti",
      "attivo": False
    },
    {
      "id": 6,
      "nome": "Libro1",
      "categoria": "Libro",
      "titolo": "Guida Python",
      "attivo": True
    }
    ]
    print(leggi_da_file("/home/samupy/SamuPython/Enaip_esame/Enaip_esame_042025/dati/test.json"))
    print(processa_dati(lista_test))
    print(processa_dati(leggi_da_file("/home/samupy/SamuPython/Enaip_esame/Enaip_esame_042025/dati/test.json")))

    dizionario = leggi_da_file("Enaip_esame_042025/dati/test.json")
    attivi = processa_dati(dizionario)
    print(attivi)