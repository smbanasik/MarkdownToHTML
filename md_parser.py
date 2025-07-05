from regex_replacer import RegexReplacer

class MDParser:

    def __init__(self):
        self.inc_replacer = RegexReplacer({})
        self.exc_replacer = RegexReplacer({})
        self.symbol_stack = []
    
    # TODO: Open a file and run parse_line until the file ends
    def parse_file(self, file):
        pass

    # TODO: Parse a line, run exclusive then run inclusive.
    def parse_line(self, line):
        pass

    # TODO: Parse exclusive formatting symbols (header, list, etc.)
    # Break after one is found.
    # If we have a list or blockquote, add it to the stack.
    # If we don't find an exclusive, check the stack and add that.
    def parse_exclusive(self, line):
        pass

    # TODO: Parse inclusive formatting symbols (italics, bold)
    def parse_inclusive(self, line):
        pass

    INCLUSIVE_FORMATTING = {
        r"\*\*([^\*\n]+)\*\*": r"<strong>\1</strong>",
        r"__([^_\n]+)__": r"<strong>\1</strong>",
        r"(?<!\*)\*([^\*\n]+)\*": r"<em>\1</em>",
        r"(?<!_)_([^_\n]+)_": r"<em>\1</em>",
    }
    # r"(?<!\!)\[(.+)\]\((.+)\)": r"<a href={\2}>{\1}</a>"
    # r"!\[(.+)\]\((.+)\)": r"<img src={\2} alt={\1}/>"
    
    EXCLUSIVE_FORMATTING = {
        r"(?<!#)# (.+)": r"<h1>\1</h1>",
        r"(?<!#)## (.+)": r"<h2>\1</h2>",
        r"(?<!#)### (.+)": r"<h3>\1</h3>",
        r"(?<!#)#### (.+)": r"<h4>\1</h4>",
        r"(?<!#)##### (.+)": r"<h5>\1</h5>",
        r"(?<!#)###### (.+)": r"<h6>\1</h6>",
        r"- (.+)": "", # Start a list, new line, list item
        r"[0-9]\. (.+)": "", # Start a list, new line, list item
        r"> (.+)": "", # Start a block quote, new line, block quote item (wrapped in <p>)
    }