import urllib
from HTMLParser import HTMLParser

comments = []

class MyHTMLParser(HTMLParser):
    inside = []
    inComment = 0
    def handle_starttag(self, tag, attrs):
        attr = {}
        for val in attrs:
            attr[val[0]] = val[1]
        self.inside.append((tag, attr))
        if 'class' in attr and attr['class'] == 'comment-item':
            comments.append({'text': '', 'author': '', 'title': '', 'date': '', 'id': ''})
        if tag == 'div' and 'class' in attr and attr['class'] == 'comment-text':
            self.inComment = 1
            

    def handle_data(self, data):
        if self.inComment:
            comments[-1]['text'] += data.replace("*", "")
            if 'id' in self.inside[-1][1] and self.inside[-1][1]['id'][0:7] == 'comm-id':
                comments[-1]['id'] = self.inside[-1][1]['id'][8:]
        if len(self.inside) >= 2:
            if 'class' in self.inside[-2][1] and self.inside[-2][1]['class'] == 'comment-user' and self.inside[-1][0] == 'a':
                comments[-1]['author'] = data
            if self.inside[-2][0] == 'h3' and self.inside[-1][0] == 'a':
                comments[-1]['title'] = data
            if 'class' in self.inside[-1][1] and self.inside[-1][1]['class'] == 'comment-date':
                comments[-1]['date'] = data
    def handle_endtag(self, tag):
        if len(self.inside) > 0:
            if self.inside[-1][0] == 'div' and 'class' in self.inside[-1][1] and self.inside[-1][1]['class'] == 'comment-text':
                self.inComment = 0
            self.inside.pop()



parser = MyHTMLParser()
res = urllib.urlopen("https://www.lada.kz/index.php?do=lastcomments").read().decode("utf-8").replace("--!>", "-->")
parser.feed(res)
