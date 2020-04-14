# Valorant Key Farm Script

## Dependencies

* Python 3.7 or higher
* twitch-python (`pip install --user twitch-python`)
* A web browser (easiest with Google Chrome)

## Usage

Clone or download this repo and `python3 valorant.py {CLIENT_ID}`. `{CLIENT_ID}` is your client id from the Twitch API - if you don't have one already you can get one [here](https://dev.twitch.tv/docs/v5#getting-a-client-id).

If you want to use a different browser than Chrome, you can provide one of the typenames from [this table](https://docs.python.org/3/library/webbrowser.html#webbrowser.register) as a second argument:
```
python3 valorant.py {CLIENT_ID} {WEB_BROWSER}
```
Remember to log into Twitch on the browser you use with this script.

If you aren't using Linux the script won't be able to kill Chrome once the stream ends.

## Valorant Key Drop System

This script is based on my current understanding of the Valorant key drop system:
- You need to be logged in to a Twitch account that's linked to a Riot account.
- You need to watch Valorant streams for at least two hours before you're even considered for a key - after that, the more you watch, the likelier you are to get a key.
- Watching more than one stream at a time doesn't improve your chances or log more watch time.
