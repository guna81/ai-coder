
def clean_response(response):
    # remove first and last line
    return "\n".join(response.split("\n")[1:-1])

def markdown_to_text(markdown):
    # remove first and last line
    return "\n".join(markdown.split("\n")[1:-1])