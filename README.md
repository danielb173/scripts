# A collection of Python Scripts

## cmd_toolkit.py
This is a python app created using `tkinter`. The idea behind this app is to save time writing out commands by providing a list of commands to choose from, selecting a command will save it to your clipboard and close the app. I used a version of this on Windows using AutoHotKey and needed to get it working with Ubuntu. ChatGPT made this in python which will work with most Operating systems providing you can install the dependencies below.
- My advice is to run this script via a shortcut (I use Ubuntu custom shortcuts within `Settings`).
- Once the shortcut is activated, the script will open a GUI where your cursor is currently located.
- I tried to keep the app small and less obtrusive, it will automatically close once you have selected the command you need.
- Displays different section/categories on mouse hover.
- Contains various commands within each section and can be easily customised to your own needs.

### Install instructions
```
sudo apt update
```
```
sudo apt install python3
```
```
sudo apt install python3-tk
```
```
sudo apt install python3-pip
```
```
pip install pyperclip
```
You will also need the following font: [Major Mono Display](https://fonts.google.com/download?family=Major%20Mono%20Display)
But please note you can easily change this to your preferred font if you wish.
```
sudo cp ~/Downloads/MajorMonoDisplay-Regular.ttf /usr/share/fonts/
```
```
sudo fc-cache -f -v
```
Verify installation was successful by running this:
```
fc-list : family | grep "Major Mono Display"

```

## paste_flow.py
This simple script is used for splitting up the contents of your clipboard, then pasting each line one at a time, pressing the enter key between each paste.
- Can split text separated by commas and spaces.
  - Taking the comma as priority, whilst removing the spaces.
- Can split text separated by spaces only.
- Can split text separated by commas only.
- Can split text separated by lines only.
- Once the data you have copied has been split, it will then be pasted one after the other.

### Install instructions
```
sudo apt update
```
```
sudo apt install python3-pip
```
```
pip3 install pyperclip pyautogui
```
```
sudo apt install python3-tk
```
