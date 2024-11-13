import reflex as rx

def index() -> rx.Component:
    return rx.container(
        #boton para cambiar el tema
        rx.color_mode.button(position="top-right"),
        
        rx.heading("**♥ـﮩ٨ـﮩﮩtatto designsـﮩـ٨ﮩ♥**", size="9",color="white",fontFamily="runas"),
        rx.hstack(
            rx.text(
                "tatto designs es una aplicación móvil diseñada para los amantes de los tatuajes que no tienen algo en mente que les gustaria tatuarse y poder ayudales con los diseños que gusten",
                size="5", color="white"
            ),
            rx.text(
                "tatto designs es una aplicación móvil diseñada para raemos una recopilación de las mejores aplicaciones de tatuajes para Android e iOS de este 2024. Todas las herramientas imprescindibles para usuarios, diseñadores y tatuadores.",
                size="5",
            ),
            rx.vstack(
                rx.hstack(
                    rx.link(
                        rx.button("Registrate aqui!",color_scheme="green"),
                        href="https://forms.gle/Gj2CstmbZuhy1V2c9",
                        is_external=True,
                    ),
                    rx.link(
                        rx.button("estilos",color_scheme="purple"),
                        href="https://forms.gle/Gj2CstmbZuhy1V2c9",
                        is_external=True,
                    ),
                    rx.link(
                        rx.button(rx.icon(tag="instagram"),color_scheme="pink"),
                        href="https://instagram.com",
                        is_external=True,
                    ),
                    rx.link(
                        rx.button(rx.icon(tag="facebook"),color_scheme="blue"),
                        href="",
                        is_external=True,
                    ),
                ),
                rx.image(src="imagen 3.jng", alt="Tattoo Design"),
                rx.image(src="imagen 4.jng", alt="tattoo Design"),
                rx.image(src="imagen 6.jng", alt="tattoo Design"),
                rx.text("Te quieres hacer un tatuaje pero no sabes si te va a quedar bien?", size="9",color="white",align="center"),
                rx.text("Has llegado al lugar indicado. Hoy, en TuAppPara, traemos una recopilación de las mejores aplicaciones de tatuajes para Android e iOS de este 2024.")
            
                  
            
            ),
            spacing="5",
            justify="center",
            min_height="85vh",
        ),
        bg=rx.image(src="imagen 9.jng", alt="Tattoo Design"),
    ),
 


app = rx.App()
app.add_page(index)

