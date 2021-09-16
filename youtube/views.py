from django.shortcuts import render

import json
import urllib.request
import string
import random

API_KEY = "AIzaSyCEeAi2pdn8YaGlOk2Wu1O8BhM7N8i1vsA"

def generateRandomString(N):
  return ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(N))
  
def getListVideo():
  count = 21
  random = generateRandomString(2)
  regionCode = "ID"
  urlApi = "https://www.googleapis.com/youtube/v3/search?key={}&maxResults={}&part=snippet&type=video&q={}&regionCode={}".format(API_KEY, count, random, regionCode)
  
  webUrl = urllib.request.urlopen(urlApi)
  data = webUrl.read()
  encoding = webUrl.info().get_content_charset('utf-8')
  result = json.loads(data.decode(encoding))
  
  return result
  
def getVideo(idVideo):
  urlApi = "https://www.googleapis.com/youtube/v3/videos?key={}&part=snippet,statistics&type=video&id={}".format(API_KEY, idVideo)
  
  webUrl = urllib.request.urlopen(urlApi)
  data = webUrl.read()
  encoding = webUrl.info().get_content_charset('utf-8')
  result = json.loads(data.decode(encoding))
  
  return result
  

def getChannel(idch):
  urlApi = "https://www.googleapis.com/youtube/v3/channels?part=snippet,statistics,brandingSettings&id={}&key={}".format(idch, API_KEY)
  
  webUrl = urllib.request.urlopen(urlApi)
  data = webUrl.read()
  encoding = webUrl.info().get_content_charset('utf-8')
  result = json.loads(data.decode(encoding))
  
  return result
  

def getCommandVideo(idVideo):
  count = 50
  urlApi = "https://www.googleapis.com/youtube/v3/commentThreads?key={}&textFormat=plainText&part=snippet&videoId={}&maxResults={}".format(API_KEY, idVideo, count)
  
  webUrl = urllib.request.urlopen(urlApi)
  data = webUrl.read()
  encoding = webUrl.info().get_content_charset('utf-8')
  result = json.loads(data.decode(encoding))
  
  return result
  
  
def getSearchVideo(q):
  count = 50
  urlApi = "https://www.googleapis.com/youtube/v3/search?part=snippet&type=video&q={}&key={}&maxResults={}".format(q, API_KEY, count)
  
  webUrl = urllib.request.urlopen(urlApi)
  data = webUrl.read()
  encoding = webUrl.info().get_content_charset('utf-8')
  result = json.loads(data.decode(encoding))
  
  return result
  

def getPlaylist(idch):
  urlApi = "https://www.googleapis.com/youtube/v3/playlists?part=snippet&channelId={}&maxResults=50&key={}".format(idch, API_KEY)
  
  webUrl = urllib.request.urlopen(urlApi)
  data = webUrl.read()
  encoding = webUrl.info().get_content_charset('utf-8')
  result = json.loads(data.decode(encoding))
  
  return result
  

def getVideoByChannel(chid, maxres = 50):
  urlApi = "https://www.googleapis.com/youtube/v3/search?order=date&part=snippet&channelId={}&maxResults={}&key={}".format(chid, maxres, API_KEY)
  
  webUrl = urllib.request.urlopen(urlApi)
  data = webUrl.read()
  encoding = webUrl.info().get_content_charset('utf-8')
  result = json.loads(data.decode(encoding))
  
  return result
  
def getVideoInPlaylist(idPlay):
  urlApi = "https://www.googleapis.com/youtube/v3/playlistItems?part=snippet&playlistId={}&key={}&maxResults=50".format(idPlay, API_KEY)
  
  webUrl = urllib.request.urlopen(urlApi)
  data = webUrl.read()
  encoding = webUrl.info().get_content_charset('utf-8')
  result = json.loads(data.decode(encoding))
  
  return result
  
def month(no):
  month = ''
  if no == '01':
    month = 'January'
  elif no == '02':
    month = 'February'
  elif no == '03':
    month = 'March'
  elif no == '04':
    month = 'April'
  elif no == '05':
    month = 'May'
  elif no == '06':
    month = 'June'
  elif no == '07':
    month = 'July'
  elif no == '08':
    month = 'August'
  elif no == '09':
    month = 'September'
  elif no == '10':
    month = 'October'
  elif no == '11':
    month = 'November'
  elif no == '12':
    month = 'December'
  else:
    month = 'None'
  
  return month

# Create your views here.
def IndexView(req):
  listVideo = getListVideo()
  
  context = {
    'title' : 'Home',
    'list_video' : listVideo['items'],
  }
  
  return render(req, 'yt/index.html', context)
  
  
