import os
# os.environ["KIVY_CAMERA"] = "android"
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.lang import Builder

Builder.load_string('''
<CameraClick>:
    orientation: 'vertical'
    Camera:
        id: camera
        resolution: (640, 480)
        play: False
    ToggleButton:
        text: 'Init'
        on_release: camera.play = not camera.play
        size_hint_y: None
        height: '48dp'
    Button:
        text: 'Play'
        size_hint_y: None
        height: '48dp'
        on_release: camera.play = True
    Button:
        text: 'Stop'
        size_hint_y: None
        height: '48dp'
        on_release: camera.play = False
''')


class CameraClick(BoxLayout):
    pass
