import os
import re
import pandas as pd
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from datetime import datetime
from reportlab.lib.utils import simpleSplit

def create_composers_pdf(csv_file):
    df = pd.read_csv(csv_file)
    
    width, height = letter
    
    x = 50
    y = height - 60
    max_width = width - 2 * x    
    
    for index, row in df.iterrows():
        
        id = row["ID"]
        email = row["Email de contacto"]
        telefono = row["Teléfono de contacto"]
        nombre_completo = row["Nombre completo"]
        nombre_artistico = row["Nombre artístico"]
        
        fecha_nacimiento = row["Fecha de nacimiento."]
        fecha_formato = datetime.strptime(fecha_nacimiento, "%m/%d/%Y")
        today = datetime.today()
        edad = today.year - fecha_formato.year - ((today.month, today.day) < (fecha_formato.month, fecha_formato.day))
        
        ciudad_nacimiento = row["Ciudad de nacimiento"]
        ciudad_residencia = row["Ciudad de residencia actual"]        
        semblanza = row["Semblanza breve"]
        foto = row["Liga a fotografía"]
        
        titulo1 = row["Título de la obra"]
        estreno1 = row["¿Es estreno?"]
        duracion1 = row["Duración en minutos"]
        dotacion1 = row["Dotación instrumental"]
        ano1 = row["Año de creación"]
        nota1 = row["Nota de programa"]
        partitura1 = row["Liga a partitura"]
        partichela1 = row["Liga a partichelas (en caso de ser necesario)"]
        material1 = row["Liga a material digital o grabación de la obra (en caso de ser necesario)"]
        
        titulo2 = row["Título de la obra2"]
        estreno2 = row["¿Es estreno?2"]
        duracion2 = row["Duración en minutos2"]
        dotacion2 = row["Dotación instrumental2"]
        ano2 = row["Año de creación3"]
        nota2 = row["Nota de programa2"]
        partitura2 = row["Liga a partitura2"]
        partichela2 = row["Liga a partichelas (en caso de ser necesario)2"]
        material2 = row["Liga a material digital o grabación de la obra (en caso de ser necesario)3"]
        
        
        filename = f"{id}_{nombre_artistico.replace(" ", "_")}.pdf"
        save_name = os.path.join("compositores/", filename)
        
        c = canvas.Canvas(save_name, pagesize=letter)
        c.setFont("Helvetica-Bold", 40)                
        c.drawString(x, y, f"{id}. {nombre_artistico}")
        c.line(50, height - 70, 600, height - 70)
        
        interlinea = 60
        c.setFont("Helvetica", 10)
        c.drawString(x, y-interlinea, f"Nombre completo: {nombre_completo}")
        interlinea += 12
        c.drawString(x, y-interlinea, f"Email: {email}   |   Teléfono: {telefono}")
        interlinea += 12
        c.drawString(x, y-interlinea, f"Fecha de nacimiento: {fecha_nacimiento}   |   Edad: {edad}")
        interlinea += 12
        c.drawString(x, y-interlinea, f"Ciudad de nacimiento: {ciudad_nacimiento}   |   Ciudad de residencia: {ciudad_residencia}")
        interlinea += 20
        
        c.setFont("Helvetica-Bold", 10)
        c.drawString(x, y-interlinea, f"Semblanza breve:")
        interlinea += 20
        
        c.setFont("Helvetica", 10)
        lines = simpleSplit(semblanza, c._fontname, c._fontsize, max_width)
        for line in lines:
            c.drawString(x, y-interlinea, line)
            interlinea +=10
        interlinea +=10
            
        
        c.drawString(x, y-interlinea, f"Liga a fotografía:")
        interlinea += 12
        c.setFillColor("blue")
        c.drawString(x, y-interlinea, foto)
        c.linkURL(foto, (x, y-interlinea, x + 200, y-interlinea + 10), relative=1)
        
        # OBRA 1
        c.showPage()
        interlinea = 20
        c.setFont("Helvetica-Bold", 25)
        c.setFillColor("black")
        c.drawString(x, y-interlinea, f"Obra 1:")
        interlinea += 30
        
        c.setFont("Helvetica", 10)
        c.drawString(x, y-interlinea, f"Título de la obra: {titulo1}")
        interlinea += 12
        c.drawString(x, y-interlinea, f"Duración en minutos: {duracion1}   |   ¿Estreno?: {estreno1}   |   Año de creación: {ano1}")
        interlinea += 12
        c.drawString(x, y-interlinea, f"Dotación instrumental:")
        interlinea +=10
        if pd.notna(dotacion1):
            lines7 = simpleSplit(dotacion1, c._fontname, c._fontsize, max_width)
            for line in lines7:
                c.drawString(x, y-interlinea, line)
                interlinea +=10
        interlinea += 20
        
        c.setFont("Helvetica-Bold", 10)
        c.drawString(x, y-interlinea, f"Nota de programa")
        interlinea += 12
        c.setFont("Helvetica", 10)
        
        lines2 = simpleSplit(nota1, c._fontname, c._fontsize, max_width)
        for line in lines2:
            c.drawString(x, y-interlinea, line)
            interlinea +=10
        interlinea +=10
        
        c.drawString(x, y-interlinea, f"Liga a partitura:")
        interlinea += 12
        c.setFillColor("blue")
        c.drawString(x, y-interlinea, partitura1)
        c.linkURL(partitura1, (x, y-interlinea, x + 200, y-interlinea + 10), relative=1)
        interlinea += 12
        
        c.setFillColor("black")
        c.drawString(x, y-interlinea, f"Liga a partichelas:")
        interlinea += 12
        if pd.notna(partichela1):           
            c.setFillColor("blue")
            c.drawString(x, y-interlinea, partichela1)
            c.linkURL(partichela1, (x, y-interlinea, x + 200, y-interlinea + 10), relative=1)            
            c.setFillColor("black") 
        
        interlinea += 12
        c.drawString(x, y-interlinea, f"Liga a material digital:")
        interlinea += 12
        if pd.notna(material1):
            c.setFillColor("blue")
            c.drawString(x, y-interlinea, material1)
            c.linkURL(material1, (x, y-interlinea, x + 200, y-interlinea + 10), relative=1)
        
        # OBRA 2
        if pd.notna(titulo2):    
            interlinea += 50
            c.setFont("Helvetica-Bold", 25)
            c.setFillColor("black")
            c.drawString(x, y-interlinea, f"Obra 2:")
            interlinea += 30
            
            c.setFont("Helvetica", 10)
            c.drawString(x, y-interlinea, f"Título de la obra: {titulo2}")
            interlinea += 12
            c.drawString(x, y-interlinea, f"Duración en minutos: {duracion2}   |   ¿Estreno?: {estreno2}")
            interlinea += 12
            c.drawString(x, y-interlinea, f"Dotación instrumental:")
            interlinea +=10
            if pd.notna(dotacion2):
                lines6 = simpleSplit(dotacion2, c._fontname, c._fontsize, max_width)
                for line in lines6:
                    c.drawString(x, y-interlinea, line)
                    interlinea +=10
            interlinea += 20
            
            c.setFont("Helvetica-Bold", 10)
            c.drawString(x, y-interlinea, f"Nota de programa")
            interlinea += 12
            c.setFont("Helvetica", 10)
            
            if pd.notna(nota2):
                lines3 = simpleSplit(nota2, c._fontname, c._fontsize, max_width)
                for line in lines3:
                    c.drawString(x, y-interlinea, line)
                    interlinea +=10
            interlinea +=10
            
            c.drawString(x, y-interlinea, f"Liga a partitura:")
            interlinea += 12
            if pd.notna(partitura2):
                c.setFillColor("blue")
                c.drawString(x, y-interlinea, partitura2)
                c.linkURL(partitura2, (x, y-interlinea, x + 200, y-interlinea + 10), relative=1)
                c.setFillColor("black")
            
            interlinea += 12
            c.setFillColor("black")
            c.drawString(x, y-interlinea, f"Liga a partichelas:")
            interlinea += 12
            if pd.notna(partichela2):           
                c.setFillColor("blue")
                c.drawString(x, y-interlinea, partichela2)
                c.linkURL(partichela2, (x, y-interlinea, x + 200, y-interlinea + 10), relative=1)            
                c.setFillColor("black") 
            
            interlinea += 12
            c.drawString(x, y-interlinea, f"Liga a material digital:")
            interlinea += 12
            if pd.notna(material2):
                c.setFillColor("blue")
                c.drawString(x, y-interlinea, material1)
                c.linkURL(material1, (x, y-interlinea, x + 200, y-interlinea + 10), relative=1)     

        c.save()

