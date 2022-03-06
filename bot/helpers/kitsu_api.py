import requests

async def kitsu_get_title(name):
    titles = []
    a_id = []
    url = f"https://kitsu.io/api/edge/anime?filter[text]={name}"
    r = requests.get(url)
    if r.status_code == 200:
        data = r.json()
        for i in data["data"]:
            titles.append(i["attributes"]["titles"]["en"])
            a_id.append(i["id"])
    return titles, a_id

async def kitsu_get_anime(a_id):
    url = f"https://kitsu.io/api/edge/anime?filter[id]={a_id}"
    r = requests.get(url)
    msg = ""
    if r.status_code == 200:
        data = r.json()
        for i in data["data"]:
            msg += f"<b>Title :</b> {i['attributes']['titles']['en']}\n\n"
            msg += f"<b>Rating :</b> {i['attributes']['ratingRank']}\n\n"
            msg += f"<b>Description :</b> {i['attributes']['synopsis']}\n\n"
            msg += f"<b>Status :</b> {i['attributes']['status']}"
    return msg
    