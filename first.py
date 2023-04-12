import json

nom_fichier = "data.json"

lecons = []


def ajouter():
    while True:
        nom_lecon = input(
            "Entrez le nom de la leçon (ou 'exit' pour arrêter): ")
        if nom_lecon == "exit":
            break

        seances = {}
        while True:
            nom_seance = input(
                f"Entrez le nom de la séance pour la leçon '{nom_lecon}' (ou 'done' pour terminer la leçon): ")
            if nom_seance == "done":
                break

            seance_info = {}
            seance_info["date"] = input(
                f"Entrez la date de la séance '{nom_seance}': ")
            seance_info["sequence"] = input(
                f"Entrez la séquence pour la séance '{nom_seance}': ")
            seance_info["module"] = input(
                f"Entrez le module pour la séance '{nom_seance}': ")

            seances[nom_seance] = seance_info

        lecon_info = {}
        lecon_info[nom_lecon] = seances
        date_lecon = input("Entrez la date de cette lecon ")
        lecon_info[nom_lecon]["date"] = date_lecon

        with open(nom_fichier, 'r') as fichier:
            contenu = fichier.read()
            if contenu.strip():
                try:
                    donnees = json.load(fichier)
                except json.JSONDecodeError as e:
                    print("Failed to load JSON data from file.")
                    print("Error:", e)

            else:
                donnees = []

        donnees.append(lecon_info)

        with open(nom_fichier, 'w') as fichier:

            json.dump(donnees, fichier, indent=4)


ajouter()


def rechercher_nom():
    with open(nom_fichier, "r") as fichier:
        donnees = json.load(fichier)
    valeur_recherchee = input("Veuillez saisir le nom de lecon : ")
    for dictionnaire in donnees:
        if valeur_recherchee in dictionnaire.keys():
            print("Dictionnaire correspondant trouvé :")
            print(dictionnaire)
            break
    else:
        print("Aucun dictionnaire correspondant trouvé.")
    fichier.close()


def rechercher_date():
    with open(nom_fichier, "r") as fichier:
        donnees = json.load(fichier)
    valeur_recherchee = input("Veuillez saisir le nom de lecon : ")
    for dictionnaire in donnees.keys():
        if dictionnaire['date'] == valeur_recherchee:
            print("Dictionnaire correspondant trouvé :")
            print(dictionnaire)
            break
    else:
        print("Aucun dictionnaire correspondant trouvé.")
    fichier.close()


def supprimer():
    with open(nom_fichier, "r") as fichier:
        donnees = json.load(fichier)
    valeur_recherchee = input("Veuillez saisir le nom de lecon : ")
    for dictionnaire in donnees:
        if valeur_recherchee in dictionnaire.keys():
            donnees.pop(valeur_recherchee)
            break
    else:
        print("Aucun dictionnaire correspondant trouvé.")
    fichier.close()


while True:
    print("Taper le chiffre correspondant:")
    print("1. Ajouter une leçon ou activité")
    print("2. Rechercher une leçon selon le code de la leçon")
    print("3. Rechercher une leçon selon la date")
    print("4. Trier toutes les leçons selon la date (choisir l'un des algorithmes de tri)")
    print("5. Ajouter une remarque")
    print("6. Supprimer une leçon ou activité")
    print("7. Enregistrer")
    print("8. Quitter")

    choix = input("Entrez le numéro de votre choix: ")

    if choix == "1":
        # Ajouter une leçon ou activité
        ajouter()

    elif choix == "2":
        # Rechercher une leçon selon le code de la leçon
        rechercher_nom()

    elif choix == "3":
        # Rechercher une leçon selon la date
        rechercher_date()

    elif choix == "4":
        # Trier toutes les leçons selon la date (choisir l'un des algorithmes de tri)
        supprimer()

    elif choix == "5":
        # Quitter
        print("Au revoir!")
        break

    else:
        print("Choix invalide. Veuillez entrer un numéro entre 1 et 5.")
