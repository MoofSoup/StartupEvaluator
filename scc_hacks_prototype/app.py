import reflex as rx
def tag(text:str, color:str = "gray" )\
-> rx.Component:
    return rx.box(
        rx.text(text, color='white', font_size="sm"),
        bg=color,
        px=2,
        py=1,
        border_radius="md",
        mr=2,
    )
def company_card(
        logo: str,
        name: str,
        solution: str,
        tags: list[ str ],
        open_roles: list[str],
) -> rx.Component:
    return rx.link(
        rx.box(
            rx.hstack(
                rx.image(src=logo, box_size="50px",),
                rx.vbox(
                    rx.heading(name, size="md",),
                    rx.text(solution, font_size="sm"),
                    align_items="flex_start",

                ),
                spacing=4,

            ),
#                rx.hstack()
            padding=4,
            border_width=1,
            border_radius="md",
            border_color="gray.200",
            _hover={"shadow": "md"},
            width="100%",
        ),
        href=f"/company/name"
    )
    

