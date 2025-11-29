from browser import document
from javascript import import_js

print('Markdown Module Loaded')

import_js("markdown-it.js", alias="markdown_it")
import_js("purify.js", alias="purify_js")

class md:
    def html(raw):
        return purify_js.purify(markdown_it.md.render(raw))
    

__builtins__.md = md








# print('DOM Module Loaded')

# def dom(selector):
#     class DOMWrapper:
#         def text(self, value):
#             document[selector].text = value
#     return DOMWrapper()

# __call__ = dom

# __builtins__.dom = dom
