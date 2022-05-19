def play(sound): 
    from pygame import mixer
    mixer.init()
    mixer.music.load(sound)
    mixer.music.play()