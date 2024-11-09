import reflex as rx
from .tabs_page import tabs_function

def tag(text: str, color: str = "gray") -> rx.Component:
    return rx.box(
        rx.text(text, color='white', font_size="sm"),
        bg=color,
        px="2",
        py="1",
        border_radius="md",
        mr="2",
    )

def company_card(
    logo_url: str,
    name: str,
    pitch: str,
) -> rx.Component:
    return rx.link(
        rx.box(
            rx.hstack(
                rx.image(
                    src=logo_url,
                    box_size="50px",  # Controls both width and height
                    fit="contain",    # Maintains aspect ratio
                    max_width="50px", # Additional size constraints
                    max_height="50px",
                    border_radius="md", # Optional: rounds the corners
                ),
                rx.vstack(
                    rx.heading(name, size="md",),
                    rx.text(pitch, font_size="sm"),
                    align_items="flex_start",
                ),
                spacing='4',
            ),
            padding=4,
            border_width=1,
            border_radius="md",
            border_color="gray.200",
            _hover={"shadow": "md"},
            width="100%",
        ),
        href=f"/company/{name.lower().replace(' ', '_')}"
    )
