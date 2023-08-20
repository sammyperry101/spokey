# Convert the key integer value to a note
def keyIntToNote(item):
    if item["key"] == 0:
        item["key"] = "C"
    elif item["key"] == 1:
        item["key"] = "C#/D♭"
    elif item["key"] == 2:
        item["key"] = "D"
    elif item["key"] == 3:
        item["key"] = "D#/E♭"
    elif item["key"] == 4:
        item["key"] = "E"
    elif item["key"] == 5:
        item["key"] = "F"
    elif item["key"] == 6:
        item["key"] = "F#/G♭"
    elif item["key"] == 7:
        item["key"] = "G"
    elif item["key"] == 8:
        item["key"] = "G#/A♭"
    elif item["key"] == 9:
        item["key"] = "A"
    elif item["key"] == 10:
        item["key"] = "A#/B♭"
    elif item["key"] == 11:
        item["key"] = "B"

    return item

# Convert the key mode integer to major/minor
def modeIntToNote(item):
    if item["mode"] == 0:
        item["mode"] = "Minor"
    elif item["mode"] == 1:
        item["mode"] = "Major"

    return item