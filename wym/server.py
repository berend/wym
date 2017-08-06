from sanic import Sanic
from sanic.response import json
from wym.playlist import Playlist

app = Sanic()

playlist = Playlist()

queue = []

@app.route("/add", methods=['POST'])
async def add_url(request):
    return json({"hello": "world"})


@app.route("/playlist", methods=['GET'])
async def show_playlist(request):
    return json(playlist.as_dict())

@app.route("/downloadqueue", methods=['GET'])
async def show_download_queue(request):
    return json({"queue": queue})

@app.route("/control", methods=['POST'])
async def show_download_queue(request):
    return json({})



if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)