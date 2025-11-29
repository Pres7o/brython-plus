from browser import document

print('Main Brython+ Module Loaded')

def dom(selector):
    class DOMWrapper:
        def text(self, value):
            document[selector].text = value
        def html(self, value):
            document[selector].html = value
    return DOMWrapper()

__call__ = dom

__builtins__.dom = dom

