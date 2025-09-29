# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define a = Character(_("Annalisse"), color="#ec468a")
define k = Character(_("Kael"), color="#a5c9cf")
define Cashier = Character(("Cashier"))
define pc = Character(color="#8760af")

default preferences.text_cps = 45
default preferences.afm_enable = False

init python:
    persistent.confessions = 0
    persistent.last_confess = []
    persistent.endings = []

define k_a =0
define k_n = 0
define ego = 0
define p = 0
define completion = 0
define realism = 0
define lecture = False

# affection / nervousness stats !!

define a_a =0
define a_n =0
define ann_aff =0
define kae_aff =0

define pot_kettle= False
define rejection = False
define meet = False
define sneaky = False
define skipper = False

define jacket = False
define nn = "loser"

default ann_aff = 0
default kae_aff = 0




label start:

    "[persistent.last_confess]"
    "[persistent.confessions]"

    jump confession
    scene bg room


    "TODAY'S THE DAY, U ABSOLUTE LOSER !!"
    "UP AND AT EM !!"

    "YOU LOOK... "

        
    menu:
        "Depressed":
            $realism+=1
            "Very realistic of you !"
            "regardless... you look like yourself, and that's ogreish enough"

        "GORGEOUS !!!":
            $ego+=1
            "Urgh, ur ego is crazy"
            "regardless... you look like yourself, and that's ogreish enough"
        
        "woeful and melancholic. the days that pass are filled of nothing but nuance.":
            $p+=1
            "Yes, yes, Shakespeare. We get it."
            "regardless... you look like yourself, and that's ogreish enough"
        

label mirror_after:

    "Don't forget to scribble on your ID info"

    $name = renpy.input("whats ur FIRST name")
    $pc = name.strip() or "Lyan"
    
    $name = renpy.input("whats ur LAST name")
    $last = name.strip() or "Sicit"

    $major = renpy.input("whats ur MAJOR IN UNIVERSITY")
    $mj = major.strip() or "Psychology"
    
    "Ok so ur name is [pc] [last], right? AND you're majoring in [mj]? that'd be embarassing if not..."
    
    
    menu:
        "yes":
            jump campus
        "no":
            jump mirror_after   

        
label campus:
    scene bg uni 
    with Dissolve(0.5)
    pause.5
    

    "And with an (unfortunately) beating heart, you're off to confess. this past week has been a blur thankfully."
    "You've met so many gorgeous people."
    "And hot people."
    "And pretty people."
    "OH AND SPEAK OF THE DEVIL!!"

    show a neutral at left
    show k happy at right

    "They're conversing civilly. You take a step towards them and wave."

    menu:
        "yo chat wsg":
            $realism +=2

        "Annalisse, Kael. Good to see you both? How are you this morning?":
            $p+=2
            $realism+=1
            
        "First thing in the morning is two gorgeous people, how blessed am I? Or the real question is how blessed are you two to see me?":
            $p+=1
            $ego+=2
            

 
    label postgreeting:
    "Annalisse looks you over slowly, eyes trailing your figure and attire. Kael, who has seemingly clammed up, has their stare trained to the ground."
    show a snark
    a "Someone's energetic this morning. Especially considering how you chose to leave the house… in that."
    show k neutral 
    "Oooooh… and do you rise to the bait ???"
    menu:
        "I don’t want to hear that from someone who just went diving in a pink dumpster and grabbed what they could!!":
            $ego+=2
            $a_a+=1
        "As marvelous as the clothes you don are, that is no excuse to claim we are not both beautiful. Our standards simply differ, and that is not something of shame.":
            $p+=2
            jump p_fight
        "LOL 0/10 rageBAIT":
            $realism+=1
            $ego+=2

    label fight: 
        show a snark 
        a "Thats a bullshit accusation and we both know it."
        "They scoff, a knowing grin on their face."
        a "You’re lucky I’m not embarrassing you further in front of Kael. God knows they think too highly of you."
        $a_a+=1
        "Kael lets out a quiet, undignified noise."
        show k nervous 
        k "I don’t know what you mean!"
        show a partial mad 
        a "Everyone thinks too highly of you, considering {i}what{/i} you are."
        show a snark 
        "Their lip curls as your face darkens. You both know what they’re talking about, even if Kael doesn’t. The hypocrisy has you seething. But you’re more mature than Annalisse ever has been."
        show a partial mad
        pc "Bold words, especially considering your position."
        show a mad 
        "Annalisse simply throws the middle finger at you before patting Kael on the shoulder."
        show a flip mad 
        show k nervous 
        a "Fuck you, [last]."
        show a partial mad at left
        jump fight_end

    label p_fight:
        show a partial mad 
        a "Ugh, your flowery words this morning are a pain in my ass. You’re not special, quit acting like it."
        $a_a+=2
        "You sound like a fucking tryhard LOL. Kael lifts their gaze to your shoulders, offering an awkward smile."
        show k happy at right
        k "It was… an effort! Nice try, [pc]!"
        "Their diction may irk you a bit, but all the words are said genuinely and kindly… as usual."
        pc "Thanks Kael..."
        "There’s a lull in the conversation without you and Annalisse bickering like usual. You begin to wonder how the two of you are still friends. This whole trio is a little messed up."
        "Analisse, apparently done with the awkward silence, rolls their eyes before flipping you off."
        show a flip mad at left
        show k nervous at right
        a "You’re no fun today."
        show a partial mad at left

    label fight_end:
        show a neutral at left
        "Annalisse turns to Kael, gaze softening as Kael offers a shy smile back to them."
        a "I'll... see you after class."
        show k neutral
        "Kael stays rooted in place as Annalisse leaves, before quickly waving and stuttering out their goodbye."
        show k happy at right
        hide a neutral
        with Dissolve(0.25)
        k "Bye Ann..!"

        show k nervous at center
        k "... Sorry about Ann. You know how they are, they don’t mean it."
        "Of course they have fucking nicknames for each other. That’s how close of friends they are. Frankly, you don’t know how they stand each other." 
        "Annalisse barely stands anyone other than Kael, and Kael can’t communicate with anyone other than Annalisse."
        "You frown. Made for each other, truly. But you had your crush, and you wouldn’t let this one-sided rivalry end your love life."
        pc "Yeah... I'm sure..."
        "You never got why Annalisse was such a relentless... What's the word? Bully? Clearly, it's not just you. The general public has always found one answer to the aggressive behaviour. Power."
        "The exception to this very wrath?"
        "Kael."
        "Maybe it's pity for an innate shy and frail nature. Or maybe the pleading eventually got on Annalisse's good side. Somehow."
        show k neutral
        k "Well, did you finish the essay?"
        menu:
            "Oh yeah, obviously LOL":
                $p+=2
                $completion = 100
                pc "Wanna hang out for a bit?"
                $k_a+=5
                show k happy
                k "Sure!"
                show k neutral
                jump cafe

            "Ogh. i forgot abt that.... speedrun?":
                $realism+=1
                $completion = 50

            "Yea, I'm gonna go work on that. I'll see you in class!":
                $realism+=2
                $completion = 75
                jump library

