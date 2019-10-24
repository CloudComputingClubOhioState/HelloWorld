# Copyright 2018 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

# [START gae_python37_app]
import json
import requests
from mapbox import Static
from flask import Flask
from flask import send_file

token = "pk.eyJ1IjoiYnJpY2UtbWV0emdlciIsImEiOiJjazF0bHVkM3owMDlrM3BtdGVmd3hybHoyIn0.XvAsgBSbjTHQwHfT_JePPg"
# If `entrypoint` is not defined in app.yaml, App Engine will look for an app
# called `app` in `app.py`.
app = Flask(__name__)



@app.route('/' )
def hello():
    service = Static(access_token=token)
    my_address = {
        "type": "FeatureCollection",
        "features": [
             {
                "type": "Feature",
                "properties": {},
                "geometry": {
                    "type": "Point",
                    "coordinates": [-83.01076948642731, 39.991954218170605]
                    }
                }
            ]
    }

    this_image = service.image('mapbox.streets', features=[my_address])
    this_image.headers['Content-Type'] = 'image/png'

    maybe_image = open("testName.png", "wb")
    maybe_image.write(this_image.content)

    return send_file("testName.png")


@app.route('/someEndpoint')
def custom_response():
    return "Run This Again"

if __name__ == '__main__':
    # This is used when running locally only. When deploying to Google App
    # Engine, a webserver process such as Gunicorn will serve the app. This
    # can be configured by adding an `entrypoint` to app.yaml.
    app.run(host='127.0.0.1', port=8080, debug=True)
# [END gae_python37_app]
