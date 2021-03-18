import flask
from camera import Camera

app = flask.Flask(__name__)
camera = Camera()

@app.route('/image.jpg')
def get_image():
    response = flask.Response()
    image = camera.capture()
    response.headers['Content-type'] = 'image/jpeg'
    headers = {'Content-type': 'image/jpeg'}
    return image, headers


# Start the server on the external interface
app.run(host='0.0.0.0', port=8082, threaded=True)
