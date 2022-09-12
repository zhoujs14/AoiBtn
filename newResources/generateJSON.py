import json
import os
import time


# class Voice:
#     def __init__(self, name):
#         self.name = name[:-4]
#         self.path = name
#         localtime = time.localtime(time.time())
#         self.date = f'{localtime.tm_year}-{localtime.tm_mon}-{localtime.tm_mday}'
#         self.translate = {'zh-CN': name, 'en-US': name}
#         self.usePictures = {'zh-CN': name, 'en-US': name}
#         self.category = ''
#         self.mark = {"title": '', 'time': '', 'url': ''}

#     def change_type(self, byte):
#         if isinstance(byte, bytes):
#             return str(byte, encoding="utf-8")
#         return json.JSONEncoder.default(byte)

#     def getJSON(self):
#         print(json.dumps(self, cls=self.change_type, indent=4))
#         return json.dumps(self, cls=self.change_type, indent=4)


localtime = time.localtime(time.time())
jsons = []
# 为当前目录下.mp3文件生成voiceJSON
for root, dirs, files in os.walk('D:\\aoibtn\\newResources'):
    for file in files:
        if file.endswith('.mp3'):
            voice = {
                "name": file[:-4],
                "path": file,
                "date": f'{localtime.tm_year}-{localtime.tm_mon}-{localtime.tm_mday}',
                "translate": {'zh-CN': file, 'en-US': file},
                "usePicture": {'zh-CN': '', 'en-US': ''},
                "category": '怪叫怪叫',
                "mark": {"title": '', 'time': '', 'url': ''}
            }
            # 不使用unicode转码
            jsons.append(json.dumps(voice, ensure_ascii=False)+',')

txt = open('D:\\aoibtn\\newResources\generatedJSON.txt', mode='w')
txt.writelines(jsons)
