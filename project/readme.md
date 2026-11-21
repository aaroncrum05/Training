#Inventory Management - Finalized 11/21/2026


#### Video Demo: https://www.youtube.com/watch?v=AdU7tknJZKA

## Description:
In this project, I have created an inventory management system used to track tooling for my machine shop. Only certain users are able to access the system
and each user's login and actions are recorded in a seperate csv file.
The user can both add and remove tools from the system just like a standard tool crib management system.
Since csv files are hard to read, the user also has the option to output a pdf file that summarizes all of the inventory in a printable format.
Because this code could be downloaded into a computer that doesn't already have the appropriate csv inventory file, I have gone ahead and added a script right
at the top that will automatically create a dummy report csv file on their hard drive to get the ball rolling.

## Test File:
The test file reviews the login to ensure that other people outside of the 3 authorized people can login to the system.  Right now, only employees named Aaron, Brad, and Steve can login
and all others will be denied and taken out of the program. The test file also checks that the user inputs one of the valid 1-3 number choices when moving along the program to what they
want the program to do for them.  Finally, it tests to make sure the user cannot remove more tools from inventory than we have in stock. Obviously this wouldn't work in the real world
so it shouldn't work here either.

## Thoughts and considerations:
Since the last set of problems were regarding classes, and tools are real-world objects, I had actually started building this file using tools as classes and had a decent amount of work
completed before I realized that nothing was getting saved anywhere. When the file shut down and was reopened, all of my inventory changes would be lost forever so if I'm going to
use a similar system at my office, which is a machining warehouse, then we can't have our inventory get lost.  The only way I could think of permanently tracking inventory is with a csv
file that stays with the main file.  I had completed the script, then realized "what if someone tries to open this without the csv file" and realized that it would crash immediately.
So then I added in a section to automatically create a dummy csv file for the 'new user' of the python file.


TODO
