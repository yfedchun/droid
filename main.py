from kivy.app import App
from kivy.uix.label import Label

# Define the main app
class HelloApp(App):
    def build(self):
        # Return a simple Label widget with "Hello, World!" text
        return Label(text='Hello, World!')

# Run the app
if __name__ == '__main__':
    HelloApp().run()
