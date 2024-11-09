import reflex as rx
def tag(text:str, color:stru = "gray" )\
-> rx.Component:
    return rx.box(
        rx.text(text, color='white', font_size="sm"),
        bg=color,
        px=2,
        py=1,
        border_radius="md",
        mr=2,
    )