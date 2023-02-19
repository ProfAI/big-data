import praw
from datetime import datetime
import pandas as pd
from pymongo import MongoClient

def get_database():
    CONNECTION_STRING = "mongodb://root:example@127.0.0.1/"

    client = MongoClient(CONNECTION_STRING)

    return client['crypto']


if __name__ == "__main__":

    reddit = praw.Reddit(client_id='2WTS7UmVGH4Tfg',
                         client_secret='hbwEHbyrcp5eJCdDWtJtUUiJAEI',
                         user_agent='my user agent')
    
    crypto_subreddit = reddit.subreddit('CryptoCurrency')
    posts = []
    now = datetime.now()
    for post in crypto_subreddit.hot(limit=10):
        posts.append([str(post.title), str(post.score), str(post.id), str(post.subreddit), str(post.url), str(post.num_comments), str(post.selftext), str(post.created), now.strftime("%d/%m/%Y %H:%M:%S")])
    
    pd_posts = pd.DataFrame(posts, columns=['title', 'score', 'id', 'subreddit', 'url', 'num_comments', 'body', 'created', 'saved'])

    parquet_filename = './parquet/posts_' + now.strftime("%d_%m_%Y_%H_%M_%S")+'.gzip'
    pd_posts.to_parquet(parquet_filename,
                        compression='gzip')

    out = pd_posts.to_dict('records')
    db = get_database()
    collection_name = db["reddit"]
    collection_name.insert_many(out)

    print(pd_posts.head())

