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
        if tag == 'div' and 'class' in attr and attr['class'] == 'comment-text':
            self.inComment = 1
            comments.append("")
    def handle_data(self, data):
      if len(self.inside) > 0:
        if self.inComment:
            comments[-1] += data.replace("*", "")
    def handle_endtag(self, tag):
        if len(self.inside) > 0:
            if self.inside[-1][0] == 'div' and 'class' in self.inside[-1][1] and self.inside[-1][1]['class'] == 'comment-text':
                self.inComment = 0
            self.inside.pop()



parser = MyHTMLParser()
res = urllib.urlopen("https://www.lada.kz/index.php?do=lastcomments").read().decode("utf-8").replace("--!>", "-->")
parser.feed(res)
for text in comments:
    print text.encode("utf-8"), "\n\n"