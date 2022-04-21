# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define p = Character("[player_name]")
define t = Character("Teo")
define n = Character("Narrator")
define v = Character("Volunteer")

default plantingBg = None
default plantingLoc = None
default plantingExp = None

# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg frist campus center

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    # show bean happy

    # These display lines of dialogue.

    n "{w}So.{w} You’re procrastinating again."

    n "This might be one of the worst Tuesday afternoons in recent memory."

    n "You have a paper due this Friday, a problem set you haven’t started due Thursday at midnight, and your big group project has a long way to go before the presentation tomorrow."

    n "But at least there’s a fun giveaway this afternoon!"

    n "Perfect to waste an hour or two on before holing back up in the library."

    n "So, what’s your name?"

    $ player_name = renpy.input("What's your name?")
    $ player_name = player_name.strip()

    if player_name == "":
        $ player_name="Protagonist"

    n "Well, %(player_name)s, you should probably get going to the giveaway before you miss it!"

    scene bg frist lawn

    n "Supposedly, it’s some gardening-themed thing."

    n "You’re not really a big plant person – in fact… have you ever planted anything before?"

    menu:
        "Have you ever planted anything before?"
        "Nope.":
            $plantingExp = "anything"
            jump ch1_nope
        "A few.":
            $plantingExp = "Teosinte"
            jump ch1_few
        "A lot!":
            $plantingExp = "Teosinte"
            jump ch1_lot

label ch1_nope:

    p "Nope! I haven’t really had much planting experience."

    n "Yeah, I didn’t think so.{w} But I’m sure you’ll do a good job with this one."

    jump post_ch1

label ch1_few:

    p "I’ve planted a few things before, but not a lot."

    n "Wow. That’s cool!{w} So you know a little already about how to plant a seed."

    jump post_ch1

label ch1_lot:

    p "Actually, I’ve planted many things before. I’m a big fan!"

    n "Wow! Really?{w} So maybe you’ll be a pro at taking care of your giveaway plant."

    jump post_ch1

label post_ch1:

    scene bg frist lawn

    n "You can see the volunteers handing out seed packets and little pots with dirt in the distance."

    n "There’s not too much of a line, so you get to the front fast."

    n "A volunteer hands you a pot with dirt and a seed packet, which reads \“Teosinte Seeds\”."

    menu:
        " "
        "Teosinte?":
            jump ch2_teo
        "What's that?":
            jump ch2_what

label ch2_teo:

    p "Teosinte? Haven’t heard of it before."

    jump post_ch2

label ch2_what:

    p "What’s that?"

    jump post_ch2

label post_ch2:

    v "I’m not surprised you haven’t heard of Teosinte before!"

    v "Basically, it’s a wild ancestor to corn."

    p "So, I’m going to be growing corn.{w} In a pot.{w} In my room?"

    v "Slow down!"

    v "First, you’re not really growing corn."

    v "It’s an old corn ancestor that looks more like a bush than corn."

    v "And there’s no big cobs, instead there are little spikes of seeds."

    v "But you can actually eat these seeds if you pop them, like popcorn!"

    p "Oh.{w} That's pretty cool!"

    v "Also, we’re giving you this pot in case you want to use it."

    n "The volunteer leans in to whisper a bit more quietly."

    v "But I’d recommend you plant it somewhere a bit roomier if you’d like to see your plant truly flourish."

    v "So...{w} {i}{b}if you want to plant your teosinte somewhere else on campus...{/b}{/i}"

    v "Well, all I’m saying is I won’t tell anyone!"

    p "...{w} I think I get it. Thanks!"

    p "Last thing, what do I need to do to take care of my plant?"

    v "Like most other plants, I’d recommend watering it regularly."

    v "But also, it’s important to listen to your plant!"

    v "If you keep your eyes and ears open, your plant might tell you something important."

    v "Even better, {i}{b}you might be able to tell your plant something important!{/b}{/i}"

    p "... Okay. Water it regularly, got it."

    p "Thanks for the stuff!"

    v "You’re welcome!{w} I think you might find you’ll learn a lot from planting this seed."

label transition_1:

    scene bg woolworth

    n "You leave the giveaway area with your plant and pot in tow."

    n "Maybe... it's time head to the library?"

    p "Well, I would..."

    p "But the volunteer told me to listen to the plant, and I think my plant is saying \“Plant me now!\”"

    n "I’m going to pretend you’re not just trying to avoid your homework."

    n "Anyways, where do you want to plant your teosinte?"

    n "You’ve got the pot...{w} but you could also plant it somewhere on campus like the volunteer said."

    p "Hmm... it’s a big decision."

    menu:
        "Where will you plant your seed?"
        "In the pot":
            $plantingBg = "Dorm"
            $plantingLoc = "your room"
            jump ch3_pot
        "On campus somewhere":
            $plantingBg = "Dirt"
            $plantingLoc = "the planting spot"
            jump ch3_campus

