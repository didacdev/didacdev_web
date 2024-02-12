import reflex as rx

import didacdev.constants as const
from didacdev.styles.styles import Size, Color, max_width_style
from didacdev.components.social_link import social_link


def footer() -> rx.Component:
    return rx.vstack(
        rx.hstack(
            rx.image(
                src="/dark_logo.png",
                width="7em",
            ),
            rx.spacer(),
            social_link("github", const.GITHUB_URL),
            social_link("linkedin", const.LINKEDIN_URL),
            width="100%"
        ),
        padding_x=Size.BIG.value,
        padding_y=Size.DEFAULT.value,
        style=max_width_style
    )
