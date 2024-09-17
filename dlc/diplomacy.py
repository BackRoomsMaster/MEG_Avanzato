import random

class Comunita:
    def __init__(self, nome):
        self.nome = nome
        self.popolazione = random.randint(20, 100)
        self.forza_militare = random.randint(1, 10)
        self.risorse = random.randint(100, 500)
        self.relazioni = 50  # 0-100, 50 è neutrale
        self.specializzazione = random.choice(["Militare", "Agricola", "Tecnologica", "Medica"])

    def __str__(self):
        return f"{self.nome} (Pop: {self.popolazione}, Forza: {self.forza_militare}, Relazioni: {self.relazioni})"

class GestoreComunita:
    def __init__(self):
        self.comunita = [
            Comunita("Fortezza dell'Aquila"),
            Comunita("Valle Verde"),
            Comunita("Tecnocity"),
            Comunita("Rifugio Sanitario")
        ]

    def genera_evento(self, campo):
        comunita = random.choice(self.comunita)
        evento = random.choice(["visita", "richiesta", "offerta", "minaccia"])

        if evento == "visita":
            self.gestisci_visita(campo, comunita)
        elif evento == "richiesta":
            self.gestisci_richiesta(campo, comunita)
        elif evento == "offerta":
            self.gestisci_offerta(campo, comunita)
        elif evento == "minaccia":
            self.gestisci_minaccia(campo, comunita)

    def gestisci_visita(self, campo, comunita):
        print(f"\nLa comunità {comunita.nome} ha inviato una delegazione in visita.")
        scelta = input("Come vuoi accoglierli? (1: Calorosamente, 2: Neutralmente, 3: Con sospetto): ")
        if scelta == "1":
            comunita.relazioni += 10
            print("La delegazione apprezza la vostra calorosa accoglienza!")
        elif scelta == "2":
            print("La delegazione viene accolta con cortesia formale.")
        elif scelta == "3":
            comunita.relazioni -= 5
            print("La delegazione nota la vostra diffidenza e sembra a disagio.")

    def gestisci_richiesta(self, campo, comunita):
        risorsa_richiesta = random.randint(10, 50)
        print(f"\nLa comunità {comunita.nome} richiede {risorsa_richiesta} risorse.")
        if campo.risorse >= risorsa_richiesta:
            scelta = input(f"Accetti di dare loro {risorsa_richiesta} risorse? (s/n): ")
            if scelta.lower() == 's':
                campo.risorse -= risorsa_richiesta
                comunita.relazioni += 15
                print(f"Hai dato {risorsa_richiesta} risorse. Le relazioni con {comunita.nome} sono migliorate.")
            else:
                comunita.relazioni -= 5
                print(f"Hai rifiutato. Le relazioni con {comunita.nome} sono leggermente peggiorate.")
        else:
            print("Non hai abbastanza risorse per soddisfare la richiesta.")

    def gestisci_offerta(self, campo, comunita):
        risorsa_offerta = random.randint(10, 50)
        print(f"\nLa comunità {comunita.nome} offre {risorsa_offerta} risorse in segno di buona volontà.")
        scelta = input("Accetti l'offerta? (s/n): ")
        if scelta.lower() == 's':
            campo.risorse += risorsa_offerta
            comunita.relazioni += 10
            print(f"Hai accettato {risorsa_offerta} risorse. Le relazioni con {comunita.nome} sono migliorate.")
        else:
            comunita.relazioni -= 10
            print(f"Hai rifiutato l'offerta. Le relazioni con {comunita.nome} sono peggiorate.")

    def gestisci_minaccia(self, campo, comunita):
        print(f"\nLa comunità {comunita.nome} minaccia di attaccare il vostro campo!")
        forza_campo = sum(s.forza for s in campo.sopravvissuti) + len(campo.guardie) * 5
        
        if forza_campo > comunita.forza_militare * 10:
            print("La vostra forza superiore scoraggia l'attacco.")
            comunita.relazioni -= 5
        else:
            scelta = input("Come vuoi rispondere? (1: Prepararsi alla difesa, 2: Cercare di negoziare): ")
            if scelta == "1":
                self.gestisci_attacco(campo, comunita)
            elif scelta == "2":
                if random.random() < 0.5:
                    print("I negoziati hanno successo! L'attacco è stato evitato.")
                    comunita.relazioni += 5
                else:
                    print("I negoziati falliscono. Preparatevi all'attacco!")
                    self.gestisci_attacco(campo, comunita)

    def gestisci_attacco(self, campo, comunita):
        print(f"\nLa comunità {comunita.nome} attacca il vostro campo!")
        forza_campo = sum(s.forza for s in campo.sopravvissuti) + len(campo.guardie) * 5
        forza_attaccanti = comunita.forza_militare * 10

        if forza_campo > forza_attaccanti:
            print("Avete respinto l'attacco con successo!")
            perdite_risorse = random.randint(10, 50)
            campo.risorse -= perdite_risorse
            print(f"Avete perso {perdite_risorse} risorse durante l'attacco.")
            comunita.relazioni -= 20
        else:
            print("L'attacco ha avuto successo. Il vostro campo ha subito gravi danni.")
            perdite_risorse = random.randint(50, 100)
            campo.risorse -= perdite_risorse
            print(f"Avete perso {perdite_risorse} risorse durante l'attacco.")
            feriti = random.randint(1, 5)
            for _ in range(feriti):
                sopravvissuto = random.choice(campo.sopravvissuti)
                sopravvissuto.salute -= random.randint(20, 50)
            print(f"{feriti} sopravvissuti sono stati feriti durante l'attacco.")
            comunita.relazioni -= 30

