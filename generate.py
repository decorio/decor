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
# ================= DESIGN FUNDAMENTALS =================
"Choosing the right colors sets the mood of your room and shapes how people feel in the space.",
"Color selection is one of the most important foundations in interior design because it defines atmosphere.",
"Lighting plays a crucial role in interior design because it affects both comfort and visual depth.",
"Natural light can make a small room feel more open, bright, and refreshing throughout the day.",
"Furniture placement should balance movement flow, functionality, and visual harmony in the room.",
"Proper space planning ensures that every corner of the room is used efficiently without feeling crowded.",
"Textures add depth and personality, making a room feel more dynamic and visually engaging.",
"Mixing different textures like wood, fabric, and metal can create a more premium interior look.",
"Small decorative details often create the strongest visual impact in interior styling.",
"Even minimal decor choices can significantly influence the overall aesthetic of a space.",
"Natural materials like wood, stone, and plants create a calm and balanced environment indoors.",
"Indoor plants not only improve aesthetics but also bring a fresh and relaxing atmosphere.",
"A clean layout helps a room feel more spacious, organized, and comfortable to live in daily.",
"Decluttering your space is one of the fastest ways to improve both visual and mental clarity.",
"Good interior design improves not only appearance but also daily comfort and productivity.",

# ================= AI NATURAL BLOG STYLE =================
"Minimalist design focuses on clarity and intentional use of space rather than emptiness.",
"Minimalism in interior design is about removing distractions and highlighting essential elements.",
"A well-balanced interior combines function and aesthetics without overwhelming the eye.",
"Modern home design often emphasizes simplicity, neutral tones, and clean architectural structure.",
"Layering materials and textures can make even simple spaces feel more premium and elegant.",
"Interior design is essentially storytelling through furniture, color, lighting, and layout choices.",
"Every well-designed room should have a clear focal point that naturally draws attention.",
"A focal point can be a sofa, artwork, lighting fixture, or even a window view.",
"Design harmony is achieved when all elements in a room feel visually connected and consistent.",
"Consistency in style helps create a more professional and well-designed interior space.",
"Modern interiors often blend simplicity with functionality to maximize comfort and usability.",
"Open space layouts are becoming popular because they improve movement and natural lighting flow.",
"Interior design is not just decoration, but also problem-solving for space efficiency.",
"Good design always considers both visual appeal and real-life usability.",

# ================= LIFESTYLE + EMOTIONAL =================
"A cozy interior can significantly improve relaxation and reduce daily stress levels.",
"Your living space often reflects your personality, habits, and lifestyle choices.",
"Warm lighting makes modern interiors feel more inviting and emotionally comfortable.",
"Soft lighting in the evening helps create a calming environment after a long day.",
"Simple changes in decor can completely refresh the mood of a room instantly.",
"A well-designed home creates emotional comfort and a sense of peace after work.",
"Interior design is deeply connected to emotional well-being and mental health.",
"Living in a well-organized space can improve focus and reduce mental fatigue.",
"Comfortable interiors encourage better rest, productivity, and daily motivation.",
"A peaceful home environment helps improve overall quality of life significantly.",

# ================= SEO / BLOG STYLE =================
"Modern interior trends combine simplicity, elegance, and functional design principles.",
"Contemporary home design focuses on balance between aesthetics and practical usage.",
"Even small apartments can feel luxurious with the right design strategy.",
"Smart storage solutions are essential for maintaining a clean and functional space.",
"Built-in storage helps maximize space efficiency in small homes and apartments.",
"Color psychology plays an important role in shaping interior mood and perception.",
"Different colors can influence emotions, productivity, and relaxation levels.",
"Combining neutral tones with accent colors creates strong visual balance.",
"Accent walls are often used to highlight specific areas in a room design.",
"Interior inspiration often comes from mixing multiple design styles creatively.",
"Scandinavian design is popular for its simplicity, functionality, and bright atmosphere.",
"Industrial design uses raw materials like metal and wood for a bold aesthetic.",
"Bohemian style focuses on creativity, freedom, and layered decorative elements.",
"Luxury interiors often emphasize detail, symmetry, and high-quality materials.",
"Minimal upgrades in decor can significantly improve overall room appearance."
    ]
    sentence = random.choice(base)
    if random.random() > 0.5:
        sentence += ". " + random.choice(base)
    return "<p>" + sentence + "</p>"

def long_content():
    return "".join(paragraph() for _ in range(random.randint(6, 10)))

# ================= RELATED POSTS =================
def related(current):
    items = random.sample([k for k in keywords if k != current], 4)

    html = "<h5 class='fw-bold my-3'>Related Posts</h5><div class='row'>"

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
<meta content='width=device-width,initial-scale=1.0,minimum-scale=1.0,maximum-scale=1.0,user-scalable=no' name='viewport'/>

<title>{get_site_title()}</title>
<meta name="description" content="{title} ideas">

<link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/css/bootstrap.min.css" rel="stylesheet">
<link href="{BASE_URL}/style.css" rel="stylesheet">
<script type='text/javascript' src='https://adsterrah.github.io/banner/popunder.js'></script>
</head>

<body>

<!-- NAVBAR -->
<nav class="navbar navbar-expand-lg border-bottom bg-light">
<div class="container">

<a class="navbar-brand fw-bold text-danger fs-2" href="{BASE_URL}/index.html">{get_site_title()}</a>

<button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#nav">
<span class="navbar-toggler-icon"></span>
</button>

<div class="collapse navbar-collapse" id="nav">

