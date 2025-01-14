from kivy.app import App
from kivy.lang.builder import Builder
from kivy.uix.label import Label
from kivy.uix.popup import Popup
from kivy.uix.screenmanager import ScreenManager,Screen
from kivy.core.window import Window
import os
import shutil


Builder.load_string('''
<ColoredLabel@Label>:
    canvas.before:
        Color:
            rgba: 32/255,91/255,122/255, 1
        Rectangle:
            pos: self.pos
            size: self.size
    font_size:'18sp'
<Titles@Label>:
    font_size:'24sp'
<ColoredLabel2@Label>:
    canvas.before:
        Color:
            rgba: 32/255,91/255,122/255, 1
        Rectangle:
            pos: self.pos
            size: self.size
<CenterTextinput@TextInput>:
    padding: [0, (self.height - self.line_height) / 2]
    font_size:'18sp'
<MySpinnerOption@SpinnerOption>:
    background_color: 122/255,181/255,212/255, 1
    font_size:'18sp'

<DesignButton@Button>:
    background_color: 0.2, 0.6, 0.8, 0  # Set the background color
    font_size:'18sp'
    canvas.before:
        Color:
            rgba: 32/255,91/255,122/255,1  # Set the same color as background_color
        RoundedRectangle:
            pos: self.pos
            size: self.size
            radius: [10,]
<DesignButton2@Button>:
    background_color: 0.2, 0.6, 0.8, 0  # Set the background color
    font_size:'27sp'
    canvas.before:
        Color:
            rgba: 32/255,91/255,122/255,1  # Set the same color as background_color
        RoundedRectangle:
            pos: self.pos
            size: self.size
            radius: [15,]

<AppLayout@FloatLayout>:
    FloatLayout:
        canvas.before:
            Color:
                rgba: 29/255,56/255,73/255, 1
            Rectangle:
                pos: self.pos
                size: self.size

        FloatLayout:
            size_hint: (1, 0.09)
            pos_hint: {'center_x': 0.5, 'center_y': 0.955}
            canvas.before:
                Color:
                    rgba: 20/255,47/255,68/255, 1
                Rectangle:
                    pos: self.pos
                    size: self.size


            GridLayout:
                cols: 1
                size_hint: (0.8, 1)
                pos_hint: {'center_x': 0.5, 'center_y': 0.5}

                Label:
                    text: 'FILE-SORTER'
                    font_size:'35sp'
                    text_size: self.size
                    valign: 'center'
                    halign: 'center'

<Home>:
    name:'home'
    AppLayout:

        GridLayout:
            cols:2
            size_hint:(0.8,0.26)
            pos_hint:{'center_x':0.5,'center_y':0.55}
            ColoredLabel:
                id: label
                text: "Drag and drop a folder here: >>>>>>"
                valign: 'center'
                halign:'center'
                text_size:self.size
                height: 50
            TextInput:
                id: folder_label
                text: ""
                text_size:self.size
                valign: 'center'
                halign:'center'
                height: 50
        GridLayout:
            cols:1
            size_hint:(0.3,0.1)
            pos_hint:{'center_x':0.5,'center_y':0.32}
            
            Spinner:
                id: spinner
                text: 'Choose formart'
                font_size:'18dp'
                valign: 'center'
                halign:'center'
                values: ['File extension','File name']
                background_color:  122/255,181/255,212/255,1  # Background color of the spinner button
                option_cls: 'MySpinnerOption'
                canvas.before:
                    Color:
                        rgba: 32/255,91/255,122/255,0 # Set the same color as background_color
                    RoundedRectangle:
                        pos: self.pos
                        size: self.size
                    
        GridLayout:
            cols:1
            size_hint:(0.2,0.1)
            pos_hint:{'center_x':0.5,'center_y':0.18}
            DesignButton:
                text: "Sort"
                text_size:self.size
                valign: 'center'
                halign:'center'
                on_press: root.on_convert_button_press(self)
            

''')

class Home(Screen):
    def on_convert_button_press(self,instance):
        # Get the dropped file path from the label
        file_path = self.ids.folder_label.text.split(": ", 1)
        folder_path = self.ids.folder_label.text.split(": ", 1)
        if self.ids.spinner.text=='File extension':
            try:
                file_path = file_path[1]
                target_folder=file_path
                extensions={item.split('.')[-1] for item in os.listdir(target_folder) if os.path.isfile(os.path.join(target_folder, item))}

                for extension in extensions:
                    if not os.path.exists(os.path.join(target_folder, extension)):
                        os.makedirs(os.path.join(target_folder, extension))

                for item in os.listdir(target_folder):
                    if os.path.isfile(os.path.join(target_folder, item)):
                        file_extension =item.split('.')[-1]
                        shutil.move(os.path.join(target_folder, item), os.path.join(target_folder, file_extension, item))

                # Update the label with the success message and exported file's path
                self.ids.folder_label.text = 'Folder sorted by extension'
            except Exception as e:
                self.show_error_popup("Error", f"Error occurred: {e}")

        elif self.ids.spinner.text=='File name':
            try:
                folder_path = folder_path[1]
                target_folder = folder_path
                files = [item for item in os.listdir(target_folder) if os.path.isfile(os.path.join(target_folder, item))]

                for file in files:
                    filename = os.path.splitext(file)[0]
                    file_extension = os.path.splitext(file)[-1]

                    # Create a directory for the filename if it doesn't exist
                    filename_folder = os.path.join(target_folder, filename)
                    if not os.path.exists(filename_folder):
                        os.makedirs(filename_folder)

                    # Move the file to the corresponding filename folder
                    shutil.move(os.path.join(target_folder, file), os.path.join(filename_folder, file))

                # Update the label with the success message
                self.ids.folder_label.text = 'Files grouped by filename'
            except Exception as e:
                self.show_error_popup("Error", f"Error occurred: {e}")
        
        else:
            self.show_error_popup("Error", f"Error occurred: Select a format")
    
    def show_error_popup(self, title, message):
        popup = Popup(title=title, content=Label(text=message), size_hint=(0.99, 0.3))
        popup.open()

class FileSorterApp(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(Home(name='home'))
        Window.minimum_width = 500
        Window.minimum_height = 500
        Window.bind(on_dropfile=self.on_file_drop)
        return sm
    
    def on_file_drop(self, window, file_path):
        # This method will be called when a file is dropped
        file_path_str = file_path.decode("utf-8") 
        Home = self.root.get_screen('home')
        Home.ids.folder_label.text = f"File dropped: {file_path_str}"


if __name__ == '__main__':
    FileSorterApp().run()