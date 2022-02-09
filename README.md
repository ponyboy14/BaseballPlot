# Pitching Plot
## Overview
This project was created as a way to develop my skills in python and to learn different libraries like sqlite and matplotlib. This was also created because of my love for baseball and all the stats in the sport, so I wanted to create a way to help visualize certain stats.

## Objectives
1. Creating a plot of a strike zone where users can click where the pitch was.
2. Store the inputted point from the user into a .db file using sqlite3.
3. Be able to plot the points from the .db file onto the strike zone plot.

## Running the Code
At the beginning of the code, you will be presented with three options, enter the number next to that option to execute it.
1) Add Points
2) Plot Points
3) Exit
### Adding Points
After selecting to add Points, you can either add a player, select an existing player, or go to the previous page.
#### Add Player
- Now you will be prompted with three questions where you will need to input the player's college, first name, and last name.
- After entering the necessary information, you will then be prompted to select where the pitch was in the strike zone by clicking on the position on the displayed plot.
- Lastly, you will need to enter the number that is associated with the right pitch.
- You will then be returned to the adding points page.
#### Search for Player
- Now you will be asked to search for a player by first name, last name, college, or to display all saved players. You also have the option to go back to the previous page.
  - If first name, last name, or college is chosen, you will then be prompted enter which name or college you are searching for.
  - If Display all is chosen, all names in the database will be displayed.
 - Next, you will need to select the id of the player you want to display.
 - After entering the necessary information, you will then be prompted to select where the pitch was in the strike zone by clicking on the position on the displayed plot.
- Lastly, you will need to enter the number that is associated with the right pitch.
- You will then be returned to the adding points page.
### Plotting Points
- Firstly, you will be asked to search for a player by first name, last name, college, or to display all saved players. You also have the option to go back to the previous page.
  - If first name, last name, or college is chosen, you will then be prompted enter which name or college you are searching for.
  - If Display all is chosen, all names in the database will be displayed.
 - Next, you will need to select the id of the player you want to display.
 - The pitches should now be plotted on the strike zone.
 ### Exiting
 - Selecting this will end the program.
## Future Goals
- Tidy up the code with functions so there is not repition in the code.
- Add more comments to further explain what is going on.
- Expand to plotting other areas of the sport.
