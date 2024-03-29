import reflex as rx

from didacdev.styles.styles import Size, TextColor
from datetime import datetime


def language(title: str, date: str) -> rx.Component:
    return rx.vstack(
        rx.heading(
            title,
            size="md",
            color=TextColor.PRIMARY.value
        ),
        rx.hstack(
            rx.text(date),
            width="100%",
            font_size=Size.SMALL.value,
            justify_content="space-between"
        ),
        align_items="start",
        spacing=Size.DEFAULT.value,
        border_bottom=f"1px inset {TextColor.PRIMARY.value}",
        padding_y=Size.XSMALL.value,
        width=["100%", "100%", "100%", "30em", "30em"]
    )
