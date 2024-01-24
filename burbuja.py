import flet as ft
import random
import time
# ft.Page crea la ventana, seria parecido al tk.window


def main(page: ft.Page):

    def create_containers(number):
        container_list = []
        for _ in range(number):
            container_list.append(
                ft.Container(
                    content=ft.Text(value=random.randint(1, 100)),
                    alignment=ft.alignment.center,
                    width=100,
                    height=100,
                    bgcolor=ft.colors.RED,
                    border_radius=50,
                )
            )
        return container_list

    row = ft.Row(controls=create_containers(8))

    page.add(row)

    time.sleep(3)

    arr = row.controls

    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            arr[j].bgcolor = ft.colors.BLUE
            arr[j + 1].bgcolor = ft.colors.BLUE
            time.sleep(1)
            page.update()
            if int(arr[j].content.value) > int(arr[j + 1].content.value):
                arr[j], arr[j+1] = arr[j+1], arr[j]
            arr[j].bgcolor = ft.colors.RED
            arr[j+1].bgcolor = ft.colors.RED
        arr[n-i-1].bgcolor = ft.colors.GREEN
    page.update()


# ft app esta a cargo de construir la ventana
# y toma el target que seria la duncion principal de nuestro codigo
ft.app(target=main)
