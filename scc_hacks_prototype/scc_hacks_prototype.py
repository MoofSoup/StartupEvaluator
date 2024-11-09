
import reflex as rx
from .data import companies
from .app import company_card



def homepage() -> rx.Component:
    return rx.box(
        rx.heading("Startup Evaluator", size="xl", mb="4"),
        rx.box(
            *[
                company_card(
                    logo=company["logo"],
                    name=company["name"],
                    solution=company["solution"],
                    tags=company["tags"],
                    open_roles=company["open_roles"]
                )
                for company in companies
            ],
            spacing="4"
        ),
        padding="4"
    )

app = rx.App()
app.add_page(homepage, route="/")
#`app._compile()