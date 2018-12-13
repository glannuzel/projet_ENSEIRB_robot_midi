from mido import MidiFile

noteon = []
noteoff = []

mid = MidiFile('[Free-scores.com]_couperin-francois-le-petit-rien-45962.midi')
for i, track in enumerate(mid.tracks):
    #print('Track {}: {}'.format(i, track.name))
    for msg in track:
        if msg.type == 'note_on':
            noteon.append(msg.note)
print(noteon)