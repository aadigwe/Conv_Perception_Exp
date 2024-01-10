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
        <a href="https://aadigwe.github.io/Conv_Perception_Exp/">Go back</a><br /> '

def reformat_ctrl(values):
    partitioned_values = []
    for index, item in enumerate(values):
        partitioned_values.append(str(index+1)+ '.\t' +  ' '.join(item.split('_')))

    return '<br >'.join(partitioned_values)

def generate_html_page(sent_dict):
    control_values = []
    outputfile = 'lj_htmls/' + sent_dict["name"]
    with open(outputfile, "w") as file:
        file.write("<html>\n")
        file.write(head_html)
        file.write("<body>\n")
        file.write(sent_dict["transcript"] + '<br />')
        file.write("Model: BVAE TTS" + '<br />')
        file.write('<button onclick="toggleParagraph()">Show Control Values</button>')
        file.write("<ol>\n")
        directory = sent_dict["audiodir"]
        for audio_file in os.listdir(sent_dict["audiodir"]):
            file.write(f'\t<li><audio controls><source src="../{directory}/{audio_file}" type="audio/mpeg"></audio></li>\n')
            sent_ctrl = audio_file.split('_')[1:]
            control_values.append(audio_file)
            #file.write(f'\t<li id="myParagraph" style="display: none; >{sent_ctrl}</li>\n')
        file.write("</ol>\n")
        ctrl_values = reformat_ctrl(control_values)
        print(ctrl_values)
        file.write(f'\t<p id="myParagraph" style="display: none;">Control Values <br />{ctrl_values}</p>')
        file.write("</body>\n")
        file.write("</html>\n")


data = [
    {"name": "sent01.html", "transcript":"They estimated that most of the material received by his office originated in this fashion",  "audiodir": "./lj2/sent01/"},
    {"name": "sent02.html", "transcript":"Our modern practice has prudently tried to steer between the two extremes, accepting as the best system, a combination of both ",  "audiodir": "./lj2/sent02/"},
    {"name": "sent03.html", "transcript":"They reluctantly agreed to open the gallery which had formerly been occupied by strangers on these occasions",  "audiodir": "./lj2/sent03/"},
    {"name": "sent04.html", "transcript":"A new member shall be appointed by the president in office",  "audiodir": "./lj2/sent04/"},
    {"name": "sent05.html", "transcript":"After a period of six months I was doing it myself",  "audiodir": "./lj2/sent05/"},
    {"name": "sent06.html", "transcript":"That was an extra job on the side",  "audiodir": "./lj2/sent06/"},
    {"name": "sent07.html", "transcript":"And then the pleasure is already more or less gone",  "audiodir": "./lj2/sent07/"},
    {"name": "sent08.html", "transcript":"That was the most extreme version of a witch hunt throughout history",  "audiodir": "./lj2/sent08/"},
    {"name": "sent09.html", "transcript":"The line between good and evil cuts through every human being",  "audiodir": "./lj2/sent09/"},
    {"name": "sent10.html", "transcript":"We were traveling around the city and the bus was really full",  "audiodir": "./lj2/sent10/"},
    {"name": "sent11.html", "transcript":"Once you master your thought no one can help you as much",  "audiodir": "./lj2/sent11/"},
    {"name": "sent12.html", "transcript":"The preparation is actually very simple",  "audiodir": "./lj2/sent12/"},
    {"name": "sent13.html", "transcript":"It happened also in the chinese culture revolution in nineteen sixty six",  "audiodir": "./lj2/sent13/"},
    {"name": "sent14.html", "transcript":"When I come home my dog greets me at the door",  "audiodir": "./lj2/sent14/"},
    {"name": "sent15.html", "transcript":"You will get a confirmation to your phone soon.",  "audiodir": "./lj2/sent15/"}
]

for sent_dict in data:
    generate_html_page(sent_dict)