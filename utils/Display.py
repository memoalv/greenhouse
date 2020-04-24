import Adafruit_CharLCD as LCD


class Display:
    def __init__(self, rs=26, en=19, d4=13, d5=6, d6=5, d7=11, backlight=None, columns=20, rows=4):
        # Raspberry Pi pin configuration:
        self.lcd_rs = rs
        self.lcd_en = en
        self.lcd_d4 = d4
        self.lcd_d5 = d5
        self.lcd_d6 = d6
        self.lcd_d7 = d7
        self.lcd_backlight = backlight

        # Define LCD column and row size for columnsXrows LCD.
        self.lcd_columns = columns
        self.lcd_rows = rows

        # Initialize the LCD using the pins above.
        self.lcd = LCD.Adafruit_CharLCD(self.lcd_rs, self.lcd_en, self.lcd_d4, self.lcd_d5, self.lcd_d6, self.lcd_d7,
                                   self.lcd_columns, self.lcd_rows, self.lcd_backlight)
        self.lcd.set_backlight(0)

    def printMessage(self, message):
        self.lcd.message(message)

    def clearScreen(self):
        self.lcd.clear()
    
    def showCursor(self):
        self.lcd.show_cursor(True)

    def hideCursor(self):
        self.lcd.show_cursor(False)
    
    def blink(self, show):
        self.lcd.blink(show)

    



# # Print a two line message
# lcd.message('Hello\nworld!')

# # Demo showing the cursor.
# lcd.clear()
# lcd.show_cursor(True)
# lcd.message('Show cursor')

# time.sleep(5.0)

# # Demo showing the blinking cursor.
# lcd.clear()
# lcd.blink(True)
# lcd.message('Blink cursor')

# time.sleep(5.0)

# # Stop blinking and showing cursor.
# lcd.show_cursor(False)
# lcd.blink(False)

# # Demo scrolling message right/left.
# lcd.clear()
# message = 'Scroll'
# lcd.message(message)
# for i in range(lcd_columns-len(message)):
#     time.sleep(0.5)
#     lcd.move_right()
# for i in range(lcd_columns-len(message)):
#     time.sleep(0.5)
#     lcd.move_left()

# # Demo turning backlight off and on.
# lcd.clear()
# lcd.message('Flash backlight\nin 5 seconds...')
# time.sleep(5.0)
# # Turn backlight off.
# lcd.set_backlight(0)
# time.sleep(2.0)
# # Change message.
# lcd.clear()
# lcd.message('Goodbye!')
# # Turn backlight on.
# lcd.set_backlight(1)
