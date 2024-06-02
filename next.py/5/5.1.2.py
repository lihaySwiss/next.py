import os
#i have a linux so i needed to be a lil creative to play the sound
#i used the sox library to play the sound

def main():
    freqs = {
        "la": 220,
        "si": 247,
        "do": 261,
        "re": 293,
        "mi": 329,
        "fa": 349,
        "sol": 392,
    }

    notes = "sol,250-mi,250-mi,500-fa,250-re,250-re,500-do,250-re,250-mi,250-fa,250-sol,250-sol,250-sol,500"
    note_list = notes.split("-")
    os.system("apt install sox")
    for note in note_list:
        note_parts = note.split(",")
        frequency = freqs[note_parts[0]]
        duration = int(note_parts[1])
        os.system('play -n synth %s sin %s' % (duration/1000, frequency))



if __name__ == '__main__':
    main()
