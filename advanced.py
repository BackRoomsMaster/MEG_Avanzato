import random
import os
import importlib
from dlc import miglioramenti_tecnici

class Mostro:
    def __init__(self, livello):
        self.forza = random.randint(5 * livello, 10 * livello)
        self.salute = random.randint(20 * livello, 40 * livello)

    def attacca(self):
        return random.randint(1, self.forza)

class Sopravvissuto:
    def __init__(self, nome):
        self.nome = nome
        self.forza = random.randint(1, 10)
        self.intelligenza = random.randint(1, 10)
        self.agilita = random.randint(1, 10)
        self.resistenza = random.randint(1, 10)
        self.abilita_speciale = random.choice(["Medicina", "Ingegneria", "Combattimento", "Cucina"])
        self.compito = None
        self.salute = 100

    def __str__(self):
        return f"{self.nome}: F:{self.forza} I:{self.intelligenza} A:{self.agilita} R:{self.resistenza} - {self.abilita_speciale} - Compito: {self.compito or 'Nessuno'} - Salute: {self.salute}"

    def attacca(self):
        return random.randint(1, self.forza + 5)
class CampoBase:
    def __init__(self):
        self.risorse = 100
        self.sopravvissuti = []
        self.guardie = []
        self.capacita_massima = 20
        self.giorno = 1
        self.livelli_sbloccati = [0]
        self.strutture = {
            "Torre Radio": 0,
            "Abitazioni": 1,
            "Infermeria": 0,
            "Officina": 0,
            "Centro di Addestramento": 0,
            "Magazzino": 0
        }
        self.produzione_risorse = 5
        self.genera_sopravvissuti_iniziali()

    def genera_sopravvissuti_iniziali(self):
        nomi = ["Alex", "Sam", "Jordan", "Taylor", "Casey", "Morgan", "Riley", "Avery", "Quinn", "Skyler"]
        for _ in range(10):  # Genera 10 sopravvissuti iniziali
            nome = random.choice(nomi)
            nomi.remove(nome)  # Evita duplicati
            self.sopravvissuti.append(Sopravvissuto(nome))

    def mostra_stato(self):
        print(f"\nGiorno: {self.giorno}")
        print(f"Risorse: {self.risorse}")
        print(f"Sopravvissuti: {len(self.sopravvissuti)}/{self.capacita_massima}")
        print(f"Guardie: {len(self.guardie)}")
        print(f"Produzione giornaliera di risorse: {self.produzione_risorse}")
        print(f"Livelli sbloccati: {', '.join(map(str, self.livelli_sbloccati))}")
        print("Strutture:")
        for struttura, quantita in self.strutture.items():
            print(f"  {struttura}: {quantita}")

    def mostra_sopravvissuti(self):
        print("\nLista dei Sopravvissuti:")
        for i, sopravvissuto in enumerate(self.sopravvissuti, 1):
            print(f"{i}. {sopravvissuto}")

    def assegna_compito(self, indice_sopravvissuto, compito):
        if 0 <= indice_sopravvissuto < len(self.sopravvissuti):
            self.sopravvissuti[indice_sopravvissuto].compito = compito
            print(f"Compito {compito} assegnato a {self.sopravvissuti[indice_sopravvissuto].nome}")
        else:
            print("Indice sopravvissuto non valido")

    def assegna_guardia(self, indice_sopravvissuto):
        if 0 <= indice_sopravvissuto < len(self.sopravvissuti):
            sopravvissuto = self.sopravvissuti[indice_sopravvissuto]
            if sopravvissuto not in self.guardie:
                self.guardie.append(sopravvissuto)
                print(f"{sopravvissuto.nome} è stato assegnato come guardia.")
            else:
                print(f"{sopravvissuto.nome} è già una guardia.")
        else:
            print("Indice sopravvissuto non valido")

    def rimuovi_guardia(self, indice_sopravvissuto):
        if 0 <= indice_sopravvissuto < len(self.sopravvissuti):
            sopravvissuto = self.sopravvissuti[indice_sopravvissuto]
            if sopravvissuto in self.guardie:
                self.guardie.remove(sopravvissuto)
                print(f"{sopravvissuto.nome} non è più una guardia.")
            else:
                print(f"{sopravvissuto.nome} non era una guardia.")
        else:
            print("Indice sopravvissuto non valido")

    def aggiorna_guardie(self):
        for guardia in self.guardie:
            guardia.resistenza = max(1, guardia.resistenza - 1)
            guardia.agilita = max(1, guardia.agilita - 1)
    def esegui_compiti(self):
        risorse_generate = 0
        for sopravvissuto in self.sopravvissuti:
            if sopravvissuto.compito == "Raccolta Risorse":
                efficienza = (sopravvissuto.forza + sopravvissuto.resistenza) / 2
                risorse_generate += int(efficienza * 1.5)
            elif sopravvissuto.compito == "Ricerca":
                efficienza = sopravvissuto.intelligenza
                risorse_generate += int(efficienza * 1.2)
            elif sopravvissuto.compito == "Manutenzione":
                efficienza = (sopravvissuto.intelligenza + sopravvissuto.agilita) / 2
                risorse_generate += int(efficienza)
        self.risorse += risorse_generate
        print(f"I compiti giornalieri hanno generato {risorse_generate} risorse.")

    def esplora(self):
        esploratori = [s for s in self.sopravvissuti if s not in self.guardie][:3]
        if len(esploratori) < 3:
            print("Servono almeno 3 sopravvissuti per l'esplorazione!")
            return

        print("Gruppo di esplorazione:")
        for esploratore in esploratori:
            print(f"- {esploratore.nome}")

        livello_esplorato = random.choice(self.livelli_sbloccati)
        print(f"Il gruppo esplora il Livello {livello_esplorato}")

        if random.random() < 0.5 + (livello_esplorato * 0.05):
            mostro = Mostro(livello_esplorato + 1)
            print(f"Il gruppo ha incontrato un mostro di livello {livello_esplorato + 1}!")
            self.combattimento_esplorazione(esploratori, mostro)
        else:
            efficacia = sum(e.agilita + e.resistenza for e in esploratori) / len(esploratori)
            if random.random() < efficacia / 20:
                risorse_trovate = random.randint(10, 50)
                self.risorse += risorse_trovate
                print(f"L'esplorazione ha fruttato {risorse_trovate} risorse!")
                
                if random.random() < 0.2 and len(self.livelli_sbloccati) < 10:
                    nuovo_livello = max(self.livelli_sbloccati) + 1
                    self.livelli_sbloccati.append(nuovo_livello)
                    print(f"Scoperto l'accesso al Livello {nuovo_livello}!")
            else:
                print("L'esplorazione non ha portato risultati significativi.")

    def combattimento_esplorazione(self, esploratori, mostro):
        print("Inizia il combattimento!")
        while mostro.salute > 0 and any(e.salute > 0 for e in esploratori):
            for esploratore in esploratori:
                if esploratore.salute > 0:
                    danno = esploratore.attacca()
                    mostro.salute -= danno
                    print(f"{esploratore.nome} infligge {danno} danni al mostro.")
                    if mostro.salute <= 0:
                        print("Il mostro è stato sconfitto!")
                        return

            bersaglio = random.choice([e for e in esploratori if e.salute > 0])
            danno = mostro.attacca()
            bersaglio.salute -= danno
            print(f"Il mostro infligge {danno} danni a {bersaglio.nome}.")

        if all(e.salute <= 0 for e in esploratori):
            print("Tutti gli esploratori sono stati sconfitti!")
        else:
            print("Il gruppo ha sconfitto il mostro!")
            risorse_guadagnate = random.randint(20, 100)
            self.risorse += risorse_guadagnate
            print(f"Guadagnate {risorse_guadagnate} risorse dal combattimento!")

    def evento_notturno(self):
        print("\nDurante la notte...")
        eventi = [
            ("tranquillo", "La notte passa tranquillamente."),
            ("entità", "Un'entità soprannaturale si aggira intorno al campo!"),
            ("anomalia", "Si verifica un'anomalia spazio-temporale. Alcuni oggetti scompaiono."),
            ("incubo", "I sopravvissuti sono tormentati da terribili incubi."),
            ("visione", "Alcuni sopravvissuti hanno visioni profetiche."),
            ("portale", "Un misterioso portale si apre brevemente nel campo.")
        ]
        evento, descrizione = random.choice(eventi)
        print(descrizione)

        if evento == "entità":
            self.combattimento()
        elif evento == "anomalia":
            perdita = random.randint(5, 20)
            self.risorse -= perdita
            print(f"Perse {perdita} risorse a causa dell'anomalia.")
        elif evento == "incubo":
            for s in self.sopravvissuti:
                s.resistenza = max(1, s.resistenza - 1)
            print("La resistenza di tutti i sopravvissuti è diminuita.")
        elif evento == "visione":
            sopravvissuto = random.choice(self.sopravvissuti)
            sopravvissuto.intelligenza += 1
            print(f"{sopravvissuto.nome} ha guadagnato 1 punto intelligenza.")
        elif evento == "portale":
            if random.random() < 0.5:
                risorse_trovate = random.randint(10, 50)
                self.risorse += risorse_trovate
                print(f"Dal portale emergono {risorse_trovate} risorse!")
            else:
                sopravvissuto = random.choice(self.sopravvissuti)
                self.sopravvissuti.remove(sopravvissuto)
                print(f"{sopravvissuto.nome} è stato risucchiato dal portale!")

    def combattimento(self):
        difensori = self.guardie + [s for s in self.sopravvissuti if s.abilita_speciale == "Combattimento"]
        if not difensori:
            print("Non ci sono difensori! Il campo subisce danni.")
            perdita = random.randint(20, 50)
            self.risorse -= perdita
            feriti = random.randint(1, 3)
            for _ in range(feriti):
                sopravvissuto = random.choice(self.sopravvissuti)
                sopravvissuto.resistenza = max(1, sopravvissuto.resistenza - 2)
            print(f"Perse {perdita} risorse e {feriti} sopravvissuti feriti.")
        else:
            forza_difesa = sum(d.forza for d in difensori)
            if random.randint(1, 100) < forza_difesa:
                print("I difensori respingono l'entità con successo!")
            else:
                print("L'entità riesce a causare alcuni danni prima di essere respinta.")
                perdita = random.randint(10, 30)
                self.risorse -= perdita
                print(f"Perse {perdita} risorse nel combattimento.")
