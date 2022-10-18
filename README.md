# Quotation source
  - [cltv语录](https://www.charliebbs.com/furudesatoko/yuan-tou-cltvyuan-you-de-automodyu-lu-1b12)
  - [chonglangTV语录](https://scored.co/c/chonglangTV/p/142AwK6LMx/rchonglangtv-20192022-html/c)
  - [baomiTV语录](https://scored.co/c/chonglangTV/p/15JTb2hn6I/rbaomitv/c)
  - 如果上述地址无法打开，这里有github的备份 [备份](https://github.com/chonglang-TV/chonglangTV_full_backup)

# What does this bot do
  监听几个subreddit的最新post和comment，根据冲浪tv之前的mod关键词自动回复，重铸冲浪荣光，我辈义不容辞


# Prerequisites
  [看官方文档](https://praw.readthedocs.io/en/stable/getting_started/quick_start.html)


# How to start
  - 须知

    - 首先需要python3.8.7以上的环境，然后pip3 install -r requirements.txt。

    - global_constants去掉了登录信息，需要换成自己的
  - 运行
    ```
      python3 reply_comment.py
      python3 reply_submission.py
    ```

      - 因为俺是个菜鸡，没看懂python的多线程or多进程怎么用，两个任务放不到一个文件里，只能拆开在两个终端运行了。

      - 如果你是在服务器上不方便多开终端，可以使用nohup命令让任务后台运行，格式如下。log文件会在nohup.out里

    ```
      nohup python3 reply_comment.py &
      nohup python3 reply_submission.py &
    ```

# Dir list
```
  ├── README.md
  ├── crawl_chonglangtv_data.py       // 从下载的html文件里爬取AutoModerator语录
  ├── data
  │   ├── data_baomitv_origin.json    // 爬到的baomiTV原始语录
  │   ├── data_chonglang.json
  │   ├── data_chonglang.md
  │   ├── data_chonglang_origin.json  // 爬到的chonglangTV原始语录
  │   ├── data_cltv.json
  │   ├── data_cltv.md
  │   └── data_special.json           // 评论和关键词都有多个的回复列表
  ├── global_constants.py             // 登录信息、监听的sub等全局变量
  ├── md2json.py                      // 把整理的md文件变成json数据
  ├── reply_comment.py                // 根据关键词自动回复评论
  ├── reply_submission.py             // 根据关键词自动回复帖子             
  └── requirements.txt
```