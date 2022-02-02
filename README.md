# PersonaAllEvents
A terrible Python script that generates flow and msg files that run every event it can find in Persona 5's files.

## How does it work?
It looks for **.PAK** files in Persona's events folder, copys the names of the **.PAK** files to a text file and then turns it into FlowScript. For .msg files it does the same thing again only this time it turns it into Message Script.

## What does the FlowScript do?
It runs the events it found in the order that it found them.

## Why did you make this?
I couldnt find a list of every event in the game. The only list I found was this incomplete one https://amicitia.miraheze.org/wiki/Event_(P5).

## How do I set a path to my events folder?
Modify the events_folder variable in both code.py and msg.py.

## What do I need to run the script?
https://www.python.org/ and a copy of Persona 5

## How do I compile the FlowScript?
https://github.com/tge-was-taken/Atlus-Script-Tools
