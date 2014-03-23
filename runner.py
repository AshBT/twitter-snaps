import os
import urllib
import cv2
import numpy as np
from TwitterAPI import TwitterAPI


api = TwitterAPI(
    os.environ['consumer_key'],
    os.environ['consumer_secret'],
    os.environ['access_token_key'],
    os.environ['access_token_secret']
)


def is_snap(img, verbose=False):
    """Baseline approach is to check for the presence of the timer in the upper right corner of the image"""
    templates = ["templates/%s.png" % i for i in range(1, 11)]
    scores = []

    for filename in templates:
        img = img.copy()
        template = cv2.imread(filename, 0)
        w, h = template.shape[::-1]
        res = cv2.matchTemplate(img, template, cv2.TM_CCOEFF_NORMED)

        min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)

        # Bounding rect of match
        top_left = max_loc
        bottom_right = (top_left[0] + w, top_left[1] + h)

        scores.append(max_val)

        if verbose:
            print "Attempting template %s" % filename
            print "Max value is %s" % max_val
            print "Rectangle is %s %s" % (top_left, bottom_right)

    return any([score >= .8 for score in scores])


def get_photo_stream():
    # Any geo-tagged tweet, don't have access to firehose :(
    r = api.request('statuses/filter', {'locations': '-180,-90,180,90'})

    for item in r.get_iterator():
        try:
            if 'media_url' in item['entities']['media'][0] and item['entities']['media'][0]['type'] == "photo":
                media_url = item['entities']['media'][0]['media_url']

                content = urllib.urlopen(media_url).read()
                img_array = np.asarray(bytearray(content), dtype=np.uint8)
                img = cv2.imdecode(img_array, 0)

                if img is not None and (img.shape[::-1] == (576, 1024) or img.shape[::-1] == (600, 900)):  # Compressed iPhone 4/5 sizes
                    if is_snap(img):
                        print media_url
        except KeyError:
            continue


if __name__ == "__main__":
    get_photo_stream()