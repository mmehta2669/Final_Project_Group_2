# Space Debris

**Project description:**  Welcome to Space Debris! Here you will get to test your grit in the cockpit of a state of the art, intersellar war machine!  The main objective is to clear all of the flying space rubble in the field of view which enters from both the left and right sides of the game window. Fire projectiles at the incoming danger confetti to see it reduce in size. Keep shooting until it is all gone and do not forget to fire up the boosters if something gets a little too close for comfort.  If you are able to clear all of the space junk, you have cleared the level and will advance.  If an asteroid hits your ship then lights out and you lose a life.  Use caution, you only have three lives available to make it to the end of the game and each time you advance so will the difficulty.  Have fun smashing rocks and trying to make it to the end!

## Requirements

 - 1. Python 3.2 or above
   3. Python Libraries:
      - Pygame
      - Pickle
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
  +__init__(self)
}

 class space_rubble {
  self
  +__init__(self)
  +update(self)
}


 class background {
  image_file : string
  location : 
}

 class ammunition {
  self
  +__init__(self)
}

 class App {
  self
  +__init__(self)
  +on_init(self)
  +on_event(self)
  +on_loop(self)
  +on_render(self)
  +on_cleanup(self)
  +on_execute(self)
}

 App o-- spaceship : has-a
 App o-- space_rubble : has-a
 App o-- title_screen : has-a
 App o-- background : has-a
 spaceship o-- ammunition : has-a
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
     
## How to Use

To play the game, download the GitHub zip file or clone the repository.  Run the main.py file.  See **Game Controls** for player movement and action.

## Game Controls
- **Left Arrow:**  Rotate ship to the left
- **Right Arrow:** Rotate ship to the right
- **Up Arrow:** Move ship forward across game screen
- **Spacebar:** Fire bullets at asteroids

## Authors
Mark Meta\
Tyrek Blanks\
Andrew Vazzano\
Marcus Snell

