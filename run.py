import requests
from bs4 import BeautifulSoup
import pandas as pd

# URL of the YouTube Music site
url = "https://music.youtube.com/"

# Send a GET request to the URL
response = requests.get(url)

# Parse the HTML content using BeautifulSoup
soup = BeautifulSoup(response.content, "html.parser")

# Find the elements that contain the artist name, song title, and play count
# Adjust the CSS selectors according to the structure of the YouTube Music site
songs = soup.select("css-selector-for-songs")

Artists = []
Titles = []
Counts = []

# Iterate over the songs and extract the desired information
for song in songs:
    artist = song.select_one("css-selector-for-artist").text.strip()
    title = song.select_one("css-selector-for-title").text.strip()
    play_count = song.select_one("css-selector-for-play-count").text.strip()

    # Convert the play count to an integer
    play_count = int(play_count.replace(",", ""))

    # Filter songs with play count greater than 5,000
    if play_count > 5000:
        # print("Artist:", artist)
        # print("Title:", title)
        # print("Play Count:", play_count)
        # print("---")
        
        Artists.append(artist)
        Titles.append(title)
        Counts.append(play_count)

dict = {'Artist': Artists, 'Title': Titles, 'Count': Counts,}
df = pd.DataFrame(dict)

df.to_csv('Youtube.csv', index = False)