# Space Debris

**Project description:**  Welcome to Space Debris! Here you will get to test your grit in the cockpit of a state of the art, intersellar war machine!  The main objective is to clear all of the flying space rubble in the field of view which enters from both the left and right sides of the game window as well as the top and bottom. Fire projectiles at the incoming danger confetti to see it reduce in size. Keep shooting until it is all gone and do not forget to fire up the boosters if something gets a little too close for comfort.  If you are able to clear all of the space junk, you have cleared the level and will advance.  If an asteroid hits your ship then lights out and you lose a life.  Use caution, you only have three lives available to make it to the end of the game and each time you advance, so will the difficulty. To keep things interesting, your score for each game is displayed at the top left of the game screen.  Each time you play, try and beat your last score!  There is also a point multiplier displayed next to your score.  The more space rocks you remove without dying, the higher your multiplier will go.  Don't forget to chase down the green arrows that appear on the screen!  These are upgrades that will enhance your ship and weapons.  Have fun smashing rocks and trying to make it to the end!

## Requirements

 - 1. Python 3.2 or above
   3. Python Libraries:
      - Pygame
      - Typing
      - Random
      - Math
## System Design
```mermaid
---
title: Space Debris - Logical View
---
classDiagram 
 direction LR
 class spaceship {
  image_path: string
  x: int
  y: int
  screen_width: int
  screen_height: int 
  +__init__(self, image_path, x, y, screen_width, screen_height)
  +rotate(self)
  +update(self)
  +draw(self, screen)
}

 class title_screen {
  self
  text: str
  +__init__(self, text)
  +show(self, screen)
}

 class space_rubble {
  self
  +__init__(self)
  +get_speed(self)
  +increase_speed(self)
  +update(self)
  +hit(self)
}

 class bullet {
  self
  screen:
  x: int
  y: int
  angle: int
  speed: int
  color: list(int)
  size: int
  +__init__(self, screen, x, y, angle, speed, color, size)
  +update(self)
  +draw(self)
}

 class life_header {
  self
  screen:
  x: int
  y: int
  +__init__(self, screen, x, y)
  +get_lives(self)
  +remove_life(self)
  +draw(self)
}

 class game_level {
  self
  +__init__(self)
  +get_new_rubble(self)
  +get_max_rubble(self)
  +set_rubble_count(self)
  +next_level(self)
  +display_text(self)
}

 class explosion {
  self
  position: list(int, int)
  +__init__(self, position)
  +update(self)
}

 class score_calculator {
  self
  +__init__(self)
  +increase_score(self)
  +get_score(self)
  +get_multiplier(self)
  +increase_multiplier(self)
  +reset_multiplier(self)
}

 class main {
  self
  +__init__(self)
  +on_init(self)
  +on_event(self)
  +on_loop(self)
  +on_render(self)
  +on_cleanup(self)
  +on_execute(self)
}

 main o-- spaceship : has-a
 main --> space_rubble : uses-a
 main o-- title_screen : has-a
 main o-- life_header: has-a
 main o-- game_level: has-a
 main o-- explosion: has-a
 main o-- score_calculator: has-a
 spaceship o-- bullet : has-a
 game_level o-- space_rubble: has-a
```

## Logical Flow of the Game Loop
```mermaid
---
title: Game Loop Diagram
---
flowchart TD
    classDef green stroke:#0f0
    classDef red stroke:#f00
    classDef blue stroke:#00f

    A[Start] --> B["`Initialize Game:
                    _______________________
                     +Load Assets
                     +Initialize Variables
                     +Setup Display`"]
    B --> C{Is Running?}:::blue

    C --> |Yes| D["`Handle Events
                   _______________________
                    +Check for User Input`"]:::green
    D --> E["`Update Game State: 
             ____________________
              +Move Spaceship
              +Move Space Rubble
              +Check Collisions`"]:::green
    E --> F["`Render Frame:
             ____________________
              +Draw Background
              +Draw Spaceship
              +Draw Space Rubble`"]:::green
    F --> C

    C --> |No| G[Cleanup and Exit]:::red
    G --> H[End]:::red
```


## State Diagram
```mermaid
---
title: State Transition Diagram
---
stateDiagram-v2
  [*] --> Init
  Init --> Running: Initialization Complete
  Running --> Running: Process Events
  Running --> Running: Update Spaceship and Rubble
  Running --> Render: Render Frame
  Render --> Running: Continue Game Loop
  Running --> Cleanup: User Quits or Collision
  Cleanup --> [*]
```
     
## How to Use

To play the game, download the GitHub zip file or clone the repository.  Run the main.py file.  See **Game Controls** for player movement and action.

## How to test

To test, ensure that you have pytest installed using pip install pytest, then call python -m unittest discover tests

## Game Controls
- **Mouse** Select start, resume, and quit
- **Left Arrow:**  Rotate ship to the left
- **Right Arrow:** Rotate ship to the right
- **Up Arrow:** Move ship forward across game screen
- **z:** Fire bullets at asteroids
- **ESC** Opens pause menu

## Authors
Mark Meta\
Tyrek Blanks\
Andrew Vazzano\
Marcus Snell

