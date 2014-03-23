##Snapchat screenshots from Twitter Streaming API
###By [@jasdev](https://twitter.com/jasdev)
---

###Approach
Twitter has a lot of images. People tend to screencap Snapchats. Why don't we try to mine them? The approach taken in this repo is to fetch all get-tagged tweets in the world (don't have access to the firehose :( ). Then, if the tweet contains an image of the size of an iPhone 4/5 screen, we apply [template matching](http://opencv-python-tutroals.readthedocs.org/en/latest/py_tutorials/py_imgproc/py_template_matching/py_template_matching.html) to determine the presence or absence of the infamous 'timer' present in the upper tight of Snapchats (see image below for timer).

![alt text](http://i.imgur.com/0HUaqBG.png "Notice timer in upper right")

###Setup
You will need the following dependencies:


* OpenCV, `brew install homebrew/science/opencv`


* numpy, `pip install numpy`


* TwitterAPI, `pip install TwitterAPI`


Also, you will need to set the following environment variables from your Twitter dev accout:


* consumer_key
* consumer_secret
* access_token_key
* access_token_secret


To kickoff scraper, use `python runner.py`


URLs outputted from the script will be those that the template matcher detects as Snapchat screenshots


###Tests
run `nosetests test.py` in the root level of repo after installing needed dependencies