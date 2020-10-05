from bottle import Bottle, run, response
from led_strip import LedStrip

led_strip = LedStrip()
app = Bottle()


@app.post('/toggle')
def toggle():
    print('toggling...')
    led_strip.toggle_light()
    response.set_header('Access-Control-Allow-Origin',  '*')
    response.set_header('Access-Control-Allow-Methods',  'GET, POST, PATCH, PUT, DELETE, OPTIONS')
    response.set_header('Access-Control-Allow-Headers',  'Origin, Content-Type, X-Auth-Token')
    return


@app.get('/status')
def status():
    return led_strip.get_status()


# Start the server on the external interface
run(app, host='0.0.0.0', port=80)
