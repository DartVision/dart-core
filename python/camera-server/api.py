from bottle import Bottle, run, response
from camera import Camera

app = Bottle()
camera = Camera()


@app.route('/image.jpg')
def get_image():
    image = camera.capture()
    response.set_header('Content-type', 'image/jpeg')
    return image


# Start the server on the external interface
run(app, host='0.0.0.0', port=80)
