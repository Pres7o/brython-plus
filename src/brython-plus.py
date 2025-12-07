from browser import document
from javascript import import_js

import_js("/dist/purify.js", alias="purify_js")


print("Main Brython+ Module Loaded")


def dom(selector):
    class DOMWrapper:
        def text(self, *value):
            if value == ():
                return document[selector].text
            else:
                document[selector].text = value[0]

        def html(self, *value):
            if value == ():
                return document[selector].html
            else:
                document[selector].html = value[0]

        def delete(self):
            del document[selector]

    return DOMWrapper()



def purify(raw):
    return purify_js.purify(raw)


__builtins__.dom = dom
__builtins__.purify = purify
