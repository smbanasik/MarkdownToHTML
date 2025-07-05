import re

class RegexReplacer:
    """ Replace arbitrary regex expressions with other 
    regex expressions."""
    def __init__(self, symbols, **kwargs):
        self.regex_map = symbols

    def replace_line(self, line):

        new_line = line
        for key, value in self.regex_map.items():
            new_line = re.sub(key, value, new_line)
        
        return new_line

test_string = "This *text* is _really_ **cool** and __very__ ***neat*** and ___formatted___ wildly!"

replacer = RegexReplacer({r"(?<!#)# (.+)": r"<h1>\1</h1>",
    r"(?<!#)## (.+)": r"<h2>\1</h2>",
    r"(?<!#)### (.+)": r"<h3>\1</h3>",
    r"(?<!#)#### (.+)": r"<h4>\1</h4>",
    r"(?<!#)##### (.+)": r"<h5>\1</h5>",
    r"(?<!#)###### (.+)": r"<h6>\1</h6>",
    r"\*\*([^\*\n]+)\*\*": r"<strong>\1</strong>",
    r"__([^_\n]+)__": r"<strong>\1</strong>",
    r"(?<!\*)\*([^\*\n]+)\*": r"<em>\1</em>",
    r"(?<!_)_([^_\n]+)_": r"<em>\1</em>",
})

new_string = replacer.replace_line(test_string)

print("Old: " + test_string)
print("New: " + new_string)