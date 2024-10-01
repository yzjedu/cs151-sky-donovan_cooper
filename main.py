# Programmers:Donovan Raymond & Cooper Nazar
import math

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

# Constants
# set all constant variables to 0
height = 0
points_per_meter = 0
par = 0

# Data In:
# Prompt the user to give the hill type
# Prompt the user to give the type of hill and the jumper’s speed at the end of the ramp
hill_type = input('What is the hill type? (normal or large) ')
speed = input('What is the speed of the jumper at the end of the ramp? ')

# Decisions:
# create boolean for if ramp is normal, large, or otherwise
# set the variables for the constants for height, points_per_meter, par for the respective ramp types
# If ramp is not large or normal print error and use last else function or exit function
if hill_type == 'normal':
    height = 46
    points_per_meter = 2
    par = 90
elif hill_type == 'large':
    height = 70
    points_per_meter = 1.8
    par = 120
else:
    print('That hill type will not work!')

# Processing:
# do calculations to find the jumpers time_in_air (sqrt((2*height)/9.8))
# calculate the distance (speed * time in the air)
# calculate the amount of points gained (60 + (distance – par)*points_per_meter)
# Data Out:
# if distance is above 60 the print Great job for doing better than par!
# if distance is below 10 the print What happened?
# otherwise print Sorry you didn't go that far

air_time = int(math.sqrt((2*height)/9.8))
distance = int(speed * air_time)
points = 60 + (distance - par) * points_per_meter

print('Distance: ', distance)
print('Points: ', points)

if points > 60:
    print('Great job for doing better than par!')
elif points < 10:
    print('What happened?')
else:
    print('Sorry you did not go very far.')

# Credits:

