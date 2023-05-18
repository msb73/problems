import os

d = "/run/media/milin/F66E233A6E22F2D3/Users/Arch/Videos/Twenty.Five.Twenty.One.S01.KOREAN.WEBRip.x264-ION10[eztv.re]/Subs/"
def change_to_sub():
    os.chdir(r'/run/media/milin/F66E233A6E22F2D3/Users/Arch/Videos/Twenty.Five.Twenty.One.S01.KOREAN.WEBRip.x264-ION10[eztv.re]/Subs/')
def change_to_ep(string):
    three = '3_English.srt'
    five = '5_English.srt'
    os.chdir(r'/run/media/milin/F66E233A6E22F2D3/Users/Arch/Videos/Twenty.Five.Twenty.One.S01.KOREAN.WEBRip.x264-ION10[eztv.re]/Subs/'+ string + r'/')
    os.rename(string,string + '.srt')
    # print(os.listdir())

change_to_sub()
s = os.path
s = os.listdir()
# s = os.listdir('/run/media/milin/F66E233A6E22F2D3/Users/Arch/Videos/Twenty.Five.Twenty.One.S01.KOREAN.WEBRip.x264-ION10[eztv.re]/Subs')
for i in s:
    change_to_ep(i)
    change_to_sub()