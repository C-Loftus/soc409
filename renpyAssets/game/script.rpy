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

init:
    $ import time

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg frist campus center

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

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

    show volunteer with fade

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
        scene bg dorm with fade
        show pot

    if plantingBg == "Dirt":
        scene bg dirt with fade

    n "You head to [plantingLoc] with your seed."

    p "This is so exciting!"

    n "Unsure if you’re excited because you get to avoid the library or because you get to plant, you open the seed packet."

    if plantingBg == "Dorm":
        hide pot

    show teosinte seed

    n "The teosinte seeds look somewhat triangular, and they poke a bit into your skin."

    if plantingBg == "Dirt":
        n "You make a small divot into the dirt and put a seed in."
    else:
        n "You make a small divot into the pot's dirt and put a seed in."

    # pop up window here
    call screen PopUp("Now, it’s time to go plant YOUR seed!\n\nYes, you, in real life!\n\nCome back here only once you’ve planted your seed.\n\nDon’t forget to take a picture of where you’ve planted it!")

    $ year, month, day, hour, minute, second, dow, doy, dst = time.localtime()

    hide teosinte seed

    if plantingBg == "Dorm":
        show pot

    p "There. My seed's all planted!"

    n "You take a second to admire your work."

    if plantingBg == "Dirt":
        n "It’s a strange feeling, planting something in the ground."
    else:
        n "It’s a strange feeling, planting something."

    n "You feel... responsible for it."

    n "You feel... as though it’s your job to take good care of it."

    "..."

    n "But before you have too much time to think about the promise you’ve made to your plant...{w} a little plant pops out from the dirt!"

    hide pot

    show teo happy with fade

    n "How strange. Plants don’t usually grow that fast."

    p "What the..."

    show teo talking

    t "Hey! You! Are you the one who planted me?"

    menu:
        "Yes":
            jump ch4_yes
        "No":
            jump ch4_no

label ch4_yes:

    show teo happy

    p "Yes, that’s me!"

    show teo talking

    t "Wow! It’s so great to meet you."

    t "Thanks for taking the time to plant me and take care of me."

    t "It means a lot!"

    jump post_ch4

label ch4_no:

    show teo happy

    p "Uh... no. That was, um, somebody else."

    show teo confused

    t "Oh. Really?"

    n "The little green thing looks confused."

    show teo talking

    t "Well, you’re the one taking care of me, then, right?"

    t "Or you wouldn’t be here now!"

    t "Thanks for doing this! It means a lot."

    jump post_ch4

label post_ch4:

    show teo talking

    t "So what should I call you, my lovely caretaker?"

    show teo happy

    p "My name is %(player_name)s."

    p "But... what should I call you?"

    p "What... even are you?"

    show teo talking

    t "Obviously, I’m your Teosinte plant!"

    t "But you can just call me Teo."

    show teo happy

    p "It’s nice to meet you, Teo!"

    n "That's interesting."

    n "You’ve never talked to a plant before."

    n "Is there anything you want to ask it?"

    p "Well, I’ve never planted [plantingExp] before."

    p "The volunteer who gave you to me just told me to water you regularly, but..."

    p "Is there anything else I can do for you?"

    show teo talking

    t "You definitely should water me!"

    t "But more than just watering goes into caring for a plant."

    t "You didn’t know that?"

    show teo happy

    p "What else does a plant even need besides water?"

    p "Dirt?"

    show teo talking

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

    show teo happy

    p "Wow. I really had no idea."

    show teo confused

    t "Now that I think about it, how could you?"

    show teo talking

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
    call screen PopUp("Now that you’ve heard Teo tell his story, write a poem for your plant!\n\nYes, you, in real life!\n\nThe poem can encourage your plant to grow big and strong or it can just tell a story about the place you are planting your Teosinte.\n\nSave your poem to share with the community!")

    show teo happy

    p "You’re saying plants have histories?"

    show teo talking

    t "Well, of course! Doesn’t everything?"

    show teo happy

    p "What’s your story, then?"

    t "Well..."

    hide teo talking

    show bg organic farm with fade

    t "Me and my sisters, beans and squash, used to live together."

    t "We made such a great trio."

    t "Each of us complimented each other’s weaknesses."

    t "What one took from the earth the other gave back."

    t "Yet, one day we were separated against our will."

    show bg industrial farm with fade

    t "My dear sisters, the beans and squash, were taken to their own fields away from me and the other corn."

    t "We forgot our history.{w} We forgot our family."

    t "Most of all, we forgot where we came from."

    t "As time went on there were those who tried to sell our very genetics."

    t "Who tried to separate us from our stories."

    if plantingBg == "Dorm":
        scene bg dorm with fade

    if plantingBg == "Dirt":
        scene bg dirt with fade

    show teo talking

    t "Despite this, there’s some like me who haven’t given up."

    t "My sisters and I, we will always have a story."

    t "The people who we grew alongside deserve to have rights in how they plant us."

    t "After all, they are the ones that respect our stories."

    t "They are the ones who remember the kind of earth we came from."

    t "This is what seed sovereignty is all about."

    t "It’s not only being able to live alongside my sisters, but also being able to preserve my story."

    show teo happy

    p "Seed... sovereignty? I’ve never even heard of that!"

    show teo talking

    t "I’m not surprised."

    t "So few people these days have!"

    t "Don’t worry, I’ll explain it a little bit for you."

    t "A long time ago, we didn’t have these crazy things called corporations you humans love."

    t "We just had plants."

    t "There were so many different types of seeds, like angel beans, winged beans, and the butterfly pea.{w} And don’t forget the Teosinte!"

    t "But these days, only three companies control about half the seeds grown on earth!"

    t "Isn’t that crazy?"

    menu:
        "So crazy!":
            jump ch5_yes
        "Well... capitalism...":
            jump ch5_no