def gestisci_personale(campo):
    while True:
        print("\nGestione Personale")
        print("1. Mostra lista sopravvissuti")
        print("2. Assegna compiti")
        print("3. Assegna guardia")
        print("4. Rimuovi guardia")
        print("5. Torna al menu principale")

        scelta = input("Seleziona un'azione (1-5): ")

        if scelta == "1":
            campo.mostra_sopravvissuti()
        elif scelta == "2":
            campo.mostra_sopravvissuti()
            indice = int(input("Seleziona il numero del sopravvissuto: ")) - 1
            print("Compiti disponibili: Raccolta Risorse, Ricerca, Manutenzione, Difesa")
            compito = input("Inserisci il compito da assegnare: ")
            campo.assegna_compito(indice, compito)
        elif scelta == "3":
            campo.mostra_sopravvissuti()
            indice = int(input("Seleziona il numero del sopravvissuto da assegnare come guardia: ")) - 1
            campo.assegna_guardia(indice)
        elif scelta == "4":
            campo.mostra_sopravvissuti()
            indice = int(input("Seleziona il numero del sopravvissuto da rimuovere dalle guardie: ")) - 1
            campo.rimuovi_guardia(indice)
        elif scelta == "5":
            break
        else:
            print("Scelta non valida.")
  
def passa_giorno(campo):
      campo.giorno += 1
      print("Passaggio al giorno successivo...")
      
      campo.esegui_compiti()
      campo.esplora()
      campo.evento_notturno()
      campo.aggiorna_guardie()
      
      # Effetto della Torre Radio
      nuovi_sopravvissuti = campo.strutture["Torre Radio"] * random.randint(0, 2)
      for _ in range(nuovi_sopravvissuti):
          if len(campo.sopravvissuti) < campo.capacita_massima:
              nuovo_sopravvissuto = Sopravvissuto(f"Nuovo_{campo.giorno}_{_}")
              campo.sopravvissuti.append(nuovo_sopravvissuto)
              print(f"Un nuovo sopravvissuto si è unito al campo: {nuovo_sopravvissuto.nome}")
          else:
              print("Il campo ha raggiunto la capacità massima. Nessun nuovo sopravvissuto può unirsi.")
              break
      
      # Produzione di risorse
      campo.risorse += campo.produzione_risorse
      print(f"Sono state prodotte {campo.produzione_risorse} risorse.")
      
      # Effetto dell'Infermeria
      if campo.strutture["Infermeria"] > 0:
          for sopravvissuto in campo.sopravvissuti:
              if sopravvissuto.salute < 100:
                  guarigione = min(campo.strutture["Infermeria"] * 10, 100 - sopravvissuto.salute)
                  sopravvissuto.salute += guarigione
                  print(f"{sopravvissuto.nome} ha recuperato {guarigione} punti salute nell'Infermeria.")
      
      # Effetto del Centro di Addestramento
      if campo.strutture["Centro di Addestramento"] > 0:
          for sopravvissuto in random.sample(campo.sopravvissuti, min(campo.strutture["Centro di Addestramento"], len(campo.sopravvissuti))):
              stat_to_improve = random.choice(["forza", "intelligenza", "agilita", "resistenza"])
              setattr(sopravvissuto, stat_to_improve, getattr(sopravvissuto, stat_to_improve) + 1)
              print(f"{sopravvissuto.nome} ha migliorato la sua {stat_to_improve} grazie al Centro di Addestramento.")
      
      # Effetto del Magazzino
      capacita_extra = campo.strutture["Magazzino"] * 50
      if campo.risorse > 100 + capacita_extra:
          risorse_perse = campo.risorse - (100 + capacita_extra)
          campo.risorse = 100 + capacita_extra
          print(f"A causa della limitata capacità di stoccaggio, {risorse_perse} risorse sono andate perse.")
  