def create_interpreters_pdf(csv_file):
    df = pd.read_csv(csv_file)
    
    width, height = letter
    
    x = 50
    y = height - 60
    max_width = width - 2 * x    
    
    for index, row in df.iterrows():
        
        id = row["ID"]
        email = row["Email de contacto"]
        telefono = row["Teléfono de contacto"]
        nombre_completo = row["Nombre completo de la persona responsable"]
        nombre_artistico = row["Nombre artístico del intérprete o ensamble"]
        
        dotacion = row["Dotación instrumental"]
        ciudad_residencia = row["Ciudad de residencia actual"]                
        semblanza = row["Semblanza breve"]
        foto = row["Liga a fotografía"]
        
        programa = row["Programa propuesto"]        
        partituras = row["Liga a partituras"]
        nota = row["Nota de programa de cada obra propuesta"]
        carta = row["Liga a carta de consentimiento (revisar convocatoria)"]
        material = row["Liga a materiales digitales o audios de las obras (sólo en caso de ser necesario)"]
        requerimientos = row["Requerimientos técnicos"]
        
        estado = row["Estado de la república donde se realizará el concierto"]
        sede = row["Sede donde se realizará el concierto"]
        fecha = row["Fecha del concierto"]
        hora = row["Hora del concierto"]
        liga = row["Liga a carta de aceptación de la sede"]
        
        
        filename = f"{id}_{re.sub(r'[ /]', '_', nombre_artistico)}.pdf"
        save_name = os.path.join("interpretes/", filename)
        
        c = canvas.Canvas(save_name, pagesize=letter)
        
        # DATOS DEL INTERPRETE Y SEDE
        
        c.setFont("Helvetica-Bold", 30)                
        c.drawString(x, y, f"{id}. {nombre_artistico}")
        c.line(50, height - 70, 600, height - 70)        
        interlinea = 40
        
        c.setFont("Helvetica-Bold", 20)         
        c.drawString(x, y-interlinea, f"{estado}")
        interlinea += 25
        
        c.setFont("Helvetica", 10)
        c.drawString(x, y-interlinea, f"Dotación instrumental: {dotacion}")
        interlinea += 12
        c.drawString(x, y-interlinea, f"Nombre completo: {nombre_completo}")
        interlinea += 12
        c.drawString(x, y-interlinea, f"Email: {email}   |   Teléfono: {telefono}")
        interlinea += 12        
        c.drawString(x, y-interlinea, f"Ciudad de residencia: {ciudad_residencia}")
        interlinea += 20
        
        c.setFont("Helvetica-Bold", 10)
        c.drawString(x, y-interlinea, f"Semblanza breve:")
        interlinea += 20        
        c.setFont("Helvetica", 10)
        lines = simpleSplit(semblanza, c._fontname, c._fontsize, max_width)
        for line in lines:
            c.drawString(x, y-interlinea, line)
            interlinea +=10
        interlinea +=10
            
        
        c.drawString(x, y-interlinea, f"Liga a fotografía:")
        interlinea += 12
        c.setFillColor("blue")
        c.drawString(x, y-interlinea, foto)
        c.linkURL(foto, (x, y-interlinea, x + 200, y-interlinea + 10), relative=1)
        
        if pd.notna(sede):
            interlinea +=20
            c.setFont("Helvetica-Bold", 25)
            c.setFillColor("black")
            c.drawString(x, y-interlinea, f"Datos del concierto")
            interlinea += 20
            
            c.setFont("Helvetica", 10)
            c.drawString(x, y-interlinea, f"Sede donde se realizará el concierto: {sede}")
            interlinea += 12
            c.drawString(x, y-interlinea, f"Fecha del concierto: {fecha}   |   Hora del concierto: {hora}")
            interlinea += 12
            
            c.drawString(x, y-interlinea, f"Liga a carta de aceptación:")
            interlinea += 12
            c.setFillColor("blue")
            c.drawString(x, y-interlinea, liga)
            c.linkURL(liga, (x, y-interlinea, x + 200, y-interlinea + 10), relative=1)
        
        
        
        # PROGRAMA
        c.showPage()
        interlinea = 20
        c.setFont("Helvetica-Bold", 25)
        c.setFillColor("black")
        c.drawString(x, y-interlinea, f"Programa propuesto")
        interlinea += 30
        c.setFont("Helvetica", 10)
        lines2 = simpleSplit(programa, c._fontname, c._fontsize, max_width)
        for line in lines2:
            c.drawString(x, y-interlinea, line)
            interlinea +=10
        interlinea +=20
       
        c.setFont("Helvetica-Bold", 15) 
        c.drawString(x, y-interlinea, f"Requerimientos técnicos")
        interlinea += 15
        c.setFont("Helvetica", 10)
        lines5 = simpleSplit(requerimientos, c._fontname, c._fontsize, max_width)
        for line in lines5:
            c.drawString(x, y-interlinea, line)
            interlinea +=12
        interlinea +=10
        
        c.drawString(x, y-interlinea, f"Liga a partituras:")
        interlinea += 12
        c.setFillColor("blue")
        c.drawString(x, y-interlinea, partituras)
        c.linkURL(partituras, (x, y-interlinea, x + 200, y-interlinea + 10), relative=1)
        interlinea += 20        
        c.setFillColor("black")   
             
        if pd.notna(carta):
            c.drawString(x, y-interlinea, f"Liga a carta de consentimiento:")
            interlinea += 12           
            c.setFillColor("blue")
            c.drawString(x, y-interlinea, carta)
            c.linkURL(carta, (x, y-interlinea, x + 200, y-interlinea + 10), relative=1)            
            c.setFillColor("black")
            interlinea += 20
            
        c.drawString(x, y-interlinea, f"Liga a materiales digitales o audios:")
        interlinea += 12
        if pd.notna(material):           
            c.setFillColor("blue")
            c.drawString(x, y-interlinea, material)
            c.linkURL(material, (x, y-interlinea, x + 200, y-interlinea + 10), relative=1)            
            c.setFillColor("black") 
        
        # NOTAS DE PROGRAMA
        c.showPage()
        interlinea = 20
        c.setFont("Helvetica-Bold", 25)
        c.setFillColor("black")
        c.drawString(x, y-interlinea, f"Notas de programa de cada obra propuesta")
        interlinea += 30
        c.setFont("Helvetica", 10)
        if pd.notna(nota):
            lines3 = simpleSplit(nota, c._fontname, c._fontsize, max_width)
            for line in lines3:
                c.drawString(x, y-interlinea, line)
                interlinea +=12
        interlinea +=10

        c.save()

create_composers_pdf("comp.csv")
create_interpreters_pdf("inter.csv")
        