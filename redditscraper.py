import praw
import os
import urllib.request
from os import path,system,getenv
from datetime import datetime, timedelta

#list to store the names of the subreddits to download from
reddits = []
reddits.append('earthporn') #picutes of earth / scenery
reddits.append('NIotD') #NASA image of the day

#check if the directory exists, if not then create it
directory = 'wallpaper'
if not os.path.exists(directory):
    os.makedirs(directory)

#change working directory
os.chdir('wallpaper')

#delete files that are older than a week
for i in os.listdir(os.getcwd()):
    created = datetime.fromtimestamp(path.getctime(i))
    weekAgo = datetime.now() - timedelta(days=7)
    if created < weekAgo:
        print ('file is older than a week' + i)
        os.remove(i)

r = praw.Reddit('Simple reddit scraper for reddit')
for i in range(len(reddits)):
    print (reddits[i])
    for submission in r.get_subreddit(reddits[i]).get_new(limit=10):
            extension = submission.url[-4:]
            if os.path.isfile(path.basename(submission.url)) == False:
                        if extension == '.jpg' or extension == '.png' or extension == '.gif':
                                        print (submission.url)
                                        urllib.request.urlretrieve(submission.url, path.basename(submission.url))
