import time
import random
import sys

def typewriter_effect(text, delay=0.03):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()

def make_choice(options):
    while True:
        for i, option in enumerate(options, 1):
            print(f"{i}. {option}")
        choice = input("Fai la tua scelta: ")
        if choice.isdigit() and 1 <= int(choice) <= len(options):
            return int(choice)
        print("Scelta non valida. Riprova.")

def game_over(reason):
    typewriter_effect(f"\n{reason}")
    typewriter_effect("La tua coscienza si dissolve nell'eternità del Livello Θ.")
    typewriter_effect("Grazie per aver giocato. Ritorno al menu principale...")
    time.sleep(2)
    import menu  # Ritorna al menu principale

def sanity_check():
    global sanity
    sanity -= random.randint(5, 15)
    if sanity <= 0:
        game_over("La tua mente si frantuma sotto il peso dell'incomprensibile realtà del Livello Θ.")
        return False
    return True

def play_game():
    global sanity
    sanity = 100
    turns = 0
    inventory = []
    enigma_solved = False
    entity_awareness = 0

    typewriter_effect("Benvenuto nel Livello Θ dei Backrooms.")
    typewriter_effect("Ti ritrovi in un luogo al di là della comprensione umana, dove il tempo e lo spazio perdono significato.")
    typewriter_effect("Un senso di terrore primordiale ti pervade mentre realizzi di essere intrappolato in questo regno eterno.")
    
    while True:
        turns += 1
        if turns > 20 and random.random() < 0.1:
            game_over("Il tempo stesso si piega e ti consuma. La tua esistenza diventa parte del tessuto del Livello Θ.")
            return

        typewriter_effect(f"\nTurno {turns}. Sanità mentale: {sanity}")
        typewriter_effect("Cosa vuoi fare?")
        choice = make_choice([
            "Esplorare la galleria infinita",
            "Cercare una via di fuga impossibile",
            "Interagire con le statue viventi",
            "Decifrare gli enigmi cosmici",
            "Nasconderti dall'entità",
            "Confrontare l'entità"
        ])
        
        if not sanity_check():
            return

        if choice == 1:
            typewriter_effect("Ti addentri nella galleria infinita, circondata da un'oscurità palpabile.")
            event = random.choice([
                "Vedi figure contorte che sembrano muoversi quando non le guardi direttamente.",
                "Senti sussurri incomprensibili che sembrano provenire dalle pareti stesse.",
                "Un corridoio sembra ripetersi all'infinito, causandoti vertigini e nausea.",
                "Trovi un oggetto inquietante che sembra pulsare di vita propria."
            ])
            typewriter_effect(event)
            if "oggetto inquietante" in event:
                inventory.append("oggetto inquietante")
                typewriter_effect("Hai aggiunto l'oggetto inquietante al tuo inventario.")

        elif choice == 2:
            typewriter_effect("Cerchi disperatamente un'uscita, ma ogni porta si apre su un nuovo orrore.")
            event = random.choice([
                "Una porta si apre su un abisso infinito che minaccia di risucchiarti.",
                "Trovi una finestra che mostra un paesaggio alieno e impossibile.",
                "Un corridoio sembra portare alla libertà, ma si rivela essere un loop infinito.",
                "Una scala che scende sembra non avere fine, i gradini si moltiplicano mentre scendi."
            ])
            typewriter_effect(event)
            entity_awareness += 1

        elif choice == 3:
            typewriter_effect("Ti avvicini a una delle statue 'viventi', congelate nel tempo.")
            event = random.choice([
                "La statua sembra seguirti con gli occhi, anche se non si muove.",
                "Senti un grido silenzioso provenire dalla bocca immobile della statua.",
                "Toccando la statua, senti un fremito di vita impossibile al suo interno.",
                "La statua ti sussurra segreti cosmici che minacciano di far crollare la tua sanità."
            ])
            typewriter_effect(event)
            sanity -= random.randint(10, 20)

        elif choice == 4:
            typewriter_effect("Cerchi di decifrare gli enigmi cosmici scritti nelle pareti del Livello Θ.")
            if "oggetto inquietante" in inventory and random.random() < 0.3:
                typewriter_effect("L'oggetto inquietante nel tuo inventario reagisce agli enigmi!")
                typewriter_effect("Hai sbloccato un frammento di conoscenza proibita.")
                enigma_solved = True
            else:
                typewriter_effect("I simboli e le equazioni sembrano mutare mentre li osservi, sfuggendo alla comprensione.")
                sanity -= random.randint(15, 25)

        elif choice == 5:
            typewriter_effect("Cerchi di nasconderti dall'entità onnipresente del Livello Θ.")
            if random.random() < 0.7:
                typewriter_effect("Ti rannicchi in un angolo oscuro, sentendo la presenza dell'entità passare oltre.")
                entity_awareness -= 1 if entity_awareness > 0 else 0
            else:
                typewriter_effect("L'entità sembra essere ovunque. Non c'è nascondiglio sicuro in questo regno.")
                entity_awareness += 2

        elif choice == 6:
            typewriter_effect("Decidi di confrontare l'entità che governa questo luogo impossibile.")
            if enigma_solved and entity_awareness < 5 and random.random() < 0.1:
                typewriter_effect("Usando la conoscenza proibita, riesci a sfidare l'entità.")
                typewriter_effect("Per un momento, sembra che tu abbia una possibilità di sfuggire...")
                typewriter_effect("Ma l'entità ride, un suono che scuote le fondamenta della realtà.")
                typewriter_effect("'Nessuno sfugge al Livello Θ,' tuona la voce. 'Tu sei già parte di me.'")
                game_over("La tua esistenza viene assorbita nell'essere dell'entità, diventando parte della sua eterna galleria.")
                return
            else:
                typewriter_effect("L'entità si manifesta in tutta la sua terrificante gloria.")
                typewriter_effect("'Sono l'Alpha e l'Omega di questo luogo,' tuona. 'Tu sei solo un frammento nell'eternità.'")
                game_over("L'entità ti cancella dall'esistenza con un semplice pensiero.")
                return

        entity_awareness += random.randint(0, 2)
        if entity_awareness >= 10:
            game_over("L'entità diventa pienamente consapevole della tua presenza. Vieni assimilato nella sua collezione eterna.")
            return

if __name__ == "__main__":
    play_game()
