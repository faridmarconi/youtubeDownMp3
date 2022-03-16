import youtube_dl

def download_ytvid_as_mp3():
    video_url = open("links_mp3.txt", "r")
    for line in video_url:
        video_info = youtube_dl.YoutubeDL().extract_info(url = line,download=False)
        filename = f"{video_info['title']}.mp3"
        options={
            'format':'bestaudio/best',
            'keepvideo':False,
            'outtmpl':filename,
        }
        with youtube_dl.YoutubeDL(options) as ydl:
            ydl.download([video_info['webpage_url']])
        print("Download complete... {}".format(filename))
download_ytvid_as_mp3()
