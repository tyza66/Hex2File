'''
常见的魔数
PNG	89 50 4E 47 0D 0A 1A 0A	Portable Network Graphics
JPEG	FF D8 FF	JPEG图像文件
GIF	47 49 46 38 39 61 或 47 49 46 38 37 61	GIF 89a/GIF 87a
BMP	42 4D	Windows Bitmap
MP3	49 44 33	MP3（ID3v2 Tag）
ZIP	50 4B 03 04	ZIP压缩文件
RAR	52 61 72 21 1A 07 00	RAR压缩文件
PDF	25 50 44 46	PDF文件
EXE	4D 5A	Windows可执行文件
TAR	75 73 74 61 72	tar归档文件
ELF	7F 45 4C 46	Linux可执行文件格式
WAV	52 49 46 46	WAV音频格式
AVI	52 49 46 46	AVI视频文件
FLAC	66 4C 61 43	FLAC音频格式


IEND 49 45 4E 44 AE 42 60 82
'''

hex_data = """
0030   89 50 4e 47 0d 0a 1a 0a 00 00
0040   00 0d 49 48 44 52 00 00 00 8c 00 00 00 8c 08 06
0050   00 00 00 ae c0 41 3e 00 00 2a 99 49 44 41 54 78
0060   da ed 7d 69 98 55 d5 99 ee fb ad b5 c7 53 73 31
0070   c9 20 32 17 20 20 a0 42 8c 22 6a d4 a8 d1 06 31
0080   b4 b6 8a 51 4c 6b 3b 66 e8 ee dc ee be 7f 72 9f
0090   db b7 93 9b db dd 6a 1c 12 8d b3 82 1a e7 d9 88
00a0   23 2a 22 82 18 11 44 90 79 9e 6a ae 73 f6 b8 be
00b0   fb 63 ed 53 54 41 01 35 9f 53 ca fb 3c fb 11 4f
00c0   9d b3 f7 da 6b bf 7b 7d df fa 46 62 66 7c 07 40
00d0   60 26 30 83 c1 04 06 01 fa be a3 6d 5b 4e 52 0d
00e0   f5 29 55 5d 59 ec af 5e 31 5e 65 d2 06 a2 08 04
00f0   00 82 00 c3 02 a5 0a 42 7b f4 b8 15 b2 b4 bc 8e
0100   0a 8b ea 8d 7e fd 3f 83 fe 06 83 00 02 31 88 18
0110   94 7c f6 2d 86 91 eb 01 74 01 08 4a 09 8e 63 03
0120   71 24 c1 4c 71 d5 de 0a 7f f5 ca d3 bd 4f 3f 9a
0130   ee 7f b1 74 4c f0 cd ea e3 50 5f eb 98 c9 b3 55
0140   0c a8 e4 49 67 9f 36 23 a1 44 f2 5f 91 f0 87 92
0150   ef 87 44 a0 92 b2 8c 3d 66 fc 26 77 c2 49 ab 9c
0160   13 4f 79 df 1a 31 7a a1 28 29 5b 0b 21 18 52 c6
0170   24 65 04 12 ea db 44 22 fa 56 ac 30 cc 82 c3 d0
0180   e6 c0 b7 38 93 2e 8b 36 af 9f 92 7e 7f c1 85 0d
0190   6f bc 78 b6 dc ba a1 bf 45 fa a9 c7 0c 44 0c c4
01a0   e0 46 92 b4 6b d2 00 10 69 12 19 20 18 a4 c9 a4
01b0   18 f0 85 00 86 8f de 56 78 fe c5 6f b9 a7 9c f1
01c0   8a 31 e0 d8 a5 e4 ba 55 64 39 3e 19 46 00 a2 f6
01d0   5e 36 2f d0 73 09 a3 94 64 df 2b 50 99 b4 ab 2a
01e0   f7 0e f1 96 7c 30 b3 fe b9 79 b3 78 d5 5f 47 59
01f0   82 10 33 10 32 23 e2 ee 7d bd 05 00 93 00 93 08
0200   44 80 27 04 e4 c4 a9 ab 8b 67 5e fe ac 35 69 ca
0210   8b a2 b4 7c 93 70 0b 32 64 5b 69 90 88 73 3d 8d
0220   6d 45 cf 22 0c 33 71 18 b8 aa ae b6 54 ed da 31
0230   2c f3 c1 82 cb d3 2f 3c 31 43 6c 59 3f 00 00 02
0240   c5 88 0e 10 2d b9 04 1d 40 a0 80 19 62 f4 84 6d
0250   45 b3 ae 78 de 3e f9 b4 f9 a2 77 df 8d a2 a8 a4
0260   86 4c 33 93 27 43 3e f2 3d f5 08 c2 28 25 55 43
0270   7d a9 da b3 73 60 b8 fa cb e9 f5 7f 7e e8 5a b5
0280   e4 a3 13 88 00 3f 21 49 4f 00 01 b0 88 60 12 e0
0290   01 b0 a7 9f b7 bc 68 f6 9c fb cd e1 15 0b 45 ef
02a0   7e 3b 84 9b aa ca 77 91 95 df 84 51 4a c6 d5 fb
02b0   8e 89 37 6f 1c ee 2d 7e 6f 76 c3 13 0f 5c 66 ec
02c0   dd dd 3b 60 46 c0 cd 15 d3 9e 82 ec 6c 0b 00 b6
02d0   00 04 08 18 32 62 4f e1 e5 3f 9d 6f 4e 9c f2 b4
02e0   31 e8 b8 8d a2 b8 74 47 be 12 27 3f 09 c3 2c e2
02f0   7d 7b 06 c5 eb d7 8c cc 2c 78 e9 fa fa 79 7f 9a
0300   6d 0a c0 53 5a 69 45 0f 24 4a 8b b7 99 dc 87 49
0310   80 4d 84 c0 76 51 3c f7 e6 27 ad 53 cf ba d7 1c
0320   3a 6a 9d 28 29 dd 0a a2 bc 7a 40 79 47 18 55 53
0330   d5 3f fc ea 8b 71 fe bb 6f 5c db f0 d8 bd 97 0a
0340   00 19 e6 9e 21 e0 3b 08 49 80 43 84 c0 b4 50 7a
0350   dd 2f e6 9b 53 a7 3f 60 8e 19 b7 4a a4 0a 77 e6
0360   7a 6c 59 e4 0d 61 d8 cb 94 05 ab fe 3a 2e 5a ba
0370   68 56 f5 1d ff fb e7 12 04 8f b9 dd 5b df 9e 0c
0380   03 80 2b 08 be 53 80 5e ff f8 eb ff 92 e3 27 bf
0390   60 56 8c fb 92 4c b3 3a d7 63 cb 3d 61 98 8d e0
03a0   9b d5 13 f8 8b 4f cf d9 77 e7 6f 7f 69 ec d9 d9
03b0   37 a3 18 f1 b7 44 ec 74 04 06 08 8e 00 d4 88 31
03c0   3b 4b ae fb c5 7f 1b 13 4e 7a cb 18 74 dc 0a 10
03d0   e5 4c cf cf 29 61 54 5d 6d bf 60 f1 fb 67 d5 3f
03e0   fb d8 cd fc e1 db a7 64 94 a2 88 8f 12 e5 40 d8
03f0   44 10 86 54 ee 45 b3 3f b2 ce bd f8 6e 7b ca a9
0400   ef 09 37 b5 2b 17 63 c9 19 61 82 15 9f 9d 1a 7d
0410   fa e1 8f 6a ef fa ed 2f 62 3f e3 f8 f9 21 19 f3
0420   16 22 11 53 5c d6 a7 a1 e4 a6 5f dd 6e 9c 3c ed
0430   55 73 f8 a8 8f bb 7b 1c dd 4e 18 f6 bd 12 ff a3
0440   b7 cf aa 7f fc 4f ff 43 2d 5b 74 62 3a 08 8d a3
0450   5c 69 3d 4c 02 6c d7 0d ad b3 2e 58 62 cd bc fc
0460   77 ce d4 69 ef 91 61 d6 76 d7 f5 bb 95 30 d1 f6
0470   2d 63 a2 85 6f 5e 54 fd a7 db 6e 8d 76 6e 1f 10
0480   2a a6 9e 68 4b c9 25 38 71 82 3a 86 a1 68 c8 c8
0490   ad 45 d7 dc 7c a7 3d fd dc 57 64 79 ef d5 dd 71
04a0   fd 6e 23 8c ff f9 92 33 82 57 9f 9d eb bd f2 e7
04b0   99 99 9a ea a2 f8 e8 b2 d2 6e 34 b5 df 98 bd fa
04c0   d4 14 5e 3a f7 05 f3 87 33 1e b4 46 8e 59 d8 d5
04d0   d7 ee 7a c2 28 65 66 de 79 6d 46 fa c9 07 7e 16
04e0   7e f6 c9 c9 5e 26 63 7f 17 b7 ca 5d 01 ca da 6e
04f0   8a 4b 3c fb f4 73 3e b1 67 cd b9 c3 99 3a ed 15
0500   10 85 5d 75 cd 2e 8d 87 61 df 2f f5 df 7a 79 66
0510   dd 7d ff fd ab 60 dd 9a 8a 28 8e 05 27 a1 01 47
0520   d1 39 88 01 64 6a 6b 1c b5 e0 e5 69 e1 ae 1d bd
0530   54 26 5d e8 4e 3b fb 25 32 8c 9a ae b8 5e 97 ad
0540   30 ca cb 94 06 2f 3d 75 4d dd c3 77 df e4 6d 5a
0550   3f 34 52 4a 74 f5 e4 7d 97 41 00 2c d3 54 e6 a8
0560   b1 eb 52 57 df 74 57 ea bc 99 8f 90 61 76 3a 69
0570   ba 84 30 71 6d f5 c0 f0 95 a7 e7 d4 3f 72 cf 0d
0580   e9 2d 1b 07 47 e8 29 ce fb 9e 0d 02 60 0a 01 73
0590   d8 c8 0d 85 73 6f f9 83 7b fe ac 79 c2 71 b7 77
05a0   ea 35 3a 9b 30 71 e5 de a1 c1 0b f3 7f da 30 ff
05b0   fe ab d3 db b7 0c 38 aa dc 76 3f 0c 22 58 c7 0d
05c0   db 5a 70 cd cd 0f a5 2e 9c fd 80 48 15 6c ea ac
05d0   73 cb 5f ff fa d7 9d 36 d0 b8 b6 7a 60 f0 dc e3
05e0   d7 37
"""  # ws右键选复制为Hex Dump

# 去掉空行
hex_data = "\n".join(line for line in hex_data.strip().splitlines() if line.strip())

# 去掉每行开头的偏移地址
hex_data = "\n".join(line[4:].strip() for line in hex_data.strip().splitlines())

# 去掉每行的空格
hex_data = hex_data.replace(" ", "")

# 将所有行连接成一个长字符串
hex_data = hex_data.replace("\n", "")

print(hex_data)


# 将十六进制字符串转换为二进制数据
binary_data = bytes.fromhex(hex_data)

# 将数据写入文件
with open("output.png", "wb") as file:
    file.write(binary_data)

print("图片已保存为 output.png")
