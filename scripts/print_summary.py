import json
import sys

sys.stdout.reconfigure(encoding='utf-8')
with open('scratch/all_blogs_summary.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

for k, v in data.items():
    title = v.get('title', '')
    pages = v.get('pages', 0)
    captions = []
    headings = []
    for p in v.get('sample', []):
        for line in p.get('lines', []):
            if any(roman in line for roman in ['I.', 'II.', 'III.', 'IV.', 'V.', '1.', '2.', '3.']) and len(line) < 80:
                headings.append(line)
            if any(word in line.lower() for word in ['tủ bếp', 'nội thất', 'căn hộ', 'phòng ngủ', 'quận']) and len(line) < 90:
                captions.append(line)
    print(f"[{k}] {title} ({pages} trang)")
    if headings:
        print(f"    Mục: {' // '.join(headings[:3])}")
