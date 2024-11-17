import math

# Paramètres
n = 50  # Nombre d'essais
p = 0.34  # Probabilité de succès
threshold = 0.99  # Seuil de probabilité

def binomial_probability(n, k, p):
    """Calcule P(X = k) pour une loi binomiale."""
    comb = math.comb(n, k)
    return comb * (p**k) * ((1 - p)**(n - k))

def cumulative_range_probability(n, p, a, b):
    """Calcule P(a <= X <= b)."""
    return sum(binomial_probability(n, k, p) for k in range(a, b + 1))

# Recherche de (a, b)
min_range = None
result = None

for a in range(n + 1):
    for b in range(a, n + 1):
        prob = cumulative_range_probability(n, p, a, b)
        if prob >= threshold:
            if min_range is None or (b - a) < min_range:
                min_range = b - a
                result = (a, b)

print(result)