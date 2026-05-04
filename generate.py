import os, random
from datetime import datetime

# ================= CONFIG =================
BATCH_SIZE = 12

domain = open("domain.txt").read().strip()
keywords = [k.strip() for k in open("keyword.txt").readlines() if k.strip()]

os.makedirs("posts", exist_ok=True)

# ================= PROGRESS =================
start = 0
if os.path.exists("last_index.txt"):
    start = int(open("last_index.txt").read().strip())

end = start + BATCH_SIZE
selected = keywords[start:end]

open("last_index.txt","w").write(str(end))

# ================= TEMPLATE =================
def head(title, url):
    return f"""
<meta charset='UTF-8'>
<meta name='viewport' content='width=device-width, initial-scale=1'>
<title>{title}</title>
<meta name='description' content='{title} ideas and inspiration'>
<link rel='canonical' href='{url}'>

<link href='https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/css/bootstrap.min.css' rel='stylesheet'>
<link href='/style.css' rel='stylesheet'>

<style>
.ads {{ background:#f1f1f1; padding:25px; text-align:center; margin:25px 0; }}
.card:hover {{ transform:translateY(-5px); transition:0.3s; }}
</style>
"""

def navbar():
    return """
<nav class='navbar navbar-expand-lg navbar-dark bg-dark'>
<div class='container'>
<a class='navbar-brand' href='/index.html'>Decor Blog</a>

<button class='navbar-toggler' data-bs-toggle='collapse' data-bs-target='#nav'>
<span class='navbar-toggler-icon'></span>
</button>

<div id='nav' class='collapse navbar-collapse'>
<ul class='navbar-nav me-auto'>
<li class='nav-item'><a class='nav-link' href='/index.html'>Home</a></li>
<li class='nav-item'><a class='nav-link'>Living Room</a></li>
<li class='nav-item'><a class='nav-link'>Bedroom</a></li>
<li class='nav-item'><a class='nav-link'>Kitchen</a></li>
</ul>

<form class='d-flex'>
<input class='form-control me-2' placeholder='Search...'>
<button class='btn btn-outline-light'>Search</button>
</form>

</div>
</div>
</nav>
"""

def sidebar():
    return """
<div class='col-md-4'>

<div class='ads'>ADS SPACE</div>

<div class='card mb-3'>
<div class='card-body'>
<h5>About</h5>
<p>Modern decor ideas and inspiration.</p>
</div>
</div>

<div class='card mb-3'>
<div class='card-body'>
<h5>Categories</h5>
<ul class='list-unstyled'>
<li>Living Room</li>
<li>Bedroom</li>
<li>Kitchen</li>
<li>Bathroom</li>
</ul>
</div>
</div>

<div class='ads'>ADS SPACE</div>

</div>
"""

def footer():
    return """
<footer class='bg-dark text-white text-center p-3 mt-4'>
© 2026 Decor Blog
</footer>
"""

def layout(title, content, url):
    return f"""
<!DOCTYPE html>
<html>
<head>
{head(title, url)}
</head>
<body>

{navbar()}

<div class='container mt-4'>
<div class='row'>

<div class='col-md-8'>

<div class='ads'>ADS SPACE</div>

{content}

<div class='ads'>ADS SPACE</div>

</div>

{sidebar()}

</div>
</div>

{footer()}

</body>
</html>
"""

# ================= CONTENT =================
def paragraph():
    base = [
        "Choosing the right colors sets the mood of your room.",
        "Lighting plays an important role in interior design.",
        "Furniture placement should balance style and comfort.",
        "Textures can add depth and personality.",
        "Small details can create a big impact.",
        "Natural elements create a calming atmosphere."
    ]
    return "<p>" + " ".join(random.sample(base,4)) + "</p>"

def long_content():
    return "".join([paragraph() for _ in range(random.randint(8,12))])

def related(current):
    items = random.sample([k for k in keywords if k != current], 4)
    html = "<h3>Related Posts</h3><div class='row'>"

    for i in items:
        slug = i.lower().replace(" ","-")
        img = "https://tse1.mm.bing.net/th?q=" + i + "&w=400"

        html += f"""
        <div class='col-md-6 mb-3'>
        <div class='card'>
        <a href='/posts/{slug}.html'>
        <img src='{img}' loading='lazy' class='card-img-top'>
        </a>
        <div class='card-body'>
        <a href='/posts/{slug}.html' class='text-dark text-decoration-none'>
        <b>{i.title()}</b>
        </a>
        </div>
        </div>
        </div>
        """

    html += "</div>"
    return html

# ================= GENERATE POSTS =================
for kw in selected:
    slug = kw.lower().replace(" ","-")
    title = kw.title()
    url = f"https://{domain}/posts/{slug}.html"

    image = "https://tse1.mm.bing.net/th?q=" + kw + "&w=800"

    content = f"""
<h1>{title}</h1>

<img src='{image}' loading='lazy' class='img-fluid mb-3'>

{long_content()}

<h2>Tips</h2>
{long_content()}

{related(kw)}
"""

    html = layout(title, content, url)

    open(f"posts/{slug}.html","w",encoding="utf-8").write(html)

# ================= HOMEPAGE =================
posts = os.listdir("posts")
random.shuffle(posts)

grid = "<div class='row'>"

for p in posts[:40]:
    t = p.replace(".html","").replace("-"," ").title()
    img = "https://tse1.mm.bing.net/th?q=" + t + "&w=400"

    grid += f"""
    <div class='col-md-3 mb-4'>
    <div class='card h-100'>
    <a href='/posts/{p}'>
    <img src='{img}' loading='lazy' class='card-img-top'>
    </a>
    <div class='card-body'>
    <a href='/posts/{p}' class='text-dark text-decoration-none'>
    <h6>{t}</h6>
    </a>
    </div>
    </div>
    </div>
    """

grid += "</div>"

home_content = f"""
<h1>Latest Decor Ideas</h1>

{grid}
"""

home_html = layout("Decor Blog", home_content, f"https://{domain}")

open("index.html","w",encoding="utf-8").write(home_html)

# ================= SITEMAP =================
sitemap = ["<?xml version='1.0'?>","<urlset xmlns='http://www.sitemaps.org/schemas/sitemap/0.9'>"]

for p in posts:
    sitemap.append(f"<url><loc>https://{domain}/posts/{p}</loc></url>")

sitemap.append("</urlset>")
open("sitemap.xml","w").write("\n".join(sitemap))

# ================= RSS =================
rss = ["<?xml version='1.0'?>","<rss version='2.0'><channel>"]
rss.append(f"<title>Decor Blog</title>")
rss.append(f"<link>https://{domain}</link>")

for p in posts[:30]:
    title = p.replace(".html","").replace("-"," ").title()
    link = f"https://{domain}/posts/{p}"
    rss.append(f"<item><title>{title}</title><link>{link}</link></item>")

rss.append("</channel></rss>")
open("feed.xml","w").write("\n".join(rss))

print("✅ Generated:", len(selected), "posts")