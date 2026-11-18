from dataclasses import dataclass, asdict
import json

@dataclass(frozen=True, slots=True)
class Livre:
    titre: str
    auteur: str
    annee: int
    prix: float

    def to_json(self):
        return json.dumps(asdict(self), ensure_ascii=False)
livre = Livre("1994", "verctor hugo", 1939, 9.90)
print(livre.to_json())