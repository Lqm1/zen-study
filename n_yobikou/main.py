import httpx
from bs4 import BeautifulSoup, Tag

from models import (
    User,
    Notice,
)

class NotLoggedInError(Exception):
    pass

class InternalError(Exception):
    pass

class LoginError(Exception):
    pass

class NYobikou:
    def __init__(self, _zane_session: str | None = None) -> None:
        self._zane_session = _zane_session
        cookies = {
            '_zane_session': self._zane_session,
        } if self._zane_session else {}
        headers = {
            'accept': 'application/json, text/plain, */*',
            'accept-language': 'ja',
            'dnt': '1',
            'origin': 'https://www.nnn.ed.nico',
            'priority': 'u=1, i',
            'referer': 'https://www.nnn.ed.nico/',
            'sec-ch-ua': '"Chromium";v="124", "Google Chrome";v="124", "Not-A.Brand";v="99"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-site',
            'sec-gpc': '1',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36',
        }
        self.client = httpx.Client(headers=headers, cookies=cookies, http2=True, follow_redirects=True)

    def login_by_n_high_school(self, login_id: str, password: str):
        """N高等学校でログインする

        Args:
            login_id (str): 学籍番号
            password (str): パスワード

        Raises:
            InternalError: 内部エラー
            LoginError: 学籍番号またはパスワードが違います。

        Returns:
            User: 自分自身のユーザー情報
        """
        response = self.client.get('https://www.nnn.ed.nico/oauth_login?next_url=https://www.nnn.ed.nico/home&target_type=n_high_school_mypage')
        soup = BeautifulSoup(response.text, 'html.parser')
        request_id_found = soup.find('input', {'name': 'requestId'})
        if not request_id_found or not isinstance(request_id_found, Tag):
            raise InternalError('requestId not found')
        request_id = request_id_found.get('value')
        _token_found = soup.find('input', {'name': '_token'})
        if not _token_found or not isinstance(_token_found, Tag):
            raise InternalError('_token not found')
        _token = _token_found.get('value')
        data = {
            'requestId': request_id,
            'loginId': login_id,
            'password': password,
            '_token': _token,
        }
        response = self.client.post('https://secure.nnn.ed.jp/mypage/oauth/login', data=data)
        if response.url != 'https://www.nnn.ed.nico/home':
            raise LoginError('login failed')
        self._zane_session = self.client.cookies.get('_zane_session')
        if not self._zane_session:
            raise InternalError('_zane_session not found')
        response = self.client.get('https://api.nnn.ed.nico/v1/users')
        user = User.model_validate(response.json())
        return user

    def login_by_s_high_school(self, login_id: str, password: str):
        """S高等学校でログインする

        Args:
            login_id (str): 学籍番号
            password (str): パスワード

        Raises:
            InternalError: 内部エラー
            LoginError: 学籍番号またはパスワードが違います。

        Returns:
            User: 自分自身のユーザー情報
        """
        response = self.client.get('https://www.nnn.ed.nico/oauth_login?next_url=https://www.nnn.ed.nico/home&target_type=s_high_school_mypage')
        soup = BeautifulSoup(response.text, 'html.parser')
        request_id_found = soup.find('input', {'name': 'requestId'})
        if not request_id_found or not isinstance(request_id_found, Tag):
            raise InternalError('requestId not found')
        request_id = str(request_id_found['value'])
        _token_found = soup.find('input', {'name': '_token'})
        if not _token_found or not isinstance(_token_found, Tag):
            raise InternalError('_token not found')
        _token = str(_token_found['value'])
        data = {
            'requestId': request_id,
            'loginId': login_id,
            'password': password,
            '_token': _token,
        }
        response = self.client.post('https://s-secure.nnn.ed.jp/mypage/oauth/login', data=data)
        if response.url != 'https://www.nnn.ed.nico/home':
            raise LoginError('login failed')
        self._zane_session = self.client.cookies.get('_zane_session')
        if not self._zane_session:
            raise InternalError('_zane_session not found')
        response = self.client.get('https://api.nnn.ed.nico/v1/users')
        user = User.model_validate(response.json())
        return user

    def get_user(self):
        """自分自身のユーザー情報を取得する

        Raises:
            NotLoggedInError: ログインしていません

        Returns:
            User: 自分自身のユーザー情報
        """
        if not self._zane_session:
            raise NotLoggedInError('not logged in')
        response = self.client.get('https://api.nnn.ed.nico/v1/users')
        user = User.model_validate(response.json())
        return user

    def get_unread_notices(self):
        """未読のお知らせを取得する

        Raises:
            NotLoggedInError: ログインしていません

        Returns:
            list[Notice]: 未読のお知らせ
        """
        if not self._zane_session:
            raise NotLoggedInError('not logged in')
        response = self.client.get('https://api.nnn.ed.nico/v1/notices/unreads')
        print(response.json())
        notices = [Notice.model_validate(notice) for notice in response.json()['notices']]
        return notices

if __name__ == '__main__':
    from dotenv import load_dotenv
    load_dotenv()
    import os
    n_yobikou = NYobikou(os.getenv('ZANE_SESSION'))
    # user = n_yobikou.login_by_s_high_school(input('学籍番号: '), input('パスワード: '))
    notices = n_yobikou.get_unread_notices()
    print(notices)