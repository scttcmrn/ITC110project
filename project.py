from flask import Flask, request, url_for
import random

app = Flask(__name__)
app.secret_key = 'This is really unique and secret'

personne = ''
health = 100
mushroom = 0
hatchet = 0

@app.route('/')
def hello_person():
    return """
        <body style="margin:60;padding:0">
        <style>
        #wrapper{
        width:640px;
        margin:0 auto;
        }
        .yourname{
        width:640px;
        margin:0 auto;
        }
        .form1{
        width:640px;
        margin:0 auto;
        }
        </style>
        <div id="wrapper">
        <p class="yourname">What is your name?</p>
        <p class="break"> </p>
        <form class="form1" method="POST" action="%s"><input name="person" /><input type="submit" value="Continue" /></form>
        </div>
        </body>
        """ % (url_for('greet'),)

@app.route('/greet', methods=['POST'])
def greet():
    global personne
    global health
    health = 100

    personne = request.form["person"]
    greet = random.choice(["Welcome", "Hello", "Greetings", "Hi"])
    return """
        <body style="margin:60;padding:0">
        <style>
        #wrapper{
        width:640px;
        margin:0 auto;
        }
        .namegreet{
        width:640px;
        margin:0 auto;
        }
        .link{
        width:640px;
        margin:0 auto;
        }
        </style>
        <div id="wrapper">
        <p class="namegreet">%s, %s!</p>
        <p class="healthval"><font color="green">Health: %i</font></p>
        <p class="break"> </p>
        <p class="link"><a href="%s">Click here to begin your journey...</a></p>
        </div>
        </body>
        """ % (greet, personne, health, url_for('intro'))

@app.route('/intro')
def intro():
    global personne
    global health
    health = health - 1

    intro = """
        <body>
        <style>
        #wrapper{
        width:640px;
        margin:0 auto;
        }

        </style>
        <div id="wrapper">
        <p>As you wander out of town and into the woods you're shaking your head in disbelief...
        Kicked out of yet another pub for involvement in a brawl... Nevermind the fact that
        you started it!</p>

        <p>While lost deeply in disgust and muttering to yourself you have failed to notice that
        the woods have become much thicker, the undergrowth sparse, the trees very large, and very
        little light filtering through to the path along which you are - <b>OOPS!</b> - tripping.
        <font color="red">(Health - 1)</font></p>

        <p>You pick yourself up and dust off your nether regions, pleased to note the only damage
        is to your pride. <font color="orange">(Pride - 1)</font> You glance around and see to your right what appears to be a lovely
        meadow. You leave the relative safety of the path and head toward green grass and sunshine.</p>

        <p>The meadow is not large and in the center is a flat rock approximately 4 feet in diameter. On the
        rock are two items which could be considered valuable. The first is a pile of apples - 5 or 7
        at a rough count. The other is a hatchet. Unfortunately, you are only able to carry one
        of these two items.</p>

        <p>Will you pick up the hatchet, or inspect the apples?</p>
        </div>
        </body>
        """
    return """
        <body>
        <style>
        #wrapper{
        width:640px;
        margin:0 auto;
        }
        .player{
        width:640px;
        margin:0 auto;
        }
        .link1{
        width:640px;
        margin:0 auto;
        }
        .link2{
        width:640px;
        margin:0 auto;
        }
        </style>
        <div id="wrapper">
        <p class="player">%s,%s</p>
        <p class="healthval"><font color="green">Health: %i</font></p>
        <p class="link1"><a href="%s">Pick up the hatchet.</a></p>
        <p class="link2"><a href="%s">Inspect the apples.</a></p>
        </div>
        </body>
        """ % (personne, intro, health, url_for('static', filename='option1'), url_for('static', filename='option2'))

