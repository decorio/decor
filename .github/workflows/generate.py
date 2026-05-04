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

# ================= CONTENT =================
def paragraph():
    base = [
        "Choosing the right colors sets the mood of your room.",
        "Lighting plays an important role in interior design.",
        "Furniture placement should balance style and comfort.",
        "Textures can add depth and personality.",
        "Small details can create a big impact.",
        "Combining different materials improves aesthetics.",
        "A clean layout makes your space feel larger.",
        "Natural elements create a calming atmosphere."
    ]
    return "<p>" + " ".join(random.sample(base,4)) + "</p>"

def long_content():
    html = ""
    for _ in range(random.randint(8,12)):
        html += paragraph()
    return html

def related(current):
    items = random.sample([k for k in keywords if k != current], 4)
    html = "<h3 class='mt-4'>Related Posts</h3><div class='row'>"
    for i in items:
        slug = i.replace(" ","-")
        img = "https://tse1.mm.bing.net/th?q=" + i + "&w=400"
        html += f"""
        <div class='col-md-6 mb-3'>
        <div class='card h-100 shadow-sm'>
        <a href='{slug}.html'>
        <img src='{img}' class='card-img-top'>
        </a>
        <div class='card-body'>
        <a href='{slug}.html' class='text-dark text-decoration-none'>
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
    slug = kw.replace(" ","-")
    title = kw.title()
    image = "https://tse1.mm.bing.net/th?q=" + kw + "&w=800"

    html = f"""
<!DOCTYPE html>
<html lang='en'>
<head>
<meta charset='UTF-8'>
<meta name='viewport' content='width=device-width, initial-scale=1'>
<title>{title}</title>

<link href='https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/css/bootstrap.min.css' rel='stylesheet'>
<link href='../style.css' rel='stylesheet'>

<style>
.card:hover {{ transform: translateY(-5px); transition: 0.3s; }}
.ads {{ background:#f1f1f1; text-align:center; padding:20px; margin:20px 0; }}
</style>

</head>
<body>

<nav class='navbar navbar-expand-lg navbar-dark bg-dark'>
<div class='container'>
<a class='navbar-brand' href='../index.html'>Decor Blog</a>

<div class='collapse navbar-collapse'>
<ul class='navbar-nav me-auto'>
<li class='nav-item'><a class='nav-link' href='../index.html'>Home</a></li>
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

<div class='container mt-4'>
<div class='row'>

<div class='col-md-8'>

<h1>{title}</h1>
<img src='{image}' class='img-fluid rounded mb-3'>

<div class='ads'>ADS SPACE</div>

{long_content()}

<h2>Tips & Ideas</h2>
{long_content()}

<div class='ads'>ADS SPACE</div>

{related(kw)}

</div>

<div class='col-md-4'>

<div class='card mb-3'>
<div class='card-body'>
<h5>About</h5>
<p>Modern home decor ideas and inspiration.</p>
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

<div class='card mb-3'>
<div class='card-body'>
<h5>Popular</h5>
<ul class='list-unstyled'>
<li>Modern Living Room</li>
<li>Small Bedroom</li>
<li>Kitchen Setup</li>
</ul>
</div>
</div>

</div>

</div>
</div>

<footer class='bg-dark text-white text-center p-3 mt-4'>
© 2026 Decor Blog
</footer>

</body>
</html>
"""

    open(f"posts/{slug}.html","w",encoding="utf-8").write(html)

# ================= HOMEPAGE =================
posts = os.listdir("posts")
random.shuffle(posts)

index = """
<!DOCTYPE html>
<html>
<head>
<meta charset='UTF-8'>
<meta name='viewport' content='width=device-width, initial-scale=1'>
<title>Decor Blog</title>

<link href='https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/css/bootstrap.min.css' rel='stylesheet'>
<link href='style.css' rel='stylesheet'>

<style>
.card:hover { transform: translateY(-5px); transition: 0.3s; }
</style>

</head>
<body>

<nav class='navbar navbar-dark bg-dark'>
<div class='container'>
<a class='navbar-brand'>Decor Blog</a>
</div>
</nav>

<div class='container mt-4'>
<div class='row'>
"""

for p in posts[:40]:
    t = p.replace(".html","").replace("-"," ").title()
    img = "https://tse1.mm.bing.net/th?q=" + t + "&w=400"

    index += f"""
    <div class='col-md-3 mb-4'>
    <div class='card h-100 shadow-sm'>
    <a href='posts/{p}'>
    <img src='{img}' class='card-img-top'>
    </a>
    <div class='card-body'>
    <a href='posts/{p}' class='text-dark text-decoration-none'>
    <h6>{t}</h6>
    </a>
    </div>
    </div>
    </div>
    """

index += """
</div>

<div class='ads'>ADS SPACE</div>

</div>

<footer class='bg-dark text-white text-center p-3 mt-4'>
© 2026 Decor Blog
</footer>

</body>
</html>
"""

open("index.html","w",encoding="utf-8").write(index)

# ================= SITEMAP =================
sitemap = ["<?xml version='1.0'?>","<urlset xmlns='http://www.sitemaps.org/schemas/sitemap/0.9'>"]

for p in posts:
    sitemap.append(f"<url><loc>https://{domain}/posts/{p}</loc><lastmod>{datetime.utcnow().date()}</lastmod></url>")

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