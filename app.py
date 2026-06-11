try:
    import importlib
    flask = importlib.import_module("flask")
    Flask = flask.Flask
except ImportError:
    Flask = None

if Flask:
    app = Flask(__name__)

    @app.route("/")
    def home():
        return "Hello from Kubernetes Flask App 🚀"

    if __name__ == "__main__":
        app.run(host="0.0.0.0", port=5000)
else:
    from wsgiref.simple_server import make_server

    def home():
        return "Hello from Kubernetes Flask App 🚀"

    def simple_app(environ, start_response):
        if environ.get("PATH_INFO", "/") == "/":
            start_response("200 OK", [("Content-Type", "text/plain; charset=utf-8")])
            return [home().encode("utf-8")]
        start_response("404 Not Found", [("Content-Type", "text/plain; charset=utf-8")])
        return [b"Not Found"]

    if __name__ == "__main__":
        with make_server("0.0.0.0", 5000, simple_app) as server:
            server.serve_forever()