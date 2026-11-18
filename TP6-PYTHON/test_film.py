from favoris import Favoris
import unittest
from Film import Film


class TestFilm(unittest.TestCase):

    def test_ajouter_favoris(self):
        favoris = Favoris()
        favoris.ajouter(self.film)

        self.assertEqual(len(favoris.films), 1)

    def test_favoris_to_json(self):
        favoris = Favoris()
        favoris.ajouter(self.film)

        resultat = favoris.to_json()

        self.assertIn("Inception", resultat)

    def test_favoris_from_json(self):
        favoris = Favoris()
        favoris.ajouter(self.film)

        chaine = favoris.to_json()
        nouveaux_favoris = Favoris.from_json(chaine)

        self.assertEqual(len(nouveaux_favoris.films), 1)
        self.assertEqual(
            nouveaux_favoris.films[0].titre,
            "Inception"
        )

    def test_favoris_objet_invalide(self):
        favoris = Favoris()

        with self.assertRaises(TypeError):
            favoris.ajouter("Inception")


    def setUp(self):
        self.film = Film("Inception", "Christopher Nolan", 2010, 8.8)

    def test_creation_film(self):
        self.assertEqual(self.film.titre, "Inception")
        self.assertEqual(self.film.realisateur, "Christopher Nolan")
        self.assertEqual(self.film.annee, 2010)
        self.assertEqual(self.film.note, 8.8)

    def test_est_classique(self):
        film = Film("Titanic", "James Cameron", 1997, 7.8)
        self.assertTrue(film.est_classique())

    def test_non_classique(self):
        self.assertFalse(self.film.est_classique())

    def test_note_invalide(self):
        with self.assertRaises(ValueError):
            Film("Film", "Realisateur", 2020, 12)

    def test_note_negative(self):
        with self.assertRaises(ValueError):
            Film("Film", "Realisateur", 2020, -2)

    def test_annee_invalide(self):
        with self.assertRaises(TypeError):
            Film("Film", "Realisateur", "2020", 8.5)

    def test_titre_vide(self):
        with self.assertRaises(ValueError):
            Film("", "Realisateur", 2020, 8.5)

    def test_immuabilite(self):
        with self.assertRaises(AttributeError):
            self.film.note = 9.5

    def test_to_json(self):
        resultat = self.film.to_json()
        self.assertIn("Inception", resultat)
        self.assertIn("Christopher Nolan", resultat)

    def test_from_json(self):
        chaine = self.film.to_json()
        film = Film.from_json(chaine)

        self.assertEqual(film.titre, self.film.titre)
        self.assertEqual(film.note, self.film.note)
    def test_comparaison_par_note(self):
        film1 = Film("Film A", "Realisateur A", 2000, 6.5)
        film2 = Film("Film B", "Realisateur B", 2020, 9.0)

        self.assertLess(film1, film2)
        self.assertGreater(film2, film1)

    def test_trier_films(self):
        films = [
            Film("Film A", "Real A", 2000, 8.5),
            Film("Film B", "Real B", 2001, 5.0),
            Film("Film C", "Real C", 2002, 9.5)
        ]

        films_tries = sorted(films)

        self.assertEqual(
            [f.note for f in films_tries],
            [5.0, 8.5, 9.5]
        )

if __name__ == "__main__":
    unittest.main()
