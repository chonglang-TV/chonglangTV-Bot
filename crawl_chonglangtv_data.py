# CHONGLANG_HTML_PATH html文件夹下载地址：https://scored.co/c/chonglangTV/p/142AwK6LMx/rchonglangtv-20192022-html/c
# 爬取chonglangTV的mod语录到data_chonglang_origin, 然后手动添加到data_chonglang.md
from lxml import etree
import os
import json
import global_constants

mod_replys = []
# TARGET_FILE = open('data/data_chonglang_origin.json', 'w', encoding='utf8')
TARGET_FILE = open('data/data_baomitv_origin.json', 'w', encoding='utf8')

HTML_DIR = os.walk(global_constants.CHONGLANG_HTML_PATH)

def main():
  for path, dir_list, file_list in HTML_DIR:
    for file_name in file_list:
      collect_replys(os.path.join(path, file_name))
  convet_replys()

# 解析html，获取mod回复的语录
def collect_replys(path):
  print(path)
  if '.DS_Store' in path:
    return
  # meta和gitf标签部分没有闭合，解析失败
  html = etree.parse(path, etree.HTMLParser(encoding='utf-8'))
  # 获取关键词所在的句子
  # kewwordsList = html.xpath('//a[@href="https://old.reddit.com/u/AutoModerator"]/../../../p/text()')
  # 获取回复的句子
  kewwordsList = html.xpath('//a[@href="https://old.reddit.com/u/AutoModerator"]/../../div/p/text()')
  mod_replys.append(kewwordsList)

# 语录扁平化、去重、写文件
def convet_replys():
  global mod_replys
  # 扁平化二维数组
  mod_replys = [item for l in mod_replys for item in l]
  # 去掉空值 去掉重复项
  mod_replys = set(mod_replys)
  tmp_replys = []
  for reply in mod_replys:
    tmp_replys.append({
      "comment": reply
    })

  print(mod_replys)
  TARGET_FILE.write(json.dumps(tmp_replys, ensure_ascii=False))
  
if __name__ == "__main__":
    main()