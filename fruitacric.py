import flet as ft


def main(page: ft.page):
    page.add(
        # \n is the line break in here
        ft.Row(controls=[ft.Text("my favorite furit:\n")]),
        ft.Row(controls=[ft.Text("Apple"),
                         ft.Text("Mango"),
                         ft.Text("Guava")]),

    ft.Row(controls=[ft.Text("my favorite furit:\n")]),
    ft.Column(controls=[ft.Text("Apple"),
                     ft.Text("Mango"),
                     ft.Text("Guava")])
    )


ft.app(target=main)