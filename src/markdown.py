from browser import document
from javascript import import_js

print('Markdown Module Loaded')

import_js("/dist/markdown-it.js", alias="markdown_it")
import_js("/dist/purify.js", alias="purify_js")

class md:
    def html(raw):
        return purify_js.purify(markdown_it.md.render(raw))
    
__builtins__.md = md
