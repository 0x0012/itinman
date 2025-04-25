import reflex as rx

def side_panel() -> rx.Component:
    return rx.vstack(
        rx.text('{ itinman }', color='black', size='3'),
        rx.spacer(),
        align='start',
        width='10%',
        padding='0.5em',
        background_color='gray.100',
    )

def main_panel() -> rx.Component:
    pass


def index() -> rx.Component:
    return rx.hstack(
        side_panel(),
        main_panel(),
        width='100%',
        height='100%',
        padding='0.5em',
        spacing='0.5em',
        background_color='white',
    )
