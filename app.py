import requests

class mystr:
    def __init__(self, txt):
        self.txt=txt

    def toUpperCase(self):
        return self.txt.upper()

    def toLowerCase(self):
        return 'self.txt.lower()'


if __name__ == '__main__':
    st1=mystr('my friend!')
    print("Hi ",st1.toUpperCase())