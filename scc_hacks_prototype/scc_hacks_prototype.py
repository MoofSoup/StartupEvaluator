# main.py
import reflex as rx
from .data import companies
from .app import company_card
from dotenv import load_dotenv
from .getcompanies import get_companies_dict
from .tabs_page import tabs_function

# Add a State class for handling the redirect
class RedirectState(rx.State):
    def on_load(self):
        return rx.redirect("/tabs")

def homepage() -> rx.Component:
    success, companies_data, error = get_companies_dict()
    
    if not success:
        return rx.box(
            rx.heading("Error loading companies", size="xl", color="red"),
            rx.text(error),
            padding='4'
        )
    
    return rx.box(
        rx.heading("Startup Evaluator", size="xl", mb=4),
        rx.vstack(
            *[
                company_card(
                    logo_url=company["logo_url"],
                    name=company["name"],
                    pitch=company["pitch"],
                )
                for company in companies_data.values()
            ],
            spacing='4'
        ),
        padding='4'
    )

# Redirect page component
@rx.page(route="/company/kaedim")
def kaedim_redirect():
    return rx.box(
        on_mount=RedirectState.on_load
    )

app = rx.App()
app.add_page(homepage, route="/")
app.add_page(tabs_function, route="/tabs")