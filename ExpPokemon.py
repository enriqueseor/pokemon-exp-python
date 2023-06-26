# Calculadora Sistema Experiencia Pokemon
#https://bulbapedia.bulbagarden.net/wiki/Experience

def input_check(nivel):
    valid = False
    inrange = False
    while not valid:
        try:
            nivel = int(input('Nivel Pokemon: '))
            valid = True
        except ValueError:
            print('Esto no es un nivel')
        else:
            if nivel in range(2, 100):
                break
            else:
                print('Nivel fuera de Rango')
    return nivel


def rapido(nivel):
    e = 0.8 * nivel ** 3
    print("rapido    ", int(e))


def normal(nivel):
    e = nivel ** 3
    print("normal    ", int(e))


def lento(nivel):
    e = 1.25 * nivel ** 3
    print("lento     ", int(e))


def parabolico(nivel):
    e = 1.2 * nivel ** 3 - 15 * nivel ** 2 + 100 * nivel - 140
    print("parabolico", int(e))


def erratico(nivel):
    if 0 < nivel <= 50:
        e = (nivel ** 3 * (100 - nivel)) / 50
    elif 51 <= nivel <= 68:
        e = (nivel ** 3 * (150 - nivel)) / 100
    elif 69 <= nivel <= 98:
        e = (nivel ** 3 * ((1911 - 10 * nivel) / 3)) / 50
    else:
        e = (nivel ** 3 * (160 - nivel)) / 100
    print("erratico  ", int(e))


def fluctuante(nivel):
    if 0 < nivel <= 50:
        e = (nivel ** 3 * (24 + (nivel + 1) / 3)) / 50
    elif 51 <= nivel <= 68:
        e = (nivel ** 3 * (14 + nivel)) / 50
    else:
        e = (nivel ** 3 * (32 + (nivel / 2)) / 50)
    print("fluctuante", int(e))


def main(nivel=None):
    print("press 0 to exit")
    nivel = input_check(nivel)
    while nivel != 0:
        rapido(nivel)
        normal(nivel)
        lento(nivel)
        parabolico(nivel)
        erratico(nivel)
        fluctuante(nivel)
        nivel = input_check(nivel)
    print("FIN")

'''
if __name__ == "__main__":
    main()
'''