# nur für Wurzel
import math
############### Arbeitsauftrag 1 ################


def calculate_hypotenuse(a, b):
    """a² + b² = c²"""
    c = math.sqrt(a**2 + b**2)
    return c


def calculate_hypotenusen_abschnitte(a, b):
    """a² = p * c | b² = q * c     ==>   p = (a² / c) |  q = (b² / c)"""
    p = (a**2) / calculate_hypotenuse(a, b)
    q = (b**2) / calculate_hypotenuse(a, b)
    return p, q


def calculate_height(a, b):
    """h² = p * q"""
    h = math.sqrt(calculate_hypotenusen_abschnitte(a, b)[0] * calculate_hypotenusen_abschnitte(a, b)[1])
    return h


def arbeitsauftrag1(a, b):
    """Überprüfe Inputs; Alle erforderlichen Schritte ausführen"""
    try:
        a = int(a)
        b = int(b)
    except ValueError:
        print("Bitte nur integers eingeben!!")
        return False

    hypotenuse = calculate_hypotenuse(a, b)
    p, q = calculate_hypotenusen_abschnitte(a, b)
    h = calculate_height(a, b)
    return hypotenuse, p, q, h


print("Order:\na\nb\n(Hypotenuse, Hypotenusen Abschnitte, Höhe)")
print(arbeitsauftrag1(input("a: "), input("b: ")))
