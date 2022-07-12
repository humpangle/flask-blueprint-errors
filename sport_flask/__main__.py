from . import create_app

app = create_app()


@app.route("/")
def root():
    return "ok\n"


if __name__ == "__main__":
    app.run()