def resultView(req, *args, **kwargs):
  keyword = kwargs['keyword']
  resultSearch = getSearchVideo(keyword)
  
  context = {
    'title' : 'Result Search',
    'title_video' : "Some quick example text to build on the card title and make up the bulk of the card's content.",
    'keywordSearch' : keyword,
    'resultSearch' : resultSearch['items'],
  }
  
  return render(req, 'yt/result.html', context)
  
  
def singleVideoView(req, *args, **kwargs):
  videoId = kwargs['videoId']
  chid = kwargs['chId']
  
  video = getVideo(videoId)
  channel = getChannel(chid)
  command = getCommandVideo(videoId)
  video_list = getListVideo()
  
  for date in video['items']:
    pub = date['snippet']['publishedAt']
    pub2 = date['snippet']['publishedAt']
    
  pub = pub.split('-')
  pub2 = pub2.split('-')[2]
  pub2 = pub2.split('T')
  
  monthCh = pub[1]
  monthVar = month(monthCh)
  
  context = {
    'title' : 'Single Video',
    'title_video' : "Some quick example text to build on the card title and make up the bulk of the card's content.",
    'video' : video,
    'id' : videoId,
    'channel' : channel,
    'command' : command,
    'video_list' : video_list['items'],
    'pub' : pub,
    'pub2' : pub2,
    'month' : monthVar,
  }
  
  return render(req, 'yt/singleVideo.html', context)
  

def listPlay(req, *args, **kwargs):
  idPlay = kwargs['playId']
  chId = kwargs['chId']
  
  videoPlay = getVideoInPlaylist(idPlay)
  playlist = getPlaylist(chId)
  
  for date in playlist['items']:
    pub = date['snippet']['publishedAt']
    pub2 = date['snippet']['publishedAt']
    
  pub = pub.split('-')
  pub2 = pub2.split('-')[2]
  pub2 = pub2.split('T')
  
  monthCh = pub[1]
  monthVar = month(monthCh)
  
  context = {
    'title' : 'Show Playlist Video',
    'videoPlay' : videoPlay,
    'playlist' : playlist,
    'idPlay' : idPlay,
    'monthVar' : monthVar,
    'pub' : pub,
    'pub2' : pub2,
  }
  
  return render(req, 'yt/listPlay.html', context)
  
def myTools(req, *args, **kwargs):
  context = {
    'title' : 'Fbaz Tools',
  }
  
  return render(req, 'yt/listTools.html', context)
  
def coomingSoon(req, *args, **kwargs):
  context = {
    'title' : 'Cooming Soon Page',
  }
  
  return render(req, 'yt/coomingSoon.html', context)
  

def chanel(req, *args, **kwargs):
  chId = kwargs['chId']
  
  chanel = getChannel(chId)
  videoBeranda = getVideoByChannel(chId, 3)
  
  context = {
    'title' : 'Show Chanel',
    'chanel' : chanel,
    'videoBeranda' : videoBeranda['items'],
    'main' : 'berandaTemplate',
  }
  
  return render(req, 'yt/chanel.html', context)
  
  
def chanelVideo(req, *args, **kwargs):
  chId = kwargs['chId']
  
  chanel = getChannel(chId)
  video = getVideoByChannel(chId)
  
  context = {
    'title' : 'Show Chanel',
    'chanel' : chanel,
    'video' : video['items'],
    'main' : 'videoTemplate',
  }
  
  return render(req, 'yt/chanel.html', context)

def chanelPlay(req, *args, **kwargs):
  chId = kwargs['chId']
  
  chanel = getChannel(chId)
  playlist = getPlaylist(chId)
  
  context = {
    'title' : 'Show Chanel',
    'chanel' : chanel,
    'playlist' : playlist,
    'main' : 'playTemplate',
  }
  
  return render(req, 'yt/chanel.html', context) 

def chanelDet(req, *args, **kwargs):
  chId = kwargs['chId']
  
  chanel = getChannel(chId)
  
  for date in chanel['items']:
    pub = date['snippet']['publishedAt']
    pub2 = date['snippet']['publishedAt']
    
  pub = pub.split('-')
  pub2 = pub2.split('-')[2]
  pub2 = pub2.split('T')
  
  monthCh = pub[1]
  monthVar = month(monthCh)
  
  context = {
    'title' : 'Show Chanel',
    'chanel' : chanel,
    'main' : 'detailTemplate',
    'pub' : pub,
    'pub2' : pub2,
    'month' : monthVar,
  }
  
  return render(req, 'yt/chanel.html', context) 

