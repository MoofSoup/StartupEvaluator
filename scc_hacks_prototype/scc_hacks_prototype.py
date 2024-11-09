
import reflex as rx

def homepage() -> rx.Component:
    return rx.box(
        rx.heading("startup evaluator", size="xl", mb=4),
        padding=4,
    )

app = rx.App()
app.add_page(homepage, route="/")
#`app._compile()