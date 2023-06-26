# Calculadora Sistema Experiencia Pokemon
# https://bulbapedia.bulbagarden.net/wiki/Experience

import tkinter as tk


def input_check():
    nivel = nivel_entry.get()
    try:
        nivel = int(nivel)
        if 2 <= nivel <= 100:
            return nivel
        else:
            raise ValueError
    except ValueError:
        error_label.config(text="Nivel fuera de rango")
        return None


def calculate():
    nivel = input_check()
    if nivel is not None:
        rapido(nivel)
        normal(nivel)
        lento(nivel)
        parabolico(nivel)
        erratico(nivel)
        fluctuante(nivel)


def rapido(nivel):
    e = 0.8 * nivel ** 3
    rapido_label.config(text="rapido: " + str(int(e)))


def normal(nivel):
    e = nivel ** 3
    normal_label.config(text="normal: " + str(int(e)))


def lento(nivel):
    e = 1.25 * nivel ** 3
    lento_label.config(text="lento: " + str(int(e)))


def parabolico(nivel):
    e = 1.2 * nivel ** 3 - 15 * nivel ** 2 + 100 * nivel - 140
    parabolico_label.config(text="parabolico: " + str(int(e)))


def erratico(nivel):
    if 0 < nivel <= 50:
        e = (nivel ** 3 * (100 - nivel)) / 50
    elif 51 <= nivel <= 68:
        e = (nivel ** 3 * (150 - nivel)) / 100
    elif 69 <= nivel <= 98:
        e = (nivel ** 3 * ((1911 - 10 * nivel) / 3)) / 50
    else:
        e = (nivel ** 3 * (160 - nivel)) / 100
    erratico_label.config(text="erratico: " + str(int(e)))


def fluctuante(nivel):
    if 0 < nivel <= 50:
        e = (nivel ** 3 * (24 + (nivel + 1) / 3)) / 50
    elif 51 <= nivel <= 68:
        e = (nivel ** 3 * (14 + nivel)) / 50
    else:
        e = (nivel ** 3 * (32 + (nivel / 2)) / 50)
    fluctuante_label.config(text="fluctuante: " + str(int(e)))


def main():
    global \
        nivel_entry, \
        error_label, \
        rapido_label, \
        normal_label, \
        lento_label, \
        parabolico_label, \
        erratico_label, \
        fluctuante_label

    # Create the main window
    window = tk.Tk()
    window.title("Calculadora Sistema Experiencia Pokemon")

    # Create and place the input elements
    nivel_label = tk.Label(window, text="Nivel Pokemon:")
    nivel_label.pack()
    nivel_entry = tk.Entry(window)
    nivel_entry.pack()

    # Create and place the error label
    error_label = tk.Label(window, text="")
    error_label.pack()

    # Create and place the calculate button
    calculate_button = tk.Button(window, text="Calcular", command=calculate)
    calculate_button.pack()

    # Create and place the result labels
    rapido_label = tk.Label(window, text="")
    rapido_label.pack()

    normal_label = tk.Label(window, text="")
    normal_label.pack()

    lento_label = tk.Label(window, text="")
    lento_label.pack()

    parabolico_label = tk.Label(window, text="")
    parabolico_label.pack()

    erratico_label = tk.Label(window, text="")
    erratico_label.pack()

    fluctuante_label = tk.Label(window, text="")
    fluctuante_label.pack()

    # Run the main loop
    window.mainloop()


if __name__ == "__main__":
    main()
