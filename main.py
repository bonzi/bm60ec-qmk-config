from flask import Flask, render_template, url_for
from random import randint
app = Flask(__name__)


"""
Is this a quick and Dirty bodge? Yes.
Is it better than having to use jQuery in the browser? 100%
"""
bgs = [
    'https://media.giphy.com/media/3oEduF1bUfWc1moXzq/giphy.gif',
    'https://media.giphy.com/media/3oEdv4idg2DBlVCU6I/giphy.gif',
    'https://media.giphy.com/media/l41m1Zg0lxRbvHWcU/giphy.gif',
    'https://media.giphy.com/media/3oEdv1Mnz8oM0oZq48/giphy.gif',
    'https://media.giphy.com/media/3o85gd3noLuSkE4Lkc/giphy.gif',
    'http://media.tumblr.com/tumblr_ma3s22ZEO61qg7p8h.gif',
    'https://media.giphy.com/media/26vIdwyqU5FuUG27m/giphy.gif',
    'https://media.giphy.com/media/BqTukQ50m74Y0/giphy.gif',
]

@app.route('/')
def index():
    rand = randint(0, 7)
    return render_template('wulf.html', bg=bgs[rand])

if __name__ == '__main__':
  app.run(host='127.0.0.1', port=8000, debug=True)
 