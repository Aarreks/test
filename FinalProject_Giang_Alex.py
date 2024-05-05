# Final Project CIS 117
# Alex Giang
# 19 May 2023

if __name__ == '__main__':
    '''
    The main method creates the Tkinter window tool Word Frequency Search.
    '''
    import time
    from tkinter import *
    from urllib.request import urlopen
    from html.parser import HTMLParser
    import re
    import sqlite3

    try:
        con = sqlite3.connect('first250.db')
        cur = con.cursor()

        cur.execute("""
            CREATE TABLE IF NOT EXISTS freq_search_giang
            (title text, report text);
            """)
    except:
        pass

    start_time = time.time()


    class MyHTMLParser(HTMLParser):
        '''
        An extended class of HTMLParser with method handle_data overriden and two new methods frequency and dump_data
        '''

        def __init__(self):
            '''
            Initializes a new instance of MyHTMLParser.
            '''
            HTMLParser.__init__(self)
            self.title = "none"
            self.counts = {}

        def handle_data(self, data):
            '''
            Overrides handle_data in the HTMLParser class and counts words in body text, stripped of punctuation other
            than apostrophes, and updates the dictionary self.counts with new terms and increased count values.
            '''
            import re
            data = data.lower()
            n = data.find("*** start of the project gutenberg ebook ") + 41
            if n >= 41 and self.title == "none":
                self.title = re.sub(pattern=r"[*'\r\n;\!\\?\-\",\.\+]", repl='', string=data[n:])
            clean = re.sub(pattern=r"[\'\r\n;\!\\?\-\",\.\+]", repl='', string=data)
            clean = re.sub(pattern=r'[-—]', repl=' ', string=clean)
            words = clean.split(" ")
            for word in words:
                if word in self.counts.keys():
                    self.counts[word] += 1
                else:
                    if len(word) > 3:
                        self.counts[word] = 1

        def get_report(self, n_rows):
            '''
            Returns a table that describes how many times each word appears in the text attribute,
            including n_rows/3 rows each with three ranks, words, and counts. Words with less than ten
            occurrences are omitted. Words shorter than four letters are omitted.
            '''
            self.counts = {key: val for key, val in self.counts.items() if val > 10}
            keys = list(self.counts.keys())
            values = list(self.counts.values())

            def argsort(seq):
                '''
                This helper method takes a sequence and outputs the keys of items in order of ascending value.
                '''
                return sorted(range(len(seq)), key=seq.__getitem__)

            sorted_value_index = argsort(values)
            self.counts = {keys[i]: values[i] for i in reversed(sorted_value_index)}
            ret = 'Results for book with title ' + self.title.upper() + ':\n'
            n = 1
            for key, value in self.counts.items():
                ret += ("{:<16}{:<5}| ".format((str(n) + '. ' + key), value))
                if n >= n_rows:
                    break
                if n % 3 == 0:
                    ret += '\n'
                n += 1
            try:
                command = "INSERT INTO freq_search_giang VALUES ('" + self.title.upper() + "', '" + ret + "');"
                print(command)
                cur.execute(command)
                con.commit()
            except:
                pass
            return ret

    def get_link(query):
        '''
        This method takes a query for a title, searches it on gutenberg.org, and outputs the HTML5
        link of the book that came up as the first result of the search. If the search fails,
        it will use the error book - the Declaration of Independence.
        '''
        query = query.replace(' ', '+')
        q_link = "https://www.gutenberg.org/ebooks/search/?query=" + query + "&submit_search=Go%21"

        class MyHTMLParser2(HTMLParser):
            def __init__(self):
                '''
                Initializes a new instance of MyHTMLParser.
                '''
                HTMLParser.__init__(self)
                self.book_num = '1'

            def handle_starttag(self, tag, attrs):
                # Only parse the 'anchor' tag.
                if tag == "a":
                    # Check the list of defined attributes.
                    for name, value in attrs:
                        # If href is defined, print it.
                        if name == "href":
                            if re.match("/ebooks/[0-9]", value):
                                self.book_num = value[8:]
                        if self.book_num != '1':
                            break

        response2 = urlopen(q_link)
        html_page2 = response2.read()
        html_page2 = html_page2.decode()
        parser2 = MyHTMLParser2()
        parser2.feed(html_page2)
        n = parser2.book_num
        link = "https://www.gutenberg.org/cache/epub/" + n + "/pg" + n + ".html"
        try:
            urlopen(link)
        except:
            try:
                link = "https://www.gutenberg.org/cache/epub/" + n + "/pg" + n + "-images.html"
                urlopen(link)
            except:
                link = 'https://www.gutenberg.org/files/1/1-h/1-h.htm'  # give up
        return link



    def click():
        '''
        Handles downclicks of buttons by processing the URL in txt (entry box)
        opening the URL, parsing the resulting HTML in MyHTMLParser for emails, and counting the
        number of qualifying emails and displaying them in the output text box.
        '''
        output.delete(0.0, END)
        query = txt.get()
        try:
            if -1 < txt2.get().find("http://"):
                txt2.insert(0.0, "http://")
            urlopen(txt2.get())
        except:
            if query.find('.') > -1:
                link = query # accidentally putting a url in the first text box
            else:
                link = get_link(query)
                if len(query) < 1:
                    link = 'https://www.gutenberg.org/files/1/1-h/1-h.htm'  # give up
        else:
            link = txt2.get()
        if -1 < link.find("http://"):
            link = "https://" + link
        try:
            command = "SELECT * FROM freq_search_giang WHERE title LIKE '%" + query.strip().upper() + "%';"
            cur.execute(command)
            if len(cur.fetchone()[1]) > 200:
                output.insert(END, cur.fetchone()[1])
            else:
                raise
        except:
            response = urlopen(link)
            html_page = response.read()
            html_page = html_page.decode()
            parser = MyHTMLParser()
            parser.feed(html_page)
            parser.get_report(50)
            output.insert(END, str(parser.get_report(50)))

    # BELOW IS CODE TO LOAD UP THE LOCAL DATABASE, CHANGE THE LOWER BOUND TO 1 AND RUN IT (LOAD TAKES ABOUT 7 MINUTES)
    # If first250.db is included, you don't have to run this.
    # INCLUDES FIRST 250 PROJECT GUTENBERG BOOKS


    for n in range(250, 250):
        n = str(n)
        try:
            link = "https://www.gutenberg.org/cache/epub/" + n + "/pg" + n + ".html"
            try:
                urlopen(link)
            except:
                try:
                    link = "https://www.gutenberg.org/cache/epub/" + n + "/pg" + n + "-images.html"
                    urlopen(link)
                except:
                    continue
            response = urlopen(link)
            html_page = response.read()
            html_page = html_page.decode()
            parser = MyHTMLParser()
            parser.feed(html_page)
            parser.get_report(50)
        except:
            continue


    # main
    win = Tk()
    win.title("Word Frequency Search on Book")
    win.configure(background='beige')

    # headings
    Label(win, text="Hello! Hi! Welcome!", bg='beige', font='Modern 48 bold italic').grid(row=1, column=1)
    Label(win,
          text="Word Frequency Search on Book by Alex Giang\n\nThis program takes a book title as an input,"
               "\nopens the book, and outputs a table of the 50\nmost frequently used words in that book!"
               "\n\nENTER THE TITLE YOU WOULD LIKE TO SEARCH HERE!", bg='beige', font='Modern 18').grid(row=2, column=1)

    # entry box for title
    txt = Entry(win, width=60, bg="white")
    txt.grid(row=3, column=1)

    Label(win, text=" ", bg='beige').grid(row=4, column=1)

    # GO (submit) button for title
    Button(win, text="GO!", width=6, command=click, bg='tan2').grid(row=5, column=1)

    Label(win, text="\nOR ENTER A PROJECT GUTENBERG LINK HERE!", bg='beige', font='Modern 18').grid(row=7, column=1)

    # second entry box for link
    txt2 = Entry(win, width=60, bg="white")
    txt2.grid(row=8, column=1)

    Label(win, text=" ", bg='beige').grid(row=9, column=1)

    # second GO (submit) button for link
    Button(win, text="GO!", width=6, command=click, bg='tan2').grid(row=10, column=1)

    Label(win, text="\n" + "." * 180 + "\n", bg='beige').grid(row=11, column=1)

    # Output box
    Label(win, text="Results will show up here: (scroll down for more)", bg='beige', font='Modern 18').grid(row=12,
                                                                                                            column=1)

    output = Text(win, width=71, height=6, wrap=WORD, background="tan4", fg="white")
    output.grid(row=12, column=1)
    print(type(output))

    win.mainloop()
