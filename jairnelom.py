
import time
import winsound
sleeptime=2.5
def c1():
    print("""
             |follow|or|attack|""")

def c2():
    print("""
             |talk|or|attack|""")

def c3():
    print("""
             |head|or|chest|""")

             
def c4():
    print("""
             |kill|or|spare|""")

def c5():
    print("""
             |jay|jair|jamal|""")
def c6():
    print("""
             |eryk|callum|gondor|""")

def c7():
    print("""
             |eichenwalde|narnia|elendoor|""")

def c8():
    print("""
             |daisy|peach|cinderella|""")

def c9():
    print("""
             |troll|elf|god|""")
def dub2():
    print("""
    ⡿⠉⣉⡁⠈⠁⢀⣰⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⠇⢉⣿⢇⣀⠘⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠿⠿⠿⠿⠿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⠏⠉⠻⣯⠍⠀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠟⠋⠁⠀⠀⠀⠀⠀⠀⠀⠈⠻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣮⣿⣶⣤⢀⣻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠏⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠛⠋⠀⠉⠻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠷⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀⠀⠀⠀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠃⠀⢀⠴⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢹⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠃⠀⠠⣼⣥⣴⣾⠟⣻⣿⢿⣶⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⠿⣿⣿⣿⠀⠀⠀⠀⠉⢻⣿⣿⣄⡛⠛⣨⣿⣧⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣤⣄⡀⠹⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⡟⠟⠟⣦⠙⣇⣀⡄⠀⠀⠀⠈⠛⠿⠿⠿⠿⢿⠟⠛⠀⢀⡀⠀⠀⠀⠀⣴⣾⡟⢛⣿⣿⣶⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⡇⠘⢀⣩⣆⣼⠉⢿⣄⠀⣀⣀⡀⢀⠀⠀⠀⠀⠀⠀⠀⢀⣴⡟⠉⣲⡄⡿⣿⣧⣌⣋⣽⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣧⢠⣾⣉⣛⢸⠀⢦⣿⣿⣿⣉⣉⡀⠀⠀⠀⠀⠀⠀⠐⢻⠟⠃⢠⣿⠇⠀⠈⠛⠛⠛⠋⢹⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣧⣙⠺⠙⣿⡄⠀⠘⡍⢻⣿⣿⣷⣶⣶⣤⣤⣤⣀⣀⠘⠂⠀⠈⠃⠀⠀⠀⠀⢀⠀⠀⡘⠻⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣦⣿⡇⠀⠀⠁⠈⣿⣿⣿⣿⣿⣿⡿⡿⡿⣿⣿⣿⣶⣤⣤⣤⣄⣀⠀⢀⣷⣾⠖⠉⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⢷⠀⠀⠀⠀⠈⢿⣿⣿⣿⣿⣿⣾⣿⣿⣥⣿⣏⣿⣻⠻⣿⣿⣿⡿⣿⡟⠰⢠⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠘⣧⠀⠂⢀⠀⠈⠉⢿⣿⣥⣏⡿⣿⣿⣿⣿⣿⣿⣷⣶⣿⣿⠛⢡⠟⢁⣴⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣟⢀⢻⣧⠀⡌⠀⠀⠀⠀⢻⣿⣿⣷⣯⣹⡟⣝⣛⣯⣽⣿⡟⠁⢠⣯⣤⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠛⢸⢿⣿⣧⣼⣷⠀⠀⠀⠀⡙⠻⣿⣿⣿⣿⣿⣿⣿⠟⠋⠀⣠⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⢿⡟⠀⠘⡃⢹⣿⣿⣮⣧⠀⠀⠀⠈⠁⠉⠌⣉⣙⡻⠋⠁⡀⣀⣼⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⠛⠛⠛⠛⠋⠉⠉⠉⠀⢠⡞⠀⠀⢀⡇⠘⣿⣿⣿⣿⣷⠀⠀⠀⠀⠀⠀⠁⠀⠀⠀⠀⣻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠠⠇⢠⠀⢨⡇⠀⠋⣿⣿⣿⣿⣷⣄⠀⠀⠀⠀⠀⠀⠀⣠⢾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠄⠸⡅⠀⠀⠘⠿⣿⣿⣿⣿⣷⣶⣶⣤⣤⣤⣴⢋⢺⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡀⠉⣿⣿⣿⣿⣿⣿⣿⡿⠋⠀⡜⠻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠠⠀⢀⠀⠀⠀⠀⠀⢳⣶⣾⣿⣿⣿⣿⣿⡏⠀⠀⡰⠁⠀⠈⠻⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⡀⣶⣽⣿⣿⣿⣿⡟⡍⡀⠀⠀⠁⠀⠀⠀⠀⠀⠙⠻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
    """)
