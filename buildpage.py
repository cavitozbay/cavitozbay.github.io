from jinja2 import Environment, FileSystemLoader
from publist import preprints, published
env = Environment(loader=FileSystemLoader("./"))
index_temp = env.get_template("index.html.jinja")

aboutme_temp = env.get_template("aboutme.html.jinja")
activities_temp = env.get_template("activities.html.jinja")
publications_temp = env.get_template("publications.html.jinja")

pages = [
    {
        "title": "About Me",
        "id" : "aboutme",
        "hrefto" : "#aboutme",
        "content": aboutme_temp.render()
    },
    {
        "title": "Publications",
        "id" : "publications",
        "hrefto" : "#publications",
        "content": publications_temp.render(preprints=preprints,published=published)
    },
        {
        "title": "Activities",
        "id" : "activities",
        "hrefto" : "#activities",
        "content": activities_temp.render()
    },
]




index_content = index_temp.render(
    pages = pages
    )

with open("index.html", mode="w", encoding="utf-8") as index_out:
    index_out.write(index_content)