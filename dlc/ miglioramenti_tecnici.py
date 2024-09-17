import time
import sys

def caricamento(durata=1, messaggio="Caricamento"):
    for _ in range(3):
        sys.stdout.write(f"\r{messaggio}" + "." * (_ + 1) + " " * (2 - _))
        sys.stdout.flush()
        time.sleep(durata / 3)
    print()

def stampa_lenta(messaggio, velocita=0.03):
    for carattere in messaggio:
        sys.stdout.write(carattere)
        sys.stdout.flush()
        time.sleep(velocita)
    print()

def inizializza_dlc(campo):
    print("DLC Miglioramenti Tecnici inizializzato!")
    campo.usa_effetti_visivi = True

def applica_caricamento(funzione):
    def wrapper(*args, **kwargs):
        caricamento(messaggio="Elaborazione in corso")
        risultato = funzione(*args, **kwargs)
        return risultato
    return wrapper

def visualizza_eventi_giornalieri(campo, eventi):
    print("\nRiepilogo degli eventi giornalieri:")
    for evento in eventi:
        stampa_lenta(f"- {evento}")
        time.sleep(0.5)

def passa_giorno_migliorato(campo):
    eventi = []
    
    caricamento(messaggio="Il giorno sta per finire")
    
    # Esegui le azioni giornaliere e raccogli gli eventi
    campo.giorno += 1
    eventi.append(f"Giorno {campo.giorno} iniziato.")
    
    campo.esegui_compiti()
    eventi.append("I compiti giornalieri sono stati completati.")
    
    risorse_prodotte = campo.produzione_risorse
    campo.risorse += risorse_prodotte
    eventi.append(f"Prodotte {risorse_prodotte} risorse.")
    
    # Esegui le azioni dei DLC
    for dlc in campo.dlc_modules:
        if hasattr(dlc, 'esegui_azioni_giornaliere'):
            eventi_dlc = dlc.esegui_azioni_giornaliere(campo)
            if eventi_dlc:
                eventi.extend(eventi_dlc)
    
    # Aggiorna le guardie
    campo.aggiorna_guardie()
    eventi.append("Le guardie hanno completato il loro turno.")
    
    # Esplora
    risultato_esplorazione = campo.esplora()
    if risultato_esplorazione:
        eventi.append(risultato_esplorazione)
    
    # Evento notturno
    evento_notturno = campo.evento_notturno()
    if evento_notturno:
        eventi.append(evento_notturno)
    
    # Visualizza gli eventi raccolti
    visualizza_eventi_giornalieri(campo, eventi)
    
    caricamento(messaggio="Preparazione per il nuovo giorno")

# Decoratori per le funzioni esistenti
@applica_caricamento
def gestisci_personale_migliorato(campo):
    # Implementazione esistente di gestisci_personale
    pass

@applica_caricamento
def gestisci_risorse_migliorato(campo):
    # Implementazione esistente di gestisci_risorse
    pass

@applica_caricamento
def esplorazione_migliorata(campo):
    # Implementazione esistente di esplorazione
    pass

@applica_caricamento
def diplomazia_migliorata(campo):
    # Implementazione esistente di diplomazia
    pass

def sostituisci_funzioni(campo):
    campo.gestisci_personale = gestisci_personale_migliorato
    campo.gestisci_risorse = gestisci_risorse_migliorato
    campo.esplora = esplorazione_migliorata
    campo.passa_giorno = passa_giorno_migliorato
    # Sostituisci altre funzioni se necessario

def menu_effetti_visivi(campo):
    while True:
        print("\nImpostazioni Effetti Visivi")
        print(f"1. {'Disattiva' if campo.usa_effetti_visivi else 'Attiva'} effetti visivi")
        print("2. Torna al menu principale")

        scelta = input("Seleziona un'opzione: ")
        if scelta == "1":
            campo.usa_effetti_visivi = not campo.usa_effetti_visivi
            print(f"Effetti visivi {'attivati' if campo.usa_effetti_visivi else 'disattivati'}.")
        elif scelta == "2":
            break
        else:
            print("Scelta non valida.")