label cafe:
    k "What was your topic again for class?"
    $topic = renpy.input("topic pending...")
    $t = topic.strip() or "sigma ass thing" 
    k "[t]? I'm sure you had a good time...right?"
    pc "Yeah, it sure was... I love having research papers for my literature elective that have nothing to do with literature..."
    show k happy
    k "Mr. Woizo is a real special character !"
    pc "You can just say it at this point. He teaches jackshit."
    show k nervous
    k "Doesn't he always say cussing isn't elevated?"
    pc "Yeah... whatever."
    "You get a ping from your phone..."
    "IT'S ANNALISSE !!!!"
    hide k nervous
    with Dissolve(0.5)
    show a silhouette
    a "wyd rn"
    menu:
        "respond to annalisse (MEAN)":
            $a_a +=3
            $k_n +=2
            $response = "mean"
        "RESPOND TO ANNALISSE (DESPERATE)":
            $a_a +=3
            $k_n +=3
            $response = "desperate"
        "DON'T RESPOND !!!":
            $realism+=3
            $k_a +=5
            $a_n +=1
            $response = "ok"
    if response == "mean":
        pc "and what is it to you ??? fucker ???"
        $a_a+=1
        a "ur acc so easy to rile"
        a "its almost embarassing"
        a "meet me in 10 minutes"
        $meet = True
    elif response == "desperate":
        $a_n+=1
        "in RECORD time, your fingers fly across your screen"
        pc "NOTHING"
        pc "what do u need me for"
        a "..."
        a "that was quick"
        a "too quick"
        a "whatever. meet me in 10, don't be late"
        $meet = True
    else:
        "you close your phone."
        $k_a+=2
        show k happy
        pause.1
        hide k happy
    hide a silhouette
    scene bg cafe outside 
    with Dissolve(0.5)
    pause.25

    "Kael is still prattling on about how, sometimes, Mr. Woizo does have some logic to his lectures. Before you know it, you're both outside the cafe entrance."
    hide k happy
    
    scene bg cafe inte
    with Dissolve(0.25)
    pause.5
    "{i}DING DING DING !!! A CUSTYOMER IS HERE !!! DING DING DING !!! {/i}"
    with Dissolve(0.25)
    show k happy at left
    "The both of you enter the cafe uneventfully. The aroma of freshly ground coffee floods your senses, accompanied with a heavy scent of powdered sugar. Mindless chattering of those sat at tables surrounds your ears."
    k "Would you like to order first?"
    menu:

        "YEAH ME FIRST VRO":
            $ego +=2
            $k_a+=1
        
        "i'll go after you !":
            $k_n+=2
            $realism +=4
            show k nervous
            k "I'll have a... uhhh..."
            pause.5
            k "I'll take a caramel iced latte... with whipped cream? and two shots espresso...?"
            show k happy
            "Kael quickly orders theirs and then it's your turn to pay."

    scene bg cafe cash
    with Dissolve(0.25)
    pause.4
    
    Cashier "What can I get you, chat?"
    hide k happy
    "That's some customer service alright..."
    $order = (renpy.input("ur order twin?")).strip() or "PEAK"
    "You pay like an upstanding citizen before heading over to Kael."
    scene bg cafe inte
    "{i} BHRRIIINNGGG GHIRINNGN !!!! RHINNNGGNGN !!! {/i}"
    show k odd
    pause.2
    show k nervous
    k "Sorry !! I'm getting a call ! Do you mind picking up my order too?"
    pc "No probl--"
    $k_a+=1
    "You're cut off as Kael shuffles to a corner."
    menu:
        "EAVESDROP.":
            "U LISTEN IN"
            $ego+=2
            $a_n+=3
            $k_n+=2
            $k_a+=10
            "You warily tiptoe behind Kael, your back flat against the wall of the corner, the chosen corridor."
            jump ed
        "DON'T EAVESROPD !!":
            $realism+=5
            $a_a+=5
            $k_a+=1
    
    scene bg cafe inte
    with Dissolve(0.25)

    "You zone out, nothing entertaining or amusing you for the next 5-10 minutes as they prep your drink."
    "You wonder about Annalisse. Whatever it is you've done to incur the devil's wrath, you aren't sure how to fix it."
    "You distinctly remember getting screamed at last time you asked why, a rage-colored face accompanied with it."
    "... and the punch that followed the next minute."
    "Phantom pain blooms over your right cheek, a tentative hand raised to it."
    pause.2
    "At least you can check off being beat by a hot person from your bucket list... right? LOLL"
    jump post_ed

    label ed:
        scene bg cafe side
        with Dissolve(0.25)
        pause.5
        $sneaky = True
        show k silhouette
        "You hear... a familiar voice."
        if meet == True:
            hide k silhouette
            show a silhouette
            a "Yo, where are you? Did you ditch [pc] yet? I told them to meet me now."
            $a_n+=2
            "You check the time... and sure enough, it's been 10 minutes since you messaged Annalisse."
        else:
            hide k silhouette
            show a silhouette
            a "Yo where are you? Did you ditch [pc] yet?"
        hide a silhouette
        show k silhouette
        k "Calm down. You're too loud."
        "... That's odd. Not Annalisse wanting to ditch you for Kael. Ugh, how are you STILL not good enough for them?"
        "But Kael... Kael sounds different. That tone..."
        k "No, I haven't."
        "You just turn the corner a bit to get a glimpse of Kael's expression over their shoulder."
        with Dissolve(0.25)
        show k odd
        k "Yeah, yeah, whatever. Let me have this. Alright?"
        "Kael's voice is... dismissive of Annalisse? No. It can't be."
        pause.2
        k "Yeah, I know. I'm paying for it. Where? On campus. Obviously. Stop prying."
        show k snark
        k "You're curious today, damn. Wonder what [pc] would--"
        $k_a+=2
        "Suddenly, Annalisse's sharp voice cuts through the phone."
        hide k snark
        show a silhouette
        a "I'll fucking kill you if you don't shut up now."
        hide a silhouette
        show k snark
        $k_a+=3
        k "Well, what if I told you that--"
        show k neutral
        jump post_ed


    label post_ed:
    $pc_upper = pc.upper()
    $order_upper = order.upper()
    Cashier "[order_upper] ORDER FOR [pc_upper] !! CARAMEL ICED LATTE WITH WHIPPED CREAM AND TWO SHOTS ESPRESSO ORDER FOR KAEL !!" 
    
    
    pc "Shit."
    "You quickly sprint towards your order and Kael’s before taking a swift seat at a table."
    
    scene bg cafe inte
    with Dissolve(0.25)
    pause.2
    scene bg cafe kael
    with Dissolve(0.25)
    pause.4
    hide k neutral

    "Kael's eyes meet yours as they slide into the seat across you, the cool drink steadily in front of them as your gaze raises to meet theirs."

    if sneaky:
        $k_a+=2
        "You struggle to meet their gaze, questions filling your mind."
        "What were they talking about? Why do they sound different?"

      
    
    if completion <100:
        scene bg cafe kael talk
        k "[t] gives you a lot to work with actually... Hm. Did you start explaining on how it's interpretated in the modern era?"
        scene bg cafe kael
        pc "Oh yeah. Studying. Presentation. I almost forgot that's what we came here for LOL"
        if meet:
            "Your phone surprisingly doesn't blow up with angry messages from Annalisse."
            "Somehow."
            $a_n+=2
        "And despite not knowing anything about it, magically, Kael knows more of your topic than you do. It's almost irksome."
        $completion = 150

    if completion == 100:
        scene bg cafe kael talk
        k "[order], huh? That's an interesting order."
        scene bg cafe kael
        pc "Yeah, it's my usual. I get it everytime I go to a cafe! Is it weird?"
        $k_a+=2
        scene bg cafe kael nervous 
        pause.2
        scene bg cafe kael talk
        k "...Um, not at all!"
        "...That's reassuring."
    
    if meet:
        "Should you go meet Annalisse?"
        menu:
            "See Annalisse":
                $a_a+=2
                $k_n+=2
                "You stand up out of the blue, Kael looks at you surprised."
                scene bg cafe kael nervous
                pause.4
                scene bg cafe kael talk
                k "[pc]?"
                scene bg cafe kael nervous
                pc "I've got to... I have to... I have to go. Sorry."
                "A flimsy excuse. It's rather mean."
                jump cafe_ditch
            "Stay with Kael":
                $a_n+=3
                $k_a+=2
    scene bg cafe kael
    "The two of you chat for the rest of your time until it's time to go to class."
    scene bg cafe kael talk
    k "Oh! Would you look at that! It's time to get to class!"
    scene bg cafe kael
    pc "Yeah, yeah, I'm.... pumped."
    "Kael, assuming your nerves are for your presentation, tries to assuage your nerves."
    scene bg cafe kael talk
    k "You're gonna do great!"
    show bg cafe kael nervous
    pc "...Or I could just skip out on it."
    pause.1
    scene bg cafe kael talk
    k "Well... Uh,,, You shouldn't !!!"
    scene bg cafe kael
    menu:
        "skip that damn class...":
            scene bg cafe kael nervous
            pause.2
            scene bg cafe kael talk
            k "Alright [pc]... I'll think of something to tell him."
            pc "Thanks Kael. It means a lot."
            $ego+=1
            $skipper = True
            jump library
        "tough it out goat!!":
            pc "...I'll stick around. Let's get to class."
            $realism+=2
            jump presentation
    
