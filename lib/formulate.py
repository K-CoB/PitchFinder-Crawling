def note_to_midi(note):
    notes = {'C': 0, 'C#': 1, 'D': 2, 'D#': 3, 'E': 4, 'F': 5, 'F#': 6, 'G': 7, 'G#': 8, 'A': 9, 'A#': 10, 'B': 11}
    octave = int(note[-1])
    note_name = note[:-1]
    midi_note = octave * 12 + notes[note_name]
    return midi_note

def formulate_data(singer, song, highest_note, lowest_note, gender):
    song_data = {
        "title": song,
        "singer": singer,
        "high": note_to_midi(highest_note),
        "low": lowest_note(lowest_note),
        "gender": gender
    }
    return song_data