# *************************************************************************** #
#                                                                             #
#                                                         :::      ::::::::   #
#   ft_garden_intro.py                                  :+:      :+:    :+:   #
#                                                     +:+ +:+         +:+     #
#   By: tde-alme <tde-alme@student.42porto.com>     +#+  +:+       +#+        #
#                                                 +#+#+#+#+#+   +#+           #
#   Created: 2026/07/30 14:14:15 by tde-alme           #+#    #+#             #
#   Updated: 2026/07/30 16:06:20 by tde-alme          ###   ########.fr       #
#                                                                             #
# *************************************************************************** #

#!/usr/bin/env python3

def ft_garden_intro(plant: str, height: int, age: int) -> None:
    plant_formated: str = plant.capitalize()

    print("=== Welcome to My Garden===")
    print(f"Plant: {plant_formated}")
    print(f"Height: {height}cm")
    print(f"Age: {age} days")


if __name__ == "__main__":
    ft_garden_intro("Rose", 25, 30)
