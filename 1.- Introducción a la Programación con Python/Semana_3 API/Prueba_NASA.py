"""
1. Haga una consulta a la API, incluyendo dentro de la request la API Key entregada al 
momento de registrarse, que recupere la información asociada a las imágenes 
tomadas por el mars rover. Quédese solo con los 25 primeros registros entregados 
por la API y descarte los demás.
"""

import requests
import json

url = "https://api.nasa.gov/mars-photos/api/v1/rovers/curiosity/latest_photos?api_key=VMClP6jgB3lZb8CEROzMZLVGDAtaONaFtGDzqInD"
def request(requested_url):
    payload=""
    headers = {
        'cache-control': "no-cache",
        'app_id': '541f27c0-0669-4f3d-a66a-b0c331137c38',      
    }
    response = requests.request("GET", requested_url, headers=headers, data=payload)
    return json.loads(response.text)
print(request(url)['latest_photos'][0:25])

"""
2. Genere una lista que contenga solo las URLs de las imágenes encontradas en el 
diccionario de respuesta filtrado de la consulta del punto anterior. La lista de URLs 
debe ser generada mediante código, se considerará como respuesta incorrecta el 
copy/paste manual de las direcciones en una lista.
"""
images=[]
for i in request(url)['latest_photos'][0:25]:
    images.append(i['img_src'])
print(images)

"""
3. Genere una función llamada build_web_page que debe recibir como parámetro una 
lista con URLs de imágenes en la web y construir una página web que muestre las 
fotos.
"""
def build_web_page(images):
    html_page=""
    count=0

    for i in range(len(images)+2):
        if count == 0:
            #print("<html>\n<head>\n</head>\n<body>\n<ul>\n")
            html_page+="<html>\n<head>\n</head>\n<body>\n<ul>\n"
            count+=1
        elif count > 0 and count < len(images)+1:
            #print(count)
            html_page+= "<li><img src=\"{}\"><li>\n".format(images[i-1])
            count+=1
            #print("<li><img src=\"{}\"><li>\n".format(images[i-1]))
        elif count==len(images)+1:
            html_page+="</ul>\n</body>\n</head>\n</html>\n"
    
    with open("prueba_nasa_becks.html","w") as f:
        f.write(html_page)
    return html_page

print(build_web_page(images))