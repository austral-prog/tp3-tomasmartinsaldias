def check_vowels():
    nombre = input("Ingrese un nombre: ")
    a = "a" in nombre or "A" in nombre
    e = "e" in nombre or "E" in nombre
    i = "i" in nombre or "I" in nombre
    o = "o" in nombre or "O" in nombre
    u = "u" in nombre or "U" in nombre
    print("Contiene a:", a)
    print("Contiene e:", e)
    print("Contiene i:", i)
    print("Contiene o:", o)
    print("Contiene u:", u)
