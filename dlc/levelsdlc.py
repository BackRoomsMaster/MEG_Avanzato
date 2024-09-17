import random

class LivelloAvanzato:
    def __init__(self, numero):
        self.numero = numero
        self.difficolta = numero // 10 + 1  # Aumenta ogni 10 livelli
        self.tipo_ambiente = self.genera_ambiente()
        self.risorse_base = numero * 5
        self.pericolo = min(numero * 2, 100)  # Percentuale di pericolo, max 100%

    def genera_ambiente(self):
        ambienti = ["Urbano", "Foresta", "Deserto", "Montagna", "Sotterraneo"]
        return random.choice(ambienti)

    def genera_evento(self):
        eventi = [
            "Imboscata di mostri",
            "Anomalia temporale",
            "Rifugio abbandonato",
            "Tempesta di energia",
            "Incontro con altri sopravvissuti"
        ]
        return random.choice(eventi)

    def __str__(self):
        return f"Livello {self.numero} - {self.tipo_ambiente} (Difficoltà: {self.difficolta})"

class GestoreLivelli:
    def __init__(self):
        self.livelli = [LivelloAvanzato(i) for i in range(1, 51)]
        self.livello_massimo_sbloccato = 1

    def sblocca_livello(self):
        if self.livello_massimo_sbloccato < 50:
            self.livello_massimo_sbloccato += 1
            return self.livelli[self.livello_massimo_sbloccato - 1]
        return None

    def esplora_livello(self, numero_livello, squadra):
        if 1 <= numero_livello <= self.livello_massimo_sbloccato:
            livello = self.livelli[numero_livello - 1]
            print(f"Esplorazione del {livello}")
            
            # Calcola la forza della squadra
            forza_squadra = sum(s.forza + s.agilita for s in squadra)
            
            # Determina il successo dell'esplorazione
            successo = random.randint(1, 100) < (forza_squadra - (livello.difficolta * 10))
            
            if successo:
                risorse_trovate = random.randint(livello.risorse_base, livello.risorse_base * 2)
                print(f"Esplorazione riuscita! Trovate {risorse_trovate} risorse.")
                
                # Possibilità di sbloccare il livello successivo
                if numero_livello == self.livello_massimo_sbloccato and random.random() < 0.3:
                    nuovo_livello = self.sblocca_livello()
                    if nuovo_livello:
                        print(f"Sboccato un nuovo livello: {nuovo_livello}")
                
                return risorse_trovate
            else:
                danno = random.randint(10, 20) * livello.difficolta
                print(f"Esplorazione fallita. La squadra subisce {danno} danni.")
                for membro in squadra:
                    membro.salute -= danno // len(squadra)
                return 0
        else:
            print("Livello non disponibile per l'esplorazione.")
            return 0

def inizializza_dlc(campo):
    print("DLC Espansione Livelli inizializzato!")
    campo.gestore_livelli = GestoreLivelli()
    campo.livelli_sbloccati = [1]  # Inizia con il primo livello sbloccato

def esegui_azioni_giornaliere(campo):
    # Possibilità casuale di sbloccare un nuovo livello
    if random.random() < 0.1 and campo.gestore_livelli.livello_massimo_sbloccato < 50:
        nuovo_livello = campo.gestore_livelli.sblocca_livello()
        if nuovo_livello:
            campo.livelli_sbloccati.append(nuovo_livello.numero)
            print(f"Scoperto l'accesso al {nuovo_livello}")

def menu_esplorazione(campo):
    while True:
        print("\nMenu Esplorazione Avanzata")
        print("Livelli disponibili:")
        for livello in campo.livelli_sbloccati:
            print(campo.gestore_livelli.livelli[livello - 1])
        print("\n0. Torna al menu principale")
        
        scelta = input("Seleziona un livello da esplorare (0 per tornare indietro): ")
        if scelta == "0":
            break
        
        try:
            livello_scelto = int(scelta)
            if livello_scelto in campo.livelli_sbloccati:
                squadra = seleziona_squadra(campo)
                if squadra:
                    risorse = campo.gestore_livelli.esplora_livello(livello_scelto, squadra)
                    campo.risorse += risorse
            else:
                print("Livello non disponibile.")
        except ValueError:
            print("Inserisci un numero valido.")

def seleziona_squadra(campo):
    squadra = []
    while len(squadra) < 3:
        campo.mostra_sopravvissuti()
        scelta = input(f"Seleziona il sopravvissuto #{len(squadra)+1} per la squadra (0 per terminare): ")
        if scelta == "0":
            break
        try:
            indice = int(scelta) - 1
            if 0 <= indice < len(campo.sopravvissuti):
                sopravvissuto = campo.sopravvissuti[indice]
                if sopravvissuto not in squadra:
                    squadra.append(sopravvissuto)
                else:
                    print("Questo sopravvissuto è già nella squadra.")
            else:
                print("Indice non valido.")
        except ValueError:
            print("Inserisci un numero valido.")
    
    if len(squadra) < 3:
        print("Servono almeno 3 sopravvissuti per l'esplorazione.")
        return None
    return squadra