label ch3_pot:

    p "I think I better plant it in the pot."

    p "They gave it to me for a reason.{w} Plus I’m worried the gardeners might uproot my teosinte."

    n "A smart choice, though your plant might not get quite as tall as it would outdoors."

    p "That’s unfortunate, but you can’t win them all."

    p "Let’s go back to the room and find a sunny spot for my plant."

    jump post_ch3

label ch3_campus:

    p "Why don’t I plant it on campus somewhere?"

    p "The plant could use some more space than this tiny pot anyways."

    p "Plus...{w} the campus could always use more plants, I think!"

    n "That sounds fun!"

    n "I would try to choose somewhere the gardeners won’t uproot the plant thinking it’s a weed."

    p "Oh, I didn’t even think about that."

    p "I’ve got the perfect place, though..."

    jump post_ch3

label post_ch3:

    if plantingBg == "Dorm":
        scene bg woolworth

    if plantingBg == "Dirt":
        scene bg dirt

    n "You head to [plantingLoc] with your seed."

    p "This is so exciting!"

    n "Unsure if you’re excited because you get to avoid the library or because you get to plant, you open the seed packet."

    n "The teosinte seeds look somewhat triangular, and they poke a bit into your skin."

    n "You make a small divot into the dirt and put a seed in."

    # pop up window here

    p "There. My seed's all planted!"

    n "You take a second to admire your work."

    n "It’s a strange feeling, planting something in the ground."

    n "You feel... responsible for it."

    n "You feel... as though it’s your job to take good care of it."

    "..."

    n "But before you have too much time to think about the promise you’ve made to your plant...{w} a little plant pops out from the dirt!"

    # show teosinte

    n "How strange. Plants don’t usually grow that fast."

    p "What the..."

    t "Hey! You! Are you the one who planted me?"

    menu:
        "Yes":
            jump ch3_pot
        "No":
            jump ch3_campus

label ch4_yes:

    p "Yes, that’s me!"

    t "Wow! It’s so great to meet you."

    t "Thanks for taking the time to plant me and take care of me."

    t "It means a lot!"

    jump post_ch4

label ch4_no:

    p "Uh... no. That was, um, somebody else."

    t "Oh. Really?"

    n "The little green thing looks confused."

    t "Well, you’re the one taking care of me, then, right?"

    t "Or you wouldn’t be here now!"

    t "Thanks for doing this! It means a lot."

    jump post_ch4

label post_ch4:

    t "So what should I call you, my lovely caretaker?"

    p "My name is %(player_name)s."

    p "But... what should I call you?"

    p "What... even are you?"

    t "Obviously, I’m your Teosinte plant!"

    t "But you can just call me Teo."

    p "It’s nice to meet you, Teo!"

    n "That's interesting."

    n "You’ve never talked to a plant before."

    n "Is there anything you want to ask it?"

    p "Well, I’ve never planted [plantingExp] before."

    p "The volunteer who gave you to me just told me to water you regularly, but..."

    p "Is there anything else I can do for you?"

    t "You definitely should water me!"

    t "But more than just watering goes into caring for a plant."

    t "You didn’t know that?"

    p "What else does a plant even need besides water?"

    p "Dirt?"

    t "Dirt too!{w} But I’m talking about a less tangible sort of care."

    t "How you treat a little seedling kindly."

    t "The importance of letting nature be free rather than controlling it in the way humans love to control things."

    if plantingBg == "Dirt":
        t "I’m already glad you decided to plant me in the world rather than in a pot."

    t "Planting doesn’t have to be so organized with us corn plants all in a row."

    t "Once, my ancestors were all over the place."

    t "We roamed free and spread our kin across the land."

    t "Planting a seed isn’t just about watering it or growing your crops in nice rows."

    t "And it’s not even about just me!"

    t "It’s about the whole earth, and building a supportive ecosystem of plants."

    t "It’s about growing plants like me wherever you think is best."

    t "After all, we once grew free."

    p "Wow. I really had no idea."

    t "Now that I think about it, how could you?"

    t "You don’t get to grow the food you eat."

    t "You don’t get to sit in the grass or dirt and listen to the plants around you."

    t "The world has become a place where you walk into an air-conditioned building and come out with a bagful of corn..."

    t "Rather than the huge, beautiful garden it once was."

    t "The way that plants are grown has changed so drastically in the last few hundred years."

    t "Once, I remember hearing about how the corn who came before me lived freely with other types of plants."

    t "We weren’t confined to little rows within fences."

    t "And if you want to know even before that, Teosinte has a rich history – like every plant does."

    t "But not a lot of people know it anymore."

    # another pop up

    p "You’re saying plants have histories?"

    t "Well, of course! Doesn’t everything?"

    p "What’s your story, then?"


    # This ends the game.

    return
