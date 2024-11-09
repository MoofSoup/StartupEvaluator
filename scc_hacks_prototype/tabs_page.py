import reflex as rx
from .data import Company  # Import the dictionary from data.py

# Define the app state for managing tabs
class TabState(rx.State):
    """State for managing the active tab."""
    active_tab: str = "Profile"  # Default tab

    def set_tab(self, tab_name: str):
        """Set the active tab."""
        self.active_tab = tab_name

@rx.page(route="/tabs")
def tabs_function() -> rx.Component:
    def display_tab_content():
        """Display content based on the active tab."""
        return rx.cond(
            TabState.active_tab == "Profile",
            rx.box(
                rx.heading("Company Profile", size="md", margin_bottom="10px"),
                rx.text("Problem Summary:", font_weight="bold"),
                rx.text(Company['profile']['problem_summary']['What specific problem is Kaedim trying to solve?']),
                rx.text("Current Solutions:", font_weight="bold"),
                rx.text(Company['profile']['problem_summary']['How do people currently solve this problem?']),
                rx.text("Solution Summary:", font_weight="bold"),
                rx.text(Company['profile']['solution_summary']['What is Kaedim\'s Core Product?']),
                rx.text("Target User Base:", font_weight="bold"),
                rx.text(Company['profile']['solution_summary']['Who is Kaedim\'s target user base?']),
                rx.text("Why Users Choose Kaedim:", font_weight="bold"),
                *[rx.text(f"{reason}: {benefit}") for reason, benefit in Company['profile']['solution_summary']['Why would users choose Kaedim\'s solution?'].items()],
                margin_top="10px",
                color="black"
            ),
            rx.cond(
                TabState.active_tab == "Jobs",
                rx.box(
                    rx.heading("Job Opportunities", size="md", margin_bottom="10px", color="black"),
                    *[rx.text(f"- {role}") for role in Company['open_roles']],
                    margin_top="10px"
                ),
                rx.box(
                    rx.text("No red flags information provided yet.", margin_top="10px", font_size="14px", color="red")
                )
            )
        )

    return rx.box(
        rx.center(
            rx.vstack(
                rx.heading(Company["name"], size="lg", color="black"),
                rx.hstack(
                    rx.text(
                        "Profile",
                        font_size="18px",
                        padding="10px",
                        cursor="pointer",
                        color=rx.cond(TabState.active_tab == "Profile", "black", "gray"),
                        font_weight=rx.cond(TabState.active_tab == "Profile", "bold", "normal"),
                        on_click=TabState.set_tab("Profile")
                    ),
                    rx.text(
                        "Jobs",
                        font_size="18px",
                        padding="10px",
                        cursor="pointer",
                        color=rx.cond(TabState.active_tab == "Jobs", "black", "gray"),
                        font_weight=rx.cond(TabState.active_tab == "Jobs", "bold", "normal"),
                        on_click=TabState.set_tab("Jobs")
                    ),
                    rx.text(
                        "Red Flags",
                        font_size="18px",
                        padding="10px",
                        cursor="pointer",
                        color=rx.cond(TabState.active_tab == "Red Flags", "black", "gray"),
                        font_weight=rx.cond(TabState.active_tab == "Red Flags", "bold", "normal"),
                        on_click=TabState.set_tab("Red Flags")
                    ),
                    spacing="20px"
                ),
                display_tab_content(),
                padding="20px",
                border_radius="15px",
                border="1px solid #e0e0e0",
                background_color="white",
                width="600px",
                box_shadow="0 2px 5px rgba(0, 0, 0, 0.1)"
            )
        ),
        position="relative",
        min_height="100vh"
    )
