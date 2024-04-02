# 大佬的b站下音乐音乐
import requests
import re
import pprint
import json

if __name__ == '__main__':

    music_name = input("请输入您想下载的歌曲名字")
    url = f'https://api.bilibili.com/x/web-interface/wbi/search/all/v2?' \
        f'__refresh__=true&_extra=&context=&page=1&page_size=42&order=' \
        f'&duration=&from_source=&from_spmid=333.337&platform=pc&' \
        f'highlight=1&single_column=0&keyword={music_name}'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
                      'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36 Edg/109.0.1518.61',
     
        'referer': 'https://www.bilibili.com/'
    }

    response = requests.get(url=url, headers=headers)
    data = response.text
    _data = json.loads(data)
    # pprint.pprint(_data)
    Bv_data = _data['data']['result'][10]['data'][0]['bvid']
    title_data = _data['data']['result'][10]['data'][0]['description']
    print(Bv_data)
    print(f"数据来源:{ title_data}")
    main_url = re.search(r'', data, re.S)

    response_ = requests.get(url=f"http://www.bilibili.com/video/{Bv_data}", headers=headers)
    main_data = response_.text

    download_ = re.findall('<script>window.__playinfo__=(.*?)</scrip', main_data, re.S)[0]
    json_data = json.loads(download_)
    audio_url = json_data['data']['dash']['audio'][0]['baseUrl']
    print(audio_url)
    audio_content = requests.get(url=audio_url, headers=headers).content
    with open(f"{music_name}.mp3", mode='wb')as f:
        f.write(audio_content)
    print('over')

# 访问 https://www.jetbrains.com/help/pycharm/ 获取 PyCharm 帮助
