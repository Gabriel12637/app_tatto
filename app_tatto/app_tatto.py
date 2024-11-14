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
                        href="https://www.instagram.com/tatuajespics/profilecard/?igsh=MXJranZoZmRsNDFpZA==",
                        is_external=True,
                    ),
                    rx.link(
                        rx.button(rx.icon(tag="facebook"),color_scheme="blue"),
                        href="",
                        is_external=True,
                    ),
                ),
                rx.image(src="https://i.pinimg.com/736x/de/95/60/de9560746c644363df6cc879f574e9a7.jpg"),
                rx.image(src="/imagen4.jng", alt="tattoo Design"),
                rx.image(src="/imagen6.jng", alt="tattoo Design"),
                
               
            
                  
            
            ),
            spacing="5",
            justify="center",
            min_height="85vh",
        ),
        rx.hstack(
            rx.text("¿Te quieres hacer un tatuaje pero no sabes si te va a quedar bien?", size="9",color="white",align="center",margin_top="-600px"),
        ),
        rx.text("Has llegado al lugar indicado. Hoy, en TuAppPara, traemos una recopilación de las mejores aplicaciones de tatuajes para Android e iOS de este 2024",margin_top="-400px"),
        
        
        rx.hstack(
            rx.text("Si te estás preguntando si un tatuaje te quedará bien", size="9",color="white",align="center",margin_top="50px"),
        ),
        
       rx.hstack(
            rx.text(
                "lo primero que debes considerar es el diseño y su colocación. Cada cuerpo es diferente, y un tatuaje que se ve genial en otra persona puede no verse igual en tu piel. Sin embargo, si eliges un diseño que realmente te gusta y trabajas con un buen tatuador, lo más probable es que el resultado te sorprenda gratamente.",
                size="5", color="white",margin_top="50px",fontFamily="monoespaciada"
            ),
             rx.image(
               src="/imagen7.jng", alt="Tattoo Design",
                size="5", color="white",margin_top="50px"
            ),
       ),
        
        bakground_image=rx.image(src="imagen 9.jng", alt="Tattoo Design"),
        
    ),
 


app = rx.App()
app.add_page(index)

