#to apply to 2 other playlists, just change playlist URIs (24-5) & playlist URI (ln 43) to new ones
#basic code taken from Kaylan https://www.youtube.com/watch?v=jSOrEmKUd_c
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import json

scope = 'playlist-modify-public'
username = 'nylx8bolt2w24k2fjh6wjm92h'

#create spotify object
auth_manager = SpotifyClientCredentials()
spotifyObject = spotipy.Spotify(auth_manager=auth_manager)

#create new playlist
#new_playlist():
#    playlist_name = input("This will be the playlist name:")
#    playlist_description = input("and the description:")
#    spotifyObject.user_playlist_create(user=username,name=playlist_name,public=True,description=playlist_description)

#create bittersweet playlist of songs that are on happy and sad playlists for a new vibe

#tracks.items[0] -for 1st song in playlist
#print(json.dumps(sad,sort_keys=4,indent=4)) -if printing remember to use
happy_songs = spotifyObject.playlist_tracks('1YLUWOWyESfPLBwtyUK42B')
sad_songs = spotifyObject.playlist_tracks('2SP5pKONqRObLNKl4joysK')
#print(json.dumps(happy_songs['items'][0]['track']['uri'],sort_keys=4,indent=4))
#print(json.dumps(sad_songs['items'][0]['track']['uri'],sort_keys=4,indent=4))
#limit is 100

#create lists of uris of happy and sad songs
happy_uris = []
sad_uris = []

#for track in playlist for t in 
#add uri to list
for i in range(len(sad_songs['items'])):
    sad_uris.append(sad_songs['items'][i]['track']['uri'])
#n=0
#for t in sad_songs:
#    for i in sad_songs['items'][n]:
#        sad_uris.append(sad_songs['items'][n]['track']['uri'])
#        n=n+1

#print('song uri appended:', sad_songs['items'][0]['track']['uri'])
#print('song uri appended:', sad_songs['items'][1]['track']['uri'])

for i in range(len(happy_songs['items'])):
    happy_uris.append(happy_songs['items'][i]['track']['uri'])

print('sad: ', json.dumps(sad_uris))
print('happy:', json.dumps(happy_uris))

#create list of bittersweet_URIs
bittersweet_URIs = []
for p in range(len(happy_uris)):
    if happy_uris[p] in sad_uris:
        bittersweet_URIs.append(happy_uris[p])
print('bittersweet uris= ', json.dumps(bittersweet_URIs,sort_keys=4,indent=4))

#add to bittersweet playlist
new_bittersweet_uris = []
for s in bittersweet_URIs:
    a_uri=s[14:]
    new_bittersweet_uris.append(a_uri)
print('bittersweet songs= ',json.dumps(new_bittersweet_uris,sort_keys=4,indent=4))
spotifyObject.playlist_add_items('6IYSxM621YyxpU59rvYKcA', new_bittersweet_uris)
