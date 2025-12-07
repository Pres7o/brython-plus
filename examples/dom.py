# Set DOM element text-test text to "Hello, World!"
dom("test-text").text("Hello, World!")

# Set DOM element test-html to some "Hello, World!" html
dom("test-html").html("<h3>Hello, World! This is HTML!<h3>")

dom('test-purify').html(purify('<p>Hello, World! This text is pure!</p>'))
element_text = dom('test-text').text()
print(element_text)
