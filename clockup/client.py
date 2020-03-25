import requests


class Client:
    """
    API client for ClickUp
    """

    def __init__(self, api_token, api_version):
        self.api_token = api_token
        self.api_version = api_version
        self.url_prefix = f'https://api.clickup.com/api/{api_version}/'

        self.session = requests.Session()
        self.session.headers.update({"Authorization": api_token})

    def _request(self, method, route, params=None, data=None):
        resp = self.session.request(
            method,
            self.url_prefix + route,
            params=params,
            data=data
        )
        resp.raise_for_status()
        return resp.json()

    def get_teams(self):
        return self._request("GET", 'team')

    def get_spaces(self, team_id, show_archived):
        return self._request("GET", f'team/{team_id}/list?archived={show_archived}')

    def get_folders(self, space_id, show_archived):
        return self._request("GET", f'space/{space_id}/list?archived={show_archived}')

    def get_lists(self, folder_id, show_archived):
        return self._request("GET", f'folder/{folder_id}/list?archived={show_archived}')
