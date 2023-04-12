import json
import os
import asyncio
import sys

from mitmproxy import options
from mitmproxy.tools import dump


def clear_window():
    if sys.platform.startswith('darwin'):
        os.system('clear')
    else:
        os.system('cls')


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
        clear_window()
        self.url = input('\n\033[1mPlease enter the keyword：').strip()
        clear_window()
        print('\n\033[1m* Locking keywords：\033[0m'+self.url)
        print('\033[1m\033[32m* Listening to localhost:8083\033[0m')
        print('\033[1m----------------------------------------------\033[0m')
        if getattr(sys, 'frozen', False):
            # 打包后的可执行文件
            working_dir = os.path.dirname(sys.executable)
        else:
            # 源代码
            working_dir = os.path.dirname(os.path.abspath(__file__))

        # 使用绝对路径来指定文件的位置
        self.json_file_name = os.path.join(working_dir, 'mit2meter.json')

        with open(self.json_file_name, 'w') as f:
            json.dump(self.origin_json, f)
            f.close()

    def request(self, flow):
        if self.url in flow.request.url:
            if flow.request.url not in self.urls:
                print('\033[1;32;43m> Entry:\033[0m ' + flow.request.url)
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


async def start_proxy(host, port):
    opts = options.Options(listen_host=host, listen_port=port)

    master = dump.DumpMaster(
        opts,
        with_termlog=False,
        with_dumper=False,
    )
    master.addons.add(Mitmproxy2Meersphere())

    await master.run()
    return master

asyncio.run(start_proxy('0.0.0.0', 8083))
if __name__ == '__main__':
    # host=sys.argv[1]
    # port=int(sys.argv[2])
    pass