# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define a = Character(_("Annalisse"), color="#c8ffc8")
define k = Character(_("Kael"), color="#c8ffc8")


default ego = 0
default poet = 0
default realism = 0

# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg room

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.
    #show pc happy

    # These display lines of dialogue.

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
            $poet+=1
            "Yes, yes, Shakespeare. We get it."
            "regardless... you look like yourself, and that's ogreish enough"
        

label mirror_after:

    "don't forget to scribble on your id info"

    $name = renpy.input("whats ur FIRST name")
    $pc = name.strip() or "Lyan"
    
    $name = renpy.input("whats ur LAST name")
    $last = name.strip() or "Sicit"

    $major = renpy.input("whats ur MAJOR IN UNIVERSITY")
    $mj = major.strip() or "Psychology"
    
    "ok so ur name is [pc] [last], right? AND you're majoring in [mj]? that'd be embarassing if not..."
    
    menu:
        "yes":
            jump campus
        "no":
            jump mirror_after   

        
label campus:
    scene bg uni 
    with Dissolve(0.5)
    pause.5

    "and with an (unfortunately) beating heart, you're off to confess. this past week has been a blur thankfully."
    "you've met so many gorgeous people."
    "and hot people."
    "and pretty people."
    "OH AND SPEAK OF THE DEVIL!!"

    show a neutral at left
    show k happy at right

    "They're conversing civilly. You take a step towards them and wave."

    menu:
        "yo chat wsg":
            $realism +=2

        "Annalisse, Kael. Good to see you both? How are you this morning?":
            $ poet+=2
            $realism+=1
            
        "First thing in the morning is two gorgeous people, how blessed am I? Or the real question is how blessed are you two to see me?":
            $poet+=1
            $ego+=2
            

 
    label postgreeting:
    "Annalisse looks you over slowly, eyes trailing your figure and attire. Kael, who has seemingly clammed up, has their stare trained to the ground."
    a "Someone's energetic this morning. Especially considering how you chose to leave the house… in that."
    show k neutral at right
    "Oooooh… and do you rise to the bait ???"
    menu:
        "I don’t want to hear that from someone who just went diving in a pink dumpster and grabbed what they could!!":
            $ego+=2
        "As marvelous as the clothes you don are, that is no excuse to claim we are not both beautiful. Our standards simply differ, and that is not something of shame.":
            $poet+=2
            jump poet_fight
        "LOL 0/10 rageBAIT":
            $realism+=1
            $ego+=2

    label fight: 
        show a snark mad at left
        a "thats a bullshit accusation and we both know it."
        "They scoff, a knowing grin on their face."
        a "you’re lucky i’m not embarrassing you further in front of Kael. god knows they think too highly of you."
        "Kael lets out a quiet, undignified noise."
        show k neutral at right
        k "i don’t know what you mean!"
        show a partial mad at left
        a "everyone thinks too highly of you, considering {i}what{/i} you are."
        show a snark mad at left
        "Their lip curls as your face darkens. You both know what they’re talking about, even if Kael doesn’t. The hypocrisy has you seething. But you’re more mature than Annalisse ever has been."
        show a partial at left
        pc "Bold words, especially considering your position."
        show a mad at left
        "She simply throws the middle finger at you before patting Kael on the shoulder."
        show a flip mad at left
        show k neutral at right
        a "Fuck you, [last]."
        show a partial mad at left
        jump fight_end

    label poet_fight:
        show a partial mad 
        a "ugh, your flowery words this morning are a pain in my ass. You’re not special, quit acting like it."
        "You sound like a fucking chuuni LOL. Kael lifts their gaze to your shoulders, offering an awkward smile."
        show k happy at right
        k "it was… an effort! Nice try, [pc]!"
        "Their diction may irk you a bit, but all the words are said genuinely and kindly… as usual."
        pc "thanks kael..."
        "There’s a lull in the conversation without you and Annalisse bickering like usual. You begin to wonder how the two of you are still friends. This whole trio is a little messed up."
        "Analisse, apparently done with the awkward silence, rolls their eyes before flipping you off."
        show a flip mad at left
        show k neutral at right
        a "you’re no fun today."
        show a partial mad at left

    label fight_end:
        show a neutral at left
        "Annalisse turns to Kael, gaze softening as Kael offers a shy smily back to them."
        a "i'll... see you after class."
        "Kael stays rooted in place as Annalisse leaves, before quickly waving and stuttering out their goodbye."
        show k happy at right
        k "Bye Ann..!"
        hide a neutral
        show k neutral at center
        k "... sorry about Ann. You know how they are, they don’t mean it."
        "Of course they have fucking nicknames for each other. That’s how close of friends they are. Frankly, you don’t know how they stand each other. Annalisse barely stands anyone other than Kael, and Kael can’t communicate with anyone other than Annalisse."
        "You frown. Made for each other, truly. But you had your crush, and you wouldn’t let this one-sided rivalry end your love life."
        pc "yeah... i'm sure..."
        "You never got why Annalisse was such a relentless... what's the word? bully? Clearly, it's not just you. The general public has always found one answer to the aggressive behaviour. Power."
        "The exception to this very wrath?"
        "Kael."
        "Maybe it's pity for an innate shy and frail nature. Or maybe the pleading eventually got on Annalisse's good side. Somehow."
        show k neutral
        k "well, did you finish the essay?"
        menu:
            "Oh yeah, obviously LOL":
                $poet+=2
                $completion = 100
                jump cafe

            "ogh. i forgot abt that.... speedrun?":
                $realism+=1
                $completion = 50
            "yeah im gonna go work on that. i'll see you in class!":
                $realism+=2
                $completion = 75

label library:
    "trust legit library i believe"
label cafe:
    "oohhh ritzy cafe"
    



    # Add your next story content here
    return