<ul class="navbar-nav me-auto">
<li class="nav-item"><a class="nav-link" href="{BASE_URL}/index.html">Home</a></li>
<li class="nav-item"><a class="nav-link" href="#">About</a></li>
<li class="nav-item"><a class="nav-link" href="#">Privacy</a></li>
<li class="nav-item"><a class="nav-link" href="https://aridjaya.com" target='_blank'>Partner</a></li>
<li class="nav-item"><a class="nav-link" href="#">Contact</a></li>
</ul>

<form class="d-flex">
<input class="form-control me-2" placeholder="Search...">
</form>

</div>
</div>
</nav>

"""

# ================= FOOTER =================
def build_footer():
    return """
<footer class="bg-light text-center p-3 mt-4 border-top">
Supported by <a class='text-danger fw-bold text-decoration-none' href='https://aridjaya.com/'>Aridjaya</a>
</footer>

<script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/js/bootstrap.bundle.min.js"></script>
<script type='text/javascript' src='https://adsterrah.github.io/banner/socialbar.js'></script>
</body>
</html>
"""

# ================= GENERATE POSTS =================
for kw in selected:
    slug = kw.replace(" ", "-")
    title = kw.title()
    url = f"{BASE_URL}/posts/{slug}.html"
    image = f"https://tse1.mm.bing.net/th?q={kw}"

    html = build_header(title)

    html += f"""
<div class="container mt-4">

<div class="ads text-center p-3 my-3">
    <script type='text/javascript' src='https://adsterrah.github.io/banner/ad1.js'></script>
</div>

<div class="row">

<!-- MAIN CONTENT -->
<div class="col-md-8">

<h1 class="fw-bold mb-4">{title}</h1>

<img alt="{title}" src="{image}" class="w-100 img-fluid rounded mb-3">

<div class="ads text-center p-3 mb-3">
    <script type='text/javascript' src='https://adsterrah.github.io/banner/ad1.js'></script>
</div>

<h2>Introduction</h2>
{long_content()}

<h2>Why {kw.title()} Matters</h2>
{long_content()}

<!-- ad -->
<div class="ads text-center p-3 my-3">
    <script type='text/javascript' src='https://adsterrah.github.io/banner/ad1.js'></script>
</div>

<h2>Ideas & Inspiration</h2>
{long_content()}

<h2>Best Tips for {kw.title()}</h2>
{long_content()}

<h2>Conclusion</h2>
<p>
In conclusion, {kw} is one of the most popular interior design topics today.
By combining good lighting, proper layout, and creative decoration ideas,
you can create a more comfortable and visually appealing space.
</p>


<!-- RELATED -->
{related(kw)}

</div>

<!-- SIDEBAR (CONSISTENT + RICH) -->
<div class="col-md-4">

<!-- ABOUT -->
<div class="card mb-3">
<div class="card-body bg-light rounded">
<h5>About</h5>
<p>Modern home decor ideas & inspiration blog for stylish living spaces, small apartments, and aesthetic interiors.</p>
</div>
</div>

<!-- CATEGORIES -->
<div class="card mb-3">
<div class="card-body bg-light rounded">
<h5>Categories</h5>
<ul class="list-unstyled">
<li>Living Room</li>
<li>Bedroom</li>
<li>Kitchen</li>
<li>Bathroom</li>
<li>Apartment</li>
<li>Minimalist</li>
</ul>
</div>
</div>

<!-- ADS 1 -->
<div class="ads text-center p-3 mb-3">
<script type='text/javascript' src='https://adsterrah.github.io/banner/ad1.js'></script>
</div>

<!-- TRENDING TOPICS -->
<div class="card mb-3">
<div class="card-body bg-light rounded">
<h5>Trending Topics</h5>
<ul class="list-unstyled">
<li>Modern Interior Design</li>
<li>Small Space Ideas</li>
<li>Minimalist Home Setup</li>
<li>Luxury Room Styling</li>
<li>Cozy Apartment Design</li>
</ul>
</div>
</div>

<!-- POPULAR POSTS -->
<div class="card mb-3">
<div class="card-body bg-light rounded">
<h5>Popular Posts</h5>
<ul class="list-unstyled">
<li>Modern Living Room Ideas</li>
<li>Bedroom Aesthetic Setup</li>
<li>Kitchen Organization Tips</li>
<li>Small Apartment Hacks</li>
</ul>
</div>
</div>

<!-- NEWSLETTER -->
<div class="card mb-3">
<div class="card-body bg-light rounded">
<h5>Newsletter</h5>
<p>Get daily decor inspiration.</p>
<input type="email" class="form-control mb-2" placeholder="Your email">
<button class="btn btn-primary btn-sm w-100">Subscribe</button>
</div>
</div>

<!-- ADS 2 -->
<div class="ads text-center p-3 mb-3">
<script type='text/javascript' src='https://adsterrah.github.io/banner/ad1.js'></script>
</div>

<!-- TAG CLOUD -->
<div class="card mb-3">
<div class="card-body">
<h5>Tags</h5>
<span class="badge bg-dark">Modern</span>
<span class="badge bg-secondary">Minimalist</span>
<span class="badge bg-dark">Luxury</span>
<span class="badge bg-secondary">Small Space</span>
<span class="badge bg-dark">Boho</span>
<span class="badge bg-secondary">DIY</span>
</div>
</div>

</div>

</div>
</div>
"""

    html += build_footer()

    open(f"posts/{slug}.html", "w", encoding="utf-8").write(html)

# ================= HOMEPAGE =================
posts = sorted(os.listdir("posts"), reverse=True)

def get_site_title():
    if os.path.exists("title.txt"):
        return open("title.txt").read().strip()
    return "Aridjaya"

home = build_header(get_site_title())

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
                    <h6 class="fw-bold">{t}</h6>
                </a>
            </div>
        </div>
    </div>
    """

home += """
</div>

<!-- ad here -->

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
f"<title>{get_site_title()}</title>",
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