class voiture:
    """
    La classe voiture représente une voiture avec des propriétés de base.

    Attributs:
    ----------
    marque : str
        La marque de la voiture.
    modèle : str
        Le modèle de la voiture.
    annee : int
        L'année de fabrication de la voiture.

    Méthodes:
    ---------
    demarrer():
        Démarre la voiture.
    arreter():
        Arrête la voiture.
    """

    def __init__(self, marque, modèle, annee):
        """
        Initialise une nouvelle voiture.

        Paramètres:
        -----------
        marque : str
            La marque de la voiture.
        modèle : str
            Le modèle de la voiture.
        annee : int
            L'année de fabrication de la voiture.
        """
        self.marque = marque
        self.modèle = modèle
        self.annee = annee

    def demarrer(self):
        """Démarre la voiture."""
        print(f"La voiture {self.marque} {self.modèle} démarre.")

    def arreter(self):
        """Arrête la voiture."""
        print(f"La voiture {self.marque} {self.modèle} s'arrête.")


def entretien_voiture(voiture):
    """
    Effectue l'entretien de la voiture.

    Paramètres:
    -----------
    voiture : voiture
        Une instance de la classe voiture.

    Retourne:
    ---------
    str
        Un message confirmant que l'entretien est terminé.
    """
    return f"L'entretien de la {voiture.marque} {voiture.modèle} est terminé."



class moteur:
    """
    La classe moteur représente un moteur simple.

    Attributs:
    ----------
    puissance : int
        La puissance du moteur en chevaux.
    type : str
        Le type de moteur (électrique, diesel, essence).
    """

    def __init__(self, puissance, type_moteur):
        """
        Initialise un moteur.

        Paramètres:
        -----------
        puissance : int
            La puissance du moteur.
        type_moteur : str
            Le type de moteur (électrique, diesel, etc.).
        """
        self.puissance = puissance
        self.type_moteur = type_moteur

    def demarrer(self):
        """Démarre le moteur."""
        print(f"Le moteur de {self.puissance} chevaux démarre.")

    def arreter(self):
        """Arrête le moteur."""
        print("Le moteur s'arrête.")