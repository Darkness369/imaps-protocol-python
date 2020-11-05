msg_template = """Hello {name},
Gracias por ser parte de {website}. 

Estamos muy
Felices de tenerte con nosotros.
"""

def format_msg(my_name="Raul", my_website="utch.edu.mx"):
    my_msg = msg_template.format(name=my_name, website=my_website)
    return my_msg