# 把yaml格式的data转化为json

import yaml
import json

SOURCE_FILE = open('data/data_cltv.md', 'r')
TARGET_FILE = open('data/data_cltv.json', 'w')

# SOURCE_FILE = open('data/data_chonglang.md', 'r')
# TARGET_FILE = open('data/data_chonglang.json', 'w')

docs = yaml.load_all(SOURCE_FILE, Loader=yaml.FullLoader)
data = []
for doc in docs:
    # yaml以---分隔每个对象，data.md两个对象之间是空数据
    if doc:
      data.append(doc)
print(data)
TARGET_FILE.write(json.dumps(data, ensure_ascii=False))

SOURCE_FILE.close()
TARGET_FILE.close()