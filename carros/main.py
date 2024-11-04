import flet as ft
from database import cars  # Verifique se a importação está correta

def main(page: ft.Page):

    def show_car_description(e):
        car = next((car for car in cars if car['id'] == e.control.parent.key), None)
        if car:
            dlg = ft.AlertDialog(
                title=ft.Text(car['descrição']),
                actions=[ft.TextButton('Fechar', on_click=lambda e: page.close(dlg))],
            )
            page.open(dlg)

    def delete_car(e):
        e.control.parent.parent.visible = False
        page.update()

    page.title = 'Carros da Galera'
    page.window.height = 800
    page.window.width = 400

    app_bar = ft.AppBar(
        leading=ft.Icon(ft.icons.DIRECTIONS_CAR_FILLED),
        leading_width=40,
        title=ft.Text('Carros'),
        center_title=True,
        bgcolor=ft.colors.SURFACE_VARIANT,
        actions=[
            ft.IconButton(
                icon=ft.icons.NOTIFICATIONS,
                tooltip='Notificações'
            ),
            ft.IconButton(
                icon=ft.icons.LOGIN,
                tooltip='Entrar na Conta'
            ),
            ft.PopupMenuButton(
                items=[
                    ft.PopupMenuItem(icon=ft.icons.PERSON, text='Perfil'),
                    ft.PopupMenuItem(icon=ft.icons.SETTINGS, text='Configurações'),
                    ft.PopupMenuItem(icon=ft.icons.LOGOUT, text='Sair'),
                ],
            ),
        ]
    )

    cars_list = ft.Column(
        scroll=ft.ScrollMode.ALWAYS,
        expand=True,
    )
    for car in cars:
        car_component = ft.ListTile(
            leading=ft.Image(
                src=car['foto'],
                fit=ft.ImageFit.COVER,
                repeat=ft.ImageRepeat.NO_REPEAT,
                height=100,
                width=100,
                border_radius=5,
            ),
            title=ft.Text(f'{car["modelo"]} - {car["marca"]}'),
            subtitle=ft.Text(car['ano']),
            trailing=ft.PopupMenuButton(
                key=car['id'],
                icon=ft.icons.MORE_VERT,
                items=[
                    ft.PopupMenuItem(
                        icon=ft.icons.REMOVE_RED_EYE_SHARP,
                        text='Ver descrição',
                        on_click=show_car_description,
                    ),
                    ft.PopupMenuItem(
                        icon=ft.icons.DELETE,
                        text='Deletar',
                        on_click=delete_car,
                    ),
                ],
            ),
        )
        cars_list.controls.append(car_component)

    nav_bar = ft.NavigationBar(
        destinations=[
            ft.NavigationBarDestination(icon=ft.icons.DIRECTIONS_CAR_FILLED_OUTLINED, label='Usados'),
            ft.NavigationBarDestination(icon=ft.icons.CAR_RENTAL_OUTLINED, label='Novos'),
            ft.NavigationBarDestination(icon=ft.icons.ELECTRIC_CAR_OUTLINED, label='Elétricos'),
        ],
    )
    
    page.add(app_bar, cars_list, nav_bar)
    page.update()
    
ft.app(main)
