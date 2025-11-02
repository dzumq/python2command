import os
import shutil

def get_terminal_width():
    try:
        return shutil.get_terminal_size().columns
    except:
        return 80

def wrap_banner_lines(banner, width):
    wrapped = []
    for line in banner.splitlines():
        if len(line) <= width:
            wrapped.append(line)
        else:
            for i in range(0, len(line), width):
                wrapped.append(line[i:i+width])
    return '\n'.join(wrapped)

def center_text(text, width):
    return '\n'.join(line.center(width) for line in text.splitlines())

ascii_banner = r"""
              _   _                 ___                                               _ 
             | | | |               |__ \                                             | |
  _ __  _   _| |_| |__   ___  _ __    ) |___ ___  _ __ ___  _ __ ___   __ _ _ __   __| |
 | '_ \| | | | __| '_ \ / _ \| '_ \  / // __/ _ \| '_ ` _ \| '_ ` _ \ / _` | '_ \ / _` |
 | |_) | |_| | |_| | | | (_) | | | |/ /| (_| (_) | | | | | | | | | | | (_| | | | | (_| |
 | .__/ \__, |\__|_| |_|\___/|_| |_|____\___\___/|_| |_| |_|_| |_| |_|\__,_|_| |_|\__,_|
 | |     __/ |                                                                          
 |_|    |___/                                                                           
"""

width = get_terminal_width()
centered_banner = center_text(wrap_banner_lines(ascii_banner, width), width)
red_banner = "\033[31m" + centered_banner + "\033[0m"
print(red_banner)


credit = "\033[31m" + center_text("created by dzuma youtube.com/@dzumq", width) + "\033[0m"
print(credit + "\n")

filename = input('Enter the path of your Python file:')

interpretor = '#!/usr/bin/env python3'

with open(filename, 'r') as file:
    content = file.read()

with open(filename, 'w') as file:
    file.write(interpretor + '\n' + content)

basename = os.path.basename(filename)
name_without_ext, ext = os.path.splitext(basename)
os.system('sudo cp ' + filename + ' /usr/local/bin/' + name_without_ext)
os.system('sudo chmod +x /usr/local/bin/' + name_without_ext)
