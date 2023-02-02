
import requests
import re
import pprint
import json
from tkinter import *
import sys



if __name__ == '__main__':

    root = Tk()
    root.geometry("400x300+0+0")
    # def myClick():
    #   myLabel=Label(root, text="按钮被点击了！")
    #   myLabel.pack()

    entry = Entry(root, width=20)
    entry.pack()
    root.title("音乐下载器1.0")


    def get_input():
        global music_name
        music_name = entry.get()
        # music_name = input("请输入您想下载的歌曲名字")
        url = f'https://api.bilibili.com/x/web-interface/wbi/search/type?__refresh__=true&_extra=&context=&page=1&page_size=42&duration=1&from_source=&from_spmid=333.337&platform=pc&highlight=1&single_column=0&keyword={music_name}&qv_id=AQ1Gm6wQbuStxaNBMGwFitQGfDFxu6ug&ad_resource=5654&source_tag=3&category_id=&search_type=video&tids=3&dynamic_offset=0&w_rid=8e0794a5e6d66abed021cbd083aca231&wts=1675320642'

        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36 Edg/109.0.1518.61',
            'cookie': "uvid3=D7BEAF5A-CE29-1E9A-B9FB-656C929FF47452204infoc; b_nut=1665216152; buvid_fp_plain=undefined; DedeUserID=12310947; DedeUserID__ckMd5=99ff7d744bdbd759; i-wanna-go-back=-1; b_ut=5; _uuid=D33C9FD3-CEB9-9310A-9101A-4B7108310C6D3782312infoc; buvid4=3A8B56F1-EDA5-71EF-4695-376711789D2885279-022101300-3SvbbFkocEboIDHoVtJIDA%3D%3D; nostalgia_conf=-1; hit-dyn-v2=1; CURRENT_BLACKGAP=0; LIVE_BUVID=AUTO7816672198586892; hit-new-style-dyn=0; rpdid=|(J|)Y)RJ~ul0J'uYY)l~kJul; CURRENT_QUALITY=80; SESSDATA=8bd86e19%2C1690344649%2C17d1b%2A11; bili_jct=965d59cb1963a42b5d941c206af8d5fb; sid=6ux4fg8f; CURRENT_FNVAL=4048; is-2022-channel=1; fingerprint=259aa6cd16fcedba1303ea42d5f8e01f; buvid_fp=259aa6cd16fcedba1303ea42d5f8e01f; b_lsid=A10651CF3_185F34F26F6; bp_video_offset_12310947=755846388137328600; innersign=1; PVID=1"
            , 'referer': 'https://www.bilibili.com/'
        }

        response = requests.get(url=url, headers=headers)
        data = response.text
        _data = json.loads(data)
        # pprint.pprint(_data)
        Bv_data = _data['data']['result'][0]['bvid']
        title_data = _data['data']['result'][0]['title']
        print(Bv_data)
        title_data = text = re.sub('<em class="keyword">', '', title_data)
        title_data = text = re.sub('</em>', '', title_data)
        print(f"数据来源:{title_data}")
        response_ = requests.get(url=f"http://www.bilibili.com/video/{Bv_data}", headers=headers)
        main_data = response_.text

        download_ = re.findall('<script>window.__playinfo__=(.*?)</scrip', main_data, re.S)[0]
        json_data = json.loads(download_)
        audio_url = json_data['data']['dash']['audio'][0]['baseUrl']

        audio_content = requests.get(url=audio_url, headers=headers).content
        try:
            with open(f"{music_name}.mp3", mode='wb') as f:
                f.write(audio_content)
            print('下载成功')
            label7=Label(root, text=f'数据来源:{title_data}')
            label7.pack()
        except:
            print('文件名不能包含那几个自己看')


    button = Button(root, text="下载", bg="orange", command=get_input)
    button.pack()


    def myClick():
        myLabel = Label(root, text="qq1071718696")
        myLabel.pack()


    myButton = Button(root, text="联系作者", command=myClick, bg="orange", fg="white")
    myButton.pack()

    Label1 = Label(root, text='输入的文字将被用作文件名 不能包含/.*<>?等字符')
    Label2 = Label(root, text='下载后的文件将被放在与exe同级目录下')
    Label3 = Label(root, text='本程序为免费开源软件 禁止用于牟利')

    Label5 = Label(root, text='如果你在某宝某鱼购买的 请申请退款 并举报！', bg="red")
    Label6 = Label(root, text='音乐来源b站,稳定性极高,后续或许会增添导入qq音乐和网易云音乐功能', bg="yellow")
    Label1.pack()
    Label2.pack()
    Label3.pack()

    Label5.pack()
    Label6.pack()

    root.mainloop()

# 访问 https://www.jetbrains.com/help/pycharm/ 获取 PyCharm 帮助
