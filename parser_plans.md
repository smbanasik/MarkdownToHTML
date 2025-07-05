# MD to React Parser
Simple concept:
Produce a react function that displays a markdown document with it's formatting.

## Initial Ideas

### Parsing MD
- Formatting always ends with a new line.
- Need a stack based system, stack ends at a newline
- Going to start off with a limited set of markdown (see test prompt)
- We're going to ignore line breaks for now (react should take care of the spacing)
- We should consider backspaces. The backspace is removed and whatever character afterwards is taken literally

### Implementing the Parser
- Parser will run line by line and then word by word within the line.
- Words get regex searched for formatting
  - Break regex into front and back searches.
- Front regex pushes stack, back regex pops stack.
- Linebreak pops whole stack.

## Current Process
I've made a regex replacer for the single line formatting. This implementation is fine for now.  

Next I'll need to consider how to do multiline additions, which will require actual parsing and a stack based system  
since react has some wrappers around individual elements (lists, blockquotes, etc.).  

I'll want to break down the type of markdown formatting into exclusive and inclusive. Exclusive would be items such  
as headers, lists, and block quotes. We can parse one and quit out from there, moving onto inclusive formatting.  
Inclusive formatting would be items such as italics, which could be found anywhere.  
Since the only multi-line formatting is exclusive, it won't be too difficult to determine when a list or block quote  
ends. Then we can add the necessary formatting afterwards.  

# **Test prompt:**

# H1
Normal text
## H2
This *text* is _really_ **cool** and __very__ ***neat*** and ___formatted___ wildly!
### H3
> Blockquote parser
> Blockquote parser test
#### H4
- List
- List
  - List
##### H5
1. List
2. List
3. List
###### H6
Backslash \*check\*
[Link](https://www.google.com)
![Image Text](./asset.png)