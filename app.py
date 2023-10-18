from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import pandas as pd


# URL of the YouTube Music site
url = "https://music.youtube.com/explore"

# Configure Chrome options to run in headless mode
chrome_options = Options()
chrome_options.add_argument("--headless")

# Create a Chrome webdriver with the specified options
driver = webdriver.Chrome(options=chrome_options)

# Navigate to the URL
driver.get(url)

# Wait for some time to ensure page content is loaded (you may need to adjust the time)
# This is important for dynamic pages that load content using JavaScript
# You can use WebDriverWait for better control over waiting for specific elements to load

# Find the song list container
song_list = driver.find_element(By.XPATH, '//*[@id="items"]')

# Find individual song elements
songs = song_list.find_elements(By.CLASS_NAME, 'style-scope ytmusic-responsive-list-item-renderer')

# Initialize lists to store song details
song_titles = []
artists = []
views = []

# Loop through the song elements and extract the desired information
for song in songs:
    title_element = song.find_element(By.CSS_SELECTOR, '.title.ytmusic-responsive-list-item-title')
    artist_element = song.find_element(By.CSS_SELECTOR, '.byline.style-scope ytmusic-responsive-list-item-renderer')
    view_element = song.find_element(By.CSS_SELECTOR, '.style-scope ytmusic-responsive-list-item-renderer')

    song_titles.append(title_element.text)
    artists.append(artist_element.text)
    views.append(view_element.text)

# Close the webdriver to release system resources
driver.quit()

# # Print the extracted song details
# for i in range(len(song_titles)):
#     print(f"Song: {song_titles[i]}")
#     print(f"Artist: {artists[i]}")
#     print(f"Views: {views[i]}")
#     print("\n")

dict = {'Artist': artists, 'Title': song_titles, 'Count': views,}
df = pd.DataFrame(dict)

df.to_csv('Youtube.csv', index = False)
