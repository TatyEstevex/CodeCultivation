# *************************************************************************** #
#                                                                             #
#                                                         :::      ::::::::   #
#   ft_garden_intro.py                                  :+:      :+:    :+:   #
#                                                     +:+ +:+         +:+     #
#   By: tde-alme <tde-alme@student.42porto.com>     +#+  +:+       +#+        #
#                                                 +#+#+#+#+#+   +#+           #
#   Created: 2026/07/30 14:14:15 by tde-alme           #+#    #+#             #
#   Updated: 2026/09/03 14:17:13 by tde-alme          ###   ########.fr       #
#                                                                             #
# *************************************************************************** #

# !/usr/bin/env python3


def ft_garden_intro(name: str, height: int, age: int) -> None:
	plant_formated: str = name.capitalize()
	
	print("=== Welcome to My Garden ===")
	print(f"Plant: {plant_formated}")
	print(f"Height: {height}cm")
	print(f"Age: {age} days")

if __name__ == "__main__":
    ft_garden_intro("Rose", 25, 30)
