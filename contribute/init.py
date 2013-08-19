from flask import Flask, render_template
app = Flask(__name__)


@app.route("/")
def hello():
    return render_template("index.html")


@app.route("/vote", methods=['GET'])
def show_vote():
    return render_template("vote.html",
                           project='fortune',
                           proposal='this is funny!')


@app.route("/choose_project", methods=['GET'])
def choose_project():
    return render_template("choose_project.html",
                           projects=['bob', 'ross'])


@app.route("/new_entry/<name>", methods=['GET'])
def create_entry(name):
    return render_template("new_entry.html",
                           project=name)


@app.route("/vote/<how>", methods=['POST', 'PUT'])
def retrieve_vote(how):
    voting = True
    if how == 'funny':
        pass
    elif how == 'lame':
        voting = False
    else:
        return 'fuck off'

    # get current project and proposal
    # check for timeout
    return str(voting)

if __name__ == "__main__":
    app.debug = True
    app.run(host="0.0.0.0", port=8082)
