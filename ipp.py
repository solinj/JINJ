from flask import request
from flask import jsonify
from flask import Flask
from flask import render_template
import datetime as d

import flask



app = Flask(__name__)
@app.route("/dict_dir")
def dictDir():
    return (str(request.__dict__) + "\n" + str(request.__dir__))


@app.route("/index", methods=["GET"])
def get_my_ip():
    # return render_template('template.html', ip_address=(jsonify({'ip_address': request.remote_addr}), 200))
    # print((jsonify({'ip_address': request.remote_addr}), 200))
    # return jsonify({'ip_address': request.remote_addr}), 200
    var_brow = request.user_agent.browser
    var_nav = request.headers.get('User-Agent')
    var_os = request.user_agent.platform
    var_ip = request.environ.get('ip_address', request.remote_addr)
    our_date = d.datetime.now().strftime("%A %d %B %Y %H %M")
    with open("journal.co", "a") as fo:
        writing = "--date : " + our_date + "\n" + "--informations = " + "\n" + "--browser : " + str(var_brow) + "\n" + "--navigateur : " + str(var_nav) + "\n" + "--os : " + str(var_os) + "\n" + "--adresse_ip : " + str(var_ip)
        fo.write(str(writing))
    return render_template('template.html', ip_address = var_ip, nav = var_nav, brow = var_brow, oos = var_os)

@app.route("/journal")
def printInfos():
    with open("journal.co", "r") as f:
        return render_template('template.html', lines = f)



if __name__ == '__main__':
    app.run(debug=True)