label cafe_ditch:
    $k_n+=5
    scene bg cafe inte
    with Dissolve(0.25)
    pause.4
    show k odd
    k "{size=-10}fuck.{/size}"
    pause.1
    show k nervous
    k "Bye [pc]!"
    scene bg cafe outside
    show k odd
    k "{size=-10}fucking interloper.{/size}"
    hide k odd
    jump library


label library:

    scene bg library 
    with Dissolve(0.5)
    pause.25
    "It's a nostalgic scent, the library. That familiar scent of fresh paper and ink on parchment makes you wistful."
    "You spy a flash of pink in your peripheral, accompanied with some muttering before Annalisse appeards in front of you."
    show a snark
    a "Well, well, well."
    if meet:
        show a partial mad
        a "You're late. Why?"
        if sneaky:
            menu:
                "Tell the truth":
                    pc "I was with Kael. And then you messaged.  That's why."
                    show a partial mad
                    a "Took your damn time, that's what you did."
                    $a_a+=2
                    $k_a+=1
                "LIE!!!":
                    pc "It took me a while to walk vro... obviously I'm gonna be a while."
                    a "Yeah sure, I don't believe that shit for a second."
                    show a snark
                    pc "Screw you, you pinkalicious crayon."
        
        pc "You told me to come. I came. That not good enough for you, {i}Ann{/i}?"
        show a mad
        a "Only Kael gets to call me that, [last]. Watch your tone."
        pc "Bullshit."
    else:
        a "Why're you here?"
        "You raise an eyebrow, not surprised to see Annalisse in their natural habitat. Underneath all the bite, bark, glitz and glamour, Ann's a high-performing scholaship student."
        if skipper:
            pc "I'm skipping."
            show a neutral
            a "Wow? Really now? That's surprising."
            pc "I'm not like Kael, not fervently dedicated to my academics."
        else:
            pc "I have an assignment to complete? What's it to you?"
            a "Really now?"
            show a snark
            a "Let me see it."
            "You raise an eyebrow at the demand, but hand it over cautiously."
            $a_a+=3
            a "not bad. I'll even help."
            $completion+=15
            "That's... new."
            "Annalisse never does anything that benefits anyone else. Unless the person in question is themselves. Or maybe Kael. So why the help?"
            pc "Um... Thanks?"
            "How... graceful of you."
            show a partial mad
            a "Yeah, you're fucking welcome. Dumbass. Do you even know what you're talking about here?"
            show a snark
            pc "Harhar. Very funny. I chose the subject. I hope both sides of your pillow are damp."

    show a snark
    a "Your colorful word choice is so stupid. You're pathetic."
    "You roll your eyes distastefully. It seems to make them laugh."
    show a neutral
    pc "Pot, meet Kettle."
    show a snark fluster
    "They manage a small smile. The event from this morning is all but forgotten and forgiven. This is more your speed. Kael acts as both a catalyst and a barrier for Annalisse's teror. But on their own, they're both neutral people."
    show a snark
    a "Whatever. Nerd."
    "It's said almost fondly. Not as fond compared to what Kael gets. But fondly, nonetheless."
    "It almost stirs butterflies in your stomach."
    show a neutral
    "The sudden idea that Annalisse might like you."
    $a_a+=1
    show a p_fluster
    "You just don't get it."
    $a_a+=1
    show a fluster
    "Why would you be {i} happy {/i} about that?"
    show a snark
    if realism >= 10:
        "You quickly find yourself displeased with the idea of it after mulling it over."

    a "[pc]. [pc]...! [pc] !!"
    show a neutral
    pc "HUH--"
    show a snark fluster
    a "God, you're infuriating."
    "HUHHH ??!?!!"
    "Did you do that stupid cliche thing off saying your thoughts out loud??"
    a "You never pay attention to anything I say. Dumbass."
    "Annalisse glances down at the phone in their hand."
    if sneaky!=True:
        show a snark
        a "I've gotta pick up a call. One sec. I'll be back."
        menu:
            "EAVESDROP":
                $sneaky=True
                "You follow Annalisse to one of the many corridors in the library, your back pressed against the bookshelves of the other aisle."
                with Dissolve(0.25)
                show a silhouette
                $k_a+=2
                $a_a+=5
                a "What do you need? I'm with [pc] right now."
                "You hear a familiar dulcet voice through the static of Annalisse's phone."
                hide a silhouette
                show k silhouette
                k "Monopolizing their time now?"
                if meet:
                    k "I was with them first, _____ ______."
                    hide k silhouette
                    show a silhouette
                    a "And now they're with me. God..."
                    hide a silhouette
                    show k silhouette
                    k "_____ _____."
                    "You peek through the crack of the bookshelves."
                    hide k silhouette
                    show a snark
                    a "You're just jealous they like me better."
                    hide a snark
                    show k silhouette
                    k "Fuck you too."
                    $k_n+=2
                hide k silhouette
                show a p_fluster
                a "They look... ___ today."
                hide a p_fluster
                show k silhouette
                k "Why not just tell them that? I'm so done with hearing--"
                hide k silhouette
                show a fluster
                a "They're so ______. I just want to ______."
                "You just miss the tail end of what Annalisse manages to whisper into the call before Kael's crisp voice cuts through it with an undertone of anger."
                hide a fluster
                show k silhouette
                k "No. You don't get to do that. Not after--"
                hide k silhouette
                show a partial mad
                a "Jesus, I get it. Whatever."
                a "Petty of you. You don't control them."
                hide a partial mad
                show k silhouette
                k "___ _____. _______."
                hide k silhouette
                show a mad
                a "Damnit. Fine. Stop calling me then. Interloper."
                "Annalisse settles back down at the table."
            "Don't eavesdrop twin,....":
                "You stay in place like asked."
                $a_a +=3
                $k_a+=4
    with Dissolve(0.25)
    show a neutral
    a "It's almost time for your class. The one you have with Kael."
    if skipper:
        pc "That's the one I'm skipping."
        call aff_update
        if (ann_aff>=10):
            show a snark
            a "Oh. Well. I guess you can stay a while."
            $k_n+=3
            $a_a+=4
            jump loiter
        else:
            show a partial mad
            a "Boo hoo. Fuck off. Get to your class."
    else:
        show a partial mad
        a "Get going. I need to take my nap."
        if (ann_aff>=10):
            show a snark
            a "Actually... I guess you can stay a while."
        
            $a_a+=4
            jump loiter
    pc "Hey, alright. I'll get going."
    if completion < 100:
        "You turn to Annalisse hesitantly. This is a really shit choice, in my opinion."
        pc "...Thanks."
        show a partial mad
        a "Huh?"
        "At the apparent confusion, you grit your teeth, heat coloring your face."
        pc "Thanks. For the help with the presentation."
        "A sharp grin covers their face, something that sends a shiver down your spine."
        show a snark
        a "You owe me now, kettle."
        "It's in reference to when you called yourself kettle and Annalise pot in reference to the hypocrisy earlier. It's so stupid. And dumb. It's the worst nickname to curse this earth."
        "But it brings this stupid, jubilant grin to your face."
        pc "Kill yourself, pot."
        $pot_kettle = True

    jump presentation

