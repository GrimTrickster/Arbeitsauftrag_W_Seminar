from math import sqrt
from math import acos


############### Arbeitsauftrag 2 ##############
def calculate_umfang(a, b, c):
    return a + b + c


def calculate_inhalt(a, b, c):
    """Satz des Heron"""
    s = calculate_umfang(a, b, c) / 2
    return sqrt(s * (s-a) * (s-b) * (s-c))


def calculate_winkel(a, b, c):
    alpha = acos((a**2 - b**2 - c**2) / (-1 * 2 * b * c))
    beta = acos(((a**2 - b**2 + c**2) / (2 * a * c)))
    gamma = acos((c**2 - a**2 - b**2) / (-2 * a * b))

    return alpha, beta, gamma


def arbeitsauftrag2(a, b, c):
    try:
        a = int(a)
        b = int(b)
        c = int(c)
    except ValueError:
        print("Bitte nur Integer eingeben.")
        return False

    umfang = calculate_umfang(a, b, c)
    inhalt = calculate_inhalt(a, b, c)
    alpha, beta, gamma = calculate_winkel(a, b, c)
    return umfang, inhalt, alpha, beta, gamma


print("Order:\nA\nB\nC\n(Umfang, Flächeninhalt, alpha, beta, gamma)\n\n")
print(arbeitsauftrag2(input("A: "), input("B: "), input("C: ")))
