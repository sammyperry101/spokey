import pandas as pd

# Convert the key integer value to a note
def keyIntToNote(item : pd.DataFrame) -> pd.DataFrame:
    if item["key"] == 0:
        item["key"] = "C"
    elif item["key"] == 1:
        item["key"] = "C#/Db"
    elif item["key"] == 2:
        item["key"] = "D"
    elif item["key"] == 3:
        item["key"] = "D#/Eb"
    elif item["key"] == 4:
        item["key"] = "E"
    elif item["key"] == 5:
        item["key"] = "F"
    elif item["key"] == 6:
        item["key"] = "F#/Gb"
    elif item["key"] == 7:
        item["key"] = "G"
    elif item["key"] == 8:
        item["key"] = "G#/Ab"
    elif item["key"] == 9:
        item["key"] = "A"
    elif item["key"] == 10:
        item["key"] = "A#/Bb"
    elif item["key"] == 11:
        item["key"] = "B"

    return item

# Convert the key mode integer to major/minor
def modeIntToNote(item : pd.DataFrame) -> pd.DataFrame:
    if item["mode"] == 0:
        item["mode"] = "Minor"
    elif item["mode"] == 1:
        item["mode"] = "Major"

    return item