def skellys():
    print("""
    
    
    ,--.                                            
   (  oo]                                          
    `- A\                                                                                   
  _  I`-'
,o(`-V'
|( `-H-'
|(`--A-'
|(`-/_\'\
O `'I ``\\
(\  I    |\,
 \\-T-"`, |H====Ojo========//
  


   
    
    
    
    
    
    
    """)
def dub():
    print("""
      A           {}
 / \, | ,        .--.
|    =|= >      /.--.\
 \ /` | `       |====|
  `   |         |`::`|
      |     .-;`\..../`;-.
     /\\/  /  |...::...|  \
     |:'\ |   /'''::'''\   |
      \ /\;-,/\   ::   /\--;
      |\ <` >  >._::_.<,<__>
      | `""`  /   ^^   \|  |
      |       |        |\::/
      |       |        |/|||
      |       |___/\___| '''
      |        \_ || _/
      |        <_ >< _>
      |        |  ||  |
      |        |  ||  |
      |       _\.:||:./_
      |      /____/\____\
    """)
def princes():
    print(""""
       __
                /__`.
               / \ `\\
              /   \  `\
             /     \   \
            /_______\  /\
            (((( ))))
           (((' . ')))
           (((\_-_/)))
           (((_) (_)))
          /((( \ / )))\
         / (((  ^  ))) \
        / / ((  ^  )) \ \
       ( (   \  ^  /   ) )
        \ \   )www(   / /
         `\\ /     \ //'
           /'       `\
          /           \
         /             \
        /               \
       /                 \
      /                   \
     /                     \
    /                       \
   /                         \
  /                           \ jgs
 |                             |
  `-----......_____......-----'

    """)
def death ():
    print("""
 ▄██   ▄    ▄██████▄  ███    █▄       ████████▄   ▄█     ▄████████ ████████▄  
███   ██▄ ███    ███ ███    ███      ███   ▀███ ███    ███    ███ ███   ▀███ 
███▄▄▄███ ███    ███ ███    ███      ███    ███ ███▌   ███    █▀  ███    ███ 
▀▀▀▀▀▀███ ███    ███ ███    ███      ███    ███ ███▌  ▄███▄▄▄     ███    ███ 
▄██   ███ ███    ███ ███    ███      ███    ███ ███▌ ▀▀███▀▀▀     ███    ███ 
███   ███ ███    ███ ███    ███      ███    ███ ███    ███    █▄  ███    ███ 
███   ███ ███    ███ ███    ███      ███   ▄███ ███    ███    ███ ███   ▄███ 
 ▀█████▀   ▀██████▀  ████████▀       ████████▀  █▀     ██████████ ████████▀  
    """)
def kingdom ():
    print("""
    ~         ~~          __
       _T      .,,.    ~--~ ^^
 ^^   // \                    ~
      ][O]    ^^      ,-~ ~
   /''-I_I         _II____
__/_  /   \ ______/ ''   /'\_,__
  | II--'''' \,--:--..,_/,.-{ },
; '/__\,.--';|   |[] .-.| O{ _ }
:' |  | []  -|   ''--:.;[,.'\,/
'  |[]|,.--'' '',   ''-,.    |
  ..    ..-''    ;       ''. '
    """)

