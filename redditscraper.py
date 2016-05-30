import praw
import os
import urllib.request
from os import path,system,getenv

#change working directory
os.chdir('wallpaper')

#delete files that are older than a week
for i in os.listdir(os.getcwd()):
    created = datetime.fromtimestamp(path.getctime(i))
    weekAgo = datetime.now() - timedelta(days=7)
    if created < weekAgo:
        print ('file is older than a week' + i)
        os.remove(i)

r = praw.Reddit('Simple reddit scraper for /r/earthporn')

for submission in r.get_subreddit('NIotD').get_new(limit=200):
    extension = submission.url[-4:]
    if os.path.isfile(path.basename(submission.url)) == False:
        if extension == '.jpg' or extension == '.png' or extension == '.gif':
            print (submission.url)
            urllib.request.urlretrieve(submission.url, path.basename(submission.url))

for submission in r.get_subreddit('earthporn').get_new(limit=200):
    extension = submission.url[-4:]
    if os.path.isfile(path.basename(submission.url)) == False:
        if extension == '.jpg' or extension == '.png' or extension == '.gif':
            print (submission.url)
            urllib.request.urlretrieve(submission.url, path.basename(submission.url))
