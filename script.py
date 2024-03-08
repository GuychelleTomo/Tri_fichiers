import datetime
import os


# Fonction pour vérifier si un fichier appartient à une année donnée
def est_fichier(dateFichier, annee)->bool:
    annee_fichier = int(datetime.datetime.strftime(dateFichier,"%Y"))
    if annee_fichier == annee:
        return True
    return False


# creetion d"un fonction pour recuperer le chemin d'acces des fichiers a trier

def est_fichier(dateFichier, annee)->bool:
    annee_fichier = int(datetime.datetime.strftime(dateFichier,"%Y"))
    if annee_fichier == annee:
        return True
    return False

# Fonction pour archiver les fichiers appartenant à une année donnée
def archiver_fichiers(directory, archive, annee):
    # Vérifier si le répertoire d'archivage existe, sinon le créer
    if not os.path.exists(archive):
        os.mkdir(archive)

    element = [] 
    for elem in os.listdir(directory):
        if os.path.isdir(os.path.join(directory, elem)):
            continue
        element.append(elem)

    liste_fichiers_annee = []
    # Parcourir les fichiers dans le répertoire donné
    for fichier in element:
        date_fichier_float = os.path.getctime(os.path.join(directory, fichier))
        date_fichier = datetime.datetime.utcfromtimestamp(date_fichier_float).date()
        # Vérifier si le fichier appartient à l'année spécifiée
        if est_fichier(date_fichier, annee):
            liste_fichiers_annee.append(fichier)

    # Pour archiver les fichiers dans le répertoire d'archivage
    for fichier in liste_fichiers_annee:
        os.rename(os.path.join(directory, fichier), os.path.join(archive, fichier))
        print(f"Fichier {fichier} archivé dans {archive}")


