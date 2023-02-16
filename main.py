import pyautogui as pt
import pyperclip as pc
from time import sleep
from whatsapp_responses import responses
import pyperclip as pl
# instructions for our WhatsApp Bot
class WhatsApp:


    # Defines the starting values
    def __init__(self, speed=.5,click_speed=.3):
        self.speed = speed
        self.click_speed = click_speed
        self.message = ''
        self.last_message = ''


    # Navigate to the green dots for new messages
    def nav_green_dot(self):
        try:
            position = pt.locateOnScreen('IMG\green_dot.png', confidence=.7)
            pt.moveTo(position[0:2], duration=self.speed)
            pt.moveRel(-100,0,duration=self.speed)
            pt.doubleClick(interval=self.click_speed)
        except Exception as e:
            print('Exception (nav_green_dot):',e)

    # Navigate to our message input box
    def nav_input_box(self):
        try:
            position = pt.locateOnScreen('IMG\clip.png', confidence=.7)
            pt.moveTo(position[0:2], duration=self.speed)
            pt.moveRel(100,10,duration=self.speed)
            pt.doubleClick(interval=self.click_speed)
        except Exception as e:
            print('Exception (nav_input_box):',e)

    # Navigate to the message we want to respond to
    def nav_message(self):
        try:
            position = pt.locateOnScreen('IMG\clip.png', confidence=.7)
            pt.moveTo(position[0:2], duration=self.speed)
            pt.moveRel(35,-50,duration=self.speed)
            
        except Exception as e:
            print('Exception (nav_message):',e)

    # Copies the message that we want to process
    def get_message(self):
        pt.tripleClick(interval=self.click_speed)
        sleep(self.speed)
        pt.rightClick(interval=self.click_speed)
        #sleep(self.speed)

        position = pt.locateOnScreen('IMG\copy.png', confidence=.7)
        pt.moveTo(position[0:2], duration=self.speed)
        #pt.moveRel(10,10,duration=self.speed)
        pt.leftClick(interval=self.click_speed)
        sleep(1)

        self.message = pc.paste()
        print('User says: ',self.message)

    # Sends the message to the user
    def send_message(self):
        try:
            # Check whether the last message was the same as the current message

            if self.message != self.last_message:
                bot_response = responses(self.message)

                print('You say: ' , bot_response)
                pt.typewrite(bot_response, interval = .1)
                #pt.typewrite('\n') # Sends the message (Disable it while testing)

                # Assigns them the same message
                self.last_message = self.message
            else:
                print('No new message received')
        except Exception as e:
            print('Exception (send_message):',e)

        # Close response box
    def nav_x(self):
        try:
            position = pt.locateOnScreen('IMG\x.png', confidence=.7)
            pt.moveTo(position[0:2], duration=self.speed)
            pt.moveRel(10,10,duration=self.speed)
            pt.leftClick( )

        except Exception as e:
            print('Exception (send_message):',e)

    def new_message(self):
        return pt.locateOnScreen('IMG\green_dot.png', confidence=.9)
    
    def go_search(self,text=None):
        position = pt.locateOnScreen('IMG\buscar.png', confidence=.7)
        print( 'position' ,position)
        pt.moveTo(position[0:2], duration=.3)
        pt.moveRel(80,19,duration=.3)
        pt.leftClick( )
        pt.typewrite(text, interval = .1)
        pt.moveRel(0,100,duration=.3)
        pt.leftClick( )

    def write_long_message(self,message):
        '''for linea in message.split('\n'):
            pt.typewrite(linea, interval = .1)
            pt.hotkey('shift','enter')'''
        pl.copy(message)
        sleep(0.5)
        pt.hotkey('ctrl','v')

    def search_group(self,group=None,message=None):
        self.go_search(group)
        '''position = pt.locateOnScreen('input.png', confidence=.9)
        print( 'position' ,position)
        pt.moveTo(position[0:2], duration=.3)'''

        self.write_long_message(message)

        


        

        






# initializes the WhatsApp Bot
wa_bot = WhatsApp(speed=.5,click_speed=.4)

# Run the programme in a loop
messages = """Para poder mejorar su experiencia y poder hacerles llegar las últimas noticias, las ofertas disponibles y los concursos y regalos que hacemos mes a mes, hemos preparado un grupo para que puedan tener toda esta información a su alcance. 
 
Está llegando Navidad y también el final del año, por lo cual hemos preparado un GRAN DESCUENTO junto con MUCHAS CLASES GRATIS. Únete ahora a nuestro grupo ingresando en este enlace: """
#while True:
    
#    if wa_bot.new_message() != None:

        
        #wa_bot.nav_green_dot()
        #wa_bot.nav_x()
        #wa_bot.nav_message()
        #wa_bot.get_message()
        #wa_bot.nav_input_box()
        #wa_bot.send_message()
sleep(2)

wa_bot.search_group('stuff business',messages)
        

   