label loiter:
    
    "You stick with Annalisse before they let down their vigilance, slumped behind a book as they begin to softly snore."

    scene bg sleep a 
    with Dissolve(0.5)
    pause.25

    "It wouldn’t be wrong to say Annalisse almost looks… approachable? Cute? Endearing?"
    "Hm."
    "Weird."
    "You stay on task, hesitantly glancing up every now and then to check on Annalisse. While your phone is much more inviting than the sight before you, you can't but stare."
    "Slouched over the plastic of the table doesn't look very comfortable."
    menu:
        "Cover the chair with your jacket.":
            $a_a+=5
            scene bg sleep a jacket
            with Dissolve(0.5)
            pause.25
            $jacket = True
        "Let Ann be. You don't want to upset them.":
            $realism+=2
    "It's only a moment later until Ann begins to stir, hair askew, eyes droopy."
    if jacket:
        scene bg awake a jacket 
        with Dissolve(0.5)
        pause.25
    else:
        scene bg awake a
        with Dissolve(0.5)
        pause.25
    "It's certainly... a new look for sure."
    "It's kind of... cute? In an ugly way???"
    "Annalisse quickly realizes the state in which they've been caught, sending you a pointed glare."
    if jacket:
        scene bg awake a jacket mad
    else:
        scene bg awake a mad
    a "You saw nothing."
    call aff_update
    if ann_aff>=15:
        menu:
            "You look cute.":
                $a_a+=6
            "Hmm... Really now?":
                $a_a+=5
            "Welcome back, Sleeping Beauty.":
                $a_a+=8
        if pot_kettle:
            $nn = "pot"
        else:
            $nn = pc
        a "Shut up, [nn]."
    "It's not a moment's hesitation before they begin grabbing their stuff to leave."
    scene bg library
    with Dissolve(0.5)
    pause.25
    "You let out an almost dramatic sigh as you're left to the library by yourself."
    jump confession

