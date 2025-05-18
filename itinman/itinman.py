import reflex as rx
from .pages.index import index

app = rx.App()

app.add_page(
    index,
    title="itinman",
    description="IT Inventory Manager.",
)
