import reflex as rx

def index() -> rx.Component:
    return rx.container(
        #boton para cambiar el tema
       
        
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
                        href="https://forms.gle/SvfayeBmBDAbpiN2A",
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
             
         rx.text("El estilo de tatuaje **anime** se inspira en el arte visual y los personajes que aparecen en las series de animación japonesa, conocido como *anime*. Este tipo de tatuaje ha ganado una gran popularidad en todo el mundo, especialmente entre los aficionados a la cultura pop japonesa",align="center",margin_top="50px",)
      
        
       ),
        

   

rx.hstack(
      rx.image(
    src="https://i.pinimg.com/736x/e8/13/82/e81382f59f22520e1ff84ebd8a25099c.jpg",
    alt="Tattoo Design",
    color="white",
    margin_top="20px",
    width="80%",
     

    ),
    rx.image(src="https://i.pinimg.com/736x/fe/ab/eb/feabeb8e703ddd617a0cb70f13a15be5.jpg",margin_left="20em"),
    alt="Tattoo Design",
    size="",
    color="white",
    margin_top="20px",
    width="30%",
),  



        bakground_image=rx.image(src="https://i.pinimg.com/736x/9f/16/f0/9f16f03a8bbf1a66ea2d89221b1d06d6.jpg", alt="Tattoo Design"),
        
    ),
 


app = rx.App()
app.add_page(index)

 