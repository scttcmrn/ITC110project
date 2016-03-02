from flask import Flask, request, url_for
import random

app = Flask(__name__)
app.secret_key = 'This is really unique and secret'

personne = ''

@app.route('/')
def hello_person():
    return """
        <p>What is your name?</p>
        <form method="POST" action="%s"><input name="person" /><input type="submit" value="Continue" /></form>
        """ % (url_for('greet'),)

@app.route('/greet', methods=['POST'])
def greet():
    global personne
    personne = request.form["person"]
    greet = random.choice(["Welcome", "Hello", "Greetings", "Hi"])
    return """
        <p>%s, %s!</p>
        <p><a href="%s">Begin</a></p>
        """ % (greet, personne, url_for('intro'))

@app.route('/intro')
def intro():
    global personne
    intro = "this is the introduction page"
    return """
        <p>%s, %s.</p>
        <p><a href="%s">option one</a></p>
        <p><a href="%s">option two</a></p>
        """ % (personne, intro, url_for('static', filename='option1'), url_for('static', filename='option2'))

@app.route('/static/option1')
def option1():
    option1 = "This is the result of option one."
    return "<p>%s</p>" % (option1)

@app.route('/static/option2')
def option2():
    global personne
    option2 = "This is the result of option two."
    return """
        <p>%s</p>
        <p>%s is a huge idiot.</p>
        """ % (option2, personne)

if __name__ == '__main__':
    app.run()
