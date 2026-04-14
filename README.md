# Hungry Pig (Pygame Zero)

A small educational arcade game built with **Python** and **Pygame Zero**.
Control a pig, collect beetroot to score points, and survive as long as possible without leaving the screen.

![Hungry Pig gameplay](hungry_pig.gif)

## Tutorial

This repository accompanies my step-by-step tutorial:

https://edu.cs-htiew.pl/learning-by-games/python/pygame-zero/hungry-pig/

## What You Will Learn

- How to structure a simple Pygame Zero project
- How to use `Actor` objects, images, sounds, and fonts
- How to handle keyboard input and movement
- How to implement collision detection and scoring
- How to add game over and restart logic

## Gameplay

- Move the pig to collect beetroot.
- Each beetroot increases your score and movement speed.
- If you move outside the game area, it is game over.

## Controls

- `Arrow keys`: move pig
- `B`: toggle bot mode (auto movement toward beetroot)
- `Space`: restart after game over

## Requirements

- Python 3.10+ (3.11 recommended)
- Dependencies from `requirements.txt`

## Installation

```bash
pip install -r requirements.txt
```

## Run The Game

```bash
pgzrun main.py
```

## Build Executable (Optional)

The included `setup.bat` builds a Windows executable with PyInstaller:

```bat
setup.bat
```

## Project Structure

```text
.
|- main.py
|- requirements.txt
|- setup.bat
|- images/
|- sounds/
|- fonts/
```

## Assets And Credits

- https://kenney.nl/
- https://comigo.itch.io/farm-puzzle-animals
- https://www.zapsplat.com/music/pig-squeal-close-up/

## License

This project is distributed under the terms of the `LICENSE` file in this repository.
