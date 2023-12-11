import requests


def download_changelog(token, package, filename):
    with requests.Session() as http:
        r = http.get(
            f'https://api.github.com/repos/ZeitOnline/{package}/contents/{filename}', headers={
                'Accept': 'application/vnd.github.3.raw',
                'Authorization': f'Bearer {token}',
            })
        r.raise_for_status()
        return r.text


def extract_postdeploy(changelog):
    lines = changelog.split('\n')
    start = 0
    end = -1
    for i, line in enumerate(lines):
        if line == 'POSTDEPLOY':
            start = i + 1
        if '.. towncrier' in line:
            end = i - 1
            break

    result = '\n'.join(lines[start:end])
    if result == '- nothing':
        return None
    return result
