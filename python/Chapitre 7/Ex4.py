def separer_pair_impaire(liste):
    return [e for e in liste if not e%2], [e for e in liste if e%2]

print(separer_pair_impaire([i for i in range(100)]))