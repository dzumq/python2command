## python2command
A simple Python script that converts your Python files into executable commands you can run from any directory. It adds a shebang line (#!/usr/bin/env python3), copies the file to /usr/local/bin without the .py extension, and sets execute permissions.
I am constantly creating scripts to automate tasks and I very much dislike having to type all of those commands manually (im lazy).

Figured I would share this simple script to help others out.

## Rundown
Takes user input for python file.
Adds shebang to your Python script (yes even if you already have one, sorry).
Copies the modified script to /usr/local/bin as an executable command (drops .py extension).
Sets execute permissions with chmod +x.
Displays a red ASCII art banner on run for coolness effect.

## Requirements
Just Python3

## Installation
```bash
git clone https://github.com/dzumq/python2command.git
```

## Usage
```bash
python3 python2command.py
```
When prompted, enter the full path to your target Python file (e.g., /path/to/your_script.py)

Thats it!!!
