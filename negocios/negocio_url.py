from auxiliares.url_servicio import url_base_jsonplaceholder as url_base

def url_servicio(origen):
    direccion = f"{url_base}{origen}"
    return direccion