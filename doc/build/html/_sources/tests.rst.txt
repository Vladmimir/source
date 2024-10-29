Tests Unitaires
===============

Cette section présente les tests unitaires pour vérifier le fonctionnement des différentes classes du projet.

Tests Unitaires de Voiture
---------------------------

Voici quelques tests unitaires pour la classe `Voiture` :

.. code-block:: python

   import unittest
   from voiture import Voiture

   class TestVoiture(unittest.TestCase):
       def test_initialisation(self):
           v = Voiture("Toyota", "Corolla")
           assert v.marque == "Toyota"
           assert v.modele == "Corolla"

       def test_demarrage(self):
           v = Voiture("Toyota", "Corolla")
           v.demarrer()
           assert v.en_marche is True
