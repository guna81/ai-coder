import re
from mistletoe import markdown

def clean_response(response):
    # remove first and last line
    return "\n".join(response.split("\n")[1:-1])

def markdown_to_text(text):

  # Parse the markdown
  html = markdown(text)
  plain_text = re.sub(r'<[^>]*>', '', html)
  return plain_text
