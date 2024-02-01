NAME = "mafonction"
ARGS = {'hello':'str', 'maListe':'list', 'monTuple':'tuple'}
DESCRIPTION = """Ceci est une fonction interressante"""

liste_arg = ", ".join(list(ARGS))
firstLine = f"def {NAME}({liste_arg}):"
print(firstLine)
print(f'\n\t"""{DESCRIPTION}')
print("\t- Args")
for i, e in enumerate(ARGS):
    print(f"\t\t {e} ({str(ARGS[e])})")
print('\t"""')