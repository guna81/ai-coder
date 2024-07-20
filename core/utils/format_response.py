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

def remove_codeblock_markers(text):
  """
  Removes generic codeblock markers (backticks or curly braces) from text.

  Args:
      text: The text containing codeblocks.

  Returns:
      The text with codeblock markers removed.
  """

  cleaned_text = text.splitlines()[1:-1]
  cleaned_text = "\n".join(cleaned_text)
  
  # Pattern to match codeblock markers (either 3 backticks or 2 curly braces)
  pattern = r"(?:```|{{(.|\n)*?}})"
  text = re.sub(pattern, "", cleaned_text, flags=re.DOTALL)

  return text