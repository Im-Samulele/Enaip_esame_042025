
class Prodotto:
    def __init__(self, nome, prezzo):
        self.nome = nome
        self.prezzo = prezzo

    def __str__(self):
        return f"{self.nome} - €{self.prezzo:.2f}"

class Ordine:
    def __init__(self, cliente):
        self.cliente = cliente
        self.prodotti = []

    def aggiungi_prodotto(self, prodotto):
        self.prodotti.append(prodotto)

    def calcola_totale(self):
        """
        Questo metodo dovrebbe calcolare il totale dell'ordine.
        """
        # TODO: Implementare il calcolo del totale dell'ordine
        totale = 0
        
        for prod in self.prodotti:
            totale += prod.prezzo

        return totale
            
        