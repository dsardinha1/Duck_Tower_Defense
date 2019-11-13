# Duck_Tower_Defense
2D Arcade Tower Defense Game
By Davina Reis Sardinha

# About
This tower defense game is run on Python programming language and mainly powered by Arcade library. At the start, the player with be introduced to three different map style that can be choosen to start the game in. By clicking on the top right corner of the screen, the player will be greeted with a dropdown menu of four different tower types and one trap. The following towers are different based on range, damage, firing speed and cost to construct. Player will start off with around $500 Sacagaweas, or simply dollars, in order to buy small amount of towers that can be placed anywhere in the map. If the player doesn't have enough funds, then a prompt will show at the bottom of the screen stating "Can't afford that!". Main objective is to defeat all enemies spawn on the left side of the map as they move to the base place on the bottom right of the screen. Three different types of enemies will spawn through as the waves increment. Each enemy that collides with the base, the base health will reduce and the red rectangle gauge will deminish. Total amount of waves in each map is five waves with a ten second break in between to place additional towers. Once the five waves are completed, the game will restart with one of the other two maps that the player didn't select. All game interactions are involved with selection of the left mouse button.

# How-to Play
    Once the player has the tower meny active, the mouse can be dragged over each of the items to display damage each bullet deals, the firing radius of the selected tower and the cost to construct the tower. The only difference being the trap will display the reduction speed of each enemy as they make direct contact with the trap. The game will go on indefinetly as long as the base health doesn't reduce to zero!
    
# Missing Elements
    (Professor Only)
    The core requirements that the game supposed to contained are implemented, as well as the additional requirements for tower defense style game. Only small elements weren't included like:
    -   Once the base health reaches zero, display a game over to the player
    -   All traps and towers can be placed anywhere, missing the small path the prevents constructing a certain area to allow enemies to use the path
    -   Once towers are placed, they can't be removed until the a new map is loaded in
    -   Overuse of similar sounds for explosions and launch of the projectiles

# Core Issues
    Once the map is selected and game started, the game will have a high likelyhood of crashing at random because of an error displaying that either explosions or towers sprites buffer couldn't find the specific texture to load. Although, the game can be played while cyclinng through all three maps with no issue, however quite rare. (I have tried entensively to figure out why this issue arises, I don't know if arcade libraries AnimatedSpriteClasses have some inner issues with buffer size or something.)
