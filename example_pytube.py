from pytube import YouTube
from pytube import Playlist
import os

# 참고 1) 폴더 생성 : https://data-make.tistory.com/170
# '폴더명'을 매개변수로 받는 함수, 파라미터로 받은 폴더명과 같은 폴더가 없으면 폴더를 새로 생성해줌
def createFolder(directory):
    try:
        if not os.path.exists(directory):
            os.makedirs(directory)
    except OSError:
        print ('Error: Creating directory. ' +  directory)


# 참고 2) pytube 기본 사용법 :  https://pytube.io/en/latest/user/playlist.html
# '플레이리스트 URL'을 매개변수로 받는 함수
def playlist_download(playlist_url):
    # 플레이리스트 제목을 폴더명으로 사용하여 폴더를 생성할 것 -> 플레이리스트 이름 가져오기
    p = Playlist(playlist_url)
    
    ############################################################################
    # 참고) 아래 방법으로 간다하게 구현할 수 있으나 고해상도 영상을 다운받을 수 없음!!    
    # for video in p.videos:
    #     video.streams.first().download(DOWNLOAD_FOLDER)
    ############################################################################
    
    print(p.title)
    DOWNLOAD_FOLDER = p.title
    
    # 플레이리스트 제목으로 폴더 생성
    createFolder(DOWNLOAD_FOLDER)

    # 플레이리스트 안의 각 영상마다 URL을 가져온 후 지정한한 경로에 다운로드를 해줌
    for url in p.video_urls:
        print(url)
        yt = YouTube(url)
        stream = yt.streams.get_highest_resolution()            
        stream.download(output_path=DOWNLOAD_FOLDER)
        
    print(p.title + " 다운로드 완료\n")

if __name__ == "__main__":
    
    # 다운로드 받을 플레이리스트 url을 리스트에 넣어줌
    playlist_url =  ['https://www.youtube.com/watch?v=~~~~~~', 
                 'https://youtube.com/playlist?list=~~~~~~~~~~~',
                 'https://youtube.com/playlist?list=~~~~~~~',
                 'https://youtube.com/playlist?list=~~~~~~~~~',
                 'https://youtube.com/playlist?list=~~~~~~~~-',
                 'https://youtube.com/playlist?list=~~~~~~-5mWbx0zdG0betdeoL']
    
    # 플레이리스트 url을 담고 있는 리스트를 반복문 안 에서 다운로드 함수 매개변수에 할당해주면서 실행
    for i in playlist_url:
        playlist_download(i)