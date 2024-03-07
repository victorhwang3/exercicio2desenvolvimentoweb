from flask import Flask, render_template
import webbrowser
import threading

app1 = Flask(__name__, template_folder='pasta1')
app2 = Flask(__name__, template_folder='pasta2')

def open_browser(port):
    url = f'http://localhost:{port}'
    webbrowser.open_new(url)

@app1.route('/')
def index1():
    return render_template('index1.html')

@app2.route('/')
def index2():
    return render_template('index2.html')

if __name__ == '__main__':
    port1 = 5000
    port2 = 5001

    thread1 = threading.Thread(target=lambda: app1.run(port=port1, debug=True, use_reloader=False))
    thread2 = threading.Thread(target=lambda: app2.run(port=port2, debug=True, use_reloader=False))

    thread1.start()
    thread2.start()

    open_browser(port1)
    open_browser(port2)
