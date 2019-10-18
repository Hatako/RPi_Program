#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
2018_1116

このプログラムは以下のサイトを参考にして作成しました
http://hira-hide.hatenablog.com/entry/20170423/1492939230
test01.pyとは少し違った処理方法をしています
XMLの解析を行い, 音声入力した単語と信頼度(CM)の抽出を行っています
OpenJtalkで喋らせるやつも入れてみました


2018_1129
音声入力後の音声認識を一時停止するやつを試してみた--->成功!


2019_1017
1. ユーザが「すいません」と話しかけるとロボット「こんにちは。何を取りに行きましょうか？」
とユーザに問いかけ待機状態に入る(それまでは「ラズパイ」コマンド入力待ち)

2. ユーザが「○○取って, 〇〇拾って」と音声入力すると「〇〇ですね？」とユーザに確認

3. 音声認識の結果が正しければ, ユーザは「はい」, 間違っていれば「いいえ」と音声入力

4. 「はい」と言われたら, 「〇〇を取りにいきます」と言って, 物体を取得しにいく
   「いいえ」と言われたら, 「何を取りにいきましょうか」とユーザに問いかけ待機状態

5. 物体をユーザの近くまで持ってきた後, 「どうぞ, ○○です。掴んで下さい」と言い物体を差し出す。
   ユーザが物体を掴んだ後, 「ありがとう」でエンドエフェクタが開き, 物体の受け渡しが完了, プログラム終了


import socket
import xml.etree.ElementTree as ET
import subprocess
from datetime import datetime
#import commands
import time
import os
import jtalk


host = 'localhost'
port = 10500
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((host, port))

	
#pause等の命令を送信
def send_command(command):
	msgbytes=command.encode('utf-8')+b'\n'
	client.sendall(msgbytes)
#	print(msgbytes)


#物体取得
def get_object(object_name):
    print('This is get_object function')

jtalk.jtalk('プログラムがスタートしました')

try:
    data = ''
    OBJECT = ''
    while True:
        if '</RECOGOUT>\n.' in data:
            root = ET.fromstring('<?xml version="1.0"?>\n' + data[data.find('<RECOGOUT>'):].replace('\n.', ''))
            for whypo in root.findall('./SHYPO/WHYPO'):
                command = whypo.get('WORD')
                score = float(whypo.get('CM'))
                print(command, score)
                if score>=0.99:
                    if command == u'ラズパイ':
                        print('物体名の音声入力待機')
                        jtalk.jtalk('こんにちわ、なにをとりましょうか？')

                    elif command == u'はい':
                        get_object(OBJECT)

                    elif command == u'いいえ':
                        continue

                    elif command == u'スマートフォン':
                        print('スマートフォンと入力されました')
                        OBJECT = 'スマートフォン'

                    elif command == u'リモコン':
                        print('リモコンと入力されました')
                        OBJECT = 'リモコン'

                    elif command == u'コップ':
                        print('コップと入力されました')
                        OBJECT = 'コップ'

                    elif command == u'飲み物':
                        print('飲み物と入力されました')
                        OBJECT = '飲み物'

                    elif command == u'ハサミ':
                        print('ハサミと入力されました')
                        OBJECT = 'ハサミ'

                    elif command == u'ホッチキス':
                        print('ホッチキスと入力されました')
                        OBJECT = 'ハサミ'

                    elif command == u'消しゴム':
                        print('消しゴムと入力されました')
                        OBJECT = '消しゴム'

                    elif command == u'鉛筆':
                        print('鉛筆と入力されました')
                        OBJECT = '鉛筆'

                    elif command == u'ボールペン':
                        print('ボールペンと入力されました')	
                        OBJECT = 'ボールペン'
                else:
                    print('scoreが0.99未満なので棄却')
                    send_command('PAUSE')
                    time.sleep(5)
                    send_command('RESUME')
            data = ''
        else:
            data = data + client.recv(1024).decode()
except KeyboardInterrupt:
	client.close()

"""

import socket
import xml.etree.ElementTree as ET
import subprocess
from datetime import datetime
#import commands
import time
import os
import jtalk


host = 'localhost'
port = 10500
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((host, port))

	
#pause等の命令を送信
def send_command(command):
	msgbytes=command.encode('utf-8')+b'\n'
	client.sendall(msgbytes)
#	print(msgbytes)


#物体取得
def get_object(object_name):
    jtalk.jtalk("{}を取りにいきます".format(object_name))
    print("物体取得中.....5秒停止")
    time.sleep(5)
    jtalk.jtalk("{}です、どうぞ".format(object_name))




jtalk.jtalk('プログラムがスタートしました')


try:
    data = ''
    OBJECT = ''
    while True:
        if '</RECOGOUT>\n.' in data:
            root = ET.fromstring('<?xml version="1.0"?>\n' + data[data.find('<RECOGOUT>'):].replace('\n.', ''))
            for whypo in root.findall('./SHYPO/WHYPO'):
                command = whypo.get('WORD')
                score = float(whypo.get('CM'))
                print(command, score)
                if score>=0.96:
                    if command == u'すいません' or command == u'すみません':
                        jtalk.jtalk('こんにちわ、なにをとりましょうか？')
                        print('物体名の音声入力待機')

                    elif command == u'スマートフォン':
                        print('スマートフォンと入力されました')
                        OBJECT = 'スマートフォン'
                        jtalk.jtalk('スマートフォンですね？')

                    elif command == u'リモコン':
                        print('リモコンと入力されました')
                        OBJECT = 'リモコン'
                        jtalk.jtalk('リモコンですね？')

                    elif command == u'はい':
                        get_object(OBJECT)
                        OBJECT = ''
                    elif command == u'いいえ':
                        jtalk.jtalk('それでは、なにをとりましょうか？')
                        OBJECT = ''
                        continue
                    elif command == u'ありがとう':
                        print("エンドエフェクタ開")
                        jtalk.jtalk('どういたしまして、また何かあれば言ってください')

                else:
                    print('scoreが0.99未満なので棄却')
                    send_command('PAUSE')
                    time.sleep(0.1)
                    send_command('RESUME')
            data = ''
        else:
            data = data + client.recv(1024).decode()
except KeyboardInterrupt:
	client.close()