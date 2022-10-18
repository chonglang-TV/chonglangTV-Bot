# 登录信息
# USER_AGENT 自定义的 可以看prew官方文档 https://praw.readthedocs.io/en/stable/getting_started/quick_start.html
# CLIENT_ID和CLIENT_SECRET 在创建机器人这里 https://www.reddit.com/prefs/apps/
USER_NAME = 'fake_cltv_mod_bot'
USER_PASSWORD = ''
USER_AGENT = 'chrome:chonglang:v1.0.0 (by /u/fake_cltv_mod_bot)'
CLIENT_ID = ''
CLIENT_SECRET = ''

# 监听的subs，多个sub用+隔开
MONITOR_SUBS = 'chonglangtv+cltv+quanlangtv+baomitv+youmotv+youmo'

# chonglangHTML文件夹地址, 重新爬取chonglangTV语录时用，如 /home/luuthink/project/chonglangTV_full_backup
CHONGLANG_HTML_PATH = ''

__all__ = [
  USER_NAME,
  USER_PASSWORD,
  USER_AGENT,
  CLIENT_ID,
  CLIENT_SECRET,
  MONITOR_SUBS,
  CHONGLANG_HTML_PATH
]
