import requests


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
            'GET', f'https://mbasic.facebook.com/me', headers=headers, allow_redirects=True)
        open('x','w',encoding='utf-8').write(r.text)
        if 'mbasic_logout_button' in r.text:
            return True
        return False
    except:
        return None


print(checkLiveCookie('', 'sb=FTB6ZOHoZb--ycycJcwbfMux; wd=1920x969; datr=FTB6ZDUociDQLk1-hqMaoq-u; locale=hi_IN; c_user=100029047154012; xs=31%3AzL1jq6SYzwtHrQ%3A2%3A1685729334%3A-1%3A8397; fr=06R3I2TB9INzZDwKF.AWUhzOp6nSISt8UBk4iU2TXyk_A.BkejAV.VG.AAA.0.0.BkejA1.AWU-mpnVFVk; m_page_voice=100029047154012'))
