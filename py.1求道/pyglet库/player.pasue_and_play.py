import pyglet

# 创建一个窗口（如果需要音频可视化等功能）
window = pyglet.window.Window()

# 创建一个音频文件的MediaSource
media_source = pyglet.media.load(r'D:\Users\vscode\python\py.1求道境\音乐随机播放器\music\Love Story--Taylor Swift.mp3')

# 创建一个Player并将MediaSource分配给它
player = pyglet.media.Player()
player.queue(media_source)

@window.event
def on_draw():
    window.clear()

# 按下空格键时，暂停或恢复播放
@window.event
def on_key_press(symbol, modifiers):
    if symbol == pyglet.window.key.SPACE:
        if player.playing:
            player.pause()
        else:
            player.play()

# 启动事件循环
pyglet.app.run()
