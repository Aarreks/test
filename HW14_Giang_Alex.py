# Homework 14 Assignment
# Alex Giang
# 2 May 2023

from tkinter import *

from urllib.request import urlopen

from html.parser import HTMLParser
import re


class MyHTMLParser(HTMLParser):
    '''
        An extended class of HTMLParser with method handle_data overriden and two new methods frequency and dump_data
        '''

    def __init__(self):
        '''
            Initializes a new instance of MyHTMLParser.
            '''
        HTMLParser.__init__(self)
        self.text = ""

    def handle_data(self, data):
        '''
            Overrides handle_data in the HTMLParser class and adds body text without special characters to the text attribute
            '''
        if not (data.count('@') and data.count('.')):
            return
        clean = ''
        for c in data:
            if 32 <= ord(c) <= 126:
                clean = clean + c
        pieces = clean.split(' ')  # check each text piece between spaces
        for piece in pieces:
            m = re.match(r"(\w+)@(\w+)\.(\w+)", piece)
            print(piece)
            if m is None:
                continue
            for p in '!"#$%&\')(*+,/:;<=>?[\\^`{|}~':
                if m.group(0).count(p):
                    continue  # special characters other than hyphen, period, or underscore not allowed in address
            self.text += m.group(0) + "\n"

    def frequency(self, n):
        '''
            Returns a table that describes how many times each word appears in the text attribute,
            including rows with more than n occurrences.
            '''
        print('Below are the words that occur at least', n, 'times:\n')
        words = self.text.split(" ")
        counts = {}
        for word in words:
            if word in counts.keys():
                counts[word] += 1
            else:
                counts[word] = 1
        print("{:<20}{}".format("Word", "Frequency"))
        for key, value in counts.items():
            if value >= n and key.isalnum():
                print("{:<20}{}".format(key, value))

    # this method should print the words that occur at least n times on the page

    def dump_data(self, filename):
        '''
            Copies clean text data, including only characters between ASCII 32 and 126 inclusive,
            into the specified file, skipping lines at the end of words every 80 characters.
            '''
        with open('file.txt', 'w') as f:
            for c in self.text:
                f.write(str(c))


def click():
    '''
    Handles downclicks of buttons by processing the URL in txt (entry box)
    opening the URL, parsing the resulting HTML in MyHTMLParser for emails, and counting the
    number of qualifying emails and displaying them in the output text box.
    '''
    output.delete(0.0, END)
    lnk = txt.get()
    if lnk.find("www.") == -1:
        lnk = "www." + lnk
    if lnk.find("https://") + lnk.find("http://") == -2:
        lnk = "https://" + lnk
    print(lnk)
    resp = urlopen(lnk)
    pg = resp.read().decode().lower()
    parser = MyHTMLParser()
    parser.feed(pg)
    output.insert(END, str(parser.text.count('\n')) + " emails found.\n")
    output.insert(END, parser.text)


# main
win = Tk()
win.title("Email Address on Webpage Search")
win.configure(background='beige')

# headings
Label(win, text="Hello! Hi! Welcome!", bg='beige', font='Modern 48 bold italic').grid(row=1, column=1)
Label(win, text="Web Email Address Search by Alex Giang\n\nThis program takes a URL as an input, opens the webpage, "
                "\nand outputs any email addresses that it finds."
                "\n\nENTER THE URL YOU WOULD LIKE TO SEARCH HERE!", bg='beige', font='Modern 18').grid(row=2, column=1)

# entry box
txt = Entry(win, width=60, bg="white")
txt.grid(row=3, column=1)

Label(win, text=" ", bg='beige').grid(row=4, column=1)

# GO (submit) button
Button(win, text="GO!", width=6, command=click, bg='tan2').grid(row=5, column=1)

Label(win, text="\n" + "." * 180 + "\n", bg='beige').grid(row=6, column=1)

# Output box
Label(win, text="Results will show up here: (scroll down for more)", bg='beige', font='Modern 18').grid(row=7, column=1)

output = Text(win, width=75, height=6, wrap=WORD, background="tan4", fg="white")
output.grid(row=8, column=1)
print(type(output))

win.mainloop()
