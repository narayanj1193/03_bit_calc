# Functions go at the start

# Put series of symbols at start and end of text (for emphasis of text)
def statement_generator(text, decoration)

    # Make string with five characters
    ends = decoration * 5

    # add decoration at start and end of statement
    statement = "{}  {}  {}".format(ends, text, ends)

    print()
    print(statement)
    print()

    return ""

# Main Routine Goes Here
statement_generator("hello world", "-")
