# Pinterest-easy-board-download

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




