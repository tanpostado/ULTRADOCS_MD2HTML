# AUTHOR: TanPostado (Shed) sometime in 2025 idr

# imports, only one wow
import sys

# constants to mask the very lazy attempt at avoiding magic values
TAGS = ('HEADER', 'WRITEUP', 'VIDEO', 'ALERT')
ALERTS = {
    'IMPORTANT':'<i class=\"fa-solid fa-bell\"></i> Important </div> ',
    'WARNING':'<i class=\"fa-solid fa-triangle-exclamation\"></i> Warning </div> ',
    'CAUTION':'<i class=\"fa-solid fa-skull\"></i> Caution </div> ',
    'TIPS':'<i class=\"fa-solid fa-lightbulb\"></i> Tips </div> ',
    'NOTE':'<i class=\"fa-solid fa-circle-exclamation\"></i> Note </div> '
}
DIFFS = ('\t<div class=\"tips\"> <div class=\"tips-header\"> ',
    '\t<div class=\"warning\"> <div class=\"warning-header\"> ',
    '\t<div class=\"caution\"> <div class=\"caution-header\"> '
)
TESTHEAD = "<!DOCTYPE html>\n<html>\n\t<head>\n\t\t<meta charset=\"utf-8\">\n\t\t<meta name=\"viewport\" content=\"width=device-width, initial-scale=1\">\n\t\t<title>Test View</title>\n\t\t<link rel=\"stylesheet\" href=\"test.css\">\n\t</head>\n\t<body>\n\t\t<!-- COPY FROM HERE -->\n"
TESTTAIL = "\t\t</details>\n\t\t<!-- COPY TO HERE -->\n\t</body>\n</html>"
DETAILHARD = "\t\t<details class=\"hard\">\n"
DETAILMEDI = "\t\t<details class=\"medium\">\n"
DETAILEASY = "\t\t<details class=\"easy\">\n"
SUMMARYHEAD = '\t\t\t<summary> <b>'
SUMMARYBODY = '</b> // <b>DIFFICULTY:</b> '
SUMMARYTAIL = " </summary>\n"
WRITEHEAD = '\t\t\t<p> '
WRITETAIL = ' </p>\n'
VIDEOHEAD = '\t\t\t<video width=\"500\" height=\"auto\" loop controls muted> <source src=\"'
VIDEOTAIL = '\" type=\"video/mp4\"> </video>\n'
ALERTHEAD = '\t\t'
ALERTTAIL = ' </div> <br />\n'

# this does something i genuinely dont remember what though
fishy = 0
def stupid():
    global fishy
    fishy = fishy + 1

# generates the header of each strat
def header(f): 
    try:
        output = ""
        if f.readline().upper().strip('\n') == TAGS[0]:
            name = f.readline().strip('\n ')
            diff = f.readline().strip('\n ')
            diffNum = int(float(diff))
            if (7 >= diffNum and diffNum <= 10):
                output = DETAILHARD
                stupid()
                stupid()
            elif (4 >= diffNum and diffNum <= 6):
                output = DETAILMEDI
                stupid()
            elif (0 >= diffNum and diffNum <= 3):
                output = DETAILEASY
            output = output + SUMMARYHEAD + name + SUMMARYBODY + diff + SUMMARYTAIL
            f.readline()
        return output
    except:
        sys.exit()

# this puts the fries in the bag
def writeup(f):
    try:
        output = ''
        if f.readline().upper().strip('\n') == TAGS[1]:
            for line in f:
                if line == '\n':
                    break
                else:
                    output = output + WRITEHEAD + line.strip('\n') + WRITETAIL
        return output
    except:
        sys.exit()

# nests videos into their proper tags
def video(f):
    try:
        output = ''
        if f.readline().upper().strip('\n') == TAGS[2]:
            for line in f:
                if line == '\n':
                    break
                else: 
                   output = output + VIDEOHEAD + line.strip('\n') + VIDEOTAIL
        return output
    except:
        sys.exit()

# nests the text into the proper alert format
def alert(f):
    try:
        if f.readline().upper().strip('\n') == TAGS[3]:
            output = ''
            for style, line in zip(f, f):
                if style == '\n' or line == '\n':
                    break
                style = style.strip('\n ').upper()
                line = line.strip('\n')
                output = output + ALERTHEAD + DIFFS[fishy] + ALERTS[style] + line + ALERTTAIL
            return output
    except:
        sys.exit()


fi = open('in.txt', 'r')
fo = open('out.html', 'w')

# writes into the file
theThing = TESTHEAD + header(fi) + writeup(fi) + video(fi) + alert(fi) + TESTTAIL
fo.write(theThing)

fi.close()
fo.close()
