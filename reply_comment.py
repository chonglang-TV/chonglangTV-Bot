from random import randint
import praw
import json
from prawcore.exceptions import Forbidden
from functools import reduce

import global_constants

DATA_CLTV_FILE = open('data/data_cltv.json', 'r')
DATA_CHONGLANG_FILE = open('data/data_chonglang.json', 'r')
DATA_SPECIAL = open('data/data_special.json', 'r')

# 类型包括submission comment any 
REPLY_DATA_ALL = []
# 不包括submission
REPLY_DATA_COMMENT = []
# 关键词和回复都有多个
REPLY_DATA_SPECIAL = []

def main():
    # 创建reddit实例并登录
    reddit = praw.Reddit(
        client_id=global_constants.CLIENT_ID,
        client_secret=global_constants.CLIENT_SECRET,
        user_agent=global_constants.USER_AGENT,
        password=global_constants.USER_PASSWORD,
        username=global_constants.USER_NAME
    )

    # 导入关键词json数据
    with DATA_SPECIAL as json_special:
        global REPLY_DATA_SPECIAL
        REPLY_DATA_SPECIAL = json.load(json_special)

    with DATA_CLTV_FILE as json_cltv:
        with DATA_CHONGLANG_FILE as json_chonglang:
            # 不加global，python会认为新建了一个REPLY_DATA变量并赋值
            global REPLY_DATA_ALL
            REPLY_DATA_ALL = json.load(json_cltv) + json.load(json_chonglang)
            # 可能两个语录有重复的，根据comment一样去重，代码俺也看不懂，网上抄的
            # REPLY_DATA_ALL = reduce(lambda y,x:y if (x['comment'] in [i['comment'] for i in y]) else (lambda z,u:(z.append(u),z))(y,x)[1],REPLY_DATA_ALL,[])
            global REPLY_DATA_COMMENT
            REPLY_DATA_COMMENT = list(filter(filter_submission, REPLY_DATA_ALL))

    # 创建subreddit实例
    subreddit = reddit.subreddit(global_constants.MONITOR_SUBS)

    # #监听最新的comment
    for comment in subreddit.stream.comments(skip_existing = True):
        process_latest_comment(comment)

def filter_submission(item):
    return item['type'] != 'submission'

def process_latest_comment(comment):
    if comment.author != global_constants.USER_NAME and comment.author != 'AutoModerator' and comment.author != 'docwuzzzz':
        # 已回复标志位，退出双重循环
        reply_flag = False
        # 同一关键字多条comment随机回复
        for data_item in REPLY_DATA_SPECIAL:
            if 'body (includes)' in data_item:
                for keyword in data_item['body (includes)']:
                    if keyword in comment.body:
                        print('special keyword---',keyword)
                        reply_flag = True
                        try:
                            random_comment_index = randint(0, len(data_item['comment']) - 1)
                            if data_item['comment'][random_comment_index] == "《大的来了》是荒诞戏剧的代表作。以几个鼠人苦等“大的”，而“大的”不来的情节，喻示人生是一场无尽无望的等待，表达了世界荒诞、人生痛苦的存在主义思想。它发生的时间地点都是模糊的，布景也是一片荒凉，他们一边等，一边用各种无意义的手段打发时光。他们经常显得头脑一片混乱，缺乏思维能力，尤其是极度地惧怕孤独。当有人询问“大的代表什么”时，鼠人们说：“我要是知道，早就说出来了。”\n":
                                str = "《大的来了》是荒诞戏剧的代表作。以几个鼠人苦等“大的”，而“大的”不来的情节，喻示人生是一场无尽无望的等待，表达了世界荒诞、人生痛苦的存在主义思想。它发生的时间地点都是模糊的，布景也是一片荒凉，他们一边等，一边用各种无意义的手段打发时光。他们经常显得头脑一片混乱，缺乏思维能力，尤其是极度地惧怕孤独。当有人询问“大的代表什么”时， u/" + comment.author.name + " 说：“我要是知道，早就说出来了。”\n"
                                comment.reply(str)
                            else:
                                comment.reply(data_item['comment'][random_comment_index])
                        except praw.exceptions.RedditAPIException:
                            print('comment error, u have been banned from', comment.subreddit)
                        break
            if reply_flag:
                return
        # if reply_flag:
        #     return
        # 同一关键字单条comment回复
        for data_item in REPLY_DATA_COMMENT:
            if 'body (includes)' in data_item:
                for keyword in data_item['body (includes)']:
                    if keyword in comment.body:
                        print('common keyword---',keyword)
                        reply_flag = True
                        try:
                            comment.reply(data_item['comment'])
                        except praw.exceptions.RedditAPIException:
                            print('comment error, u have been banned from', comment.subreddit)
                        break
            if reply_flag:
                break
if __name__ == "__main__":
    main()