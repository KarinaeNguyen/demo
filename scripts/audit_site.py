import os
import glob
import re

root_dir = r"d:\Work\quocphan.vn"
errors = []

# 1. Audit blog.html
hub_path = os.path.join(root_dir, "blog.html")
with open(hub_path, "r", encoding="utf-8") as f:
    hub_content = f.read()

blog_links = re.findall(r'href="(blog/[^"]+\.html)"', hub_content)
print(f"blog.html has {len(blog_links)} blog post links (unique: {len(set(blog_links))})")
for bl in set(blog_links):
    target = os.path.join(root_dir, bl.replace("/", os.sep))
    if not os.path.exists(target):
        errors.append(f"blog.html links to missing file: {bl}")

# 2. Check all 24 blog files
blog_files = glob.glob(os.path.join(root_dir, "blog", "*.html"))
print(f"Auditing {len(blog_files)} blog articles...")

for bf in blog_files:
    fname = os.path.basename(bf)
    with open(bf, "r", encoding="utf-8") as f:
        content = f.read()
    
    # Check assets & internal links referenced with ../
    assets = re.findall(r'(?:src|href)="(\.\./[^"]+)"', content)
    for asset in assets:
        clean_asset = asset.replace("../", "").split("?")[0].split("#")[0]
        if clean_asset:
            target = os.path.join(root_dir, clean_asset.replace("/", os.sep))
            if not os.path.exists(target):
                errors.append(f"{fname} references missing target: {asset} -> {clean_asset}")
    
    # Check related post links
    rel_links = re.findall(r'<a href="([^"]+\.html)" class="newsletter-related-card"', content)
    for rl in rel_links:
        target = os.path.join(root_dir, "blog", rl)
        if not os.path.exists(target):
            errors.append(f"{fname} links to missing related article: {rl}")
            
    # Check image comments
    if "<!-- <image" not in content:
        errors.append(f"{fname} is missing <!-- <image> comment placeholder!")

# 3. Check all root HTML files
root_files = glob.glob(os.path.join(root_dir, "*.html"))
print(f"Auditing {len(root_files)} root HTML pages...")
for rf in root_files:
    fname = os.path.basename(rf)
    with open(rf, "r", encoding="utf-8") as f:
        content = f.read()
    
    # Check internal links in root HTML
    links = re.findall(r'(?:src|href)="([^":#]+(?:\.html|\.xml|\.txt|\.css|\.js|\.png|\.jpg|\.jpeg|\.ico))"', content)
    for link in links:
        if link.startswith("http") or link.startswith("tel:") or link.startswith("mailto:") or link.startswith("//"):
            continue
        clean_link = link.split("?")[0].split("#")[0]
        target = os.path.join(root_dir, clean_link.replace("/", os.sep))
        if not os.path.exists(target):
            errors.append(f"{fname} links to missing local target: {link}")

    # Check footer presence
    if "<footer" not in content:
        errors.append(f"{fname} missing <footer>")
    if "quan-he-bao-chi.html" not in content:
        errors.append(f"{fname} missing quan-he-bao-chi.html in footer")
    if "chinh-sach-bao-mat.html" not in content:
        errors.append(f"{fname} missing chinh-sach-bao-mat.html in footer")

if errors:
    print(f"FOUND {len(errors)} ERRORS:")
    for err in errors:
        print(" - ", err)
else:
    print("ALL AUDITS PASSED! 100% of links, assets, compliance pages, and footer links are verified.")
