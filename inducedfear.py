import random
import time
import sys
import os

class Player:
    def __init__(self):
        self.sanity = 100
        self.health = 100
        self.items = []
        self.explored_areas = set()
        self.skills = set()

def print_slow(text):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(0.02)
    print()

def make_choice(options):
    for i, option in enumerate(options, 1):
        print(f"{i}. {option}")
    while True:
        try:
            choice = int(input("Fai la tua scelta: "))
            if 1 <= choice <= len(options):
                return choice
            else:
                print("Scelta non valida. Riprova.")
        except ValueError:
            print("Per favore, inserisci un numero.")

def random_event(player):
    events = [
        ("Trovi una bottiglia d'acqua contaminata.", lambda: player.items.append("Bottiglia d'acqua contaminata")),
        ("Un'ombra ti sfiora, sussurrando segreti indicibili.", lambda: setattr(player, 'sanity', max(0, player.sanity - 15))),
        ("Vedi un riflesso distorto di te stesso che ti fissa.", lambda: setattr(player, 'sanity', max(0, player.sanity - 20))),
        ("Trovi un amuleto misterioso.", lambda: player.items.append("Amuleto misterioso")),
        ("Una voce familiare ti chiama, ma non c'è nessuno.", lambda: setattr(player, 'sanity', max(0, player.sanity - 10))),
        ("Inciampi e cadi, ferendoti.", lambda: setattr(player, 'health', max(0, player.health - 15))),
        ("Trovi un kit di pronto soccorso arrugginito.", lambda: player.items.append("Kit di pronto soccorso arrugginito")),
        ("Un'entità ti attacca all'improvviso!", entity_attack),
        ("Scopri un passaggio segreto.", discover_secret_passage),
        ("Trovi un libro antico con rituali oscuri.", lambda: player.items.append("Libro dei rituali"))
    ]
    event, action = random.choice(events)
    print_slow(event)
    action(player)

def entity_attack(player):
    damage = random.randint(10, 30)
    player.health = max(0, player.health - damage)
    player.sanity = max(0, player.sanity - damage)
    print_slow(f"L'entità ti ferisce! Perdi {damage} punti salute e sanità.")

def discover_secret_passage(player):
    if random.random() < 0.1:
        print_slow("Il passaggio sembra portare a un'uscita!")
        return "exit"
    else:
        print_slow("Il passaggio ti conduce in un'area ancora più inquietante.")
        player.sanity = max(0, player.sanity - 5)
    return "continue"

def use_item(player):
    if not player.items:
        print_slow("Non hai oggetti da usare.")
        return
    
    print_slow("Quale oggetto vuoi usare?")
    for i, item in enumerate(player.items, 1):
        print(f"{i}. {item}")
    print(f"{len(player.items) + 1}. Annulla")
    
    choice = make_choice(range(1, len(player.items) + 2))
    
    if choice == len(player.items) + 1:
        return
    
    item = player.items.pop(choice - 1)
    
    if item == "Bottiglia d'acqua contaminata":
        print_slow("Bevi l'acqua contaminata. Ti senti male.")
        player.health = max(0, player.health - 20)
    elif item == "Amuleto misterioso":
        if random.random() < 0.5:
            print_slow("L'amuleto brilla, proteggendoti da un pericolo imminente.")
            player.sanity = min(100, player.sanity + 15)
        else:
            print_slow("L'amuleto si anima e ti attacca!")
            player.health = max(0, player.health - 25)
    elif item == "Kit di pronto soccorso arrugginito":
        print_slow("Usi il kit. Recuperi un po' di salute, ma l'esperienza è dolorosa.")
        player.health = min(100, player.health + 30)
        player.sanity = max(0, player.sanity - 10)
    elif item == "Libro dei rituali":
        if "Conoscenza arcana" in player.skills:
            print_slow("Esegui un rituale di protezione. Ti senti più forte.")
            player.sanity = min(100, player.sanity + 20)
            player.health = min(100, player.health + 20)
        else:
            print_slow("Non riesci a comprendere il libro. La frustrazione ti logora.")
            player.sanity = max(0, player.sanity - 15)
    else:
        print_slow(f"Usi {item}, ma non succede nulla di particolare.")

def explore_area(player, area_name):
    if area_name in player.explored_areas:
        print_slow("Hai già esplorato quest'area, ma sembra completamente diversa ora.")
    else:
        player.explored_areas.add(area_name)
        print_slow(f"Esplori {area_name}. L'ambiente si contorce intorno a te.")
    
    result = random_event(player)
    if result == "exit":
        return "exit"
    
    options = [
        "Continua ad esplorare",
        "Cerca un'uscita",
        "Usa un oggetto",
        "Riposati (molto rischioso)",
        "Medita per recuperare sanità (rischioso)",
        "Cerca di imparare dall'ambiente"
    ]
    
    choice = make_choice(options)
    
    if choice == 1:
        return "explore"
    elif choice == 2:
        if random.random() < 0.05:
            return "exit"
        else:
            print_slow("Non trovi nessuna uscita. La disperazione cresce.")
            player.sanity = max(0, player.sanity - 10)
            return "explore"
    elif choice == 3:
        use_item(player)
    elif choice == 4:
        if random.random() < 0.7:
            print_slow("Mentre riposi, vieni attaccato da un'entità terrificante!")
            entity_attack(player)
        else:
            print_slow("Riesci a riposare un po'. Recuperi salute ma perdi lucidità.")
            player.health = min(100, player.health + 20)
            player.sanity = max(0, player.sanity - 15)
    elif choice == 5:
        if random.random() < 0.4:
            print_slow("La meditazione ti aiuta a ritrovare un po' di lucidità.")
            player.sanity = min(100, player.sanity + 15)
        else:
            print_slow("Durante la meditazione, vedi cose che non dovresti. La tua mente vacilla.")
            player.sanity = max(0, player.sanity - 25)
    elif choice == 6:
        if random.random() < 0.3:
            new_skill = random.choice(["Percezione acuta", "Conoscenza arcana", "Resistenza mentale"])
            if new_skill not in player.skills:
                player.skills.add(new_skill)
                print_slow(f"Hai imparato una nuova abilità: {new_skill}")
            else:
                print_slow("Non riesci a imparare nulla di nuovo.")
        else:
            print_slow("Il tentativo di comprendere questo luogo ti lascia confuso e spaventato.")
            player.sanity = max(0, player.sanity - 20)
    
    return "explore"

def game_over_sequence():
    print_slow("\nConnessione in corso con la realtà principale...")
    for i in range(101):
        sys.stdout.write(f"\rCaricamento: [{'#' * (i // 2)}{' ' * (50 - i // 2)}] {i}%")
        sys.stdout.flush()
        time.sleep(0.05)
    print("\n\nCaricamento completato. Ritorno al menu principale...")
    time.sleep(2)
    # In un'applicazione reale, qui chiameresti il menu principale
    print("Esecuzione di menu.py")
    sys.exit()

def induced_fear_game():
    player = Player()
    areas = ["Corridoio delle Ombre", "Stanza degli Specchi Infranti", "Labirinto di Carne Pulsante", 
             "Sala delle Illusioni Mortali", "Galleria dei Sussurri Impazziti", "Abisso della Disperazione"]
    
    print_slow("Benvenuto nel livello 'Induced Fear' delle Backrooms.")
    print_slow("Questo luogo si nutre delle tue paure. Sopravvivere è quasi impossibile.")
    
    while player.sanity > 0 and player.health > 0:
        current_area = random.choice(areas)
        result = explore_area(player, current_area)
        
        if result == "exit":
            if random.random() < 0.01:  # 1% di possibilità di vincere
                print_slow("Incredibilmente, hai trovato un'uscita reale! Riesci a fuggire dal livello 'Induced Fear'.")
                print_slow("Congratulazioni, hai vinto contro ogni probabilità!")
                return
            else:
                print_slow("Pensi di aver trovato un'uscita, ma era solo un'illusione crudele.")
                player.sanity = max(0, player.sanity - 30)
        
        print_slow(f"\nSalute: {player.health} | Sanità mentale: {player.sanity}")
        if player.items:
            print_slow(f"Oggetti: {', '.join(player.items)}")
        if player.skills:
            print_slow(f"Abilità: {', '.join(player.skills)}")
        
        if random.random() < 0.3:
            print_slow("\nUn'entità terrificante si materializza davanti a te!")
            options = ["Scappa", "Affrontala", "Cerca di comunicare", "Usa un'abilità (se ne hai)"]
            entity_choice = make_choice(options)
            if entity_choice == 1:
                if "Percezione acuta" in player.skills and random.random() < 0.6:
                    print_slow("Grazie alla tua percezione acuta, riesci a sfuggire all'entità senza subire danni.")
                else:
                    print_slow("Cerchi di scappare, ma l'entità ti raggiunge.")
                    entity_attack(player)
            elif entity_choice == 2:
                if "Resistenza mentale" in player.skills and random.random() < 0.5:
                    print_slow("La tua resistenza mentale ti permette di respingere l'entità!")
                    player.sanity = min(100, player.sanity + 10)
                else:
                    print_slow("Affronti l'entità, ma è troppo potente.")
                    entity_attack(player)
                    player.sanity = max(0, player.sanity - 20)
            elif entity_choice == 3:
                if "Conoscenza arcana" in player.skills and random.random() < 0.4:
                    print_slow("Usi la tua conoscenza arcana per comunicare con l'entità. Scompare senza attaccare.")
                else:
                    print_slow("Il tentativo di comunicazione fallisce. L'entità si infuria.")
                    entity_attack(player)
            elif entity_choice == 4 and player.skills:
                skill = random.choice(list(player.skills))
                print_slow(f"Usi la tua abilità {skill}.")
                if random.random() < 0.5:
                    print_slow("L'abilità ti aiuta a superare l'incontro.")
                else:
                    print_slow("L'abilità non è sufficiente. L'entità attacca.")
                    entity_attack(player)
    
    print_slow("\nLa tua mente o il tuo corpo cedono alle torture del livello 'Induced Fear'.")
    print_slow("Hai perso.")
    game_over_sequence()

if __name__ == "__main__":
    induced_fear_game()
