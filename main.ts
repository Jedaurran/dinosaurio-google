while (true) {
    basic.showLeds(`
    . . . . .
    . . # # #
    # . # # #
    # # # . .
    . # # . .
    `)
    basic.pause(400)
    basic.showLeds(`
    . . . . .
    . . # # #
    # . # # #
    # # # . .
    . # # . #
        `)
    basic.pause(400)
    basic.showLeds(`
    . . . . .
    . . # # #
    # . # # #
    # # # . .
    . # # # .
    `)
    basic.pause(400)
    basic.pause(400)
}
input.onButtonPressed(Button.A, function pulsador() {
    basic.showLeds(`
        . . # # #
        # . # # #
        # # # . .
        . # # . .
        . . # . .
        `)
})
