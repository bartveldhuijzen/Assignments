
# coding: utf-8

# # Assignment for week 2
# 
# | Name             | Exam number |
# |------------------|:-----------:|
# | Bart Veldhuijzen | 2003139     |

# # This is a section
# ## This is a subsection
# A bullet list looks *like this*
# * Bullet 1
# * Bullet 2
# * __Bullet 3__
# 
# We can link to this [wonderful page](http://janboone.github.io/programming-for-economists/index.html).
# 
# And we can add a picture to the tekst as well.
# ![](http://images2.mtv.com/uri/mgid:file:docroot:mtv.com:/crop-images/2013/11/05/the_who_umg.jpg?enlarge=false&maxdimension=1300&matte=true&matteColor=black&quality=0.85 "The Who!")
# 
# Lets type some math:
# 
# **$$\sin (X) + \cos (x) = 2$$**
# 
# As a rule, I really like this line
# 
# _________________________________
# 
# We are done.

# In[11]:

from plotly.offline import download_plotlyjs, init_notebook_mode, plot, iplot
from plotly.graph_objs import Bar, Scatter, Figure, Layout
init_notebook_mode(connected=True)
from numpy import arange
range_x = arange(-2,2.1,0.1)
iplot([{"x": range_x, "y": [x**2 for x in range_x]}])


# In[ ]:



