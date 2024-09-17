import os
import subprocess
import time
import sys

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def loading_animation():
    animation = "|/-\\"
    for i in range(20):
        time.sleep(0.1)
        sys.stdout.write("\r" + "Caricamento " + animation[i % len(animation)])
        sys.stdout.flush()
    print("\nCaricamento completato!")
    time.sleep(1)

def run_program(program):
    try:
        subprocess.run(['python', program])
    except FileNotFoundError:
        print(f"Errore: Il file {program} non è stato trovato.")
    except Exception as e:
        print(f"Si è verificato un errore durante l'esecuzione di {program}: {e}")
    
    input("\nPremi Invio per tornare al menu precedente...")

def level_theta():
    while True:
        clear_screen()
        print("=== Level Θ ===")
        print("1. Esegui programma2.py")
        print("2. Esegui programma3.py")
        print("3. Torna a Lost Memories")
        
        choice = input("Seleziona un'opzione (1-3): ")
        
        if choice == '1':
            run_program('programma2.py')
        elif choice == '2':
            run_program('programma3.py')
        elif choice == '3':
            return
        else:
            print("Scelta non valida. Per favore, seleziona un'opzione tra 1 e 3.")
            input("Premi Invio per continuare...")

def lost_memories():
    while True:
        clear_screen()
        print("=== Lost Memories ===")
        print("1. Esegui inducedfear.py")
        print("2. Accedi a Level Θ")
        print("3. Esci")
        
        choice = input("Seleziona un'opzione (1-3): ")
        
        if choice == '1':
            run_program('inducedfear.py')
        elif choice == '2':
            level_theta()
        elif choice == '3':
            print("Grazie per aver usato il Sistema di Gestione Memorie. Arrivederci!")
            break
        else:
            print("Scelta non valida. Per favore, seleziona un'opzione tra 1 e 3.")
            input("Premi Invio per continuare...")

if __name__ == "__main__":
    clear_screen()
    print("Benvenuto nel Sistema di Gestione Memorie")
    loading_animation()
    lost_memories()
