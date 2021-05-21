from flask import Flask, render_template, Response
from datetime import datetime, timezone, timedelta

def create_app():
    app = Flask(__name__)

    @app.route('/clock/<tmz>')
    def clock(tmz):
        tmz=int(tmz)
        return Response(
            render_template('clock.svg', time=datetime.now(timezone(timedelta(hours=tmz)))), 
            mimetype='image/svg+xml'
        )
    
    return app