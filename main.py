import os
LINE = "Put the phone down when your grandmother starts the story about the war.\nI only heard the ending once, and now there is nobody left who remembers how it began."
os.makedirs("/output", exist_ok=True)
with open("/output/entry.txt", "w", encoding="utf-8") as f:
    f.write(LINE)
