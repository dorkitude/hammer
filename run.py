from hammer import *

# Configure these two params and run this script
my_url="http://my.site.domain/page"
num_swings = 10


Hammer(url=my_url, num_swings=num_swings).run()