import reflex as rx

import didacdev.constants as const
from didacdev.styles.styles import Size, Color, max_width_style, title_style
from didacdev.components.social_link import social_link
from didacdev.components.general_project import general_project


def all_projects() -> rx.Component:
    return rx.grid(
        general_project(
            "Star Wars Encyclopedia",
            "#",
            const.STAR_WARS_GITHUB_URL,
            const.STAR_WARS_TEXT,
            "Swift, SwiftUI, Alamofire",
            "/projects/others/star_wars_little.jpg"
        ),
        general_project(
            "Connect Four",
            "#",
            const.CONNECT_FOUR_GITHUB_URL,
            const.CONNECT_FOUR_TEXT,
            "Swift, SwiftUI",
            "/projects/others/connect_four_little.jpg"
        ),
        template_columns="repeat(2, 1fr)",
        gap="12",
        style=max_width_style
    )
