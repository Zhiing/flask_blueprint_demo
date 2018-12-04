from flask import Flask


app = Flask(__name__)


def register():
    from service.cbb.urls import site as cbb_site

    app.register_blueprint(cbb_site)


register()