def sleepyhead():
 print("""
   _____________
   |-( )-        |
   |/'|\`        |
   |__|_\_`______|
                 zz
       ! _    zz           _____
       |(~} zz         !  [10:00]
       |(_/__________..| =========
       |  ||:::::::::::|  |_____|
       """)
def zhizhi():
    print("""
                 ....
                                .'' .'''
.                             .'   :
\\                          .:    :
 \\                        _:    :       ..----.._
  \\                    .:::.....:::.. .'         ''.
   \\                 .'  #-. .-######'     #        '.
    \\                 '.##'/ ' ################       :
     \\                  #####################         :
      \\               ..##.-.#### .''''###'.._        :
       \\             :--:########:            '.    .' :
        \\..__...--.. :--:#######.'   '.         '.     :
        :     :  : : '':'-:'':'::        .         '.  .'
        '---'''..: :    ':    '..'''.      '.        :'
           \\  :: : :     '      ''''''.     '.      .:
            \\ ::  : :     '            '.      '      :
             \\::   : :           ....' ..:       '     '.
              \\::  : :    .....####\\ .~~.:.             :
               \\':.:.:.:'#########.===. ~ |.'-.   . '''.. :
                \\    .'  ########## \ \ _.' '. '-.       '''.
                :\\  :     ########   \ \      '.  '-.        :
               :  \\'    '   #### :    \ \      :.    '-.      :
              :  .'\\   :'  :     :     \ \       :      '-.    :
             : .'  .\\  '  :      :     :\ \       :        '.   :
             ::   :  \\'  :.      :     : \ \      :          '. :
             ::. :    \\  : :      :    ;  \ \     :           '.:
              : ':    '\\ :  :     :     :  \:\     :        ..'
                 :    ' \\ :        :     ;  \|      :   .'''
                 '.   '  \\:                         :.''
                  .:..... \\:       :            ..''
                 '._____|'.\\......'''''''.:..'''
                            \\
    """)

def jay():
    print("""         \ : /
                    '-: __ :-'
                    -:  )(_ :--
                    -' |r-_i'-
            ,sSSSSs,   (2-,7
            sS';:'`Ss   )-j
           ;K e (e s7  /  (
            S, ''  SJ (  ;/
            sL_~~_;(S_)  _7
|,          'J)_.-' />'-' `Z
j J         /-;-A'-'|'--'-j\
 L L        )  |/   :    /  \
  \ \       | | |    '._.'|  L
   \ \      | | |       | \  J
    \ \    _/ | |       |  ',|
     \ L.,' | | |       |   |/
    _;-r-<_.| \=\    __.;  _/
      {_}"  L-'  '--'   / /|
            |   ,      |  \|
            |   |      |   ")
            L   ;|     |   /|
           /|    ;     |  / |
          | |    ;     |  ) |
         |  |    ;|    | /  |
         | ;|    ||    | |  |
         L-'|____||    )/   |
             % %/ '-,- /    /
     snd     |% |   \%/_    |
          ___%  (   )% |'-; |
        C;.---..'   >%,(   "'
                   /%% /
                  Cccc'""")

def callum():
    print("""
              .-----.   ()()
             /       \ .'()
             |__...__|/
             |_....._|
           .-'  ___  '-.
           \_.-`. .`-._/
            (|\ (_) /|)
             ( \_=_/ )
               (___)
    
    """)
def eryk():
             print("""
        
    
           \|  \<|>\  /<|>/  |/
            |    -   \  -    |
            \     ______     /
             \    \/  \/    /
              \            /

        """)