@app.route('/static/option1')
def option1():
    global health
    global hatchet
    hatchet = hatchet + 1

    option1 = """
        <body>
        <style>
        #wrapper{
        width:640px;
        margin:0 auto;
        }

        </style>
        <div id="wrapper">
        <p>You pick up the hatchet before realizing it was lying in a pile of what could only be
        the fecal matter of some mammalian creature, perhaps <i>bos primigenius namadicus,</i> more commonly known as the
        Indian auroch. How a heap of excrement from an extinct bovine known only to have lived in south Asia before
        2000BC found its way to North America, you don't know. Maybe you're just drunk and it's merely a mass of common
        cow manure. In any case, it smells wretched and perhaps the hatchet should be cleaned before you carry on.</p>

        <p>There appears to be a river running along side the meadow. Should said river not be infested with flesh eating eels,
        it would be a great place to cleanse your newly acquired hatchet before you contract Salmonella. Alternatively, there
        is a mighty tasty looking mushroom at your feet, just begging to be consumed!</p>

        <p>Due to the effects of intense intoxification, your brain is only capable of processing one action at a time, and upon
        taking either action you will immediately forget what your other option was.</p>

        <p>How shall you proceed?</p>
        </div>
        </body>
        """
    return """
        <body>
        <style>
        #wrapper{
        width:640px;
        margin:0 auto;
        }
        .text{
        width:640px;
        margin:0 auto;
        }
        .link1{
        width:640px;
        margin:0 auto;
        }
        .link2{
        width:640px;
        margin:0 auto;
        }
        </style>
        <div id="wrapper">
        <p class="text">%s</p>
        <p class="healthval"><font color="green">Health: %i</font></p>
        <p class="link1"><a href="%s">Clean the feces from the hatchet.</a></p>
        <p class="link2"><a href="%s">Consume that delicious looking mushroom.</a></p>
        """ % (option1, health, url_for('static', filename='option11'), url_for('static', filename='option12'))

@app.route('/static/option11')
def option11():
    global health
    health = health - 1
    global mushroom
    mushroom = 0

    option11 = """
        <body>
        <style>
        #wrapper{
        width:640px;
        margin:0 auto;
        }

        </style>
        <div id="wrapper">
        <p>You near the river and dip your hand and hatchet into the current to rid both of the accumulated fecal matter.</p>
        <p>Ouch. <font color="red">(Health - 1)</font> Something just nibbled your fingertip. What was that?</p>
        <p><font size="10">OH GOD, EELS!</font></p>
        <p>A group of massive, man-eating eels emerges from the river! You run for dear life as they chase you across the
        meadow.</p>
        <p>Do you run back they way you came, or do you run into the thick woods?</p>
        </div>
        </body>
        """
    return """
        <body>
        <style>
        #wrapper{
        width:640px;
        margin:0 auto;
        }
        .text{
        width:640px;
        margin:0 auto;
        }
        .link1{
        width:640px;
        margin:0 auto;
        }
        .link2{
        width:640px;
        margin:0 auto;
        }
        </style>
        <div id="wrapper">
        <p class="text">%s</p>
        <p class="healthval"><font color="green">Health: %i</font></p>
        <p class="asdasd">Without time to think about how eels are able to traverse land, you:</p>
        <p class="link1"><a href="%s">Run back the way you came!</a></p>
        <p class="link2"><a href="%s">Run into the woods!</a></p>
        """ % (option11, health, url_for('static', filename='option111'), url_for('static', filename='option112'))

@app.route('/static/option111')
def option111():
    global health
    health = health - 60

    option111 = """
        <body>
        <style>
        #wrapper{
        width:640px;
        margin:0 auto;
        }

        </style>
        <div id="wrapper">
        <p>You decide it's best to run back the way you came.</p>
        <p>With the giant eels in hot persuit, you run past the large rock where you found the hatchet. The pile of apples
        still sits upon it. Looking back, you notice one of the flesh-hungry eels inspecting the apples.</p>
        <p><font size="10" color="red">BOOM</font></p>
        <p>You are knocked off your feet. <font color="red">(Health - 60)</font>
        <p>Apparently there was some kind of explosive device under that pile of apples because all the giant man-eating eels
        just blew to freaking smithereens!</p>
        <p>Unfortunately, the blast has dealt quite a bit of damage to your body. The hatchet is lodged deep into your left leg
        and your foot appears to be missing. It really sucks not having both feet, but you're also losing quite a bit of blood.</p>
        <p>Should you seek medical attention or attempt to locate your missing foot?</p>
        </div>
        </body>
        """
    return """
        <body>
        <style>
        #wrapper{
        width:640px;
        margin:0 auto;
        }
        .text{
        width:640px;
        margin:0 auto;
        }
        .link1{
        width:640px;
        margin:0 auto;
        }
        .link2{
        width:640px;
        margin:0 auto;
        }
        </style>
        <div id="wrapper">
        <p class="text">%s</p>
        <p class="healthval"><font color="green">Health: %i</font></p>
        <p class="link1"><a href="%s">Search for a medical facility.</a></p>
        <p class="link2"><a href="%s">Look for foot.</a></p>
        """ % (option111, health, url_for('static', filename='option121'), url_for('static', filename='option1112'))

