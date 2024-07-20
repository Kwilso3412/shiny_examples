
from shiny import reactive, render, req
from shiny.express import input, render, ui
from shinyswatch import theme
import sys

# load data

# Page Identifiers 
ui.page_opts(title="Dashboard",
                fillable=True,
                id="page",
                bg = "79bde9",
                )

# https://bootswatch.com/cyborg/
theme.cyborg()


with ui.sidebar(id="sidebar_left"):
    ui.tags.link(rel="stylesheet", href="https://cdn.jsdelivr.net/npm/tailwindcss@2.2.19/dist/tailwind.min.css")
    with ui.panel_conditional("input.page == 'Example 1'"):
        ui.input_radio_buttons("ex1_radio", "Select Category", {"1":'Button 1', "2":"Button 2"})
    
    with ui.panel_conditional("input.page == 'Example 2'"):
        ui.input_radio_buttons("ex2_radio", "Select Category", {"1":'Button 1', "2":"Button 2"})



def nav_content(title, body_id):
    with ui.div(class_="container mx-auto p-4", id = body_id):
        sys.displayhook(ui.h1(title, class_="text-3xl font-bold text-yellow-400 mb-4"))

time_title = "Example 1"
time_id =  "ex1
with ui.nav_panel("Example 1" ):
    # Body
    nav_content(time_title, time_id)
    


nlp_title = "Example 2"
nlp_id  =  "ex2"
with ui.nav_panel("Example 2"):
    nav_content(nlp_title, nlp_id)
    # Side bar

ui.nav_spacer()

