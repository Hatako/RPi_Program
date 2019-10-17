#!/usr/bin/python
# -*- coding: utf-8 -*-

# 2019 10/11 julius module modeの復習としてプログラムを動作させてみた
# https://hira-hide.hatenablog.com/entry/20170423/1492939230

"""
import socket
import xml.etree.ElementTree as ET

def main():
    host = 'localhost'
    port = 10500

    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((host, port))

    try:
        data = ''
        while 1:
            if '</RECOGOUT>\n.' in data:
                root = ET.fromstring('<?xml version="1.0"?>\n' + data[data.find('<RECOGOUT>'):].replace('\n.', ''))
                for whypo in root.findall('./SHYPO/WHYPO'):
                    command = whypo.get('WORD')
                    score = float(whypo.get('CM'))
                    print(data)
 #                   if command == u'ただいま' and score >= 0.9:
                        # ここにただいま処理
 #                   elif command == u'パキン' and score >= 0.996:
                        # ここにパキン処理

                data = ''
            else:
                data = data + client.recv(1024).decode()
    except KeyboardInterrupt:
        client.close()

if __name__ == "__main__":
    main()
"""
