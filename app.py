from flask import Flask, render_template, Response
from datetime import datetime, timezone, timedelta

def create_app():
    app = Flask(__name__)

    @app.after_request
    def set_response_headers(r):
        r.headers['Cache-Control'] = 'no-cache, no-store, must-revalidate'
        r.headers['Pragma'] = 'no-cache'
        r.headers['Expires'] = '0'
        return r

    @app.route('/clock/<tmz>')
    def clock(tmz):
        tmz=float(tmz)
        return Response(
            render_template('clock.svg', time=datetime.now(timezone(timedelta(hours=tmz)))), 
            mimetype='image/svg+xml'
        )
    
    return app