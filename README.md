# Water Sort Puzzle Game

This is a simple Water Sort Puzzle game implemented in Python using the Pygame library.

## Features

*   **Classic Water Sort Gameplay:** Experience the relaxing and engaging gameplay of the Water Sort Puzzle.
*   **Random Level Generation:** Each game starts with a randomly generated puzzle.
*   **Color Palette:** Features a variety of distinct colors for the water.
*   **Move Counter:** Tracks the number of moves you've made to solve the puzzle.
*   **Restart and New Game Options:** Easily restart the current puzzle or generate a new one.
*   **Timer:** Adds a challenge by tracking the time elapsed during gameplay.
*   **Collision Detection:**  Interactive elements like the clock are implemented using collision detection.
*   **Sound Effects:** Includes background music and a sound effect for pouring water.
*   **Win/Lose Condition:** Detects when the puzzle is solved or when the time runs out.
*   **Simple Graphics:** Clean and clear visual representation of the tubes and colored water.

## How to Play

1. **Run the game:** Execute the Python script.
2. **Select a tube:** Click on a tube to select the top color.
3. **Pour into another tube:** Click on another tube to pour the selected color into it, if possible (same color on top or empty tube).
4. **Solve the puzzle:**  Sort the colors so that each tube contains only one color.
5. **Restart:** Press the "Space" key to restart the current puzzle.
6. **New Game:** Press the "Enter" key to generate a new puzzle.
7. **Time Limit:** Be mindful of the clock! If it reaches the beaker icon, the game is over.

## Dependencies

Before running the game, make sure you have the following libraries installed:

*   **Pygame:** This library is used for the game's graphics, sound, and input handling.

    You can install Pygame using pip:

    ```bash
    pip install pygame
    ```

## How to Run the Game

1. **Save the code:** Save the provided Python code as a `.py` file (e.g., `water_sort.py`).
2. **Ensure resources are present:** Make sure you have the `images` and `sounds` folders in the same directory as your Python script, containing the following files:
    *   `images/bg.jpeg`
    *   `images/clock.png`
    *   `images/end.png`
    *   `sounds/bg.mp3`
    *   `sounds/water.wav`
    *   `sounds/over.wav`
    *   `fonts/font.otf`
3. **Run the script:** Open a terminal or command prompt, navigate to the directory where you saved the file, and run the script using Python:

    ```bash
    python water_sort.py
    ```

## Game Controls

*   **Mouse Click:** Select a tube and pour water.
*   **Spacebar:** Restart the current puzzle.
*   **Enter:** Start a new puzzle.

## Potential Issues

*   **Missing Resources:** The game relies on image, sound, and font files in the `images`, `sounds`, and the same directory as the script. Ensure these are present in the correct locations.
*   **Performance:** The game is generally lightweight, but older systems might experience minor performance issues.
*   **Screen Resolution:** The game window has a defined size. It might not adapt perfectly to all screen resolutions.

## Credits

This game was developed as a personal project. It utilizes the Pygame library, which is developed and maintained by the Pygame community.

## License

This project is open-source and available under the [MIT License](LICENSE.txt). (You may want to create a `LICENSE.txt` file if you choose to use a specific license).

Have fun sorting!
