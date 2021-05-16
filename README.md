# Pinterest-easy-board-download
<img src="https://camo.githubusercontent.com/b792c14c7f4dea762d5f386ad20baddb32dd9db5c9f334a68063bd8dcda3bf37/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f707974686f6e2d332e362d677265656e2e7376673f7374796c653d706c6173746963" alt="Python 3.6" data-canonical-src="https://img.shields.io/badge/python-3.6-green.svg?style=plastic" style="max-width:100%;"> <img src="https://camo.githubusercontent.com/f3346ea2f191f90086ab33fe58a2a8f71504f9a280d5535fad1c1d7f4e73a408/68747470733a2f2f696d672e736869656c64732e696f2f707970692f6c2f646f68712d6578616d706c652d70726f6a6563742e737667" alt="ExampleProject license" data-canonical-src="https://img.shields.io/pypi/l/dohq-example-project.svg" style="max-width:100%;">

This simple Python project will help you download a Pinterest board.

## Login

### run.py

In order for the application to gain access to boards, authorization is required. You can download both your own hidden boards and public ones. Email and password are entered into the following variables:

` login = "test@gmail.com"  # The email you use for authorization `

` password = "password"       # The password you use for authorization  `

Insert your details instead of "test@gmail.com" and "password"

## Download board

### run.py

The board is downloaded to the specified folder. You can change the export folder. By default, the download takes place in the specified folder.

` export_dir = "export_directory/" # Folder for exporting images `

The address of the board you want to download must be indicated here:

` desk_url = https://www.pinterest.ru/desk_url/ # The link to the Pinterest board you want to download`

You can download absolutely any board to which you have access

## Chrome Driver

### run.py

A web driver is required for the application to work correctly. You must also have Google Chrome installed.

You can download the appropriate web driver for your version of Google Chrome here:

https://chromedriver.chromium.org/downloads

The downloaded file must be placed in the project folder "Chrome Driver"

## Other parameters

### run.py

These parameters depend on your internet speed. If the program does not have time to log in, make this parameter larger.

` delay_time = 15 # If Pinterest does not have time to log in before going to your board, change this parameter `

The next parameter is responsible for the gaps between the scrolling of the board. If the images do not have time to load, also make this parameter larger.

` scroll_delay_time = 3 # Page scrolling delay. If images fail to load, increase this parameter ` 