label ch5_yes:

    show teo confused

    p "That’s so crazy! Half?!"

    show teo talking

    t "I know. That’s way too many."

    t "Actually, any more than zero is still too many for me."

    t "But can you imagine? No matter how rich your history may be with a certain seed, you likely have to buy it from a company!"

    t "Huge companies can buy the rights to seeds, taking them away from local farmers."

    jump post_ch5

label ch5_no:

    show teo confused

    p "Well, you know about this thing called capitalism...?"

    show teo talking

    t "Yes, yes, I’m aware."

    t "But that doesn’t mean it’s okay to let huge companies buy the rights to seeds!"

    t "It’s not okay to take away seeds from local farmers who may have rich histories with them."

label post_ch5:

    show teo talking

    t "And that’s why seed sovereignty is so important."

    t "So, to get back to your question, seed sovereignty is the right that farmers, gardeners, and other food producers have to save, use, breed, exchange, and sell open-source seeds."

    show teo happy

    p "Open... source... seeds?"

    show teo confused

    t "Oh, goodness."

    show teo talking

    t "They don’t teach you about open source seeds in school?"

    t "I guess I can tell you a little about them too."

    t "{b}{i}Open source seeds{/b}{/i} are seeds that are not genetically modified, patented, or controlled by corporations."

    t "Open source seeds can be sold to other food producers, but are also often exchanged between food producers via seed swaps."

    t "These seed swaps help give more people access to different seeds and help more people learn about the histories of those different seeds."

    show teo happy

    p "This all sounds great."

    show teo talking

    t "Be patient!"

    t "I haven’t even gotten to potentially the most severe aspect of seed sovereignty yet!"

    t "So, at least tell me you know what biodiversity is."

    menu:
        "Of course!":
            jump ch6_yes
        "Remind me?":
            jump ch6_no

label ch6_yes:

    show teo happy

    p "Of course I do! It’s the biological variety of all life on earth."

    show teo talking

    t "Wow! Good job."

    jump post_ch6

label ch6_no:

    show teo confused

    p "Maybe you can remind me?"

    show teo talking

    t "Biodiversity refers to the biological variety of all life on earth."

    jump post_ch6

label post_ch6:

    show teo talking

    t "And having {b}{i}biodiversity{/i}{/b} in our food system is important because it helps our means of producing food endure environmental disasters such as climate change, diseases affecting crops, and flood."

    t "Without seed sovereignty, it will get harder and harder to maintain biodiversity!"

    t "And that means, without seed sovereignty, this world will have a harder and harder time fighting climate change, as the earth won’t have the usual ecosystems used to regulate harmful pollutants and dangerous levels of carbon."

    t "I know that might sound bleak, but there’s a lot of ways to support seed sovereignty and avoid this scary future!"

    show teo happy

    p "I’m interested!"

    show teo talking

    t "Well, we can start by reclaiming seed farming as a local practice."

    t "You may not know this, but my corn ancestors like other Teosinte and maize were from places like Mexico, Guatemala, Honduras, and Nicaragua."

    t "They were grown by indigenous people who took care to pass down their stories."

    t "But now, so many of them are just owned by companies."

    t "Their histories have been stolen and replaced by corporations who want to control seeds..."

    t "And instead of preserving their stories, they want to profit off of them."

    t "These days, indigenous people are leading the seed sovereignty movement, {w}and the movement is growing as we speak!"

    show teo tired

    p "Well, tell me how to help more! Or how to join in!"

    t "I’m so tired after explaining all of that to you already."

    t "Don’t you want me to grow into a beautiful plant?"

    menu:
        "I suppose I do...":
            jump ch7_yes
        "Well, where else can I find information?":
            jump ch7_where

