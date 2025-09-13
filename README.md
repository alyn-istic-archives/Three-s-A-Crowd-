# Three-s-A-Crowd-
peak visual novel trust

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
            jump realism
        "GORGEOUS !!!":
            jump ego
        "woeful and melancholic. the days that pass are filled of nothing but nuance.":
            jump poet
    

label mirror_after:

    "don't forget to scribble on your id info"

    $ name = renpy.input("whats ur FIRST name")
    $ pc = name.strip() or "Lyan"
    
    $ name = renpy.input("whats ur LAST name")
    $ last = name.strip() or "Sicit"

    $ major = renpy.input("whats ur MAJOR IN UNIVERSITY")
    $ mj = major.strip() or "Psychology"
    
    "ok so ur name is [pc] [last], right? AND you're majoring in [mj]? that'd be embarassing if not..."
    
    menu:
        "yes":
            jump campus  
        "no":
            jump mirror_after   
label campus:
    "and with an (unfortunately) beating heart, you're off to confess. this past week has been a blur thankfully."
    "you've met so many gorgeous people."
    "and hot people."
    "and pretty people."
    "OH AND SPEAK OF THE DEVIL!!"
    scene bg uni 
    with Dissolve(0.5)
    pause.5
    show a neutral at leftish
    show k happy at rightish
    "urm so peak idk how github works"
    # Add your next story content here
    return

label realism:
    $ realism+=1
    "Very realistic of you !"
    "regardless... you look like yourself, and that's ogreish enough"
    jump mirror_after
    
label ego:
    $ ego+=1
    "Urgh, ur ego is crazy"
    "regardless... you look like yourself, and that's ogreish enough"
    jump mirror_after
    
label poet:
    $ poet+=1
    "Yes, yes, Shakespeare. We get it."
    "regardless... you look like yourself, and that's ogreish enough"
    jump mirror_after
    
