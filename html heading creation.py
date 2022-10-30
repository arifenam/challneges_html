#h2 = <!-- wp:heading --><h2>Heading 2</h2><!-- /wp:heading -->
#h3 = <!-- wp:heading {"level":3} --><h3>Heading 2</h3><!-- /wp:heading -->

# HEADING 1
def h1(heading_1_text):
    return f'<!-- wp:heading {{"level":1}} -->{heading_1_text}</h2><!-- /wp:heading -->'

print(h1('this is my heading One sample'))

# HEADING 2

def h2(heading_2_text):
    return f'<!-- wp:heading --><h2>{heading_2_text}</h2><!-- /wp:heading -->'


print(h2('this is my heading two sample'))

# HEADING 3
def h3(heading_3_text):
    return f'<!-- wp:heading {{"level":3}} -->{heading_3_text}</h2><!-- /wp:heading -->'

print(h3('this is my heading three sample'))

# HEADING 4
def h4(heading_4_text):
    return f'<!-- wp:heading {{"level":4}} -->{heading_4_text}</h2><!-- /wp:heading -->'

print(h4('this is my heading Four sample'))
