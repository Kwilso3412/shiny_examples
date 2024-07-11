from shiny import reactive
from shiny.express import input, render, ui
from shinyswatch import theme
import sys
# to run this code you will need to rename the file to app.py

# Overall theme 
# Important for understanding how Shiny works
# https://shiny.posit.co/py/docs/express-in-depth.html

# https://bootswatch.com/cyborg/
theme.cyborg()

# Page Identifiers 
ui.page_opts(title="Dashboard",
                fillable=True,
                id="page",
                bg = "79bde9",
                )

# Side bar
with ui.sidebar(id="sidebar_left"):
    ui.tags.link(rel="stylesheet", href="https://cdn.jsdelivr.net/npm/tailwindcss@2.2.19/dist/tailwind.min.css")
    ui.h1("Menu", class_="font-bold text-blue-400")

def nav_content(title, body, body_id):
    with ui.div(class_="container mx-auto p-4", id = body_id):
        sys.displayhook(ui.h1(title, class_="text-3xl font-bold text-yellow-400 mb-4"))
        sys.displayhook(ui.p(body, class_="text-white mb-4"))



example_1_title = "Example 1"
example_1__body = "Example text"
example_id =  "example_1"
with ui.nav_panel("Example 1"):
    # Body
    nav_content(example_1_title,example_1__body, example_id)

example_2_title = "Example 2"
example_2__body = "Example text"
example_id  =  "example_2"
with ui.nav_panel("Example 2"):
    nav_content(example_2_title, example_2__body, example_id)


ui.nav_spacer()

# load data
