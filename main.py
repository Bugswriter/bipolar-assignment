import os
import string
import random 
from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        if 'img' not in request.files:
            return "No File Given"

        file = request.files['img']
        rand_id = ''.join(random.choices(string.ascii_lowercase + string.digits, k = 5))
        fp = 'static/in/' + rand_id  + '.jpg'
        file.save(fp)
        os.system(f"python detect.py {fp}")
        out_path = '/out/' + rand_id + '.jpg'
        return render_template("home.html", out_img=out_path)

    return render_template("home.html")

if __name__=='__main__':
    app.run(debug=True)
