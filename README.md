# IA Assistant

Assistant with Gemini IA (Google)

<div align="center">
 
![Image](./src/images/screenshot-1.png)

</div>

## Requirements

### All OS

- Python 3.\* [(Python.org)](https://www.python.org/)
- TkInter [(Wiki Python)](https://wiki.python.org/moin/TkInter)
- Api key to Gemini IA [(Google AI Studio)](https://aistudio.google.com/app/apikey)
- Font Poppins ([From Google fonts](https://fonts.google.com/specimen/Poppins))

### Linux

- xclip [(Github)](https://github.com/astrand/xclip) or wl-clipboard [(Github)](https://github.com/bugaevc/wl-clipboard)

## Install

- Config `GOOGLE_API_KEY` in you environments
- Clone this repo
- `cd ./IA-Assistant` and execute `start.py` script

_If you OS require, set permissions to execute to `start.py` script_

## Extras

### Copy result

When show the result, press `[Shift] + [c]` to copy it
or press `[ESCAPE]` to close window, remember,
all question and response is saved in history. _See [Commands.](/#commands)_

### Commands

Start prompt with:

| Command | Action                    |
| ------- | ------------------------- |
| `:trs`  | Translate text to Spanish |
| `:tre`  | Translate text to English |
| `:hs`   | View history              |
| `:hsc`  | Clear history             |

### Waybar

Config to [waybar](https://github.com/Alexays/Waybar)

#### module

- _Important, change 'set_you_path_here' for you path_

<pre>
   "custom/ia-assistant":{
    "format": " <span>   </span>",
    "on-click": "python ~/set_you_path_here/IA-Assistant/start.py",
    "tooltip": false
  }
</pre>

#### config

In your preference module add `"custom/ia-assistant"`

#### styles.css

<pre>
# custom-ia-assistant{
    /* Add you custom style here */
}
</pre>

<div align="center">

Visit me [Leonardo Henao](https://leonardohenao.com)

</div>

<div align="center">

<a href='https://ko-fi.com/lhenaoll' target='_blank'><img height='35' style='border:0px;height:46px;' src='https://az743702.vo.msecnd.net/cdn/kofi3.png?v=0' border='0' alt='Buy Me a Coffee at ko-fi.com' />

</div>

