from .base import Notification
import logging
import requests


log = logging.getLogger(__name__)


class Slack(Notification):

    def __call__(self, channel_name, token, emoji,
                 vcs_url=None, changelog_url=None):
        if not vcs_url:
            vcs_url = f'http://github.com/ZeitOnline/{self.project}/tree/{self.version}'
        if not changelog_url:
            changelog_url = f'http://github.com/ZeitOnline/{self.project}/blob/main/CHANGES.rst'

        with requests.Session() as http:
            r = http.post(
                f'http://hackbot.zon.zeit.de/{token}/deployment/{channel_name}',
                json={
                    'project': self.project,
                    'environment': self.environment,
                    'version': self.version,
                    'emoji': emoji,
                    'vcs_url': vcs_url,
                    'changelog_url': changelog_url,
                })
            log.info('%s returned %s: %s', r.url, r.status_code, r.text)