@app.route('/static/option1112')
def option1112():
    global health
    health = health - 38

    option1112 = """
        <body>
        <style>
        #wrapper{
        width:640px;
        margin:0 auto;
        }

        </style>
        <div id="wrapper">
        <p>You crawl around on the ground in search of your missing foot. You trip and fall into the blast crater. It's walls
        are just high enough to prevent you from being able to climb out.</p>
        <p>In a pool of bloody eel remains, you slowly bleed to death from your wounds. <font color="red">(Health - 38)</font></p>
        </div>
        </body>
        """
    return """
        <body>
        <style>
        #wrapper{
        width:640px;
        margin:0 auto;
        }
        .text{
        width:640px;
        margin:0 auto;
        }
        .link1{
        width:640px;
        margin:0 auto;
        }
        .link2{
        width:640px;
        margin:0 auto;
        }
        </style>
        <div id="wrapper">
        <p class="text">%s</p>
        <p class="healthval"><font color="red">Health: %i</font></p>
        <p>You have died.
        The end.</p>
        """ % (option1112, health)

@app.route('/static/option112')
def option112():
    global health
    health = health - 200
    option112 = """
        <body>
        <style>
        #wrapper{
        width:640px;
        margin:0 auto;
        }

        </style>
        <div id="wrapper">
        <p>You run towards the woods but you realize that there are no woods! It's just a 70 foot concrete wall
        painted to look like trees! It's all a facade!</p>
        <p>The eels, the meadow, the town, it was all a game!
        <p>Cornered, you watch the gigantic flesh eating eels surround you. "Well, this is it," you
        say to yourself.</p>
        <p>An eel promptly bites your head off and you die. <font color="red">(Health - 200)</font></p>

        </div>
        </body>
        """
    return """
        <body>
        <style>
        #wrapper{
        width:640px;
        margin:0 auto;
        }
        .text{
        width:640px;
        margin:0 auto;
        }
        .link1{
        width:640px;
        margin:0 auto;
        }
        .link2{
        width:640px;
        margin:0 auto;
        }
        </style>
        <div id="wrapper">
        <p class="text">%s</p>
        <p class="healthval"><font color="red">Health: %i</font></p>
        <p>The end.</p>
        """ % (option112, health)

@app.route('/static/option12')
def option12():
    global personne
    global mushroom
    mushroom = mushroom + 1
    global health
    health = health - 25

    option12 = """
        <body>
        <style>
        #wrapper{
        width:640px;
        margin:0 auto;
        }

        </style>
        <div id="wrapper">
        <p>It tastes like the black death.</p>
        <p>You suddenly feel like your internal organs are on fire.</p>
        <p>You vomit approximately 13 times. <font color="red">(Health - 25)</font></p>
        <p>You realize that you just ate a poisonous mushroom. Why on Earth did you think
        that was a good idea?<p>
        <p>Your vision blurs. Your body aches. Is this the end?</p>
        <p>Nope, you still have like, 74 health left!</p>
        </div>
        </body>
        """
    return """
        <body>
        <style>
        #wrapper{
        width:640px;
        margin:0 auto;
        }
        .text{
        width:640px;
        margin:0 auto;
        }
        .link1{
        width:640px;
        margin:0 auto;
        }
        .link2{
        width:640px;
        margin:0 auto;
        }
        </style>
        <div id="wrapper">
        <p class="text">%s</p>
        <p class="healthval"><font color="green">Health: %i</font></p>
        <p class="see">See? You're not dying, just horribly ill! What are you going to do about it?</p>
        <p class="link1"><a href="%s">Seek medical attention.</a></p>
        <p class="link2"><a href="%s">Nothing.</a></p>
        """ % (option12, health, url_for('static', filename='option121'), url_for('static', filename='option122'))

