import flet as ft

def UserView(page, auth_controller):
    page.title = "Perfil"
    page.bgcolor = ft.Colors.LIGHT_BLUE_50

    user = getattr(page, "user_data", None)
    
    def formatear_fecha(fecha):
        if not fecha:
            return "No disponible"
        if isinstance(fecha, str) and ' ' in fecha:
            fecha_parte = fecha.split(' ')[0]
            hora_parte = fecha.split(' ')[1]
            año, mes, dia = fecha_parte.split('-')
            return f"{dia}/{mes}/{año} {hora_parte}"
        elif isinstance(fecha, str):
            año, mes, dia = fecha.split('-')
            return f"{dia}/{mes}/{año}"
        return str(fecha)

    def info_item(icono, texto):
        return ft.Container(
            content=ft.Row(
                [
                    ft.Icon(icono, color=ft.Colors.LIGHT_BLUE_700, size=28),
                    ft.Text(
                        texto,
                        size=18,
                        color=ft.Colors.BLUE_GREY_900
                    ),
                ],
                spacing=15
            ),
            padding=15,
            bgcolor=ft.Colors.WHITE,
            border_radius=12,
            border=ft.border.all(1, ft.Colors.LIGHT_BLUE_100)
        )
    
    nombre = info_item(
        ft.Icons.PERSON,
        f"Nombre: {user['nombre'] if user else 'Usuario'}"
    )

    apellido = info_item(
        ft.Icons.BADGE,
        f"Apellido: {user['apellido'] if user else 'Usuario'}"
    )

    telefono = info_item(
        ft.Icons.PHONE,
        f"Teléfono: {user['telefono'] if user else 'Usuario'}"
    )

    email = info_item(
        ft.Icons.EMAIL,
        f"Email: {user['email'] if user else 'Usuario'}"
    )

    fecha_registro = info_item(
        ft.Icons.CALENDAR_MONTH,
        f"Fecha de creación: {formatear_fecha(user['fecha_registro']) if user else 'No disponible'}"
    )

    ultimo_acceso = info_item(
        ft.Icons.ACCESS_TIME,
        f"Último acceso: {formatear_fecha(user['ultimo_acceso']) if user else 'No disponible'}"
    )

    return ft.View(
        route="/perfil",
        bgcolor=ft.Colors.LIGHT_BLUE_50,
        controls=[
            ft.AppBar(
                title=ft.Text(
                    "Perfil de Usuario",
                    size=26,
                    weight="bold"
                ),
                bgcolor=ft.Colors.LIGHT_BLUE_700,
                color=ft.Colors.WHITE,
                actions=[
                    ft.IconButton(
                        ft.Icons.DASHBOARD,
                        icon_color=ft.Colors.WHITE,
                        tooltip="Dashboard",
                        on_click=lambda _: page.go("/dashboard")
                    ),
                    ft.IconButton(
                        ft.Icons.EXIT_TO_APP,
                        icon_color=ft.Colors.WHITE,
                        tooltip="Cerrar sesión",
                        on_click=lambda _: page.go("/")
                    )
                ],
            ),

            ft.Container(
                content=ft.Column(
                    [
                        ft.Container(height=10),

                        ft.CircleAvatar(
                            content=ft.Icon(
                                ft.Icons.PERSON,
                                size=60,
                                color=ft.Colors.WHITE
                            ),
                            radius=45,
                            bgcolor=ft.Colors.LIGHT_BLUE_600
                        ),

                        ft.Text(
                            "Información del Usuario",
                            size=24,
                            weight="bold",
                            color=ft.Colors.LIGHT_BLUE_900
                        ),

                        ft.Divider(
                            thickness=2,
                            color=ft.Colors.LIGHT_BLUE_200
                        ),

                        nombre,
                        apellido,
                        telefono,
                        email,
                        fecha_registro,
                        ultimo_acceso,
                    ],
                    spacing=15,
                    horizontal_alignment=ft.CrossAxisAlignment.CENTER
                ),

                padding=25,
                margin=20,
                bgcolor=ft.Colors.WHITE,
                border_radius=20,
                shadow=ft.BoxShadow(
                    spread_radius=1,
                    blur_radius=15,
                    color=ft.Colors.BLACK12,
                    offset=ft.Offset(0, 4)
                ),
                expand=True
            ),
        ]
    )