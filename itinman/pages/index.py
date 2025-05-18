import reflex as rx
from reflex.components.radix.themes.layout.stack import hstack

md_red = '#a90533'
md_grey = '#5f6062'

def itinman_logo() -> rx.Component:
    return rx.heading(
        rx.text('{itin', as_='span', color=md_grey),
        rx.text('man', as_='span', color=md_red),
        rx.text('}', as_='span', color=md_grey)
    )

def header() -> rx.Component:
    return rx.hstack(
        itinman_logo()
    )

def side_panel() -> rx.Component:
    return rx.vstack(
        rx.text('side panel'),
        width = '10vw'
    )

def main_panel() -> rx.Component:
    return rx.vstack(
        rx.text('main panel'),
        width = '90vw'
    )

def footer() -> rx.Component:
    return rx.center(
        rx.text('by 0x0012', align='center', weight='light', color=md_grey),
        width = '100%'
    )

def index() -> rx.Component:
    return rx.vstack(
        header(),
        hstack(
            side_panel(),
            main_panel(),
            widht = '100%',
            height = '100%'
        ),
        footer(),
        height = '100vh',
        background = 'white',
        padding = '1.5em'
    )
