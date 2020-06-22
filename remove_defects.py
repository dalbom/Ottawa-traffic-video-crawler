'''
Naive heuristic codes to remove defective files
'''
import os
import cv2


filenames = sorted(os.listdir('collected'))

for filename in filenames:
    filepath = os.path.join('collected', filename)

    # Eliminate non-image files of size 14 bytes
    if os.path.getsize(filepath) < 1000:
        os.remove(filepath)
        continue

    img = cv2.imread(filepath)

    # To remove 'Camera Video Unavailable' images
    if (img[5,5,:] == [237,232,217]).all() and (img[-5,5,:] == [237,232,217]).all() and (img[5,-5,:] == [237,232,217]).all():
        os.remove(filepath)
        continue

    # To remove incomplete images causing 'Premature JPEG' error log
    if (img[-1,-25,:] == [128,128,128]).all() and (img[-1,-5,:] == [128,128,128]).all() and (img[-1,-55,:] == [128,128,128]).all():
        shutil.move(filepath, os.path.join('error', filename))
