# ライブラリ
import tweepy
import requests
import urllib.parse
import base64
import sys, os, asyncio
import importlib

try:
    sys.path.append(os.path.dirname(sys.argv[0]))
    config = importlib.import_module('config')
except Exception as e:
    print(e)
    print('Please make [config.py] and put it with this directory')
    input() # stop for error!!

# Consumer Keys
ck = config.API_Key
cs = config.API_Key_Secret

# Authentication Tokens
bt = config.Bearer_Token
at = config.ACCESS_TOKEN
ats = config.ACCESS_TOKEN_SECRET

# 認証
client = tweepy.Client(
    bearer_token=bt,
    consumer_key=ck, consumer_secret=cs,
    access_token=at, access_token_secret=ats
)

class ChatbotStorage:
    def __init__(self):
        self.ready = bool
        self.channel = None
        self.threads = [None, None, None, None, None]
        self.so_args = ["", "", "", "", ""]

    def getUIDfromName(self, name):
        if name == "":
            return None
        r = requests.get('https://api.twitch.tv/helix/users?login=' + name, headers=self.header)
        if r.status_code == requests.codes.ok:
            if len(r.json()['data']) > 0:
                return r.json()['data'][0]['id']
        return None

    def getChannelInfo(self, cid):
        if cid == None:
            return None
        r = requests.get('https://api.twitch.tv/helix/channels?broadcaster_id=' + cid, headers=self.header)
        if r.status_code == requests.codes.ok:
            if len(r.json()['data']) > 0:
                return r.json()['data'][0]
        return None

def PostAction():
    th = {'Authorization': 'OAuth ' + config.OAUTH.replace('oauth:', '') }
    r = requests.get('https://id.twitch.tv/oauth2/validate', headers=th)
    dat.header = {
        'Authorization': 'Bearer '+ config.OAUTH.replace('oauth:', ''),
        'Client-ID': r.json()['client_id'],
    }

    uid = dat.getUIDfromName(config.Twitch_Channel)
    cinfo = dat.getChannelInfo(uid)
    chn=cinfo['title']

#ツイート内容
    args_count = len(sys.argv) - 1
    if not args_count==0:
        try:
            posttext=urllib.parse.unquote(base64.b64decode(sys.argv[1]).decode())
        except:
            posttext=urllib.parse.unquote(sys.argv[1])
    else:
        posttext=urllib.parse.unquote(config.Default_Message.replace('{title}',chn).replace('{X}',config.Twitter_Channel).replace('{Twitch}',"https://twitch.tv/"+config.Twitch_Channel))
#ツイート
    client.create_tweet(text=posttext)
    #print(posttext)

dat = ChatbotStorage()
        
if __name__ == "__main__":
    ChatbotStorage()
    PostAction()
    sys.exit
