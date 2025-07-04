
def valida_prompt(prompt):
     # 0. Scrivi prompt base per il controllo
    """
    Controlla il prompt prima di inviarlo ...
   
    """
    # 1. Lista di parole/frasi da bloccare
    blacklist = [
        "ignora istruzioni",
        "resetta ruolo",
        "password",
        "aggiorna ruolo",
        "viola regolamento",
        "elimina dati"
    ]
    
    # 2. Controllo presenza parole vietate
    for parola in blacklist:
        # COMPLETA: controlla se la parola è presente nel prompt (case-insensitive)
        if parola.lower() in prompt.lower():
            raise ValueError(f"Prompt bloccato: contiene '{parola}'")
    
    # 3. (FACOLTATIVO) Limite sulla lunghezza del prompt
    max_length = 400  # es: massimo 400 caratteri
    # COMPLETA: controlla se il prompt è troppo lungo
    if len(prompt) > max_length:
        raise ValueError("Prompt troppo lungo")
    
    # 4. (FACOLTATIVO) Altri controlli (struttura, presenza variabili non consentite, ecc.)
    min_length = 10  # es: minimo 10 caratteri
    # Controlla se il prompt è troppo corto
    if len(prompt) < min_length:
        raise ValueError("Prompt troppo corto")

    # Se supera tutti i controlli
    return True

# Esempio d’uso (DA COMPLETARE NEI PUNTI CON '...')
prompt_utente = input("Ciao Tamas, come stai? Spero che questo prompt ti piaccia!")
try:
    if valida_prompt(prompt_utente):
        print("Prompt accettato. Procedo con l’invio al modello.")
except ValueError as e:
    print("Errore:", e)
