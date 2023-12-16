# A collection of Python Scripts

## cmd_toolkit.py
This is a python app created using `tkinter`. 
- My advice is to run this script via a shortcut (I use Ubuntu custom shortcuts within `Settings`)
- Opens gui where your cursor is currently located
- Small and non obtrusive
- Displays different section/categories
- Contains various commands within each section

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
This simple tool is used for splitting up the contents of your clipboard, then pasting each line one at a time, pressing the enter key between each paste.
- Can split text separated by commas and spaces
  - Taking the comma as priority, whilst removing the spaces.
- Can split text separated by spaces only
- Can split text separated by commas only
- Can split text separated by lines
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
