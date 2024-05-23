import requests
import os
import re
import json
import subprocess

request_url = input("input the Url of video:")
# resolution_radio = input("please input the resolution radio order(0-highest, 1-minor, -1-lowest):")

headers = {
        "User-Agent" : "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36",
        "Cookie" : "buvid3=953D19AB-1601-83C6-3DEC-15E02F1E8B5C42015infoc; b_nut=1711019142; i-wanna-go-back=-1; b_ut=7; _uuid=79105BF6A-E7F8-84106-BD6B-E32D6D748F8942390infoc; buvid4=401C3EAB-D471-D298-3DE4-63ED1470C2E043099-024032111-7vUXCeBPzNLXQNuHx80Tyg%3D%3D; DedeUserID=497109937; DedeUserID__ckMd5=cf2042fb0f1c4994; CURRENT_FNVAL=4048; rpdid=|(RYk~~kl|m0J'u~uu|um~Rl; buvid_fp_plain=undefined; enable_web_push=ENABLE; iflogin_when_web_push=1; FEED_LIVE_VERSION=V_DYN_LIVING_UP; header_theme_version=CLOSE; SESSDATA=2582241f%2C1728051759%2C20f48%2A41CjBiKqMOkopjIV9Nr-bX-AgYVd1DW-2grjZQPzQ36VYOpDuezLit5hoO9zvfklIycEoSVlB6SkNTNEhOUTdrWkh0Y3VEVll5M1ljM2JWUU1MT0tyanhXamYzY2w5ZHZ0dVk4TkZDT0N5bkswd0VVZVBGUl9QS2ZCZXNCWUtMcXB5YmxYNE5tR2VRIIEC; bili_jct=21d42b8068db67360f39c3dc70737c34; sid=4wbtfc26; CURRENT_QUALITY=120; home_feed_column=5; browser_resolution=1710-949; bili_ticket=eyJhbGciOiJIUzI1NiIsImtpZCI6InMwMyIsInR5cCI6IkpXVCJ9.eyJleHAiOjE3MTYyNzY4OTEsImlhdCI6MTcxNjAxNzYzMSwicGx0IjotMX0.iX9OyqK9CcfgNSszYKZQjIGKylj4N_bddYK9Dyqpwtw; bili_ticket_expires=1716276831; fingerprint=9724634b1f311c119545df1b1ba12a39; PVID=1; bp_t_offset_497109937=933580724816052249; b_lsid=6F2D7B79_18F98CFB928; bmg_af_switch=1; bmg_src_def_domain=i1.hdslb.com; buvid_fp=e4b29258f27aaa0616a80aac13df2de0",
        "Referer" : "https://www.bilibili.com/"
    }
response_html = requests.get(request_url, headers=headers).text
playinfo = re.findall("<script>window.__playinfo__=(.*?)</script>", response_html)[0]
playinfo = json.loads(playinfo)
# get the title of the video
title = re.findall('<h1 data-title="(.*?)"', response_html)
title = title[0]
# get the url of video and audio
video_url = playinfo['data']['dash']['video'][0]['baseUrl']
audio_url = playinfo['data']['dash']['audio'][0]['baseUrl']
# get the content of video and audio
video_content = requests.get(video_url, headers=headers).content
audio_content = requests.get(audio_url, headers=headers).content
# creat a folder named this video
folder_name = input("Please input the name of this foler:")
path_save_scrape_file = f"/Users/dfyy/Documents/Personal_Code/{folder_name}"
os.mkdir(path=path_save_scrape_file)
# save the video and audio to the folder
with open(path_save_scrape_file + '/video.mp4', 'wb') as video:
    video.write(video_content)
with open(path_save_scrape_file + '/audio.mp3', 'wb') as audio:
    audio.write(audio_content)
'''
# use ffmpeg to convert video and audio to mp4
cmd_ffmpeg = "ffmpeg"
cmd_cd = f"cd {path_save_scrape_file}"
cmd_convert = f"ffmpeg -i video.mp4 -i audio.mp3 -c:v copy -c:a copy output.mp4"
subprocess.run(cmd_ffmpeg)
subprocess.run(cmd_cd)
subprocess.run(cmd_convert)
'''