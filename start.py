import subprocess

import google.generativeai as genai
from wofi import Wofi

from config import API_KEY_GEMINI
from helpers import show_notification
from helpers.control_history import get_all_data, remove_all, write_in_backup
from show_windows import show_response

_title_notification = "Gemini IA - @lhenaoll"
wf = Wofi(height=200)
wofi_resul = wf.text_entry("Whats is you question?")

if not wofi_resul:
    exit()

try:
    show_notification("Gemini is loading a response...")
except:
    pass

new_promt = ""
if ":tre" in wofi_resul:
    new_promt = wofi_resul.replace(":tre", "Traduce al ingles ")
elif ":trs" in wofi_resul:
    new_promt = wofi_resul.replace(":trs", "Traduce al español ")
elif ":hsc" in wofi_resul:
    remove_all()
    subprocess.run(["notify-send", "-a", "Gemini IA", _title_notification, "Historial borrado", "-t", "2000"])
    exit()
elif ":hs" in wofi_resul:
    result = get_all_data()

    if len(result) == 0:
        subprocess.run(
            ["notify-send", "-a", "Gemini IA", _title_notification, "No hay contenido en el historial", "-t", "2000"]
        )
    else:
        to_show = ""
        for r in result:
            t = f"{r[0]}: {r[1]}\n{r[2]}\n\n"
            to_show += t

        show_response(to_show)
    exit()
else:
    new_promt = wofi_resul

genai.configure(api_key=API_KEY_GEMINI)
model = genai.GenerativeModel("gemini-pro")
response = model.generate_content(new_promt)

result_from_response = response.text
write_in_backup(text=result_from_response, question=new_promt)
show_response(result_from_response)