def troll():
    print("""
    ░░░░▄▄▄▄▄▓▓▓▄▄▄░░░░░
░░░░▄▄▓▀▀▀▀▀▀▓▓▓▓▓▓▄░░░
░░▄▄▓▀▀░░░░░░░░░░░░▀▓▄░
░▐▓▓▌░░░░░░▄▄▄▄▄░░░░░▓▌
░▐▓▒░░░░░░█░▒◐▒░█░░░░░▓
░▓▓▌░░░░░░░▀▀▀▀▀░░░░░▒▓
░▐▓░░░░░░░░░░░░░░░░▒▒▒▓
█░▀▄░█▄█▀▄▄░▀░▀▄▄▀░░█░█
░█░░░▀▄█▄█░█▀▄▄▄▄▄▀██░█
░░█░░░░█░███▄█▄█▄███░░█
░░░█░░░▀▀█░█▀█▀█▀███░█
░░░░▀▄░░░░▀▀▄█▄█▄█▄▀░█
░░░░░░▀▄▄░▒▒▒░░░░░░░░░█
░░░░░░░░░▀▀▄▄▄▄▄▄▄▄▄▄▀
    """)
def intro():
    kingdom()       
    time.sleep(sleeptime)
    print("long long ago there was a kingdom called eldendoor ")
    time.sleep(sleeptime)
    print("it was peacful")
    time.sleep(sleeptime)
    print("until the evil lord zhi attacked")
    time.sleep(sleeptime)
    zhizhi()
    print("he burned the village and took the princess daisy")
    time.sleep(sleeptime)
    print("now the last surving knight jay must slay the zhi and get the princess back")
    time.sleep(sleeptime)
    jay()
    time.sleep(sleeptime)
    print("jay set out to try and find the princes")
    time.sleep(sleeptime)
    print("A leprechaun appears do you kill him or dont kill him")
    callum()
    c4()
    
    x=True
    while x == True:
        choice1 = input()
        if choice1 == 'kill':
            print("jay swiftley kills the evil leprechaun callum") 
            st1()
           
            
            x=False

        elif choice1 == 'spare':
            print("callum throws a gold coin at jay's head he dies")
            death()
            x=False
        else:
            print("do spare or kill callum")
                   
def st1():
    print("jay sees a cave")
    time.sleep(sleeptime)
    print("jay traverse through a cave")
    time.sleep(sleeptime)
    print("when the evil vampire eryk appears")
    eryk()
    print ("do you stab the eryk in the chest or head")
    c3()
    x=True
    while True:
        choice1 = input("choose now!")

        if choice1 == 'chest':
            print("jay stabs eryk in the chest\nyou have slained vampire king eryk") 
            x=False
            st2()
            break;
        elif choice1 == 'head':
            print("you were bitten by eryk and died")
            death()
            x = False
            break;          
        else:
            print("do stabb eryk in the chest or head")
          
def st2():
    print("you")
    time.sleep(sleeptime)
    print("you go further in the cave.\nyou see a knight")
    dub()
    print("you aproach the knight")
    time.sleep(sleeptime)
    print("jay:wait are you knight form eldendoor")
    time.sleep(sleeptime)
    print("knight:yes i am sir gondor nice to meet you")
    time.sleep(sleeptime)
    print("jay:where is your emblem")
    time.sleep(1)
    print("gondor:im must have lost it in battle")
    time.sleep(1)
    print("gondor: there are more soldiers deeper in the cave if you follow me i can lead you to them")
    print("do follow gondor or attack gondor")
    print("jay gets suspicious")
    c1()
    st21()
    
def st21():
    x=True
    while x == True:
            choice1 = input()
            if choice1 == 'follow':
                print("jay follows gondor") 
                print("he brings you a cave you see other knights")
                time.sleep(sleeptime)
                print(" but they are all dead ")
                skellys()
                time.sleep(sleeptime)
                dub2()
                print("gondor starts laughin he transform")
                print("gondor attacks you with his claws")
                death()
                x=False
            elif choice1 == 'attack':
                print("jay stabs gondor in the stomach gonder eyes widen")
                print("gondor starts laughin ")
                dub2()
                print("gondor:you will never defeat the darklord zhi he will have your soul")
                st3()
                x=False
            else:
                print("do you follow gondor or do you attack gondor")   
