import random

class MostroEstremo:
    def __init__(self, nome, descrizione, forza, abilita_speciale):
        self.nome = nome
        self.descrizione = descrizione
        self.forza = forza  # da 1 a 100
        self.abilita_speciale = abilita_speciale

    def __str__(self):
        return f"{self.nome} - Forza: {self.forza}"

class LivelloEstremo:
    def __init__(self, nome, descrizione, pericolo, effetti_speciali, mostro):
        self.nome = nome
        self.descrizione = descrizione
        self.pericolo = pericolo  # da 1 a 10
        self.effetti_speciali = effetti_speciali
        self.mostro = mostro

    def __str__(self):
        return f"{self.nome} - Pericolo: {self.pericolo}/10 - Mostro: {self.mostro.nome}"

class GestoreLivelliEstremi:
    def __init__(self):
        self.mostri = [
            MostroEstremo("La Bestia della Foresta Cremisi", "Una creatura fatta di rami contorti e foglie insanguinate", 85, "Illusioni mortali"),
            MostroEstremo("Il Leviatano dell'Abisso", "Un mostro marino gigantesco con tentacoli infiniti", 90, "Controllo dell'acqua"),
            MostroEstremo("Il Fantasma Elettrico", "Un'entità fatta di pura energia elettrica", 80, "Scariche elettriche devastanti"),
            MostroEstremo("La Manifestazione del Terrore", "Una creatura che cambia forma basata sulle tue paure peggiori", 95, "Terrore paralizzante"),
            MostroEstremo("L'Inseguitore Infinito", "Un essere che non smette mai di inseguirti, aumentando costantemente di velocità", 88, "Velocità sovrumana"),
            MostroEstremo("Il Colosso del Vuoto", "Un gigante fatto di oscurità e stelle morenti", 93, "Manipolazione della gravità"),
            MostroEstremo("Il Distorsore della Realtà", "Un'entità che distorce lo spazio e il tempo intorno a sé", 97, "Alterazione della realtà"),
            MostroEstremo("La Mente Alveare", "Una massa di creature interconnesse che agiscono come una singola entità", 87, "Attacchi coordinati"),
            MostroEstremo("L'Aberrazione Quantica", "Un mostro che esiste in più stati contemporaneamente", 92, "Teletrasporto quantistico"),
            MostroEstremo("L'Incarnazione dell'Eschaton", "L'incarnazione della fine di tutte le cose", 100, "Annichilimento cosmico")
        ]

        self.livelli = [
            LivelloEstremo("Livello ! (Corri per la tua vita)", 
                           "Un'infinita distesa di corridoi bui con una creatura che ti insegue costantemente.",
                           10, ["inseguimento_costante", "buio_totale"], self.mostri[4]),
            LivelloEstremo("Livello 6 (Luci Lampeggianti)", 
                           "Un labirinto di uffici con luci lampeggianti che causano disorientamento.",
                           8, ["disorientamento", "allucinazioni"], self.mostri[2]),
            LivelloEstremo("Livello 7 (Talassofobia)", 
                           "Un oceano infinito e buio con creature marine ostili.",
                           9, ["acqua_infinita", "creature_marine"], self.mostri[1]),
            LivelloEstremo("Livello 666 (La Foresta Cremisi)", 
                           "Una foresta di alberi rossi con entità ostili e illusioni mortali.",
                           9, ["illusioni", "entita_ostili"], self.mostri[0]),
            LivelloEstremo("Livello 974 (Il Seminterrato)", 
                           "Un seminterrato infinito con creature che si nutrono della paura.",
                           8, ["paura_crescente", "buio_parziale"], self.mostri[3]),
            LivelloEstremo("Livello ∞ (L'IKEA Infinito)", 
                           "Un negozio IKEA infinito con personale ostile e labirinti di mobili.",
                           7, ["labirinto_mutevole", "personale_ostile"], self.mostri[7]),
            LivelloEstremo("Livello -33 (L'Abisso)", 
                           "Un abisso infinito con piattaforme fluttuanti e creature volanti ostili.",
                           9, ["caduta_infinita", "creature_volanti"], self.mostri[5]),
            LivelloEstremo("Livello 1.5 (La Centrale Elettrica)", 
                           "Una stazione elettrica infinita con pericoli di elettrocuzione e entità fatte di elettricità.",
                           8, ["elettrocuzione", "entita_elettriche"], self.mostri[2]),
            LivelloEstremo("Livello 283 (Il Terrore)", 
                           "Un livello che si adatta alle tue paure peggiori, cambiando costantemente.",
                           10, ["paure_personalizzate", "cambiamento_costante"], self.mostri[8]),
            LivelloEstremo("Livello 3999 (Eschaton)", 
                           "Il livello finale, una realtà in decomposizione con pericoli incomprensibili.",
                           10, ["realta_instabile", "pericoli_cosmici"], self.mostri[9])
        ]
        self.livelli_sbloccati = []

    def sblocca_livello_casuale(self):
        livelli_non_sbloccati = [l for l in self.livelli if l not in self.livelli_sbloccati]
        if livelli_non_sbloccati:
            nuovo_livello = random.choice(livelli_non_sbloccati)
            self.livelli_sbloccati.append(nuovo_livello)
            return nuovo_livello
        return None

