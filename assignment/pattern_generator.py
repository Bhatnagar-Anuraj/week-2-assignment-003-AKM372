import maya.cmds as cmds

#Imports that sick data for computational power oooh yeahh
import math

# Clears the scene.
cmds.file(new=True, force=True)

#start of my sick function which creates a sick pattern with a bunch of loops
def sick_pattern_function():

    #defines the beautiful circle
    circle_objects = 10
    circle_radius = 8

    #creates the beautiful circle
    for i in range(circle_objects):
        angle = (2 * math.pi / circle_objects) * i
        pos_x = math.cos(angle) * circle_radius
        pos_z = math.sin(angle) * circle_radius
        cmds.polySphere(name=f"ball_{i}", r=0.5)
        cmds.move(pos_x, 0, pos_z, f"ball_{i}")


        #changes every other ball in the circle to be a little bigger
        if i % 2 == 0:
            cmds.scale(2,2,2,f"ball_{i}")
    
    #defines the grid
    num_rows = 5        # Number of rows in the grid
    num_cols = 5        # Number of columns in the grid
    spacing = 1.5       # Distance between cubes

    #nested loops that create the grid
    for row in range(num_rows):
        for col in range(num_cols):
            x_pos = (col * spacing) - 3 #centers new cubes to a grid in the middle of the circle
            y_pos = (row * spacing) - 3

            #makes a ball in the middle of the grid, otherwise makes a cube
            if row == 2 and col == 2:
                cmds.polySphere(name=f"cube_{row}{col}",r=0.5)
            else:
                cmds.polyCube(name=f"cube_{row}{col}", w=1, h=1, d=1)


            #moves everything into place
            cmds.move(x_pos, 0, y_pos,f"cube_{row}{col}")

            #adds some visual interest with more conditionals (!= instead of == to preserve middle ball)
            if (row + col) % 2 != 0:
                cmds.scale(1,3,1,f"cube_{row}{col}")
                
# Runs my function
sick_pattern_function()

# Frame everything in the viewport.
cmds.viewFit(allObjects=True)
print("Yep, there's now stuff. On the screen. Congrats.")