def st3():
    print("our hero jay makes his way out of cave")
    time.sleep(sleeptime)
    print("when our hero sees the castle of the evil lord zhi")
    time.sleep(sleeptime)
    print("he finnaly made it he only needs to go over a bridge")
    time.sleep(sleeptime)
    print("fi fa fo ")
    time.sleep(sleeptime)
    print("all of the sudden a big troll sits on the bridge")
    troll()
    print("do talk to the troll or attack")
    c2()
    x=True
    while x == True:
        choice2 = input()
        if choice2 == 'attack':
            print("jay tries to attack the troll but his sword just bounce back from the troll masive belly")
            print("the troll proceeds to eat you whole ")
            death()
            x=False
        elif choice2 == 'talk':
            print("fi fa fo my name is the damian if you can anwser my question correctly i will let you pass")
            q1()
            x=False
        else:
            print("do you attack the troll or talk to the troll")

def q1():
        troll()
        print("what is youre name")
        c5()
        x=True
        while x == True:
            choice3 = input()
            if choice3 == 'jay':
                print("troll that is the right answer")
                q2()
                x=False
            elif choice3 == 'jair':
                print("thats the wrong answer")
                print("the troll proceeds to eat you whole")
                death()
            elif choice3 == 'jamal':
                print("that is the wrong answer")
                print("the troll proceeds to eat you whole")
                death()
                x=False
            else:
                print("jay:i cant say that the troll will eat me")    

def q2():
        troll()
        print("who was the first person you killed")
        c6()
        x=True
        while x == True:
            choice3 = input()
            if choice3 == 'callum':
                print("troll that is the right answer")
                q3()
                x=False
            elif choice3 == 'eryk':
                print("thats the wrong answer")
                print("the troll proceeds to eat you whole")
                death()
                x=False
            elif choice3 == 'gondor':
                print("that is the wrong answer")
                print("the troll proceeds to eat you whole")
                death()
                x=False
            else:
                print("thats definitely wrong")

def q3(): 
        troll()
        print("what is your village called ")
        c7()
        x=True
        while x == True:
            choice3 = input()
            if choice3 == 'elendoor':
                print("troll that is the right answer")
                q4()
                x=False
            elif choice3 == 'eichenwalde':
                print("thats the wrong answer")
                print("the troll proceeds to eat you whole")
                death()
                x=False
            elif choice3 == 'gondor':
                print("that is the wrong answer")
                print("the troll proceeds to eat you whole")
                death()
                x=False
            else:
                print("thats definitely wrong")
       

def q4():
        print("what is the name of youre dear princess")
        x=True
        while x == True:
            choice3 = input()
            if choice3 == 'daisy':
                print("troll that is the right answer")
                print("you may pass")
                q5()
                x=False
            elif choice3 == 'peach':
                print("thats the wrong answer")
                print("the troll proceeds to eat you whole")
                death()
                x=False
            elif choice3 == 'cindrella':
                print("that is the wrong answer")
                print("the troll proceeds to eat you whole")
                death()
                x=False
            else:
                print("thats definitely wrong")
        
def q5():
        print("our hero passes the troll and already hears the cries of the princess")
        time.sleep(sleeptime)
        print("and without hesitating jay runs in to the castle")
        zhizhi()
        time.sleep(sleeptime)
        print("zhi:so you finaly arive")
        time.sleep(sleeptime)
        print("to your grave")                                          
        print("zhi hits jay with a his magic\njay falls it looks like its over but then princess daisy stabs zhi in the neck")
        princes()
        print("princess daisy:that was for my kingdom")
        print("the princess walks off to the sunset a free woman")
        print("and jay took our hero knight after a long adventure took a long sleep")

        sleepyhead()
      #the end 

intro()