label presentation:
    scene bg lecture 
    $lecture = True
    with Dissolve(0.5)
    pause.25
    "You stare down at the grade given to you by Mr. Woizo."
    if completion == 65 or completion ==90:
        $a_a+=5
        "Mr. Woizo" "Surprisingly good job. Didn't know you had it in you."
        "Mr. Woizo." "Oddly profound for [t]."
    if completion == 100:
        $realism+=5
        "Mr. Woizo" "It's definitely your work...!"
        "Mr. Woizo" "Good job on fixing your past shortcomings though."
    if completion> 100:
        $k_a+=5
        "Mr. Woizo" "This reminds me of a certain someone else's work. Hm."
        "Mr. Woizo" "Maybe you actually started asking for help! Good job."

    "You had managed your way through your presentation, other students hurriedly taking notes. Mr. Woizo said something about submitting them for extra credit but people are taking it pretty serious."
    if skipper:
        "You mildly regret not actually skipping the class. But Annalisse made you leave... and then Kael found you. And thought you were going to class."
        "So now you're here."

    "Honestly, how did you even get to this point..."

    jump confession

    # Add your next story content here
    return


label confession:
    "From what you remember, you started this day off hoping to confess..."
    "Those capturing eyes, that infectious smile, that charming voice... Obviously you were going to confess to..."
    menu:
        "Annalisse <333":
            $k_a-=10
            $k_n+=10
            jump route_a
        "Kael !!":
            $a_a-=10
            $a_n+=10
            jump route_k
        "Either of them!!" if persistent.confessions == 2 :
            if kae_aff>ann_aff or ann_aff>kae_aff:
                $a_a-=2
                $k_a-=2
            $realism +=5
            jump route_poly
        "NEITHER of them.":
            $realism+=25
            $a_a-=10
            $k_a-=15
            jump aro
        "Full Completion" if len(persistent.endings) == 10:
            "Congrats ?? you must be a massive loser if you keep playing holy,"
            "Gold star for you!! You get to see the beta sprite of kael"
            show k beta
            $persistent.endings.append("locked in")

label route_a:
    "You couldn't help but be enamored with Annalisse. A harsh exterior and what YOU'RE sure is a soft interior. The apparent duality enraptures you."
    "Underneath all that gorgeous, brilliant star potential is someone sensitive, emotional, kind. Even if a little brash."
    "But you know Annalisse cares."
    "It's endearing."
    "You send her a message."
    menu:
        "Meetup with me trust chat":
            $realism+=2
        "You wanna see your favorite later?":
            $ego+=2
        "I need to see you as soon as possible. There's something of importance we must discuss.":
            $p+=2
    call aff_update
    show a silhouette
    if ann_aff > 12:
        a "Sure. Whatever."
        if completion == 65 or completion == 90:
            a "how was ur presentation"
            pc "Good, thanks :)"
    else:
        a "Alright."
        $rejection = True
    hide a silhouette
    if lecture and sneaky and kae_aff<=15:
        "In your peripheral you see that weird side to Kael again."
        "If you squint from across the room, he almost seems to be glaring at you..."
        "That's weird..."
        pause.25
        "Oh well."
    else:
        "You get this foreboding feeling someone isn't very happy. Your ear itches."
        "You get up from the library chair and stretch, setting off."
    "You agreed to meet up with Annalisse at the library, not having to move since they had left a couple hours ago. Something about having to get something finished."
    if rejection:
        jump a_reject
    else:
        jump a_accept
label route_k:
    show k nervous
    "Kael has always been a constant comfort at your side. Nullifying the effects of Annalisse's wrath, listening to our struggles, helping out where they can."
    "They're so selfless -- to the point of self-sacrifice. You love that about them, but you would rather they not hurt themselves for you or Annalisse."
    "There's something you can't deny about how they make you feel, eager to please, wearing their heart on their sleeve."
    show k happy
    "That genuine honesty warms you heart."
    if sneaky:
        show k odd
        "And whatever that odd behaviour has been lately... something about it intrigues you."
    "You send them a message."
    menu:
        "Meetup with me trust chat":
            $realism+=2
        "You wanna see your favorite later?":
            $ego+=2
        "I need to see you as soon as possible. There's something of importance we must discuss.":
            $p+=2
    call aff_update
    show k silhouette
    if kae_aff>=12:
        k "of course!! what do you need?"
        pc "just gotta talk with u, don't worry!"
    else:
        k "yeah sure!"
        $rejection = True
    hide k silhouette
    if not lecture and ann_aff<=15:
        "You feel a pair of eyes trail over your figure as you're leaving the library. Let's just say they're not very comforting."
        "When you make your way out the door, you're suddenly swarmed!"
        "And you land flat on your face... after someone DEFINITELY TRIPS YOU."
        "huh... weird."
    "You agreed to meet with Kael at the cafe , so you make your way over."
    if rejection:
        jump k_reject
    else:
        jump k_accept
label route_poly:
    "God. It's impossible to decide between the two. They're both just drop dead gorgeous in their own right."
    show k happy at left
    show a neutral at right
    "The way Kael smiles, the way Annalisse grins."
    if sneaky:
        show k odd
        show a fluster
        "And that underneath whatever facade they put up, they care about you."
    "You just CAN'T choose."
    if realism >=10:
        "There's definitely a part of you that feels a little awkward for being interested in both of them. But you have to confess NOW or never."
    "You message in a group."
    pc "Wanna hang out after school?"
    call aff_update
    if kae_aff>=15 and ann_aff>=15 and persistent.confessions == 2:
        show k silhouette
        show a silhouette
        k "sure"
        a "i'll be there"
    else:
        show k silhouette
        show a silhouette
        k "sure !!"
        a "wtv i'll be there"
        $rejection = True
    "You all collectively decide on meeting up outside the university."
    if rejection:
        jump poly_reject
    else:
        jump poly_accept


