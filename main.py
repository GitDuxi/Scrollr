import flask

app = flask.Flask(__name__)


@app.route('/')
def index():
    return flask.send_file("index.html")
    #return flask.redirect("https://barescroll.duxi.repl.co/index.html")

if __name__ == '__main__':
  app.run(host='0.0.0.0', port=5000)
