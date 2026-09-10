import glob
import re

files = glob.glob("blog/*.html")
count = 0
for f in files:
    with open(f, "r", encoding="utf-8") as fp:
        html = fp.read()
    
    # We replace:
    # <code class="placeholder-tag-code">&lt;image src="" alt="(.*?)" /&gt;</code>
    # with:
    # <code class="placeholder-tag-code">&lt;image src="" alt="\1" /&gt;</code>
    # <image src="" alt="\1" data-placeholder="true" style="display:none;" />
    
    def replacer(m):
        alt_val = m.group(1)
        return f'<code class="placeholder-tag-code">&lt;image src="" alt="{alt_val}" /&gt;</code>\n                <image src="" alt="{alt_val}" data-placeholder="true" style="display:none;" />'
    
    new_html = re.sub(r'<code class="placeholder-tag-code">&lt;image src="" alt="(.*?)" /&gt;</code>', replacer, html)
    if new_html != html:
        with open(f, "w", encoding="utf-8") as fp:
            fp.write(new_html)
        count += 1

print(f"Successfully injected literal <image> tags into {count} blog HTML files!")