label a_accept:
    scene bg library
    with Dissolve(0.5)
    pause.25
    "You don't really know how to go about this. You could confess over and over to the same person for eternity. And it would never change how you feel about this type of stuff."
    "Profession of feelings."
    " 'I like you. Go out with me.' "
    "Like it's that easy."
    "Like confessing is easy as breathing."
    "Liking Annalisse is much harder than anything like that."
    "Brash, harsh, biting -- like the wind on a cold winter morning."
    "It's hard to love something about someone who doesn't want to be loved. But you do."
    "You persist because everyone deserves love. It's not a matter of want, but a matter of need."
    "You try and try again and again even if you fail, because when you love someone, you want to appreciate them."
    "You want to cherish them and give them everything they want in life."
    "Because that's what it means to love someone."
    "And you might love Annalisse."
    "You want them to wake up in the morning and be glad to see the sun. You want them to be able to have their favorite food when they want."
    "You want to provide whatever they need, you want to talk to them every walking hour."
    "You want to be theirs so bad."
    "But at the end, you want their happiness above all."
    pause.1
    "And there they are."
    show a neutral
    a "You called?"
    pc "You came..."
    show a snark
    a "When have I not? I always deliver, [nn]."
    show a neutral
    "You feel the grin pull at your lips, sweat dripping down the back of your neck."
    pc "Yeah... yeah."
    "How do you even go about this....???"
    "How do you even know they like you -- much less tolerate you??"
    show a partial mad
    "Almost irritated with your silence, Annalisse frowns. Expecting better composure from you has become normalcy."
    a "So what do you need? You don't call me up for no reason. You're not itching THAT much for a fight?"
    pc "Well, you remember the first day we met right?"
    show a snark
    a "You mean like a month ago?"
    pc "No, I mean earlier than that. Like on the bus."
    "You pray to whatever god up there you're not embarassing yourself."
    "That Annalisse remembers. That they know what you're talking about."
    show a p_fluster
    a "... you remember that?"
    "Oh? You might have a shot with this?"
    pc "How could I forget? How could I ever forget someone like you?"
    show a fluster
    a "... Go on."
    "It was a spring morning. You were taking the bus somewhere for your friends. It was inconsequential considering you don't even remember the details."
    "Of course, this is an Annalisse with a different look."
    show a past
    "Starkly different look."
    "Regardless, the two of you were on the bus together. Nothing new, but the bus takes a detour and immediately, you have no clue where the HELL you're headed."
    "Reminded once again why you hate public transport."
    "You had looked around hurriedly and confused."
    "Annalisse caught your eye and had quickly explained that this was nothing new for the bus. Introducing themselves briefly as their gaze drawls over your figure."
    "Enraptured in conversation with Ann, you absentmindedly miss the fact that YOU MISSED YOUR STATION."
    "It's a few stations after that you ask Annalisse when it's your station to which you're told it passed a while back. Like a dumbass."
    "You're quickly assured you'll be fine as Annalisse sorts out everything with you, going as far as to escort you to the next bus stop and waiting until it arrives."
    "You're chided before the bus pulls up with a screeching halt."
    a "Don't go around getting lost on buses anymore."
    pc "We just met, don't make presumptions."
    a "Whatever. See you around [pc]."
    with Dissolve(.15)
    show a p_fluster
    "And you never did see them around."
    pc "You're just as brilliant, just as kind, just as patient as you were then."
    pc "But you're different, and that has never been a bad thing."
    pc "No matter what people tell you now."
    show a fluster
    pc "You're just as remarkable as the day I met you, just as beautiful as the day I met you."
    "You're starting to feel embarassed as this goes on."
    pc "You're kind, but not overtly. You know where to draw the line, even if it's too harsh for others."
    pc "Even too harsh for me."
    show a p_fluster
    pc "You protect yourself. You put yourself first."
    pc "And you always should."
    pc "You have your priorities straight, you keep people as far and close as you need, you're smart, you're intuitive."
    pause.2
    show a fluster
    pc "You're all that I want."
    pc "So that begs the question... Do you want me too?"
    show a p_fluster
    a "I..."
    if kae_aff <=10:
        k "Not so fucking fast."
        show a p_fluster at left
        show k odd at right
        k "Don't think for a damn second I'll let you win over Annalisse that easy."
        scene bg k punch1
        pause.25
        scene bg k blink1
        "Your nose burns."
        pause.3
        scene bg k punch2
        pause.25
        scene bg k blink2
        "Your face itches."
        pause.3
        scene bg k punch3
        pause.25
        scene bg k blink3
        "Your skin burns."
        pause.3
        scene bg k punch4
        pause.25
        scene bg k blink4
        "Your heart stops."
        pause.3

        k "Nice fucking try."
        "Bad Ending 1: Try to keep them amicable..."
        if "Jumped by Dog" not in persistent.endings:
            $persistent.endings.append("Jumped by Dog")
        if "Jumped by Dog" not in persistent.last_confess:
            $persistent.last_confess.append("Jumped by Dog")
        return

    else:
        show a fluster
        a "You... really want me? Even after everything. Even after it all."
        pc "I've always."
        show a snark fluster
        a "Is that so?"
        a "Lucky you then."
        pc "Is that..."
        "Your heart drops in your chest."
        a "Yes, dumbass. It's a yes."
        "Good Ending 1: Beauty and the Beast"
        if "Beauty and the Beast" not in persistent.endings:
            $persistent.endings.append("Beauty and the Beast")
        if "Beauty and the Beast" not in persistent.last_confess:
            $persistent.last_confess.append("Beauty and the Beast")
            $persistent.confessions+=1
        return
label a_reject:
    scene bg library
    with Dissolve(0.5)
    pause.25
    "You love Annalisse."
    "You know it as fact. They're gorgeous. A little rude, but that's part of the appeal."
    "After all, you wouldn't pursue them if that wasn't the case, right?"
    show a neutral
    a "I'm here."
    pc "Ah, great! I was wondering when you'd come."
    show a partial mad
    a "When do I not deliver?"
    "You feel a little awkward at their tone."
    show a mad
    "Almost irritated with your silence, Annalisse frowns."
    a "So what do you need? You don't call me up for no reason. Are you seriously itching THAT much for a fight?"
    pc "I like you."
    show a partial mad
    a "So what?"
    "HUH?"
    a "You're not fucking slick, [pc]."
    "Oh..."
    show a snark
    a "It's almost embarassing..."
    a "Whatever, just don't bother me with this nonsense again."
    pause.2
    show a flip mad
    a "Keep that shit to yourself."
    with Dissolve(0.25)
    hide a flip mad
    "Bad Ending 2: Rejection is a Cruel Mistress... and Their Name is Annalisse."
    if "Cruel Mistress" not in persistent.last_confess:
        $persistent.last_confess.append("Cruel Mistress")
    if "Cruel Mistress" not in persistent.endings:
        $persistent.endings.append("Cruel Mistress")

