from utils.utils import get_logger
from utils.validate import validate_data

logger = get_logger()


def note_to_midi(note):
    notes = {'C': 0, 'C♯': 1, 'D': 2, 'D♯': 3, 'E': 4, 'F': 5, 'F♯': 6, 'G': 7, 'G♯': 8, 'A': 9, 'A♯': 10, 'B': 11,
             'C#': 1, 'D#': 3, 'F#': 6, 'G#': 8, 'A#': 10, 'B#': 0, 'B♯': 0}
    octave = int(note[-1])
    note_name = note[:-1]
    try:
        midi_note = octave * 12 + notes[note_name]
    except KeyError:
        print("key error")
        print(note, octave, note_name, notes.get(note_name))
    return midi_note

def formulate_data(singer, song, highest_note, lowest_note, gender, youtube_url):
    song_data = {
        "title": validate_data(song),
        "singer": validate_data(singer),
        "high": note_to_midi(validate_data(highest_note)),
        "low": note_to_midi(validate_data(lowest_note)),
        "gender": gender,
        "youtube_url": youtube_url
    }
    return song_data