import threading
from kivy.clock import Clock
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.togglebutton import ToggleButton
from kivy.config import Config
from kivy.uix.label import Label
import json
import os
import asyncio
import sys
import time
from mitmproxy import options
from mitmproxy.tools import dump


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
        self.url = None

    def load(self, loader):

        # 在这里使用input()函数接受参数

        print('\033[1m\033[32m* Listening to localhost:8083\033[0m')
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
        if Middle.new_status:
            Middle.new_status = not Middle.new_status
            self.url = Middle.keyword
            self.urls=[]
            with open(self.json_file_name, 'w') as f:
                json.dump(self.origin_json, f)
                f.close()
        if self.url in flow.request.url:
            if flow.request.url not in self.urls:
                if Middle.record:
                    Middle.info_desk+='> Entry: '+flow.request.url+'\n'
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
                else:
                    Middle.info_desk += '> Not Entry: ' + flow.request.url + '\n'


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


#
def run_asyncio_loop(loop):
    asyncio.set_event_loop(loop)
    loop.run_until_complete(start_proxy('127.0.0.1', 8083))
    loop.stop()


class Middle:
    keyword = 'graphql'
    record = False
    new_status = True
    info_desk = ''


class MyApp(App):

    def build(self):
        loop = asyncio.new_event_loop()
        self.t = threading.Thread(target=run_asyncio_loop, args=(loop,), daemon=True)
        self.t.start()
        hb = BoxLayout(orientation='horizontal', size_hint_y=0.1)
        self.text_input = TextInput(text='graphql',
                                    font_size="25sp",
                                    pos=(0, 0),
                                    size_hint_x=0.6)
        hb.add_widget(self.text_input)
        button = Button(text='change keywords\nor\nclear', size_hint_x=0.2, halign='center')
        button.bind(on_press=self.change_keyword)
        hb.add_widget(button)
        toggle_button = ToggleButton(text='Entry', group='record', size_hint_x=0.2)
        toggle_button.bind(on_press=self.toggle_record)
        hb.add_widget(toggle_button)

        vb = BoxLayout(orientation='vertical', size_hint_y=0.9)
        self.real_time_label = TextInput(text="Three", font_size='18sp')
        vb.add_widget(self.real_time_label)
        superBox = BoxLayout(orientation='vertical')  # 定义盒子，并设置内部的部件水平排列
        superBox.add_widget(hb)
        superBox.add_widget(vb)
        Clock.schedule_interval(self.update_label, 0)
        return superBox

    # def on_stop(self):
    #    if not self.is_stopped:
    #     self.is_stopped = True
    #     App.get_running_app().stop()

    def change_keyword(self, instance):
        Middle.keyword = self.text_input.text
        Middle.new_status=True
        Middle.info_desk = 'cleared history and locking keywords: ' + Middle.keyword + '\n'
        Middle.info_desk+='------------------------------------------------------------------------------------------------------------------\n'
    def toggle_record(self, instance):
        Middle.record = not Middle.record

    def update_label(self, instance):
        self.real_time_label.text = Middle.info_desk


MyApp().run()
