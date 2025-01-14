# File-sorter
FileSorterApp Documentation
Overview
This is a Kivy-based Python application designed to sort files in a selected folder. The files can be sorted either by their extensions (e.g., .txt, .jpg) or by their names (grouping files into folders named after the file names). The application uses a graphical user interface with drag-and-drop functionality for folder selection.

File Structure
Home Screen: The main screen where users interact with the app to sort files.
App Layout: Includes the app title, drag-and-drop area for selecting folders, spinner for choosing sort criteria, and a button to execute the sorting.
Features
Drag-and-Drop Functionality:

Users can drag and drop a folder onto the app interface.
The dropped folder path is displayed in the text input field.
Sorting Options:

File Extension: Groups files into subfolders based on their file extensions.
File Name: Groups files into subfolders named after the file names.
Error Handling:

Displays a popup with an error message if an invalid folder is dropped or sorting fails.
Custom UI Elements:

The app uses custom-designed buttons, labels, and input fields for an enhanced user experience.
Classes

1. Home(Screen)
Represents the main app screen where file sorting operations are performed.

Methods:
on_convert_button_press(self, instance):

Triggered when the "Sort" button is pressed.
Checks the selected sorting option (File extension or File name) and sorts files accordingly.
Updates the status message in the text input field.
show_error_popup(self, title, message):

Displays an error popup with the provided title and message.

2. FileSorterApp(App)
The main application class responsible for initializing and managing the app.

Methods:
build(self):

Initializes the ScreenManager and adds the Home screen.
Sets the minimum window size.
Binds the on_dropfile method to handle drag-and-drop events.
on_file_drop(self, window, file_path):

Triggered when a file or folder is dropped onto the app.
Updates the folder_label field with the path of the dropped folder.
Kivy Layouts and Widgets
Custom Widgets:
ColoredLabel: A label with a custom background color and font size.
DesignButton: A custom-styled button with rounded corners and a consistent color theme.
MySpinnerOption: A spinner option with custom styling for dropdown items.
Screens:
Home Screen:
Contains the following:
A title bar with the app name.
A label for drag-and-drop instructions.
A text input field to display the dropped folder path.
A spinner to select the sorting option.
A button to trigger the sorting operation.
User Instructions
Launch the App:

Run the script to start the application.
Select a Folder:

Drag and drop a folder onto the app window. The folder path will appear in the input field.
Choose Sorting Option:

Use the dropdown spinner to select either File extension or File name.
Sort Files:

Click the "Sort" button to organize the files in the selected folder.
View Results:

If successful, a success message appears in the input field.
If an error occurs, a popup will display the error details.
Error Handling
Invalid Folder: Displays an error popup if the dropped folder path is invalid.
No Sorting Option Selected: Prompts the user to select a sorting option if none is chosen.
Dependencies
Python Modules:
kivy
os
shutil
Example Usage
Drag and drop a folder containing files onto the app.
Select "File extension" from the spinner.
Click the "Sort" button.
Files in the folder will be grouped into subfolders based on their extensions.
Notes
The app is currently designed for desktop usage due to its drag-and-drop functionality.
Ensure that the app has permission to modify the dropped folder's contents.
The spinner provides only two sorting options: by file extension and file name.
