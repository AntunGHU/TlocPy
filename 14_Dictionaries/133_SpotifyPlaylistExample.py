playlist = {
    'title' : 'patagonia bus',
    'author' : 'Colt Steele',
    'songs' : [
        {'title':'song1', 'artist':['blue'], 'duration':2.5},
        {'title':'song2', 'artist':['kitty'], 'duration':3.5}
    ]
}

total_length = 0 # i for zahtjeva deklaraciju inace problem: NameError: name 'total_length' is not defined
for song in playlist['songs']:
    total_length += song['duration']
print(total_length)
