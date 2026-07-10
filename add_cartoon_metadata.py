import os
import re
import io

POSTS_DIR = "_posts"

# Regexes to find first image path in the post body
markdown_img_re = re.compile(r'!\[[^\]]*\]\(([^)]+)\)')
html_img_re = re.compile(r'<img[^>]+src=["\']([^"\']+)["\']', re.IGNORECASE)

def extract_first_image(body):
    m = markdown_img_re.search(body)
    if m:
        return m.group(1).strip()
    m = html_img_re.search(body)
    if m:
        return m.group(1).strip()
    return None

def process_file(path):
    with io.open(path, "r", encoding="utf-8") as f:
        content = f.read()

    # Split front matter and body
    if not content.lstrip().startswith("---"):
        print(f"Skipping {path}: no front matter found")
        return

    parts = content.split("---", 2)
    if len(parts) < 3:
        print(f"Skipping {path}: malformed front matter")
        return

    # parts[0] is empty or preamble, parts[1] is front matter, parts[2] is body
    preamble = parts[0]
    fm = parts[1]
    body = parts[2]

    fm_lines = [line for line in fm.splitlines()]
    # Make a dict-like view of front matter for simple keys
    fm_dict = {}
    for line in fm_lines:
        if ":" in line:
            key, val = line.split(":", 1)
            fm_dict[key.strip()] = val.strip()

    # Only process posts that look like cartoons (heuristic)
    # If you want to process ONLY some files, we can add a filter here.
    image_path = extract_first_image(body)
    if not image_path:
        print(f"No image found in body for {path}, leaving unchanged")
        return

    # Ensure category: cartoons (use singular key 'category' to match our Liquid)
    fm_dict["category"] = "cartoons"
    fm_dict["image"] = image_path

    # Rebuild front matter lines (preserving order as best as possible)
    new_fm_lines = []
    keys_added = set()

    for line in fm_lines:
        if ":" in line:
            key, _ = line.split(":", 1)
            key = key.strip()
            if key == "category":
                new_fm_lines.append("category: cartoons")
                keys_added.add("category")
            elif key == "image":
                new_fm_lines.append(f"image: {image_path}")
                keys_added.add("image")
            else:
                new_fm_lines.append(line)
        else:
            new_fm_lines.append(line)

    # If category or image were not in original FM, append them
    if "category" not in keys_added:
        new_fm_lines.append("category: cartoons")
    if "image" not in keys_added:
        new_fm_lines.append(f"image: {image_path}")

    new_fm = "\n".join(new_fm_lines) + "\n"

    new_content = f"{preamble}---\n{new_fm}---{body}"

    with io.open(path, "w", encoding="utf-8") as f:
        f.write(new_content)

    print(f"Updated {path} -> category: cartoons, image: {image_path}")

def main():
    for root, _, files in os.walk(POSTS_DIR):
        for fname in files:
            if fname.endswith((".md", ".markdown", ".html")):
                process_file(os.path.join(root, fname))

if __name__ == "__main__":
    main()
