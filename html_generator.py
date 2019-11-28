"""Teil einer HTML-Seite mit Python ertellen!"""

#Dictionary anlegen:
authors = ["Darwin", "Lovelace", "Hawkin", "Noether"]

#Output öffnen (Code in eine neue Datei schreiben):
output_fh = open("list.html", "w")

#Erster Teil der HTML-Seite:
scaffold_start = """<!DOCTYPE html>
<html>
<head>
<title>Titel dieser wunderbaren Seite</title>
</head>
<body>
<h1>Eine fantastische Überschrift</h1>
<p>Ein toller Abschnitt.
<ul>
"""
output_fh.write(scaffold_start)

#Zweiter (dynamischer) Teil der HTML-Seite:
scaffold_middle = ""
for author in authors:
    scaffold_middle = scaffold_middle + "<li>" + author + "</li>"
print(scaffold_middle)
output_fh.write(scaffold_middle)

#Dritter Teil der HTML-Seite:
scaffold_end = """
</ul>
</p>
</body>
</html>
"""
output_fh.write(scaffold_end)

#Output schließen:
output_fh.close()
