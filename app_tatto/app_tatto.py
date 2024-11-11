import reflex as rx

# Asegúrate de que la función devuelva algo, como rx.no_update si no hay actualizaciones.
def generate_design(event):
    # Aquí va tu lógica de generación del diseño
    print("Diseño generado")
    return rx.no_update  # Esto asegura que no se modifiquen los componentes si no es necesario

# Crear el botón
rx.button("Generar Diseño", on_click=generate_design)

def index() -> rx.Component:
    return rx.fragment(
        rx.heading("Tattoo Designs", size="9"),
        rx.text("Una página donde podrás ver diferentes diseños de tatuajes"),
        rx.text("Y podrás generar el diseño que gustes y cuantos quieras con la ayuda de una IA"),
        rx.image(src="imagen 3.png", alt="Tattoo Design"),
        rx.image(src="imagen 4.png", alt="Tattoo Design"),
        rx.image(src="imagen 5.png", alt="Tattoo Design"),
        rx.button("Generar Diseño", on_click=generate_design),
        rx.text("Descubre tu diseño de tatuaje personalizado"),
        rx.form(
            rx.text_input("Nombre", placeholder="Ingresa tu nombre"),
            rx.text_area("Descripción", placeholder="Cuenta sobre tu idea de tatuaje"),
            rx.button("Generar Diseño", on_click=generate_design)
        )
    )

app = rx.App()
app.add_page(index)
