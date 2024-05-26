# Speed Typing Test

This is a simple terminal-based speed typing test game built with Python's `curses` library. The game presents the user
with a random text to type and calculates the typing speed in words per minute (WPM).

## Features

- Randomly selects a text passage for typing from a file.
- Displays typing speed in WPM.
- Highlights correctly and incorrectly typed characters.
- Allows backspace to correct mistakes.
- Ends the test when the entire text is correctly typed.
- Provides an option to exit at any time by pressing the ESC key.

## Files

- `speed_typing_test.py`: The main Python script containing the game logic.
- `texts.txt`: A text file containing multiple lines of text passages, one of which will be randomly selected for each
  test.

## Requirements

- Python 3.x
- `curses` library (usually included with Python)

## How to Run

1. Ensure you have Python installed on your system.
2. Place the `speed_typing_test.py` and `texts.txt` files in the same directory.
3. Open a terminal and navigate to the directory containing the files.
4. Run the script using the following command:

```bash
python speed_typing_test.py
```

## How to Play

1. Run the script as described above.
2. You will be greeted with a welcome message. Press any key to begin or ESC to exit.
3. A random text passage will be displayed. Start typing the text.
4. Your typing speed in WPM will be displayed and updated as you type.
5. Correctly typed characters will be displayed in green, while incorrect characters will be displayed in red.
6. Use the backspace key to correct mistakes.
7. The test ends when you have correctly typed the entire text. A message will be displayed, prompting you to either
   continue with a new test or exit by pressing ESC.

## Code Overview

### Functions

- `start_screen(stdscr)`: Displays the welcome screen.
- `display_text(stdscr, target, current, wpm)`: Displays the target text, current text, and WPM.
- `load_text()`: Loads a random text passage from `texts.txt`.
- `wpm_test(stdscr)`: Runs the typing test, handling user input and calculating WPM.
- `main(stdscr)`: Initializes color pairs, displays the start screen, and controls the main loop of the game.

### Colors

- Green (`curses.color_pair(1)`): Correctly typed characters.
- Red (`curses.color_pair(2)`): Incorrectly typed characters.
- White (`curses.color_pair(3)`): Default text color (not used in the current implementation but initialized).

## Customization

You can customize the texts by editing the `texts.txt` file. Each line in the file represents a different text passage
that can be randomly selected for the typing test.

## Takeaways

- **Python Fundamentals**: This project reinforces basic Python skills, including file handling, string manipulation,
  and control structures.
- **[Third-Party Libraries](https://docs.python.org/3/howto/curses.html)**: Working with the `curses` library provided
  valuable experience in using third-party
  libraries to create text-based user interfaces.
- **Interactive Applications**: Developing this typing test helped in understanding how to create interactive terminal
  applications that respond to user input in real-time.

Feel free to contribute, suggest improvements, or report issues. Enjoy improving your typing speed!