label k_accept:
    scene bg cafe outside
    with Dissolve(0.5)
    pause.25
    "Just thinking about this makes you nauseous. You're not great with words -- not in the way Kael deserves."
    "Not like Kael."
    "How do you even say this in a way that they'll understand. In a way they'll reciprocate."
    "Not that that's the only important part."
    "You just..."
    "You really want this."
    "You want to support them, you want to comfort them, you want to fuel them."
    "You want to be what they think of in the morning, and what they think of before sleep."
    "That's what loving someone is."
    "That's what it's always meant to you."
    "To help someone grow, to grow with someone."
    "And you might love Kael."
    "You want to be theirs, every hour, every day."
    "But their happiness is what you want above all."
    pause.1
    "And there they are."
    show k nervous
    k "Hi?"
    pc "It's uh, good to see you."
    show k happy
    k "Thanks. It's good to see you too."
    "You love that crooked smile. Those sweet eyebrws."
    k "Let's go inside?"
    pc "Sure... sure."
    scene bg cafe inte
    show k nervous
    k "So why'd you call me? You do have Ann's number, yeah?"
    pc "Well, you remember our first meeting, right?"
    pause.2
    show k odd
    pause.2
    show k nervous
    k "Y-Yeah? You mean in class?"
    pc "No, no. I mean earlier than that."
    pause.2
    show k odd
    pause.2
    show k nervous
    k "You remember that...?"
    "Oh...??? That's weird. They're characteristically nervous."
    pc "Yeah."
    show k odd
    k "Hmm.."
    k "Go on."
    "It was a winter evening. It was cold outside, you remember that frequently."
    "You had taken the usual route home from the cafe. But the lights flickering should have been a sign of sorts."
    "Cold metal was pressed against the flesh of your neck as you froze like a deer in headlights."
    "Someone had told you to get out your wallet. And with shaking hands, you did so."
    "In the blink of an eye--"
    pause.1
    scene bg k blink1
    pause.1
    scene bg cafe outside
    "Someone had saved you."
    "Except you screamed. In their face."
    pc "AAGH-"
    "They quickly covered your mouth, hissing at you."
    k "Shut up."
    "To you, it looked more like the person who had threatened to kill you. But you sat up, and saw someone on the ground with the lights knocked out of them."
    pc "Huh."
    show k past
    k "Huh, my ass."
    k "You're welcome."
    k "And what the hell are you doing out so late, huh?"
    pc "W-What is it to you...?"
    k "Look, you almost died. Cut me some slack."
    "After pilfering through your wallet, they toss it back to you."
    k "Yeah, there's like nothing of substance here."
    "Out of condescendent (?) concern for you, Kael agrees to walk you home after the mortifying ordeal."
    "Obviously, it's the most awkward nighttime stroll you've ever taken, but gradually your yapper nature comes through."
    "The two of you get talking before Kael yanks your arm and scribbles a number on it."
    k "There. Call me if you ever need help."
    pc "Um. Probably not."
    "They let out a boisterous laugh."
    k "Yeah, that's probably safer."
    k "See you around, [pc]."
    with Dissolve(.15)
    show k nervous
    pc "I never did see you around again."
    k "...you wanted to?"
    pc "I mean, yeah. I wanted to thank you. Wanted to tell you that I appreciated you saving my life."
    pc "I wanted to tell you that you were gorgeous."
    pc "That you were cool."
    show k neutral fluster
    pc "I wanted to tell you whatever you wanted to hear."
    pc "I wanted... I think I wanted to just talk with you."
    show k nervous
    k "Really? Talk to... {i} that {/i} Kael?"
    pc "Yeah. And you're different now. And that's not bad."
    pc "Not at all."
    pc "I like you the same, want you the same."
    pc "But do you... er... want me too?"
    if ann_aff <= 10:
        a "Wow."
        show k nervous at left
        show a partial mad at right
        a "You think that pithy bullshit is good enough for Kael?"
        "You frown, eyes narrowing at Annalisse's sudden appearance."
        pc "Annali--"
        show a mad
        a "No. Continue."
        a "Continue spouting that fucking drivel at Kael. How you love them {i}sooo{/i} much."
        show a snark
        a "You'd never compare. You're just not good enough."
        "Your eyes burn at the vitriol."
        "Furious, you throw the first punch."
        pause.1
        "But to your surprise, it's not Annalisse who catches it. But Kael."
        show k odd
        k "Hm. I guess this never would have worked out."
        scene bg k punch1
        pause.2
        scene bg k blink3
        k "You don't get to touch Annalisse."
        "Bad Ending 3: Bite the Hand That Feeds."
        if "Hand Biter" not in persistent.last_confess:
            $persistent.last_confess.append("Hand Biter")
        if "Hand Biter" not in persistent.endings:
            $persistent.endings.append("Hand Biter")
        
        return
    else:
        show k odd
        k "Annalisse told me you'd do this."
        k "That you'd... confess."
        k "And that it was inevitable."
        show k nervous
        k "She's always right."
        show k odd
        k "It's been a while since I've been honest."
        k "Can you find it in yourself to love me? Even if I told you I'm a violent monster?"
        k "Even if I'd beat you into the dirt for touching Annalisse?"
        k "Can you love that?"
        show k delirious
        k "Can you even tolerate that?"
        menu:
            "Yes.":
                pc "I don't just love the Kael you show. I love more than that of you."
                show k shock
                k "Huh?"
                pc "I can accept that."
                pc "Can you?"
                show k shock fluster
                k "HUH???"
                k "Is... is that a yes?"
                pc "It's always been?!"
                "Good Ending 2: Red Riding Hood and the Wolf; You're Red."
                if "Red Riding Hood" not in persistent.endings:
                    $persistent.endings.append("Red Riding Hood")
                if "Red Riding Hood" not in persistent.last_confess:
                    $persistent.last_confess.append("Red Riding Hood")
                    $persistent.confessions+=1
                return
            "No":
                show k odd 
                k "I guess this is where we part."
                scene bg k punch1
                pause.25
                scene bg k blink1
                "Your nose burns."
                pause.3
                scene bg k punch2
                pause.25
                scene bg k blink2
                "Your face itches."
                pause.3
                scene bg k punch3
                pause.25
                scene bg k blink3
                "Your skin burns."
                pause.3
                scene bg k punch4
                pause.25
                scene bg k blink4
                "Your heart stops."
                pause.3
                k "I can't risk getting caught."
                "Bad Ending 4: Through Life or Death"
                if "Life and Death" not in persistent.last_confess:
                    $persistent.last_confess.append("Life and Death")
                if "Life and Death" not in persistent.endings:
                    $persistent.endings.append("Life and Death")
                return
