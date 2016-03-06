from flask import Flask, request, url_for
import random

app = Flask(__name__)
app.secret_key = 'This is really unique and secret'

personne = ''

@app.route('/')
def hello_person():
    return """
        <body style="margin:60;padding:0">
        <p>What is your name?</p>
        <form method="POST" action="%s"><input name="person" /><input type="submit" value="Continue" /></form>
        </body>
        """ % (url_for('greet'),)

@app.route('/greet', methods=['POST'])
def greet():
    global personne
    personne = request.form["person"]
    greet = random.choice(["Welcome", "Hello", "Greetings", "Hi"])
    return """
        <body style="margin:60;padding:0">
        <p>%s, %s!</p>
        <p><a href="%s">Click here to begin your journey...</a></p>
        </body>
        """ % (greet, personne, url_for('intro'))

@app.route('/intro')
def intro():
    global personne
    intro = """
        <body>
        <style>
        #wrapper{
        width:640px;
        margin:0 auto;
        }

        </style>
        <div id="wrapper">
        <p>As you wander into the wood you're shaking your head in disbelief...
        kicked out of yet another pub for involvement in a brawl....nevermind the fact that
        you actually started it!</p>

        <p>While lost deeply in disgust and muttering to yourself you have failed to notice that
        the woods have become much thicker, the undergrowth sparse, the trees very large, and very
        little light filtering through to the path along which you are - <b>OOPS!</b> - tripping.</p>

        <p>You pick yourself up and dust off your nether regions, pleased to note the only damage
        is to your pride. You glance around and see to your right what appears to be a lovely
        meadow. You leave the relative safety of the path and head toward green grass and sunshine.</p>

        <p>The meadow is not large and in the center is a flat rock approximately 4 feet in diameter. On the
        rock are two items which could be considered valuable. The first is a pile of apples - 5 or 6
        at a rough count. The other is a hatchet. Unfortunately, you are only able to carry one
        of these two items.</p>

        <p>Will you pick up the hatchet, or inspect the apples?</p>
        </div>
        </body>
        """
    return """
        <body>
        <style>
        #2{
        width:640px;
        }
        .player{
        text-align:center;
        }
        .link1{
        text-align:center;
        }
        .link2{
        text-align:center;
        }
        </style>
        <div id="2">
        <p class="player">%s, %s</p>
        <p class="link1"><a href="%s">Pick up the hatchet.</a></p>
        <p class="link2"><a href="%s">Inspect the apples.</a></p>
        </div>
        </body>
        """ % (personne, intro, url_for('static', filename='option1'), url_for('static', filename='option2'))

@app.route('/static/option1')
def option1():
    option1 = """
        <body style="margin:60;padding:0">
        <p>You pick up the hatchet and realize that it was lying in a pile of what could only be
        the fecal matter of some bovine creature, perhaps <i>bos primigenius namadicus,</i> more commonly known as the
        Indian auroch. How a heap of excrement from an extinct bovine known only to have lived in south Asia before
        2000BC found its way to North America, you don't know. Maybe you're just drunk and it's merely a mass of common
        cow manure. In any case, it smells wretched and perhaps the hatchet should be cleaned before you carry on.</p>

        <p>There appears to be a river running along side the meadow. Should said river not be infested with flesh eating eels,
        it would be a great place to cleanse your newly acquired hatchet before you contract Salmonella. Alternatively, there
        is a mighty tasty looking mushroom at your feet, just begging to be consumed!</p>

        <p>Due to the effects of intense intoxification, your brain is only capable of processing one action at a time, and upon
        taking either action you will immediately forget what your other option was.</p>

        <p>How shall you proceed?</p>
        </body>
        """
    return "<p>%s</p>" % (option1)

@app.route('/static/option2')
def option2():
    global personne
    option2 = """
        <body style="margin:60;padding:0">
        <font size="24" color="red">SURPRISE PIPE BOMB!</font>

        <p>You explode into a thousand pieces.</p>
        </body>
        """
    return """
        <p>%s</p>
        <p>Nice going, %s.</p>
        """ % (option2, personne)

if __name__ == '__main__':
    app.run()