@app.route('/static/option121')
def option121():
    global health
    option121 = """
        <body>
        <style>
        #wrapper{
        width:640px;
        margin:0 auto;
        }

        </style>
        <div id="wrapper">
        <p>You stumble back into town and head in the direction of the local hospital.
        As you approach the hospital, you can see a sign hanging on the door that reads, "CLOSED."</p>
        <p>What? Since when do hospitals close?</p>
        <p>You inspect the signage above the door. Oh, it's an animal hospital.</p>
        <p>You limp your way down the street in search of the actual hospital and, lucky for you, a
        kind stranger provides you with some assistance. The stranger informs you that the real hospital
        and the animal hospital are accross the street from each other.
        <p>Three hours later, you find the actual hospital. You approach the front desk and attempt to
        describe your ailment.</p>
        <p>Everyone around you goes wide eyed and a nurse quickly ushers you into a room with a bed. After
        laying down on the bed you start to feel sleepy...
        </div>
        </body>
        """
    if mushroom == 1:
        return """
        <body>
        <style>
        #wrapper{
        width:640px;
        margin:0 auto;
        }
        .text{
        width:640px;
        margin:0 auto;
        }
        .link1{
        width:640px;
        margin:0 auto;
        }
        .link2{
        width:640px;
        margin:0 auto;
        }
        </style>
        <div id="wrapper">
        <p class="text">%s</p>
        <p class="healthval"><font color="green">Health: %i</font></p>
        <p class="link2"><a href="%s">Continue...</a></p>
        """ % (option121, health, url_for('static', filename='hosp1'))

    else:
        return """
        <body>
        <style>
        #wrapper{
        width:640px;
        margin:0 auto;
        }
        .text{
        width:640px;
        margin:0 auto;
        }
        .link1{
        width:640px;
        margin:0 auto;
        }
        .link2{
        width:640px;
        margin:0 auto;
        }
        </style>
        <div id="wrapper">
        <p class="text">%s</p>
        <p class="healthval"><font color="green">Health: %i</font></p>
        <p class="link2"><a href="%s">Continue...</a></p>
        """ % (option121, health, url_for('static', filename='hosp2'))

@app.route('/static/hosp1')
def hosp1():
    global health
    hosp1 = """
        <body>
        <style>
        #wrapper{
        width:640px;
        margin:0 auto;
        }

        </style>
        <div id="wrapper">
        <p>You wake up, unable to tell how much time has elapsed since you passed out.
        A doctor comes in to check on you, notices you have awakened, and sits down beside you. They
        say your immune system has been severely damaged, most likely due to poisoning by ingesting
        a particular type of wild mushroom, and that you also have a serious case of salmonellosis.</p>
        <p>
        </div>
        </body>
        """
    return """
        <body>
        <style>
        #wrapper{
        width:640px;
        margin:0 auto;
        }
        .text{
        width:640px;
        margin:0 auto;
        }
        .link1{
        width:640px;
        margin:0 auto;
        }
        .link2{
        width:640px;
        margin:0 auto;
        }
        </style>
        <div id="wrapper">
        <p class="text">%s</p>
        <p class="healthval"><font color="green">Health: %i</font></p>
        """ % (hosp1, health)

