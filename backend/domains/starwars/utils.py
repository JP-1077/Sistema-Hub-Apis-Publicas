



def extracao_id_url(url):
    if not url:
        return None
    try:
        return int(url.rstrip("/").split("/")[-1])
    except (ValueError, TypeError):
        return None