label k_reject:
    scene bg cafe outside
    with Dissolve(0.5)
    pause.25
    "You love Kael. Easy as that."
    "Obviously, their sacrificial nature is a bit of a pain. But their meekness is endearing."
    "After all, that's why you're pursuing them."
    "You don't really remember when you started liking them, it was some day in class, you're sure."
    show k neutral
    k "Hey, what'd you need me for?"
    pc "Ah, I was wondering when you'd get here."
    scene bg cafe inte
    with Dissolve(.25)
    show k nervous
    k "I'm not late, am I?"
    pc "No, no, not at all."
    show k neutral
    pc "I just wanted to tell you... I like you."
    show k shock
    pause.1
    show k odd
    pause.2
    show k nervous
    k "oh."
    "{i} OH????? {/i}"
    k "I don't... feel the same way. Sorry [pc]."
    "They awkwardly leave, with little fanfare."
    "Bad Ending 5: Ouch."
    if "Ouch" not in persistent.last_confess:
        $persistent.last_confess.append("Ouch")
    if "Ouch" not in persistent.endings:
        $persistent.endings.append("Ouch")
    return

label poly_accept:
    scene bg uni
    with Dissolve(0.5)
    pause.25
    "Well this is most definitely going to be really awkward."
    "Firstly, you have to confess to two gorgeous people."
    "Then propose a polyamorous relationship. With these two people."
    "Who for all you know, could like each other better. Ohhh, it's so over."
    "They're just both so important to you. Having been a part of your life from before your university run-ins."
    show a neutral at left
    show k neutral at right
    pause.3
    show a past
    show k past
    pause.3
    show a neutral
    show k neutral
    "How could you choose between the two of them when they're undeniably interconnected in your day-to-day life?"
    hide a neutral
    hide k neutral
    show a snark
    a "Yo."
    "AHRGHHGHG THERE SHE IS !! THGE ONE THE ONLY ANNALISSE !!!"
    show a partial mad
    a "...are you ok?"
    "SO KIND MY SHAYLA !!"
    pc "Yeah, yeah, I'm good. I'm good."
    "YOU ARE NOT GOOD !!!!"
    "YOUR HEART IS [[RACING]!! YOUR BLOOD IS [[PUMPING] HOLY SHIT GET OUT OF HERE,,, GHRGG"
    show a p_fluster
    a "Uh... sure. When's Kael getting here?"
    "As if on cue, Kael stumbles in the clearing from behind you."
    hide a p_fluster
    show a neutral at left
    show k nervous at right
    k "I'm not late or anything, am I?"
    "OH MY GOD HE'S SUCH A [[CUTIE PATOOTIE]] I LOVE HIM SM MY SHAYLA...."
    "*cough cough* Anyways."
    pc "So. There's a reason I brought you both here."
    pc "I, uh, I've been thinking about us. Like, all three of us."
    show a snark
    a "Wow. [pc]? [nn]? Thinking? Unheard of."
    pc "Let me finish, goddamn..."
    "You can hear Annalisse snickering as Kael nudges them to shut up."
    pc "As I was saying. I care about both of you, like a lot. Like romantically."
    show k shock
    show a p_fluster
    pc "You two are my favorite people. Like. Ever. At all."
    show k neutral fluster
    pc "And I think you'll always be special to me."
    pc "Even if you two don't remember, I remember."
    "You turn to Annalisse."
    show a fluster
    pc "The bus."
    "You turn to Kael."
    show k shock fluster
    pc "The alleyway."
    pc "This might be out of nowhere, but I can't keep pretending like you guys don't mean a lot to me."
    pc "Not after everything."
    pause.5
    "So... Is it hot out here? Or is that just you???"
    show a snark fluster
    "Annalisse elbows Kael harshly to which they let out a whine."
    show k delirious
    k "What the--"
    show a fluster
    a "Are you gonna tell them?"
    show k shock
    pause.1
    show k shock fluster
    pause.2
    show k snark
    k "Of course. Why wouldn't I?"
    "Annalisse rolls their eyes at the sharp turn in conversation."
    a "Get to it."
    show k odd fluster
    k "We -- and I mean WE -- like you too [pc]."
    show a snark fluster
    a "You're incredibly blind."
    k "And we also remember those incidents."
    show a snark
    a "What do you think we talk about on our own?"
    pc "WHAT THE FUCK--"
    "Good Ending 3: Bag the Baddies"
    if "Bag the Baddies" not in persistent.last_confess:
        $persistent.last_confess.append("Bag the Baddies")
    if "Bag the Baddies" not in persistent.endings:
        $persistent.endings.append("Bag the Baddies")
    
    return

    

label poly_reject:
    scene bg uni
    with Dissolve(0.5)
    pause.25
    "kael not peak"
    return


label aro:
    scene bg aro
    with Dissolve(0.5)
    pause.25
    "In the sunset, you see Annalisse and Kael talking. A pink-covered arm slung around a sunken shoulder."
    "Annalisse turns to you with a grin and beckons you over."
    scene bg aro a turn
    a "Yo [nn]! What the hell are you doing over there so far from all the action?"
    "Kael looks over at you from his shoulder, a sheepish grin."
    k "Ann is right! Get over here!"
    "You virtually bodyslam them with a wide grin on your face."
    pc "You called?"
    "All three of you laugh to varying degrees before shuffling apart and heading home together."

    scene bg room
    "Neutral Ending 0: You Know Which Fights To Choose"
    if "Solo" not in persistent.last_confess:
        $persistent.last_confess.append("Solo")
    if "Solo" not in persistent.endings:
        $persistent.endings.append("Solo")

    return

label aff_update:


    $ann_aff = 500 #(a_a+p)-(a_n+realism)
    $kae_aff = 500 #(k_a+ego)-(k_n+realism)

    "annalisse affection = [a_a], kael affection = [k_a], annalisse hate = [a_n], kael hate = [k_n], ego = [ego], poet = [p], realism = [realism], a_aff_total = [ann_aff]"

    return