from kivy.app import App
from kivy.uix.image import Image
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button

class PhotoViewerApp(App):
    def build(self):
        layout = BoxLayout(orientation='vertical', padding=10, spacing=10)
        self.img = Image(source='assets/photo.jpg', allow_stretch=True, keep_ratio=True)
        self.img.opacity = 0  # hidden at start

        btn = Button(
            text="Show My Photo",
            size_hint=(None, None),
            size=(180, 60),
            pos_hint={'center_x': 0.5}
        )
        btn.bind(on_press=self.show_image)
        layout.add_widget(btn)
        layout.add_widget(self.img)
        return layout

    def show_image(self, instance):
        self.img.opacity = 1  # show the image

if __name__ == '__main__':
    PhotoViewerApp().run()

