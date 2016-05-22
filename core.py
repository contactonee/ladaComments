import urllib
from HTMLParser import HTMLParser


class MyHTMLParser(HTMLParser):
    inside = []
    def handle_starttag(self, tag, attrs):
        attr = {}
        for val in attrs:
            attr[val[0]] = val[1]
        if len(attrs) > 0 or tag == 'b':
            self.inside.append((tag, attr))
    def handle_data(self, data):
      if len(self.inside) > 0:
        if 'id' in self.inside[-1][1] and self.inside[-1][1]['id'][0:7] == 'comm-id':
            print data.replace("*", "")
    def handle_endtag(self, tag):
        if len(self.inside) > 0:
            if 'id' in self.inside[-1][1] and self.inside[-1][1]['id'][0:7] == 'comm-id':
                print "------------------------------------"
            self.inside.pop()



parser = MyHTMLParser()
res = urllib.urlopen("https://www.lada.kz/index.php?do=lastcomments").read().decode("utf-8").replace("--!>", "-->")
parser.feed(res)
