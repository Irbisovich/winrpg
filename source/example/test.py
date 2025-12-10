from engine import *
import colorama
import PIL.Image

engine = Engine('TEST', 'This is a test of WinRPG Engine Functions.', colorama)

images = [
    Image('bird.png', PIL.Image),
    Image('forest.png', PIL.Image),
    Image('vetka.jpg', PIL.Image),
]

engine.place(images[0].create(), '1')
engine.update(True)
engine.place(images[1].create(), '2')
engine.update(True)
engine.place(images[2].create(), '3')
engine.update(True)
engine.place(images[0].create(), '1')
engine.update(False)
engine.place(images[1].create(), '2')
engine.update(False)
engine.place(images[2].create(), '3')
engine.update(False)

soundd = Sound('test.wav')

soundd.play()
engine.place('Sound testing', 'Playing sound')
engine.update(False)
soundd.stop()
engine.place('Sound testing', 'Stopping sound')
engine.update(False)
engine.raiseerr('Testing error raise')

engine.raiseerr('If these test runs normally, then engine is working.')