@app.route('/static/hosp2')
def hosp2():
    global health
    health = health - 38
    hosp2 = """
        <body>
        <style>
        #wrapper{
        width:640px;
        margin:0 auto;
        }

        </style>
        <div id="wrapper">
        <p>You wake up, unable to tell how much time has elapsed since you passed out.
        A doctor comes in to check on you, notices you have awakened, and sits down beside you.
        They say you've been through hours of surgery and they had to amputate all of your limbs.
        Shocked, you attempt to shout, <i>"But only two of my limbs were damaged!"</i> But nothing
        comes out. The doctor explains that due to a bite from a particular breed of poisonous eel, you
        have also been rendered completely paralyzed.</p>
        <p>They also say that since you have no medical insurance, you will have to pay the bill by
        selling your spare organs. This may include a kidney, a lung, several feet of intestine, a few gallons of blood,
        and some brain tissue.</p>
        <p>You lie there, unable to move, unable to speak. A tear wells up in your eye.</p>
        <p>"Oh, we'll also need to take one of your eyes," the doctor adds.</p>
        <p>You spend the rest of your life paralyzed and bed-ridden, slowly being butchered until your body can no
        longer sustain life. <font color="red">(Health - 38)</font></p>
        If only you had eaten that mushroom, your life may have turned out better. Oh, well.</p>
        <p>You die of
        </div>
        </body>
        """
    return """
        <body>
        <style>
        #wrapper{
        width:640px;
        margin:0 auto;
        }
        .text{
        width:640px;
        margin:0 auto;
        }
        .link1{
        width:640px;
        margin:0 auto;
        }
        .link2{
        width:640px;
        margin:0 auto;
        }
        </style>
        <div id="wrapper">
        <p class="text">%s</p>
        <p class="healthval"><font color="green">Health: %i</font></p>
        """ % (hosp2, health)

@app.route('/static/option122')
def option122():
    global health
    global mushroom
    mushroom = 1
    option122 = """
        <body>
        <style>
        #wrapper{
        width:640px;
        margin:0 auto;
        }

        </style>
        <div id="wrapper">
        <p>Seriously? You're violently ill and you want to to nothing?</p>
        </div>
        </body>
        """
    return """
        <body>
        <style>
        #wrapper{
        width:640px;
        margin:0 auto;
        }
        .text{
        width:640px;
        margin:0 auto;
        }
        .link1{
        width:640px;
        margin:0 auto;
        }
        .link2{
        width:640px;
        margin:0 auto;
        }
        </style>
        <div id="wrapper">
        <p class="text">%s</p>
        <p class="healthval"><font color="green">Health: %i</font></p>
        <p class="link1"><a href="%s">Yeah.</a></p>
        <p class="link1"><a href="%s">Okay, maybe not.</a></p>
        """ % (option122, health, url_for('static', filename='option1221'), url_for('static', filename='option121'))

@app.route('/static/option1221')
def option1221():
    global health
    health = health - 74
    option1221 = """
        <body>
        <style>
        #wrapper{
        width:640px;
        margin:0 auto;
        }

        </style>
        <div id="wrapper">
        <p>Sigh...</p>
        <p>OK.</p>
        <p>You decide to do nothing.</p>
        <p><font size="16">You do nothing for the rest of your life until you
        literally die of boredom. THE END.</p>
        </div>
        </body>
        """
    return """
        <body>
        <style>
        #wrapper{
        width:640px;
        margin:0 auto;
        }
        .text{
        width:640px;
        margin:0 auto;
        }
        .link1{
        width:640px;
        margin:0 auto;
        }
        .link2{
        width:640px;
        margin:0 auto;
        }
        </style>
        <div id="wrapper">
        <p class="text">%s</p>
        <p class="healthval"><font color="red">Health: ZERO</font></p>
        """ % (option1221)

@app.route('/static/option2')
def option2():
    global personne
    global health
    health = health - 8923487925

    option2 = """
        <body>
        <style>
        #wrapper{
        width:640px;
        margin:0 auto;
        }

        </style>
        <div id="wrapper">
        <font size="24" color="red">SURPRISE PIPE BOMB!</font>

        <p>You explode into a thousand pieces.</p>
        </div>
        </body>
        """
    return """
        <style>
        #wrapper{
        width:640px;
        margin:0 auto;
        }

        </style>
        <div id="wrapper">
        <p>%s</p>
        <p class ="healthval"><font color="red">Health: %i</font></p>
        <p>Nice going, %s.</p>
        </div>
        """ % (option2, health, personne)

if __name__ == '__main__':
    app.run()
