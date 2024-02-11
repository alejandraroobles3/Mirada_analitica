import facebook_scraper as fs
import csv
from time import sleep

# get POST_ID from the URL of the post which can have the following structure:
# https://www.facebook.com/USER/posts/POST_ID
# https://www.facebook.com/groups/GROUP_ID/posts/POST_ID"

""" pos id ya usados
jorge alvarez
pfbid02yNj42rVbfsyPPCAJeeySPjQFrva59Twrefi5QE2k6ghzVG6nM9PmqSExNDBMxf1Jl 350
pfbid02q3MvJcPzsToN5YnVDHoTQCeT2y9SUCW19TYYmgcdueFhsjSA8Bh8EoC4RJD5WXnYl 200
pfbid02YccUiY69msMNMCKmjM6LfWSiWQzcTKsPgEHyPSsUXzwzSantjDdjKiD9pAJWcq1il 50
pfbid02XNCuvAhaGM3YNMGQwtRHVHi97MAxm8v7cyV55kDFWguurXK9zEKCm8fos3FEPAs4l 90
pfbid02sBXtZ3XkRYu41zSpdhVUNaDbqcuWVNKydZUWobHw1XaoLoV8efHweRkVoEj7fiSLl 200
pfbid02cme414RrXFW29JonLvHpNTFgD5dDTxuvWjjupYb87boryWUTLPgv9To5XrPEdGQsl 79
pfbid022iNj4U9YCANTo86rQP5GVsitM5Pt2pbf4dszsqtMXqsLmKgufndgjAk4n7sRKf2l 13
pfbid0LTfPcmpCRLvYZebmEcgHA12B5Taem3zqEuc19AGKiqTpwySZXSTMFUx11NPvUwXNl 152
pfbid02Vc6XJNwbkmVgf2X7yuf6WgNseiGAJd3qvWo6n3gU2wYAPjyywWBERCKUtF6k92JAl 144
pfbid0oiv6gSG87utYpFSP7HfCqXsFhqwAJPBvV83Y3KjZNCnnNM9DB2qu9GfMCx5h7GP5l 350
pfbid025UMFtnWCqwSmdvbDG3DALxZ3HJNBhfiKQvVS8gXJYE73uz7hJ8Rd5RgaHwFvTLEPl 150
"""

POST_ID = "pfbid025UMFtnWCqwSmdvbDG3DALxZ3HJNBhfiKQvVS8gXJYE73uz7hJ8Rd5RgaHwFvTLEPl"

# number of comments to download -- set this to True to download all comments
MAX_COMMENTS = 300

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

with open('txt/jorge.txt', 'a', encoding='utf-8') as file:
    for item in coment_txt:
        file.write(item+ '\n')

