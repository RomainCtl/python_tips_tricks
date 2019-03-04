# Examples

## Equality

> See in file [equality.py](./equality.py)

## ArrayManipulator

> DB Relation manipulator

```python
personnes = [
    {"nom": 'Dupond', "prenom": 'Jean'},
    {"nom": 'Durand', "prenom": 'Pierre'},
    {"nom": 'Durand', "prenom": 'Pierre'},
    {"nom": 'toto', "prenom": 'Titi'},
    {"prenom": 'Jean', "nom": 'Dupond'}
]
ft1 = [
    {"nofour":"F3","noproduit":"P2","quantite":5},
    {"nofour":"F1","noproduit":"P1","quantite":1},
    {"nofour":"F1","noproduit":"P4","quantite":1},
    {"nofour":"F2","noproduit":"P4","quantite":1},
    {"nofour":"F1","noproduit":"P5","quantite":8},
    {"nofour":"F1","noproduit":"P6","quantite":2},
    {"nofour":"F2","noproduit":"P2","quantite":1},
    {"nofour":"F5","noproduit":"P3","quantite":10}
]
ft2 = [
    {"nofour":"F1","noproduit":"P6","quantite":2},
    {"nofour":"F2","noproduit":"P2","quantite":1},
    {"nofour":"F5","noproduit":"P3","quantite":10},
    {"nofour":"F3","noproduit":"P4","quantite":1},
    {"nofour":"F4","noproduit":"P4","quantite":2},
    {"nofour":"F4","noproduit":"P5","quantite":7},
    {"noproduit":"P1","nofour":"F1","quantite":1},
    {"nofour":"F4","noproduit":"P6","quantite":3}
]
fournisseurs = [
    {"nofour":"F1","nomf":"Bourhis","ville":"Paris"},
    {"nofour":"F2","nomf":"Bourhis","ville":"Paris"},
    {"nofour":"F4","nomf":"Bossuet","ville":"Dijon"},
    {"nofour":"F3","nomf":"Collet","ville":"Reims"},
    {"nofour":"F5","nomf":"Mercier","ville":"Riec"},
    {"nofour":"F6","nomf":"Tanguy","ville":"Lannion"}
]
produits = [
    {"noproduit":"P1","nomp":"Cassis","couleur":"Rouge","origine":"Dijon"},
    {"noproduit":"P2","nomp":"Champagne","couleur":"Blanc","origine":"Reims"},
    {"noproduit":"P5","nomp":"Salade","couleur":"Vert","origine":"Nice"},
    {"noproduit":"P3","nomp":"Huitre","couleur":"Vert","origine":"Riec"},
    {"noproduit":"P4","nomp":"Moutarde","couleur":"Jaune","origine":"Dijon"},
    {"noproduit":"P6","nomp":"Cornichon","couleur":"Vert","origine":"Dijon"},
    {"noproduit":"P7","nomp":"Muscadet","couleur":"Blanc","origine":"Nantes"}
]
fournitures = [
    {"nofour":"F3","noproduit":"P2","quantite":5},
    {"nofour":"F1","noproduit":"P1","quantite":1},
    {"nofour":"F1","noproduit":"P4","quantite":1},
    {"nofour":"F2","noproduit":"P4","quantite":1},
    {"nofour":"F1","noproduit":"P5","quantite":8},
    {"nofour":"F1","noproduit":"P6","quantite":2},
    {"nofour":"F2","noproduit":"P2","quantite":1},
    {"nofour":"F5","noproduit":"P3","quantite":10},
    {"nofour":"F3","noproduit":"P4","quantite":1},
    {"noproduit":"P4","nofour":"F4","quantite":2},
    {"nofour":"F4","noproduit":"P5","quantite":7},
    {"nofour":"F4","noproduit":"P6","quantite":3}
]

print("Unique : ",              ArrayManipulator.unique(personnes))
print("Union : ",               ArrayManipulator.union(ft1, ft2))
print("Intersect : ",           ArrayManipulator.intersect(ft1, ft2))
print("Minus : ",               ArrayManipulator.minus(ft1, ft2))
print("Project (or Select) : ", ArrayManipulator.project(ft1, ["nofour"]))
print("Where : ",               ArrayManipulator.where(ft1, lambda e: e["nofour"] == "F1"))
print("OrderBy : ",             ArrayManipulator.orderby(ft1, ["quantite", "nofour"]))
print("GroupBy : ",             ArrayManipulator.groupby(fournitures, ["nofour"], {"nbnoproduit": ArrayManipulator.count}))
print("Groupby : ",             ArrayManipulator.groupby(fournitures, ["nofour"], {"nbproduit": lambda t: ArrayManipulator.sum(t, "quantite")}))
print("Natural Join : ",        ArrayManipulator.natural_join(fournitures, produits))
print("Left Join : ",           ArrayManipulator.left_join(fournitures, produits, "noproduit", "noproduit"))
print("Right Join : ",          ArrayManipulator.right_join(fournitures, produits, "noproduit", "noproduit"))
print("Ful Join : ",            ArrayManipulator.full_join(fournitures, produits, "noproduit", "noproduit"))
```
