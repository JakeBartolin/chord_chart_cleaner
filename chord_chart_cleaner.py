import re
import sys

def print_welcome_message():
    welcome_message = """Starting TFT Script...

********************
* Text Format Tool *
********************

"""
    print(welcome_message)
    
    
def main():
    return

def get_text():
    
    print("Please paste your data below using Ctrl+Shift+V.\nWhen you are done, press Ctrl+D for Linux/Mac or Ctrl+Z for Windows.\n")
    lines = []
    try:
        lines = sys.stdin.readlines()
    except EOFError:
        pass
    return lines


def format_chord_chart_and_lyrics():
    print("Starting Extract Chords and Lyrics Subscript...\n")
    text = get_text()

    print("********************************\n*Your chords are printed below:*\n********************************\n")
    print(extract_chord_chart(text) + "\n\n")

    print("********************************\n*Your lyrics are printed below:*\n********************************\n")
    print(extract_lyrics(text))

def extract_chord_chart(text):
    output = ""

    for line in text:
        if line == "\n":
            continue
        else:
            output = output + line
            
    return output

def extract_lyrics(text):
    output = ""

    for line in text:
        space_count = 0

        if line == "\n":
            continue

        if line.startswith(" "):
            line = line.replace(" ", "", 1)
        
        for character in line:
            if character == " ":
                space_count += 1
        if space_count > (len(line) / 3):
            continue

        if line == "[Intro]":
            continue

        line = line.replace("[Chorus]", "## Chorus")
        line = line.replace("[Verse]", "## Verse")
        line = line.replace("[Bridge]", "## Bridge")
        line = line.replace("[Solo]", "## Solo")
        
        output += line
    
    print(output)
    return

main()
