from flask import Flask, render_template, Response
from datetime import datetime

def create_app():
    app = Flask(__name__)

    @app.route('/clock.svg')
    def clock():
        return Response(
            render_template('clock.svg', time=datetime.today()), 
            mimetype='image/svg+xml'
        )
    return app