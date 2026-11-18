
from dataclasses import dataclass
import json


@dataclass(frozen=True, slots=True)
class Film:
    titre: str
    realisateur: str
    annee: int
    note: float
    def __lt__(self, autre):
        if not isinstance(autre, Film):
            return NotImplemented
        return self.note < autre.note
    def __post_init__(self):
        if not isinstance(self.titre, str) or not self.titre.strip():
            raise ValueError("Le titre est invalide.")

        if not isinstance(self.realisateur, str) or not self.realisateur.strip():
            raise ValueError("Le réalisateur est invalide.")

        if type(self.annee) is not int:
            raise TypeError("L'année doit être un entier.")

        if type(self.note) not in (int, float):
            raise TypeError("La note doit être numérique.")

        if not 0 <= self.note <= 10:
            raise ValueError("La note doit être entre 0 et 10.")

    def to_json(self):
        return json.dumps({
            "titre": self.titre,
            "realisateur": self.realisateur,
            "annee": self.annee,
            "note": self.note
        }, ensure_ascii=False)
        
    @classmethod
    def from_json(cls, chaine):
        donnees = json.loads(chaine)
        return cls(**donnees)


    def est_classique(self):
        return self.annee < 2000
