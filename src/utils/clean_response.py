
def clean_response(response):
    # remove first and last line
    return "\n".join(response.split("\n")[1:-1])