
from pymongo import MongoClient

import pandas as pd

import urllib


class MongConn():
    """for connceting to mongo on port 27017 """

    def __init__(self, username, password):

        self.username = urllib.parse.quote_plus(username)
        self.password = urllib.parse.quote_plus(password)

    def connect(self):
        self.client = MongoClient(
            'mongodb://%s:%s@127.0.0.1' % (self.username, self.password))

    def post_data_to_any(self, post: dict, name_of_data_base='new_db', name_of_table='new_table'):
        self.db = self.client[name_of_data_base]
        self.open_trades = self.db[name_of_table]
        return self.open_trades.insert_one(post).inserted_id

    def post_day_data_ml_api(self, post):
        self.db = self.client["inputs"]
        self.open_trades = self.db["open_trades"]
        return self.open_trades.insert_one(post).inserted_id

    def post_data_to_options(self, post):
        self.db = self.client["option_trading_data"]
        self.open_trades = self.db["open_trades"]
        return self.open_trades.insert_one(post).inserted_id

    async def async_post_data_to_options(self, post):
        self.db = self.client["option_trading_data"]
        self.open_trades = self.db["open_trades"]
        return self.open_trades.insert_one(post).inserted_id

    def get_data_from_any(self, query, name_of_data_base='new_db', name_of_table='new_table'):
        self.db = self.client[name_of_data_base]
        self.posts = self.db[name_of_table]
        last_entry = self.posts.find()
        # last_entry.sort({"$natural":1}).limit(1)
        ret_dict_pandas = {}
        for post in self.posts.find(query, {'_id': False}):
            # print("operate curosrs!!!!!!!!!!!!!!!!!!!!!!!!")
            # if '_x' in post.keys():
            # print(post[list(post.keys())[0]])

            for i in list(post.keys()):
                # print(i, post[i])
                ret_dict_pandas[i] = pd.DataFrame(post[i])

        return ret_dict_pandas

    def clean_up_collection(self, name_of_data_base='new_db', name_of_table='new_table'):
        self.db = self.client[name_of_data_base]
        self.posts = self.db[name_of_table]
        self.posts.delete_many({})


mong_cl = MongConn(username='AzureDiamond', password='hunter2')
mong_cl.connect()
# result=mong_cl.post_data_to_options({'new':'newnew'})
# result=mong_cl.post_data_to_any(post={'predions':'testing'},name_of_data_base='django_data',name_of_table='ready_for_predictions')
# result=mong_cl.get_data_from_any(query={},name_of_data_base='django_data',name_of_table='ready_for_predictions')
