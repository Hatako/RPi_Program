# -*-coding:utf-8-*-
#H31 1/10作成
#DRV8830を用いてモータを動作させるプログラム
#T2g's blogさんの記事を参考にして作成しました


import smbus
import time
i2c=smbus.SMBus(1)
adr1=0x64
adr2=0x63


#00:待機,  01:逆転,  10:正転,  11:ブレーキ


logic1=0b10
logic2=0b01
logic3=0b00


try:
	for i in range(50,70):
		DA1=(i<<2|logic2)
		DA2=(i<<2|logic2)
		print(DA1)
		print(DA2)
		i2c.write_byte_data(adr1, 0, DA1 )
		i2c.write_byte_data(adr2, 0, DA2 )
		time.sleep(0.5)

	#両輪停止
#	DA1=(1<<2|logic1)
#	DA2=(1<<2|logic1)
#	i2c.write_byte_data(adr1, 0, DA1 )
#	i2c.write_byte_data(adr2, 0, DA2 )

except KeyboardInterrupt:
	DA1=(1<<2|logic1)
	DA2=(1<<2|logic1)
	i2c.write_byte_data(adr1, 0, DA1 )
	i2c.write_byte_data(adr2, 0, DA2 )
