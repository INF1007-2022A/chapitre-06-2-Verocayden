#!/usr/bin/env python
# -*- coding: utf-8 -*-

from matplotlib.colors import cnames


def list_to_dict(some_list: list) -> dict:
    # TODO: Transformer la liste en dictionnaire, les éléments de la liste deviennent les clés et leur index deviennent les valeurs
    """
    dict = {}
    for element in some_list:
        dict[some_list.index(element)] = element  ### Ou: dict[some_list[element]] = element
    """
    # return {some_list.index(element): element for element in some_list} # Problème si la liste contient des doublons, car index() ne pourra pas fonctionner.
    return{element: index for index, element in enumerate(some_list)}


def color_name_to_hex(colors: list) -> list:
    # TODO: Trouver la valeur hex de chaque couleur dans la liste et créer une liste de tupple où le premier élément est le nom de la couleur et le deuxième est la valeur hex
    """
    colors_list = []
    for color in colors:
        colors_list.append((color, cnames[color]))
    """
    return [(color, cnames[color]) for color in colors]


def create_list() -> list:
    # TODO: Créer une liste des 10 000 premiers entiers positifs, sauf pour les entiers de 15 à 350
    nb_list = []
    count = 0
    while len(nb_list) < 10000:
        nb_list.append(count)
        count += 1
    nb_list = nb_list[0:15] + nb_list[351:-1]
    return nb_list
def compute_mse(model_dict: dict) -> dict:
    # TODO: Calculer l'erreur quadratique moyen pour chaque modèle. Retourner un dictionnaire contenant les MSE.
    mse = {}
    for key in model_dict:
        mse[key] = 0
        for value in model_dict[key]:
            mse[key] += (value[0]-value[1])**2
        mse[key] = round(mse[key]/(len(model_dict[key])), 2)
    return mse


def main() -> None:
    some_list = ["a", "b", "z", "patate"]
    print(f"La liste suivante {some_list} est transformée en dictionnaire: {list_to_dict(some_list)}")

    colors = ["blue", "red", "green", "yellow", "black", "white"]
    print(f"La valeur hex associée aux couleurs est: {color_name_to_hex(colors)}")

    print(f"La liste des 10000 entiers est: {create_list()}")

    model_dict = {"LR": [(90, 92), (96, 100), (20, 25), (21, -2), (3, -20)],
                  "DNN": [(100, 101), (50, 50), (1,2), (-10, -12), (-1, 7)],
                  "RF": [(10, 19), (56, 70), (1, 9), (-100, -12), (-11, 7)]}
    print(f"Le mse des différents modèles est: {compute_mse(model_dict)}")


if __name__ == '__main__':
    main()
