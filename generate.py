import os, random
from datetime import datetime

# ================= AUTO BASE URL =================
def get_base_url():
    url = open("domain.txt").read().strip()
    if not url.startswith("http"):
        url = "https://" + url
    return url.rstrip("/")

BASE_URL = get_base_url()

# ================= CONFIG =================
BATCH_SIZE = 12

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
        "Natural elements create a calming atmosphere.",
        "A clean layout makes your space feel larger.",
        "Good design improves daily living experience."
    ]
    return "<p>" + " ".join(random.sample(base, 4)) + "</p>"

def long_content():
    return "".join(paragraph() for _ in range(random.randint(8, 12)))

# ================= RELATED POSTS =================
def related(current):
    items = random.sample([k for k in keywords if k != current], 4)

    html = "<h3 class='mt-4'>Related Posts</h3><div class='row'>"

    for i in items:
        slug = i.replace(" ", "-")
        url = f"{BASE_URL}/posts/{slug}.html"
        img = f"https://tse1.mm.bing.net/th?q={i}&w=400"

        html += f"""
        <div class='col-md-6 mb-3'>
            <div class='card h-100 shadow-sm'>
                <a href='{url}'>
                    <img src='{img}' class='card-img-top'>
                </a>
                <div class='card-body'>
                    <a href='{url}' class='text-dark text-decoration-none'>
                        <b>{i.title()}</b>
                    </a>
                </div>
            </div>
        </div>
        """

    html += "</div>"
    return html

# ================= HEADER (GLOBAL TEMPLATE) =================
def build_header(title):
    return f"""
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width,initial-scale=1">

<title>{title}</title>
<meta name="description" content="{title} ideas">

<link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/css/bootstrap.min.css" rel="stylesheet">
<link href="{BASE_URL}/style.css" rel="stylesheet">
</head>

<body>

<!-- NAVBAR -->
<nav class="navbar navbar-expand-lg navbar-dark bg-dark">
<div class="container">

<a class="navbar-brand" href="{BASE_URL}/index.html">Decor Blog</a>

<button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#nav">
<span class="navbar-toggler-icon"></span>
</button>

<div class="collapse navbar-collapse" id="nav">

<ul class="navbar-nav me-auto">
<li class="nav-item"><a class="nav-link" href="{BASE_URL}/index.html">Home</a></li>
<li class="nav-item"><a class="nav-link" href="#">Living Room</a></li>
<li class="nav-item"><a class="nav-link" href="#">Bedroom</a></li>
<li class="nav-item"><a class="nav-link" href="#">Kitchen</a></li>
<li class="nav-item"><a class="nav-link" href="#">Bathroom</a></li>
</ul>

<form class="d-flex">
<input class="form-control me-2" placeholder="Search...">
<button class="btn btn-outline-light">Search</button>
</form>

</div>
</div>
</nav>

"""

# ================= FOOTER =================
def build_footer():
    return """
<footer class="bg-dark text-white text-center p-3 mt-4">
© 2026 Decor Blog
</footer>

<script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/js/bootstrap.bundle.min.js"></script>

</body>
</html>
"""

# ================= GENERATE POSTS =================
for kw in selected:
    slug = kw.replace(" ", "-")
    title = kw.title()
    url = f"{BASE_URL}/posts/{slug}.html"
    image = f"https://tse1.mm.bing.net/th?q={kw}&w=800"

    html = build_header(title)

    html += f"""
<div class="container mt-4">

<div class="row">

<!-- MAIN CONTENT -->
<div class="col-md-8">

<h1>{title}</h1>

<img src="{image}" class="img-fluid rounded mb-3">

<div class="ads text-center p-3 bg-light mb-3">ADVERTISEMENT</div>

{long_content()}

<h2>Ideas & Inspiration</h2>
{long_content()}

<div class="ads text-center p-3 bg-light my-3">ADVERTISEMENT</div>

{related(kw)}

</div>

<!-- SIDEBAR (CONSISTENT) -->
<div class="col-md-4">

<div class="card mb-3">
<div class="card-body">
<h5>About</h5>
<p>Modern home decor ideas & inspiration blog.</p>
</div>
</div>

<div class="card mb-3">
<div class="card-body">
<h5>Categories</h5>
<ul class="list-unstyled">
<li>Living Room</li>
<li>Bedroom</li>
<li>Kitchen</li>
<li>Bathroom</li>
</ul>
</div>
</div>

<div class="card mb-3">
<div class="card-body">
<h5>Popular</h5>
<ul class="list-unstyled">
<li>Modern Design</li>
<li>Minimalist Home</li>
<li>Small Space Ideas</li>
</ul>
</div>
</div>

<div class="ads text-center p-3 bg-light">ADVERTISEMENT</div>

</div>

</div>
</div>
"""

    html += build_footer()

    open(f"posts/{slug}.html", "w", encoding="utf-8").write(html)

# ================= HOMEPAGE =================
posts = sorted(os.listdir("posts"), reverse=True)

home = build_header("Decor Blog")

home += """
<div class="container mt-4">
<div class="row">
"""

for p in posts[:40]:
    t = p.replace(".html","").replace("-"," ").title()
    img = f"https://tse1.mm.bing.net/th?q={t}&w=400"

    home += f"""
    <div class="col-md-3 mb-4">
        <div class="card h-100 shadow-sm">
            <a href="posts/{p}">
                <img src="{img}" class="card-img-top">
            </a>
            <div class="card-body">
                <a href="posts/{p}" class="text-dark text-decoration-none">
                    <h6>{t}</h6>
                </a>
            </div>
        </div>
    </div>
    """

home += """
</div>

<div class="ads text-center p-3 bg-light">ADVERTISEMENT</div>

</div>
"""

home += build_footer()

open("index.html", "w", encoding="utf-8").write(home)

# ================= SITEMAP =================
sitemap = [
"<?xml version='1.0' encoding='UTF-8'?>",
"<urlset xmlns='http://www.sitemaps.org/schemas/sitemap/0.9'>"
]

for p in posts:
    sitemap.append(
        f"<url><loc>{BASE_URL}/posts/{p}</loc><lastmod>{datetime.utcnow().date()}</lastmod></url>"
    )

sitemap.append("</urlset>")

open("sitemap.xml", "w").write("\n".join(sitemap))

# ================= RSS =================
rss = [
"<?xml version='1.0' encoding='UTF-8'?>",
"<rss version='2.0'><channel>",
"<title>Decor Blog</title>",
f"<link>{BASE_URL}</link>",
"<description>Home decor inspiration</description>"
]

for p in posts[:30]:
    title = p.replace(".html","").replace("-"," ").title()
    link = f"{BASE_URL}/posts/{p}"

    rss.append("<item>")
    rss.append(f"<title>{title}</title>")
    rss.append(f"<link>{link}</link>")
    rss.append("</item>")

rss.append("</channel></rss>")

open("feed.xml", "w").write("\n".join(rss))

print("✅ DONE:", len(selected), "posts generated")