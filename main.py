# Programmers:Donovan Raymond & Cooper Nazar

# Course:  Computer Sci through Programming (CS_151_05_06)
# Due Date: Oct 2,2024
# Lab Assignment: CS151 Lab3: Ski Jump

# Problem Statement:Winter is coming! One winter sport is the ski jump, where the score is determined by the distance /n
# traveled after skiing down a ramp and into the air.
# What type of speed does a ski jumper need to achieve on the ramp to make a good distance on their jump?
# Let’s make a program to calculate the distance traveled based on speed and determine how many points they’d /n
# receive if they went that distance.
# purpose : Given the type of ski jump and the jumper’s speed at the end of the ramp, predict how far they will jump \n
# and calculate the number of points they will earn

import math

# Describe the purpose of the program
print('This program uses the hill type and ski jumper speed to predict the distance of their jump and the points they'
      ' would earn for it.')

# Constants
# set all constant variables to 0
height = 0
points_per_meter = 0
par = 0

# Data In:
# Prompt the user to give the hill type
hill_type = input('What is the hill type? (normal or large) ')
hill_type = hill_type.lower().strip()

# Decisions:
# create a while loop to prompt the user to change the hill type if it is not normal or large
# create boolean for if ramp is normal or large
# set the variables for the constants for height, points_per_meter, par for the respective ramp types
while hill_type != 'normal' and hill_type != 'large':
    print('Sorry, that hill type will not work!')
    hill_type = input('What is the hill type? (normal or large) ')
    hill_type = hill_type.lower().strip()
if hill_type == 'normal':
        height = 46
        points_per_meter = 2
        par = 90
else:
        height = 70
        points_per_meter = 1.8
        par = 120

# Prompt the user to input the jumper's speed at the end of the ramp
speed = int(input('What is the speed of the jumper at the end of the ramp? '))

# Processing:
# do calculations to find the jumpers time_in_air (sqrt((2*height)/9.8))
air_time = int(math.sqrt((2*height)/9.8))

# calculate the distance (speed * time in the air)
distance = (speed * air_time)

# calculate the amount of points gained (60 + (distance – par)*points_per_meter)
points = 60 + (distance - par) * points_per_meter

# Data Out:
print('Distance: ', distance)
print('Points: ', points)

# if distance is above 60 the print Great job for doing better than par!
# if distance is below 10 the print What happened?
# otherwise print Sorry you didn't go that far
if points > 60:
    print('Great job for doing better than par!')
elif points < 10:
    print('What happened?')
else:
    print('Sorry you did not go very far.')

# Credits:

