
import json
from Film import Film


class Favoris:

    def __init__(self):
        self.films = []

    def ajouter(self, film):
        if not isinstance(film, Film):
            raise TypeError("L'objet doit être un Film.")

        self.films.append(film)

    def to_json(self):
        return json.dumps(
            [json.loads(film.to_json()) for film in self.films],
            ensure_ascii=False,
            indent=4
        )

    @classmethod
    def from_json(cls, chaine):
        donnees = json.loads(chaine)

        favoris = cls()

        for film in donnees:
            favoris.ajouter(Film(**film))

        return favoris