label ch7_yes:

    p "I suppose I do."

    show teo happy

    p "But before you go, can you point me in the right direction?"

    show teo talking

    t "That, I can!"

    jump post_ch7

label ch7_where:

    p "Well, I want to help. Where else can I find information?"

    show teo happy

    jump post_ch7

label post_ch7:

    show teo talking

    t "First, what’s the way you most want to help?"

    menu:
        "I like gardening.":
            jump ch8_garden
        "I want to volunteer.":
            jump ch8_volunteer
        "I want to donate money.":
            jump ch8_donate

label ch8_garden:

    show teo happy

    p "I think I really like the gardening aspect of this."

    p "How can I keep gardening and also support seed sovereignty?"

    show teo talking

    t "I know some great places you can buy seeds that support seed sovereignty efforts!"

    t "You can buy seeds from an organization like Alliance of Native Seedkeepers, a Native American owned seed company that sells non-GMO seeds in line with their commitment to agricultural biodiversity."

    t "Or, visit the Gaia Foundation’s Seed Saving Resouces page to learn how to produce and save your own seeds!"

    jump post_ch8

label ch8_volunteer:

    show teo happy

    p "I think I’d like to volunteer my time with organizations that work to support seed sovereignty."

    show teo talking

    t "That’s a great idea."

    t "If volunteering on a farm interests you, check out the Utopian Seed Project, an organization that supports diversity in food and farming."

    t "Or if you like organizing for change, try Navdanya International, an organization fighting for seed sovereigntiny for small farmers globally."

    t "If there are no organizations in your area, perhaps you could donate to one!"

    show teo happy

    menu:
        "Tell me where to donate.":
            jump ch8_2_donate
        "I would rather not donate.":
            jump ch8_2_no

label ch8_2_donate:

    p "Where can I donate?"

    show teo talking

    t "I’m so glad you asked!"

    t "Some great places to donate your money to for seed sovereignty are the Utopian Seed Project, an organization that supports diversity in food and farming..."

    t "Or the Native American Food Sovereignty Alliance, an national organization dedicated to helping indigineous groups take control of their food systems."

    jump post_ch8

label ch8_2_no:

    p "I’m not sure I have the funds right now to donate."

    show teo talking

    t "That’s completely okay!"

    t "It’s great that you were able to just listen and talk with me today in the first place."

    jump post_ch8

label ch8_donate:

    show teo happy

    p "I’m pretty busy, but I’d like to donate some money towards seed sovereignty."

    show teo talking

    t "That is completely understandable, and I’m happy you still want to help despite being busy!"

    t "Some great places to donate your money to for seed sovereignty are the Utopian Seed Project, an organization that supports diversity in food and farming..."

    t "Or the Native American Food Sovereignty Alliance, an national organization dedicated to helping indigineous groups take control of their food systems."

    jump post_ch8