def mostra_menu():
    print("\nMEG OMEGA 2.0 - Menu Azioni")
    print("1. Gestisci personale")
    print("2. Gestisci risorse")
    print("3. Esplorazione avanzata")
    print("4. Diplomazia")
    print("5. Passa al giorno successivo")
    print("6. Mostra stato del campo")
    print("7. Impostazioni effetti visivi")  # Nuova opzione
    print("8. Esci dal gioco")
def gestisci_risorse(campo):
      while True:
          print("\nGestione Risorse")
          print(f"Risorse disponibili: {campo.risorse}")
          print("1. Costruisci Torre Radio (Costo: 50 risorse)")
          print("2. Costruisci Abitazione (Costo: 30 risorse)")
          print("3. Costruisci Infermeria (Costo: 40 risorse)")
          print("4. Costruisci Officina (Costo: 60 risorse)")
          print("5. Costruisci Centro di Addestramento (Costo: 70 risorse)")
          print("6. Costruisci Magazzino (Costo: 45 risorse)")
          print("7. Torna al menu principale")
  
          scelta = input("Seleziona un'azione (1-7): ")
  
          costi = {
              "1": ("Torre Radio", 50),
              "2": ("Abitazioni", 30),
              "3": ("Infermeria", 40),
              "4": ("Officina", 60),
              "5": ("Centro di Addestramento", 70),
              "6": ("Magazzino", 45)
          }
  
          if scelta in costi:
              struttura, costo = costi[scelta]
              if campo.risorse >= costo:
                  campo.risorse -= costo
                  campo.strutture[struttura] += 1
                  print(f"{struttura} costruita!")
                  if struttura == "Abitazioni":
                      campo.capacita_massima += 5
                      print("La capacità massima del campo è aumentata.")
                  elif struttura == "Officina":
                      campo.produzione_risorse += 3
                      print("La produzione giornaliera di risorse è aumentata.")
              else:
                  print("Risorse insufficienti.")
          elif scelta == "7":
              break
          else:
              print("Scelta non valida.")
