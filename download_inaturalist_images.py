"""
This script downloads all images associated with iNaturalist observation 
records. Observation data are exported from iNaturalist with iNaturalist
Export CSV functionality. For more details, see 
https://github.com/amdevine/ggi-gardens-photos

Required input: 
    - observations.csv

Outputs:
    - images folder containing downloaded jpg images
    - image_metadata.csv (image metadata for downloaded images)

Command line/terminal usage:
    python download_inaturalist_images.py
    (or python3 download_inaturalist_images.py)
"""

# Import the requisite Python libraries
import os, requests, time, urllib.request
import pandas as pd

# Read observations.csv and extract observation IDs
try:
    observations = pd.read_csv('observations.csv')
except FileNotFoundError:
    print("Could not find observations.csv. Program is now quitting.")
    exit()
obs_ids = list(observations['id'])

# For each observation, use the API to retrieve the associated image data
# original.jpg is not provided in the API metadata, but it does seem to work
# to get the original image size
print("Retrieving photo data for {} observations".format(len(obs_ids)))
images = []
for idno in obs_ids[10:20]:
    url = "https://www.inaturalist.org/observations/{}.json".format(idno)
    r = requests.get(url).json()
    photos = r.get('observation_photos', [])
    for photo in photos:
        photo_data = {'observation_id': photo.get('observation_id', None)}
        photo_data.update(photo.get('photo', {}))
        photo_data['original_size_url'] = photo_data.get('large_url', '').replace('large', 'original')
        images.append(photo_data)
    time.sleep(1) # Rate limit 1 request per second

# Export retrieved photo metadata as a CSV file
print("Data retrieved for {} photos. Exporting to image_metadata.csv".format(len(images)))
keep_columns = [
    'observation_id', 'id', 'created_at', 'updated_at', 
    'native_page_url', 'native_username', 'license', 'subtype', 
    'native_original_image_url', 
    'license_code', 'attribution', 'license_name', 'license_url', 
    'type', 'original_size_url'
]
rename_columns = {
    "id": "photo_id", 
    "native_page_url": "inaturalist_page_url",
    "native_username": "inaturalist_username", 
    "native_original_image_url": "original_image_url",
    "original_size_url": "image_url"
}
images_df = pd.DataFrame(images)
images_df = images_df[keep_columns]
images_df = images_df.rename(columns=rename_columns)
images_df.to_csv('image_metadata.csv', index=False)

# Create images directory
try:
    os.mkdir('images')
    print("Created images directory.")
except FileExistsError:
    print('Images directory already exists.')

# For every photo retrieved via the API, download the photo in its original 
# size to the images directory
image_counter = 0
print("Retrieving {} images".format(len(images)))
for image in images:
    obs_id = image.get('observation_id', 'Unknown')
    photo_id = image.get('id', 'Unknown')
    image_name = "images/observation{}_image{}.jpg".format(obs_id, photo_id)
    image_url = image.get('original_size_url', None)
    if image_url:
        urllib.request.urlretrieve(image_url, image_name)
    
    image_counter += 1
    if image_counter % 10 == 0:
        print("Retrieved {} of {} images".format(image_counter, len(images)))
    time.sleep(1) # Rate limit 1 request per second
print("Done, {} of {} images have been retrieved".format(len(images), len(images)))