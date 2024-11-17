import math

def loi_binomiale(n, k, p):
    # Calcul de la probabilité binomiale P(X = k)
    comb = math.comb(n, k)
    return comb * (p**k) * ((1 - p)**(n - k))

def proba_somme(n, p, x_min):
    # Calcul de P(X >= x_min) = 1 - P(X < x_min)
    cumulative = sum(loi_binomiale(n, k, p) for k in range(x_min))
    return 1 - cumulative

def proba_somme_rang(n, p, a, b):
    # Calcul de P(a <= X <= b)
    return sum(loi_binomiale(n, k, p) for k in range(a, b + 1))

class BoiteAOutils:
    def __init__(self):
        pass

    def trouve_n(self, pr, result, k):
        n = 1
        while True:
            prob = proba_somme(n, pr, k)
            if prob >= result:
                break
            n += 1
        return n

    def trouve_bornes(self, threshold, n, p):
        # Recherche de (a, b)
        min_range = None
        result = None

        for a in range(n + 1):
            for b in range(a, n + 1):
                prob = proba_somme_rang(n, p, a, b)
                if prob >= threshold:
                    if min_range is None or (b - a) < min_range:
                        min_range = b - a
                        result = (a, b)
        return result

# Test de la classe
boite = BoiteAOutils()
print(boite.trouve_n(0.04, 0.864, 4))

print("Choisir une option : \n - 1 : Trouver un n \n - 2 : Trouver des bornes")
choice = int(input())

if choice == 1:
    p = float(input("p : "))
    k = int(input("k : "))
    resultat = float(input("résultat :"))
    print(boite.trouve_n(p,resultat,k))
else:
    p = float(input("p : "))
    n = int(input("n : "))
    resultat = float(input("résultat :"))
    print(boite.trouve_bornes(resultat, n, p))