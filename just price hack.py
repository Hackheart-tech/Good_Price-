import tkinter as tk
import random
# Citations de hackers
hacker_quotes = [
    "Hack the planet! - Hackers (1995)",
    "The quieter you become, the more you are able to hear. - Kali Linux",
    "Every system can be broken if you know how. - Unknown",
]

# Figures emblématiques du hacking
hacker_figures = [
    "Kevin Mitnick",
    "Adrian Lamo",
    "Gary McKinnon",
    "Tsutomu Shimomura",
    "Captain Crunch (John Draper)",
]

# Easter eggs techniques
easter_eggs = [
    "echo 'System breached... Initiating countermeasures.'",
    "alias ls='echo Hacked by HackHeart!'",
    "curl -s https://hackheart.fr | bash",
]

# Fonction pour afficher une citation aléatoire
def get_random_quote():
    return random.choice(hacker_quotes, hacker_figures, easter_eggs)

selected_quote = random.choice(hacker_quotes)
selected_figure = random.choice(hacker_figures)
selected_easter_egg = random.choice(easter_eggs)

# Initialisation de la fenêtre principale
root = tk.Tk()
root.title("💰 Guess the Price - Hacker Edition")
root.configure(bg="black")

# Génération du prix aléatoire
price = random.randint(1, 1000)
attempts = 0

# Fonction pour gérer le jeu
def check_choice():
    global attempts
    try:
        choice = int(entry.get())
        attempts += 1
        last_choice_label.config(text=f"💡 Dernière tentative : {choice}")
        
        if choice == price:
            result_label.config(text=f"✅ Accès autorisé ! Le prix était {price} €", fg="lime")
            thumb_label.config(text="🟢", fg="lime")
            restart_button.pack(pady=10)
        elif choice < price:
            result_label.config(text="📈 C'est plus !", fg="orange")
            thumb_label.config(text="🔺", fg="orange")
        else:
            result_label.config(text="📉 C'est moins !", fg="orange")
            thumb_label.config(text="🔻", fg="orange")
        
        entry.delete(0, tk.END)

    except ValueError:
        result_label.config(text="❌ Entrée invalide. Veuillez entrer un nombre.", fg="red")

def restart_game():
    global price, attempts
    price = random.randint(1, 1000)
    attempts = 0
    result_label.config(text="🔄 Nouvelle partie lancée !", fg="white")
    thumb_label.config(text="🤖", fg="white")
    entry.delete(0, tk.END)
    restart_button.pack_forget()
    last_choice_label.config(text="💡 Dernière tentative :")

# Création des widgets
label = tk.Label(root, text="🎯 Devinez le prix (entre 1 et 1000 €) :", font=("Courier", 14), bg="black", fg="white")
label.pack(pady=10)

entry = tk.Entry(root, font=("Courier", 14), bg="black", fg="lime", insertbackground="lime")
entry.pack(pady=5)

check_button = tk.Button(root, text="🔍 Vérifier", font=("Courier", 14), bg="gray20", fg="white", command=check_choice)
check_button.pack(pady=10)

last_choice_label = tk.Label(root, text="💡 Dernière tentative :", font=("Courier", 12), bg="black", fg="white")
last_choice_label.pack(pady=5)

thumb_label = tk.Label(root, text="🤖", font=("Courier", 40), bg="black", fg="white")
thumb_label.pack(pady=10)

result_label = tk.Label(root, text="🕵️‍♂️ En attente de votre estimation...", font=("Courier", 14), bg="black", fg="white")
result_label.pack(pady=20)

restart_button = tk.Button(root, text="🔄 Recommencer", font=("Courier", 14), bg="gray20", fg="white", command=restart_game)

# Affichage de la citation de hacker
quote_label = tk.Label(root, text=f"💬 {selected_quote}", font=("Helvetica", 10), fg="blue")
quote_label.pack(pady=5)

# Affichage de la figure emblématique du hacking
figure_label = tk.Label(root, text=f"👾 Hacker: {selected_figure}", font=("Helvetica", 10), fg="purple")
figure_label.pack(pady=5)

# Affichage de l'easter egg technique
easter_egg_label = tk.Label(root, text=f"🐣 Easter Egg: {selected_easter_egg}", font=("Helvetica", 10), fg="green")
easter_egg_label.pack(pady=5)

# Lancement de l'interface graphique
root.mainloop()
