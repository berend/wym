# wym
a Webbased Youtube Mp3extractor


## Intention of wym


Intention is to use youtube as source for mp3. Send the youtube url via a wep ui, then youtube_dl takes over, downloads
and converts to mp3. Files are then saved in a dedicated mp3 folder which is also the download cache.
So, if you download the same youtube song twice, it is already there. The player runs on the server, so connect you
audio equipment to that server (something like raspberry pi should be ok).


## Install

It should be like this:
install mpd (e.g. brew install mpd)
install this here via pip (no package yet)

## Tests

No tests yet!


## The bright future

I want to have:
- other sources than youtube
- test
- web ui (I ll start with the api first)