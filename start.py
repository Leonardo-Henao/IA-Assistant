import subprocess

import google.generativeai as genai
import pyperclip
from wofi import Wofi

from config import API_KEY_GEMINI

wf = Wofi(height=200)
wofi_resul = wf.text_entry("Whats is you question?")

if not wofi_resul:
    exit()

try:
    subprocess.run(["notify-send", "-a", "Gemini IA", "Loading...", "Gemini is loading a response"])
except:
    pass

new_promt = ""
if ":tre" in wofi_resul:
    new_promt = wofi_resul.replace(":tre", "Traduce al ingles ")
elif ":trs" in wofi_resul:
    new_promt = wofi_resul.replace(":trs", "Traduce al español ")
else:
    new_promt = wofi_resul

genai.configure(api_key=API_KEY_GEMINI)
model = genai.GenerativeModel("gemini-pro")
response = model.generate_content(new_promt)

result_from_response = response.text

selected, index = wf.select(f"Result from {new_promt}", [result_from_response])

if selected == 0:
    pyperclip.copy(result_from_response)
