import subprocess


def show_notification(message: str, title: str = "Gemini IA - @lhenaoll"):
    subprocess.run(["notify-send", "-a", "Gemini IA", title, message, "-t", "2000"])