def inizializza_dlc(campo):
    print("DLC Livelli Estremi delle Backrooms inizializzato!")
    campo.gestore_livelli_estremi = GestoreLivelliEstremi()
    campo.gestore_livelli_estremi.sblocca_livello_casuale()  # Sblocca il primo livello

def esplora_livello_estremo(campo, livello):
    print(f"\nEsplorazione del {livello.nome}")
    print(livello.descrizione)
    print(f"Attenzione! In questo livello si aggira {livello.mostro.nome}!")
    print(livello.mostro.descrizione)
    
    squadra = seleziona_squadra(campo)
    if not squadra:
        return "Esplorazione annullata."

    print("\nLa squadra si avventura nel livello estremo...")
    for effetto in livello.effetti_speciali:
        applica_effetto_speciale(squadra, effetto)

    forza_squadra = sum(membro.forza + membro.agilita + membro.intelligenza for membro in squadra)
    probabilita_successo = max(0.1, min(0.9, (forza_squadra / 2 - livello.mostro.forza) / 100))

    if random.random() < probabilita_successo:
        ricompensa = livello.pericolo * 100
        campo.risorse += ricompensa
        for membro in squadra:
            membro.resistenza += 2
            membro.forza += 1
        return f"La squadra ha sconfitto {livello.mostro.nome} e è sopravvissuta al {livello.nome}! Guadagnate {ricompensa} risorse. La squadra ha aumentato resistenza e forza."
    else:
        perdite = random.randint(1, len(squadra))
        for _ in range(perdite):
            membro_perso = random.choice(squadra)
            campo.sopravvissuti.remove(membro_perso)
        return f"La squadra è stata sopraffatta da {livello.mostro.nome} nel {livello.nome}. {perdite} membri non sono tornati."

def applica_effetto_speciale(squadra, effetto):
    effetti = {
        "inseguimento_costante": "La squadra è costretta a correre senza sosta, esaurendo le energie.",
        "buio_totale": "L'oscurità completa rende impossibile orientarsi.",
        "disorientamento": "Le luci lampeggianti causano vertigini e confusione.",
        "allucinazioni": "I membri della squadra non riescono a distinguere la realtà dalle illusioni.",
        "acqua_infinita": "La pressione dell'acqua rende difficile il movimento e la respirazione.",
        "creature_marine": "Forme oscure nuotano intorno alla squadra, minacciando di attaccare.",
        "illusioni": "La realtà si distorce, creando pericoli immaginari ma letali.",
        "entita_ostili": "Creature aggressive attaccano la squadra senza preavviso.",
        "paura_crescente": "Un terrore irrazionale si impossessa della mente dei membri della squadra.",
        "labirinto_mutevole": "I corridoi cambiano continuamente, rendendo impossibile mappare il percorso.",
        "personale_ostile": "Figure umanoidi inseguono la squadra con intenti malvagi.",
        "caduta_infinita": "La sensazione di cadere nel vuoto destabilizza l'equilibrio della squadra.",
        "creature_volanti": "Esseri alati attaccano dall'alto, rendendo difficile la difesa.",
        "elettrocuzione": "Scariche elettriche casuali minacciano di colpire i membri della squadra.",
        "entita_elettriche": "Forme di vita fatte di pura energia elettrica si avvicinano minacciosamente.",
        "paure_personalizzate": "Ogni membro della squadra affronta le proprie paure peggiori.",
        "cambiamento_costante": "L'ambiente muta rapidamente, sfidando ogni logica e previsione.",
        "realta_instabile": "Le leggi della fisica sembrano non applicarsi, creando pericoli imprevedibili.",
        "pericoli_cosmici": "Fenomeni incomprensibili minacciano l'esistenza stessa della squadra."
    }
    print(effetti.get(effetto, "Un effetto sconosciuto colpisce la squadra."))
    for membro in squadra:
        membro.resistenza = max(1, membro.resistenza - 1)

def seleziona_squadra(campo):
    squadra = []
    print("\nSeleziona i membri della squadra per l'esplorazione (massimo 5):")
    while len(squadra) < 5:
        campo.mostra_sopravvissuti()
        scelta = input(f"Seleziona il sopravvissuto #{len(squadra)+1} (0 per terminare): ")
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

def menu_livelli_estremi(campo):
    while True:
        print("\nMenu Livelli Estremi delle Backrooms")
        for i, livello in enumerate(campo.gestore_livelli_estremi.livelli_sbloccati, 1):
            print(f"{i}. {livello}")
        print("0. Torna al menu principale")

        scelta = input("Seleziona un livello da esplorare (0 per tornare indietro): ")
        if scelta == "0":
            break

        try:
            indice = int(scelta) - 1
            if 0 <= indice < len(campo.gestore_livelli_estremi.livelli_sbloccati):
                livello = campo.gestore_livelli_estremi.livelli_sbloccati[indice]
                risultato = esplora_livello_estremo(campo, livello)
                print(risultato)
            else:
                print("Selezione non valida.")
        except ValueError:
            print("Inserisci un numero valido.")

def esegui_azioni_giornaliere(campo):
    if random.random() < 0.1:  # 10% di possibilità di sbloccare un nuovo livello ogni giorno
        nuovo_livello = campo.gestore_livelli_estremi.sblocca_livello_casuale()
        if nuovo_livello:
            return [f"Scoperto un nuovo livello estremo: {nuovo_livello.nome}!"]
    return []
