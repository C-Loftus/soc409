screen PopUp(message):
    frame:
        xpadding 10
        ypadding 10
        xalign 0.5
        yalign 0.5
        xsize 600

        vbox:
            text message
            text ""
            textbutton "I did it!":
                xcenter 300
                action Return()
                style "my_button"
                text_color "#fff"
                xpadding 5
                ypadding 5
