# Homework 14 Assignment
# Alex Giang
# 25 April 2023

if __name__ == '__main__':
    link = 'https://collegeofsanmateo.edu/wellnesscenter/'
    from urllib.request import urlopen

    response = urlopen(link)
    html_page = response.read().decode().lower()
    html_page.count('wellness')

    from html.parser import HTMLParser
    import string

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
            d = data.lower()
            for p in string.punctuation:
                if d.count(p) > 0:
                    return
            self.text += str(d) + " "

        # here you will add data to the text variable that you initialized in
        # the constructor. Each time the parser encounters data that is not tag,
        # it will call this method passing the data
        # Add clean data only. Disregard data that has special characters.
        # For that, check if any character in the word is in string.punctuation
        # If it is, return without adding the data to text

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
            count = 0
            with open('file.txt', 'w') as f:
                for c in self.text:
                    if 32 <= ord(c) <= 126:
                        f.write(str(c))
                        count += 1
                        if ord(c) == 32 and count > 80:
                            f.write("\n")
                            count = 0

        # write code to write the text extracted from the page to a file


    parser = MyHTMLParser()
    parser.feed(html_page)
    parser.frequency(3)
    parser.dump_data("file.txt")
