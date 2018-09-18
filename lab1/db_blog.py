#1. Connect to database
from pymongo import MongoClient
from bson.objectid import ObjectId

uri = "mongodb://findbluelove:Cuong269@ds237072.mlab.com:37072/c4e21"

client = MongoClient(uri)
db = client.get_default_database()

#2. Select collection
posts = db["posts"]

#3. Create document
post = {
    "title": "Hôm nay trời mưa",
    "content": "Tôi đi học code",
}

#4. Insert document
posts.insert_one(post)

# print("Done")

post_list = posts.find()
# for post in post_list: # post_list ~ collection ~ list
#     print(post) # post ~ document ~ dictionary
    # print(post["content"])
cond = {
    "title": {
        "$regex": "hôm nay",
        "$options": "i",
    }
}
post = posts.find_one(cond)
print(post)