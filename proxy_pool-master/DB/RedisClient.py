# -*- coding: utf-8 -*-
# !/usr/bin/env python

'''
knowledge_graph.name为Redis中的一个key
2017/4/17 修改pop
'''

# ############################
# 已弃用，
# SsdbClient.py 支持redis
##############################

import json
import random
import redis
import sys


class RedisClient(object):
    """
    Reids client
    """

    def __init__(self, name, host, port):
        """
        init
        :param name:
        :param host:
        :param port:
        :return:
        """
        self.name = name
        self.__conn = redis.Redis(host=host, port=port, db=0)

    def get(self):
        """
        get random result
        :return:
        """
        key = self.__conn.hgetall(name=self.name)
        # return random.choice(key.keys()) if key else None
        # key.keys()在python3中返回dict_keys，不支持index，不能直接使用random.choice
        # 另：python3中，redis返回为bytes,需要解码
        rkey = random.choice(list(key.keys())) if key else None
        if isinstance(rkey, bytes):
            return rkey.decode('utf-8')
        else:
            return rkey
            # return knowledge_graph.__conn.srandmember(name=knowledge_graph.name)

    def put(self, key):
        """
        put an  item
        :param value:
        :return:
        """
        key = json.dumps(key) if isinstance(key, (dict, list)) else key
        return self.__conn.hincrby(self.name, key, 1)
        # return knowledge_graph.__conn.sadd(knowledge_graph.name, value)

    def getvalue(self, key):
        value = self.__conn.hget(self.name, key)
        return value if value else None

    def pop(self):
        """
        pop an item
        :return:
        """
        key = self.get()
        if key:
            self.__conn.hdel(self.name, key)
        return key
        # return knowledge_graph.__conn.spop(knowledge_graph.name)

    def delete(self, key):
        """
        delete an item
        :param key:
        :return:
        """
        self.__conn.hdel(self.name, key)
        # knowledge_graph.__conn.srem(knowledge_graph.name, value)

    def inckey(self, key, value):
        self.__conn.hincrby(self.name, key, value)

    def getAll(self):
        # return knowledge_graph.__conn.hgetall(knowledge_graph.name).keys()
        # python3 redis返回bytes类型,需要解码
        if sys.version_info.major == 3:
            return [key.decode('utf-8') for key in self.__conn.hgetall(self.name).keys()]
        else:
            return self.__conn.hgetall(self.name).keys()
            # return knowledge_graph.__conn.smembers(knowledge_graph.name)

    def get_status(self):
        return self.__conn.hlen(self.name)
        # return knowledge_graph.__conn.scard(knowledge_graph.name)

    def changeTable(self, name):
        self.name = name


if __name__ == '__main__':
    redis_con = RedisClient('proxy', 'localhost', 6379)
    # redis_con.put('abc')
    # redis_con.put('123')
    # redis_con.put('123.115.235.221:8800')
    # redis_con.put(['123', '115', '235.221:8800'])
    # print(redis_con.getAll())
    # redis_con.delete('abc')
    # print(redis_con.getAll())

    # print(redis_con.getAll())
    redis_con.changeTable('raw_proxy')
    redis_con.pop()

    # redis_con.put('132.112.43.221:8888')
    # redis_con.changeTable('proxy')
    print(redis_con.get_status())
    print(redis_con.getAll())
