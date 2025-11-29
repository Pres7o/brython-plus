# Test code to test the various features of brython+

# set DOM element text-test text to Hello, World!
dom('test-text').text('Hello, World!')


dom('test-md').html(md.html('''# Hello, World!

Lorem ipsum dolor sit amet...
'''))