def carica_dlc():
    dlc_folder = 'dlc'
    dlc_modules = []
    
    if os.path.exists(dlc_folder):
        for filename in os.listdir(dlc_folder):
            if filename.endswith('.py'):
                module_name = filename[:-3]  # Rimuove '.py'
                try:
                    module = importlib.import_module(f'dlc.{module_name}')
                    dlc_modules.append(module)
                    print(f"DLC caricato: {module_name}")
                except ImportError as e:
                    print(f"Errore nel caricamento del DLC {module_name}: {e}")
    
    return dlc_modules  
def main():
    campo = CampoBase()
    dlc_modules = carica_dlc()
    
    # Inizializza i DLC
    for dlc in dlc_modules:
        if hasattr(dlc, 'inizializza_dlc'):
            dlc.inizializza_dlc(campo)
    
    # Applica i miglioramenti tecnici
    miglioramenti_tecnici.sostituisci_funzioni(campo)
    
    while True:
        if campo.usa_effetti_visivi:
            miglioramenti_tecnici.caricamento(messaggio="Aggiornamento stato del campo")
        campo.mostra_stato()
        mostra_menu()
        scelta = input("Seleziona un'azione (1-8): ")

        if scelta == "1":
            campo.gestisci_personale()
        elif scelta == "2":
            campo.gestisci_risorse()
        elif scelta == "3":
            for dlc in dlc_modules:
                if hasattr(dlc, 'menu_esplorazione'):
                    dlc.menu_esplorazione(campo)
                    break
        elif scelta == "4":
            for dlc in dlc_modules:
                if hasattr(dlc, 'menu_diplomazia'):
                    dlc.menu_diplomazia(campo)
                    break
        elif scelta == "5":
            campo.passa_giorno()
        elif scelta == "6":
            campo.mostra_stato()
        elif scelta == "7":
            miglioramenti_tecnici.menu_effetti_visivi(campo)
        elif scelta == "8":
            if campo.usa_effetti_visivi:
                miglioramenti_tecnici.stampa_lenta("Grazie per aver giocato a MEG OMEGA 2.0. Arrivederci!")
            else:
                print("Grazie per aver giocato a MEG OMEGA 2.0. Arrivederci!")
            break
        else:
            print("Opzione non valida. Per favore, scegli un numero tra 1 e 8.")

if __name__ == "__main__":
    main()
