while True:
    basic.show_leds("""
    . . . . .
    . . # # #
    # . # # #
    # # # . .
    . # # . .
    """)
    basic.pause(400)
    basic.show_leds("""
    . . . . .
    . . # # #
    # . # # #
    # # # . .
    . # # . #
        """)
    basic.pause(400)
    basic.show_leds("""
    . . . . .
    . . # # #
    # . # # #
    # # # . .
    . # # # .
    """)
    basic.pause(400)
    def pulsador():
        basic.show_leds("""
        . . # # #
        # . # # #
        # # # . .
        . # # . .
        . . # . .
        """)
    basic.pause(400)
    

input.on_button_pressed(Button.A, pulsador)
    
  

