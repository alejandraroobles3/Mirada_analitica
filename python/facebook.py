import facebook_scraper as fs
import csv
from time import sleep

# get POST_ID from the URL of the post which can have the following structure:
# https://www.facebook.com/USER/posts/POST_ID
# https://www.facebook.com/groups/GROUP_ID/posts/POST_ID"

""" pos id ya usados
pfbid0f6ETDDpnuPT7qj49iiKvH1hzgSgWwpfk87wBUAheSXAnjbz2juGdw4UAq4jehLVTl
pfbid02vRCfmiU6Q8QPGnfdNJ1JPueKkD3vzNY9yXab4ATCDK2ncZW7phqbRbLkWAcfayzRl
"""

POST_ID ="pfbid0hsRiEMp9BGcjpjqUVqguURoXZez224WapgcyrzBkm3zrGBDhZL3ikb2zbzGLJEpxl"

# number of comments to download -- set this to True to download all comments
MAX_COMMENTS = 100

print(POST_ID)

# get the post (this gives a generator)
gen = fs.get_posts(
    post_urls=[POST_ID],
    options={"comments": MAX_COMMENTS, "progress": True}
)

# take 1st element of the generator which is the post we requested
post = next(gen)

# extract the comments part
comments = post['comments_full']

#file=open('claudia.csv',mode='a')

# process comments as you want...
coment_txt=[]
for comment in comments:
    
    print(comment['comment_text'])
    coment_txt.append(comment['comment_text'])

#print("este es el segundo comentario : \n",len(coment_txt))

with open('txt/xochitl.txt', 'a', encoding='utf-8') as file:
    for item in coment_txt:
        file.write(item+ '\n')

