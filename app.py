
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
    with ui.panel_conditional("input.page == 'Time Series'"):
        ui.input_radio_buttons("time_radio", "Select Category", {"1":'Number of Complaints', "2":"Review Ratings"})
    
    with ui.panel_conditional("input.page == 'Natural Language Processor'"):
        ui.input_radio_buttons("nlp_radio", "Select Category", {"1":"Key word Word Cloud","2": "Review Sentiment Analysis"})



def nav_content(title, body_id):
    with ui.div(class_="container mx-auto p-4", id = body_id):
        sys.displayhook(ui.h1(title, class_="text-3xl font-bold text-yellow-400 mb-4"))

time_title = "Time Series"
time_id =  "time"
with ui.nav_panel("Time Series", ):
    # Body
    nav_content(time_title, time_id)
    


nlp_title = "Natural Language Processing"
nlp_id  =  "nlp"
with ui.nav_panel("Natural Language Processor"):
    nav_content(nlp_title, nlp_id)
    # Side bar

ui.nav_spacer()

