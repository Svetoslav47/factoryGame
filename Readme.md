# Factorio Clone in Pygame

This is a Factorio clone implemented using the Pygame library. The game features a custom-made grid and crafting system, with various functionalities such as ore generation, a main menu, crafting, automatic mining, and crafting.

## Installation

To run the game, you need to have Python installed on your system. Additionally, the following libraries are required:

- NumPy
- Pygame

You can install the required libraries using the following command:

```bash
pip install numpy pygame
```

## Usage

Once you have the required dependencies installed, you can run the game by executing the `main.py` file. The game will start with the main menu screen.

## Game Features

### Custom Grid and Crafting System

The game utilizes a custom-made grid system where you can place various items and structures. The grid allows for precise placement and organization of your factory.

The crafting system enables you to create new items by combining different resources according to specific recipes. Although the current version doesn't have a way to select recipes for the auto crafter, this functionality will be added in the future.

### Ore Generation

The game includes an ore generation mechanism that generates resources at random locations within the game world. You can mine these ores to collect resources and use them for crafting.

### Main Menu

The game starts with a main menu screen that provides options to start a new game, load a saved game, adjust settings, or exit the game.

### Automatic Miner and Crafter

The game features an automatic mining and crafting mechanism. You can set up automatic miners to mine resources without manual intervention. Additionally, the auto crafter can automatically create items based on predefined recipes.

## Code Explanation

The game consists of several Python files that implement different aspects of the game. Here is a brief explanation of each file:

- `player.py`: Contains the implementation of the player character.
- `grid.py`: Implements the custom grid system and related functionalities.
- `inventory.py`: Manages the player's inventory and item storage.
- `miner.py`: Implements the automatic mining functionality.
- `crafter.py`: Contains the implementation of the auto crafter.
- `playerhand.py`: Manages the player's hand and interactions with the game world.
- `playerhud.py`: Implements the player's heads-up display.
- `recipe.py`: Defines the recipe objects used for crafting.
- `item.py`: Contains the implementation of the item objects used in the game.
- `building.py`: Implements various structures and buildings in the game.

## Contributing

If you are interested in contributing to the game, feel free to fork the repository and submit pull requests with your changes. Contributions are always welcome!

## License

This project is licensed under the [MIT License](https://opensource.org/licenses/MIT). You are free to modify and distribute the game as per the terms of the license.

## Acknowledgements

This game is inspired by the popular game Factorio, developed by Wube Software. I would like to acknowledge their contribution and the inspiration they provided for this project.

## Contact

If you have any questions, suggestions, or feedback, please feel free to contact the project maintainer at [email protected]
