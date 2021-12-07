library(shiny)

shinyUI(fluidPage(
  
  titlePanel('Tarea Shiny'),
  fluidRow(
    plotOutput('plot_filter',
               click = 'clk_filter',
               dblclick = 'dclk_filter',
               hover = hoverOpts('hover_filter'),
               brush = 'brush_filter')
  ),
  fluidRow(dataTableOutput('mtcars_tbl'))
  
))