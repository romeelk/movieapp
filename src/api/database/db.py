import pymongo

monogoclient = pymongo.MongoClient("mongodb://localhost:27017/")

def get_latest_movies():
    mymoviesdb = monogoclient["movies"]
    latestmovies = mymoviesdb["latestmovies"]

    for movie in latestmovies.find():
        print(movie)
