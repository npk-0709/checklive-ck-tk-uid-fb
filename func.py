import requests


class APP:
    def __init__(self) -> None:
        pass

    def checkLiveUid(self, uid: str):
        try:
            r = requests.request(
                'GET', f'https://graph2.facebook.com/v3.3/{uid}/picture?redirect=0',timeout=10)
            if 'height' in r.text and 'width' in r.text:
                return True
            return False
        except:
            return None

    def checkLiveCookie(self, cookie: str):
        try:
            headers = {
                'cookie': cookie,
                'connection': 'keep-alive',
                'cache-control': 'max-age=0',
                'sec-ch-ua-platform': '"Windows"',
                'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36'
            }
            r = requests.request(
                'GET', f'https://mbasic.facebook.com/me', headers=headers, allow_redirects=True,timeout=10)

            if 'mbasic_logout_button' in r.text:
                return True
            return False
        except:
            return None

    def checkLiveToken(self, token):
        try:
            r = requests.request(
                'GET', f'https://graph.facebook.com/v12.0/me?access_token={token}',timeout=10)
            if 'name' in r.text and 'id' in r.text:
                return True
            return False
        except:
            return None
