"""
Script to update sitemap.xml with all 24 new blog URLs.
"""
from generate_all_blogs import BLOG_POSTS

def update_sitemap():
    base_urls = [
        ("https://karinaenguyen.github.io/demo/index.html", "2026-09-10", "weekly", "1.0"),
        ("https://karinaenguyen.github.io/demo/gioi-thieu.html", "2026-09-10", "monthly", "0.8"),
        ("https://karinaenguyen.github.io/demo/noi-that.html", "2026-09-10", "weekly", "0.9"),
        ("https://karinaenguyen.github.io/demo/xuong.html", "2026-09-10", "monthly", "0.8"),
        ("https://karinaenguyen.github.io/demo/bao-gia.html", "2026-09-10", "weekly", "0.9"),
        ("https://karinaenguyen.github.io/demo/khach-hang.html", "2026-09-10", "monthly", "0.7"),
        ("https://karinaenguyen.github.io/demo/blog.html", "2026-09-10", "weekly", "0.9"),
        ("https://karinaenguyen.github.io/demo/lien-he.html", "2026-09-10", "monthly", "0.8"),
        ("https://karinaenguyen.github.io/demo/danh-cho-chu-nha.html", "2026-09-10", "monthly", "0.8"),
        ("https://karinaenguyen.github.io/demo/danh-cho-nha-dau-tu.html", "2026-09-10", "monthly", "0.8"),
        ("https://karinaenguyen.github.io/demo/danh-cho-doi-tac.html", "2026-09-10", "monthly", "0.8"),
    ]

    xml_lines = [
        '<?xml version="1.0" encoding="UTF-8"?>',
        '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">'
    ]

    for loc, lastmod, freq, prio in base_urls:
        xml_lines.append(f"""  <url>
    <loc>{loc}</loc>
    <lastmod>{lastmod}</lastmod>
    <changefreq>{freq}</changefreq>
    <priority>{prio}</priority>
  </url>""")

    for p in BLOG_POSTS:
        loc = f"https://karinaenguyen.github.io/demo/blog/{p['slug']}"
        xml_lines.append(f"""  <url>
    <loc>{loc}</loc>
    <lastmod>2026-09-10</lastmod>
    <changefreq>monthly</changefreq>
    <priority>0.8</priority>
  </url>""")

    xml_lines.append('</urlset>\n')

    with open("sitemap.xml", "w", encoding="utf-8") as f:
        f.write("\n".join(xml_lines))
    print(f"Updated sitemap.xml with {len(base_urls) + len(BLOG_POSTS)} total URLs!")

if __name__ == "__main__":
    update_sitemap()
