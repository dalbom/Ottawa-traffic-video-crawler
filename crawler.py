import os
import time
import requests
from datetime import datetime

# Camera IDs are available at https://traffic.ottawa.ca/map/camera_list
CAM_IDS_OF_INTEREST = [1, 31, 101, 133, 169, 207, 275]

# Request a certiciate at https://traffic.ottawa.ca/ts/rsadmin/certificate.jsp
CERTIFICATE = 'Type your certificate here'

# The ID is an string value assigned by you to each user or instance of your application accessing the images.
# The ID must be alphanumeric characters [a-zA-Z0-9], and can be up to 16 characters in length.
USER_ID = 'Your own application ID number'

# Crawling interval in seconds
# A given ID for a given certificate must wait 1 minute between requests for the same camera.
# More frequent access may result in a certificate being revoked.
TIME_INTERVAL = 3600

# Set it -1 if you want to download the images indefinitely
N_OF_IMAGES = 10

image_count = 0

while image_count is not N_OF_IMAGES:
    start_time = time.time()
    timestamp = datetime.today().strftime('%Y%m%d-%H%M%S')
    
    for cam_id in CAM_IDS_OF_INTEREST:
        cam_id_str = str(cam_id)
        url = 'https://traffic.ottawa.ca/opendata/camera?c=' + cam_id_str + '&certificate=' + CERTIFICATE + '&id=' + USER_ID
        data = requests.get(url)
        open(os.path.join(cam_id_str.zfill(3) + '_' + timestamp + '.jpg'), 'wb').write(data.content)
    
    image_count += 1
    time.sleep(TIME_INTERVAL - (time.time() - start_time))
