 # CAESER CIPHER
#### Video Demo:  https://youtu.be/cQmRdCGPf_0
#### Description:
A Caesar cipher is a simple and widely known encryption technique. It is a type of substitution cipher in which each letter in the plaintext is replaced by a letter some fixed number of positions down the alphabet. For example, with a left shift of 3, D would be replaced by A, E would become B, and so on. The method is named after Julius Caesar, who used it in his private correspondence.

The application is quite simple as you provide it with text that should be encrypted or decrypted and the integer key, Then the program does the encryption process and displays the result.

I used customtkinter instead of tkinter as ctk is more customizable and the widgets are much cleaner and more organized. First, I used tkinter to get familiar with GUI as it was my first-time creating GUI and the program worked well but it wasn't looking good. When I moved to CTK I had to write the whole GUI code again starting from zero, but it was relly fun as liked looking through the documents and looking for a certain parameter to a certain widget and what could make the widget as I want.

The main logic of the program consists of two functions: function to decrypt text and one to encrypt text. Both takes two arguments: the text and they key, and it performs some code to make sure that the text entered has no special characters as Caeser cipher does not handle special characters, but it forgives while space. And also checks that the key must be an integer otherwise it will raise an error by calling a method that displays an error message box.

The "show_error_message" displays the error message when the key or the text are not of the required type. It uses the message box method form tkinter not customtkinter as the message box is not in it "I guess:)".

The "printen" function displays the encrypted text inside of output text widget. It is the function that is called when encrypt button is clicked as it gets the text in the text entry widget and call the encrypt function then clear the output text widget before inserting the encrypted text.

The "printde" function displays the decrypted text inside of output text widget. It is the function that is called when decrypt button is clicked as it gets the text in the text entry widget and call the decrypt function then clear the output text widget before inserting the decrypted text.

The "clear" function clears all text inside the text and key entry widgets. It is the function that is called when the clear button is clicked.

The a few lines of code to initialize the module and creating the main windo. The setting the geometry and the title of teh window.

Then adding the widgets inside the main window. Each one with its own parameters to set its properties like the font type or the width, heigh, the foreground color, The text displayed and many other parameters.
