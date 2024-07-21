import pyglet

music = pyglet.media.load('\\Ensemble.mp3')
player = pyglet.media.Player()
player.queue(music)
player.loop = True  
player.play()
pyglet.app.run()