import json
import os
import time


class Mitmproxy2Meersphere:
    origin_json = {
        "projectId": "",
        "data": [
        ]
    }
    request_info_json = {
        "name": "",
        "method": "POST",
        "status": "Prepare",
        "protocol": "HTTP",
        "path": "",
        "request": {
            "method": "POST",
            "path": "",
            "body": {
                "raw": "",
                "type": "JSON"
            }
        }
    }

    def __init__(self):
        self.urls = []

    def load(self, loader):
        # 在这里使用input()函数接受参数
        self.url = input('请输入想要捕获接口的公共路由：')
        self.json_file_name='mit2meter.json'
        with open(self.json_file_name, 'w') as f:
            json.dump(self.origin_json, f)
            f.close()

    def request(self, flow):
        if self.url in flow.request.url:
            if flow.request.url not in self.urls:
                print('已录入：' + flow.request.url)
                self.urls.append(flow.request.url)
                last_word_with_params = flow.request.url.split('/')[-1]
                name = last_word_with_params.split('?')[-1]
                path = flow.request.url.split(self.url)[-1]
                request_body = flow.request.text
                self.request_info_json["name"] = name
                self.request_info_json["path"] = path
                self.request_info_json["request"]["path"] = path
                self.request_info_json["request"]["body"]["raw"] = request_body

                with open(self.json_file_name, 'r') as f:
                    data = json.load(f)
                with open(self.json_file_name, 'w') as fi:
                    data["data"].append(self.request_info_json)
                    json.dump(data, fi)
                    f.close()


addons = [
    Mitmproxy2Meersphere()
]

if __name__ == '__main__':
    os.system("mitmdump -q -p 8083 -s main.py")
