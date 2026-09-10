import os
import glob
import re

root_dir = r"d:\Work\quocphan.vn"
errors = []

# 1. Audit blog.html
hub_path = os.path.join(root_dir, "blog.html")
with open(hub_path, "r", encoding="utf-8") as f:
    hub_content = f.read()

# Check all blog links in blog.html
blog_links = re.findall(r'href="(blog/[^"]+\.html)"', hub_content)
print(f"blog.html has {len(blog_links)} blog post links (unique: {len(set(blog_links))})")
for bl in set(blog_links):
    target = os.path.join(root_dir, bl.replace("/", os.sep))
    if not os.path.exists(target):
        errors.append(f"blog.html links to missing file: {bl}")

# Check all 24 blog files
blog_files = glob.glob(os.path.join(root_dir, "blog", "*.html"))
print(f"Auditing {len(blog_files)} blog articles...")

for bf in blog_files:
    fname = os.path.basename(bf)
    with open(bf, "r", encoding="utf-8") as f:
        content = f.read()
    
    # Check assets referenced with ../
    assets = re.findall(r'(?:src|href)="(\.\./[^"]+)"', content)
    for asset in assets:
        clean_asset = asset.replace("../", "").split("?")[0].split("#")[0]
        if clean_asset:
            target = os.path.join(root_dir, clean_asset.replace("/", os.sep))
            if not os.path.exists(target):
                errors.append(f"{fname} references missing asset: {asset} -> {clean_asset}")
    
    # Check related post links
    rel_links = re.findall(r'<a href="([^"]+\.html)" class="newsletter-related-card"', content)
    for rl in rel_links:
        target = os.path.join(root_dir, "blog", rl)
        if not os.path.exists(target):
            errors.append(f"{fname} links to missing related article: {rl}")
            
    # Check image comments
    if "<!-- <image" not in content:
        errors.append(f"{fname} is missing <!-- <image> comment placeholder!")

if errors:
    print(f"FOUND {len(errors)} ERRORS:")
    for err in errors:
        print(" - ", err)
else:
    print("PERFECT! All links, assets, relative paths, and image placeholders are 100% verified!")
