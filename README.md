# Valorant Key Farm Script

## Dependencies

* Python 3.7 or higher
* twitch-python (`pip install --user twitch-python`)
* A web browser

## Usage

Clone or download this repo and `python3 valorant.py {CLIENT_ID}`. `{CLIENT_ID}` is your client id from the Twitch API - if you don't have one already you can get one [here](https://dev.twitch.tv/docs/v5#getting-a-client-id).

If you want to use a different browser than Chrome, you can provide one of the typenames from [this table](https://docs.python.org/3/library/webbrowser.html#webbrowser.register) as a second argument:
```python3 valorant.py {CLIENT_ID} {WEB_BROWSER}```
