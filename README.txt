# Duck_Tower_Defense
Top-down Tower Defense Game
    - Implementing a* Algorithm
By Davina Reis Sardinha

# About
This tower defense game is run on Python programming language and mainly powered by Arcade library. At the start, the player with be introduced to three different map style that can be choosen to start the game in. By clicking on the top right corner of the screen, the player will be greeted with a dropdown menu of four different tower types and one trap. The following towers are different based on range, damage, firing speed and cost to construct. Player will start off with around $500 Sacagaweas, or simply dollars, in order to buy small amount of towers that can be placed anywhere in the map. If the player doesn't have enough funds, then a prompt will show at the bottom of the screen stating "Can't afford that!". Main objective is to defeat all enemies spawn on the left side of the map as they move to the base place on the bottom right of the screen. Three different types of enemies will spawn through as the waves increment. Each enemy that collides with the base, the base health will reduce and the red rectangle gauge will deminish. Total amount of waves in each map is five waves with a ten second break in between to place additional towers. Once the five waves are completed, the game will restart with one of the other two maps that the player didn't select. All game interactions are involved with selection of the left mouse button.
Update: Monsters will now move around the map based on the placement of towers and wall obstacles and purposely head towers the base. This is done through pathfinding aStar algorithm that rescans the map, everytime a tower is placed and creates a local finely grained graph to navigate.

# How-to Play
    Once the player has the tower many active, the mouse can be dragged over each of the items to display damage each bullet deals, the firing radius of the selected tower and the cost to construct the tower. The only difference being the trap will display the reduction speed of each enemy as they make direct contact with the trap. The game will go on indefinetly as long as the base health doesn't reduce to zero!
#Added
    - Game over screen
    - Finely grained navigation per enemy
    - Clears all towers and traps at the start of a new map
# Missing Elements
    - As the game scans the map for towers and objects, the finely grained graph lists nodes of these objects off by an index of x=1,y=1. However, the enemy's maneuver around towers, walls and collide with thre base each and everytime.

# Core Issues
    Once the map is selected and game started, the game will have a high chance of crashing at random because of an error displaying that either explosions or towers sprites buffer couldn't find the specific texture to load. Although, the game can be played while cycling through all three maps with no issue, however quite rare. (I have tried entensively to figure out why this issue arises, I don't know if arcade libraries AnimatedSpriteClasses have some inner issues with buffer size or something.)
