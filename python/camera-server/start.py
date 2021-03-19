import flask
from flask_cors import CORS, cross_origin
import argparse
from datetime import datetime
from os import path
from camera import Camera

app = flask.Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

@app.route('/image.jpg')
def get_image():
    response = flask.Response()
    image = camera.capture()
    response.headers['Content-type'] = 'image/jpeg'
    headers = {'Content-type': 'image/jpeg'}
    return image, headers

@app.route('/capture', methods=['POST'])
@cross_origin()
def capture_image():
    """
    Expect the token as application/json
    :return:
    """
    if flask.request.content_type != 'text/plain':
        return 'bad request!', 400
    token = flask.request.data.decode("utf-8")
    image = camera.capture()

    today = datetime.today().strftime('%Y_%m_%d_%H_%M_%S')
    filename = today + '_' + token + '.jpeg'
    with open(path.join(path.expanduser(image_path), filename), 'wb') as file:
        file.write(image)
    return ''


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='')
    parser.add_argument('port', help=' port on which the server should be started.')
    parser.add_argument('image_path', help=' where the captured images should be stored.')
    args = parser.parse_args()
    image_path = args.image_path
    port = args.port

    camera = Camera()
    # Start the server on the external interface
    app.run(host='0.0.0.0', port=port, threaded=True)
