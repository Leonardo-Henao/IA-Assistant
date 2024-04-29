# IA Assistant

Assistant with Gemini IA (Google)

<div align="center">

![Image](./src/images/screenshot-1.png)

</div>

## Requirements

### All

- Python 3.* [(Python.org)](https://www.python.org/)
- TkInter [(Wiki Python)](https://wiki.python.org/moin/TkInter)
- Api key to Gemini IA [(Google AI Studio)](https://aistudio.google.com/app/apikey)

### Linux

- xclip [(Github)](https://github.com/astrand/xclip) or wl-clipboard [(Github)](https://github.com/bugaevc/wl-clipboard)

## Install

- Config `GOOGLE_API_KEY` in you environments
- Clone this repo
- `cd ./IA-Assistant` and execute `start.py` script

*If you OS require, set permissions to execute to `start.py` script*

## Extras

### Copy result

When show the result, press `[c]` to copy it or press `[ESCAPE]` to close window.

### Commands

Start prompt with:

| Command | Action |
|---|---|
| `:trs` | Translate text to Spanish |
| `:tre` | Translate text to English |
| `:hs` | View history |
| `:hsc` | Clear history|

### Waybar

#### module

- *Important, change 'set_you_path_here' for you path*

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
#custom-ia-assistant{
    /* Add you custom style here */
}
</pre>

<div align=center>

Visit me [Leonardo Henao]([https://leonardohenao.com])

</div>