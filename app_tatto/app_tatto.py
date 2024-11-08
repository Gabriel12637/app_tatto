import reflex as rx

def index()->rx.Component:
    return rx.fragment(
        rx.heading("tatto designs",size="9"),
        rx.text("una pagina que veras difentes diseños de tatto "),
        rx.text("y prodras generar el diseño que gustes y cuantos quieras con ayuda de una IA "),
        rx.image(src="imagen.png", alt="Tattoo Design"),
    
    )


app=rx.App()
app.add_page(index)