def inizializza_dlc(campo):
    print("DLC Comunità Esterne inizializzato!")
    campo.gestore_comunita = GestoreComunita()

def esegui_azioni_giornaliere(campo):
    if random.random() < 0.3:  # 30% di possibilità di un evento ogni giorno
        campo.gestore_comunita.genera_evento(campo)

def menu_diplomazia(campo):
    while True:
        print("\nMenu Diplomazia")
        print("Comunità conosciute:")
        for i, comunita in enumerate(campo.gestore_comunita.comunita, 1):
            print(f"{i}. {comunita}")
        print("0. Torna al menu principale")

        scelta = input("Seleziona una comunità per interagire (0 per tornare indietro): ")
        if scelta == "0":
            break

        try:
            indice = int(scelta) - 1
            if 0 <= indice < len(campo.gestore_comunita.comunita):
                comunita = campo.gestore_comunita.comunita[indice]
                gestisci_interazione(campo, comunita)
            else:
                print("Selezione non valida.")
        except ValueError:
            print("Inserisci un numero valido.")

def gestisci_interazione(campo, comunita):
    while True:
        print(f"\nInterazione con {comunita.nome}")
        print("1. Invia delegazione")
        print("2. Proponi scambio di risorse")
        print("3. Richiedi assistenza")
        print("4. Torna al menu diplomazia")

        scelta = input("Seleziona un'azione: ")

        if scelta == "1":
            comunita.relazioni += 5
            print(f"Hai inviato una delegazione. Le relazioni con {comunita.nome} sono migliorate.")
        elif scelta == "2":
            quantita = int(input("Quante risorse vuoi offrire? "))
            if campo.risorse >= quantita:
                campo.risorse -= quantita
                risorse_ricevute = int(quantita * 1.2)
                campo.risorse += risorse_ricevute
                comunita.relazioni += 10
                print(f"Hai scambiato {quantita} risorse e ricevuto {risorse_ricevute} in cambio.")
                print(f"Le relazioni con {comunita.nome} sono migliorate.")
            else:
                print("Non hai abbastanza risorse per questa offerta.")
        elif scelta == "3":
            if comunita.relazioni > 70:
                aiuto = random.randint(20, 50)
                campo.risorse += aiuto
                print(f"{comunita.nome} ha accettato di aiutarti e ti ha inviato {aiuto} risorse.")
            else:
                print(f"{comunita.nome} ha rifiutato la tua richiesta di assistenza.")
        elif scelta == "4":
            break
        else:
            print("Scelta non valida.")
