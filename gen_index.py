import os 

head_html = ' \
<head> \
    <title>Synthesis</title> \
    <script> \
        function toggleParagraph() { \
            var x = document.getElementById("myParagraph"); \
            if (x.style.display === "none") { \
                x.style.display = "block"; \
            } else { \
                x.style.display = "none"; \
            } \
        } </script> </head> \
        <a href="https://www.w3schools.com">Go back</a><br /> '


data = [
    {"name": "sent01.html", "transcript":"They estimated that most of the material received by his office originated in this fashion",  "audiodir": "./ryan2/sent01/"},
    {"name": "sent02.html", "transcript":"Our modern practice has prudently tried to steer between the two extremes, accepting as the best system, a combination of both ",  "audiodir": "./ryan2/sent02/"},
    {"name": "sent03.html", "transcript":"They reluctantly agreed to open the gallery which had formerly been occupied by strangers on these occasions",  "audiodir": "./ryan2/sent03/"},
    {"name": "sent04.html", "transcript":"A new member shall be appointed by the president in office",  "audiodir": "./ryan2/sent04/"},
    {"name": "sent05.html", "transcript":"After a period of six months I was doing it myself",  "audiodir": "./ryan2/sent05/"},
    {"name": "sent06.html", "transcript":"That was an extra job on the side",  "audiodir": "./ryan2/sent06/"},
    {"name": "sent07.html", "transcript":"And then the pleasure is already more or less gone",  "audiodir": "./ryan2/sent07/"},
    {"name": "sent08.html", "transcript":"That was the most extreme version of a witch hunt throughout history",  "audiodir": "./ryan2/sent08/"},
    {"name": "sent09.html", "transcript":"The line between good and evil cuts through every human being",  "audiodir": "./ryan2/sent09/"},
    {"name": "sent10.html", "transcript":"We were traveling around the city and the bus was really full",  "audiodir": "./ryan2/sent10/"},
    {"name": "sent11.html", "transcript":"Once you master your thought no one can help you as much",  "audiodir": "./ryan2/sent11/"},
    {"name": "sent12.html", "transcript":"The preparation is actually very simple",  "audiodir": "./ryan2/sent12/"},
    {"name": "sent13.html", "transcript":"It happened also in the chinese culture revolution in nineteen sixty six",  "audiodir": "./ryan2/sent13/"},
    {"name": "sent14.html", "transcript":"When I come home my dog greets me at the door",  "audiodir": "./ryan2/sent14/"},
    {"name": "sent15.html", "transcript":"You will get a confirmation to your phone soon.",  "audiodir": "./ryan2/sent15/"}
]


with open('index2.html', "w") as file:
    file.write("<html>\n")
    file.write(head_html)
    file.write("<body>\n")
    file.write("<h2>LJ</h2>\n")
    file.write("<ol>\n")
    for sent_dict in data:
        hurl = "https://aadigwe.github.io/Conv_Perception_Exp/" + 'lj_htmls/'+ sent_dict["name"]
        file.write(f'\t<li><a href={hurl}>{sent_dict["name"]}</a><br /></li>\n')
    file.write("</ol>\n")

    file.write("<h2>Ryan</h2>\n")
    file.write("<ol>\n")
    for sent_dict in data:
        hurl = "https://aadigwe.github.io/Conv_Perception_Exp/" + 'ryan_htmls/'+ sent_dict["name"]
        file.write(f'\t<li><a href={hurl}>{sent_dict["name"]}</a><br /></li>\n')
    file.write("</ol>\n")

    file.write("</body>\n")
    file.write("</html>\n")