label post_ch8:

    show teo happy

    p "Thanks for explaining all of this to me today, Teo."

    p "And for pointing me in the right direction on how to best support seed sovereignty!"

    show teo talking

    t "You’re welcome!"

    t "I’m going to get back in the dirt to spend some time growing now."

    t "But I’d love to hear how you might help support seed sovereignty, even if it’s just telling one other person about it!"

    hide teo with fade

    if plantingBg == "Dorm":
        show pot

    n "Teo dives back into the dirt where he came from, before you can even say goodbye."

    p "Aww. I miss him already."

    n "But you think you’ll likely see him again soon if you take good care of your plant."

    n "For now... it’s time to head to the library."

    call screen PopUp("Teo’s given you some personalized ways to support seed sovereignty efforts.\n\nAnd he wants you, in real life, to write him a letter!\n\nTell Teo about how you want to help out, even if it’s just one thing.\n\nYou could teach a friend about seed sovereignty, plant another seed, or donate five dollars.\n\nSave your letter to share with the community!\n\nAnd don’t forget to visit the resources page for more information on organizations working towards seed sovereignty!")

    n "Thank you for playing!"

    n "Please feel free to upload the photograph of your plant, the poem you wrote, and your letter on this website under the \“New Post\” page."

    n "And look at others’ posts on the \“All Posts\” page."

    n "Additionally, check out where other players have planted their seeds on the \“Maps\” page."

    n "We also have a page where you can look at a \“Timeline\” of how your plant will grow, along with some reflective questions."

    n "Finally, please take a look at the \“Resources\” page to see where you might be interested in supporting seed sovereignty efforts in the future."

    n "We hope you learned something from Teo."

    n "Save your game, and come back to this save in one month from [month]-[day]-[year], and you can hear one more thing from Teo."

    $ year2, month2, day2, hour2, minute2, second2, dow2, doy2, dst2 = time.localtime()

    if month == 12:
        if year2 - year > 1:
            jump after_one_month
        elif year2 > year:
            if month2 == 1:
                if day2 >= day:
                    jump after_one_month
            else:
                jump after_one_month
        else:
            jump before_one_month
    else:
        if year2 > year:
            jump after_one_month
        elif month2 - month > 1:
            jump after_one_month
        elif month2 - month == 1:
            if day2 >= day:
                jump after_one_month
        else:
            jump before_one_month

label before_one_month:

    n "Come back to this save in one month from [month]-[day]-[year], and you can hear one more thing from Teo."

    $ year2, month2, day2, hour2, minute2, second2, dow2, doy2, dst2 = time.localtime()

    n "It is currently [month2]-[day2]-[year2]. Please be patient! Plants take a while to grow."

    if month == 12:
        if year2 - year > 1:
            jump after_one_month
        elif year2 > year:
            if month2 == 1:
                if day2 >= day:
                    jump after_one_month
            else:
                jump after_one_month
        else:
            jump before_one_month
    else:
        if year2 > year:
            jump after_one_month
        elif month2 - month > 1:
            jump after_one_month
        elif month2 - month == 1:
            if day2 >= day:
                jump after_one_month
        else:
            jump before_one_month

label after_one_month:

    if plantingBg == "Dorm":
        scene bg dorm with fade
        show pot

    if plantingBg == "Dirt":
        scene bg dirt with fade

    n "Welcome back. Let's check in on Teo, shall we?"

    if plantingBg == "Dorm":
        hide pot

    show teo talking with fade

    t "Hey! Welcome back. Thanks for taking care of me all this time."

    t "I hope you’ve been doing well. Have you had any time to support seed sovereignty efforts since I’ve last seen you?"

    menu:
        "Yes":
            jump ch9_yes
        "No":
            jump ch9_no

label ch9_yes:

    show teo happy

    p "I actually have!"

    show teo talking

    t "Wow! Really? What have you been up to?"

    show teo happy

    $ useless = renpy.input("What have you been up to, briefly?")

    show teo talking

    t "That sounds great!"

    jump post_ch9

label ch9_no:

    show teo happy

    p "Sorry, I haven’t. I’ve been really busy."

    show teo talking

    t "That’s okay! I’m glad you’re still thinking about me and seed sovereignty though!"

    jump post_ch9

label post_ch9:

    t "Anyways, I don’t have too much to say today. I’m just happy to see you again."

    t "And I’m happy that seeds are still on your mind."

    t "We’re very important, after all!"

    t "Thanks for planting me. And thanks for listening to me, too."

    hide teo with fade

    if plantingBg == "Dorm":
        show pot

    n "Teo goes back into the dirt."

    n "Thanks for participating in this journey with Teo and us."

    n "Again, we encourage you to upload photographs of anything you plant on the \“New Post\” page, and to look at others’ posts on the \“All Posts\” page."

    n "Additionally, we encourage you to check out where other players have planted their seeds on the \“Maps\” page."

    n "Don’t forget to look at the \“Timeline\” of how your plant will grow, which also has some reflective questions for you to ponder."

    n "Finally, please take a look at the \“Resources\” page to learn about opportunities to support seed sovereignty efforts in the future."

    n "We hope you learned something from Teo."

    n "Thank you for taking the time to learn about seed sovereignty with us."

    return
