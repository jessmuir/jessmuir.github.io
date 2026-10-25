# How to update this website

A practical guide to adding and changing content on jessiemuir.com.
(This file is not published on the site. `README.md` is the original
theme's generic documentation.)

Most content is plain **Markdown** text. A few lists use **YAML** data files,
where indentation and quotes matter (see [Tips](#tips) at the end).

---

## Contents

1. [Preview your changes locally](#1-preview-your-changes-locally)
2. [Home page: bio, photo, CV, contact, news](#2-home-page)
3. [Add a press item](#3-add-a-press-item)
4. [Add a cartoon](#4-add-a-cartoon)
5. [Add or update a group member](#5-add-or-update-a-group-member)
6. [Research page: projects and talks](#6-research-page-projects-and-talks)
7. [Menu bar, new pages, and footer links](#7-menu-bar-new-pages-and-footer-links)
8. [Publish your changes](#8-publish-your-changes)
9. [Tips](#tips)

---

## 1. Preview your changes locally

From the site folder in Terminal:

```bash
PATH=/opt/homebrew/opt/ruby/bin:$PATH bundle exec jekyll serve
```

Then open <http://localhost:4000>. Saving a file rebuilds the site; refresh
the browser to see it (use **Cmd+Shift+R** if styling looks stale).

**Exception:** changes to `_config.yml` (menu, colors, footer links, site
title) are only read at startup. Stop the server with **Ctrl+C** and run the
command again.

> Use Homebrew's Ruby as above. The Anaconda Ruby that is first on this
> Mac's PATH can't install the site's gems.

---

## 2. Home page

File: **`index.md`**

The top of the page has two parts, side by side on desktop (stacked on
phones):

- **Left sidebar** (`<div class="home-sidebar" markdown="1">`): photo, CV
  link, Education, and Contact.
- **Right** (`<div class="home-intro" markdown="1">`): the bio.

Keep each block's `markdown="1"`, the blank lines inside, and its closing
`</div>`.

The **name and tagline** above the bio come from `title:` and `subtitle:`
at the top of `index.md`; edit them there.

### Bio
Edit the paragraphs inside the `home-intro` block.

### Education and contact
Bullets in the sidebar. An education entry is the degree in bold, then
`<br>`, then the institution:

```markdown
* **PhD, Physics**<br>University of Michigan, 2018
```

### Photo
1. Put a square photo in `img/` (about 1200×1200 px keeps it sharp but fast).
2. In `index.md`, change `src="/img/headshot_uc_2026.jpg"` in the `<img>` tag
   at the top of the sidebar.
3. Also change `share-img:` at the top of the file (the image shown when the
   site is shared on social media or in messages).

To shrink a large photo on a Mac:
```bash
sips -Z 1200 "path/to/original.jpg" --out img/new-headshot.jpg
```

### CV
1. Put the new PDF in the site's top folder, e.g. `Muir-CV-2026.pdf`.
2. In `index.md`, update the CV link in the sidebar:
   `[CV (PDF)](Muir-CV-2026.pdf)` (keep the `{: .cv-link}` line under it).
3. Optionally delete the old PDF.

### News item
Add a bullet at the **top** of the list under `## News and updates`:

```markdown
* October 2026 - Short description with a [link](https://example.com).
```

Interviews, press releases, and media coverage go on the **Press** page
instead (section 3), so they aren't listed twice.

---

## 3. Add a press item

File: **`press.md`**

Add a bullet at the **top** of the list (newest first). End it with the date
and type in parentheses, wrapped in single asterisks:

```markdown
* I was interviewed by Jane Doe for a [Nature article](https://example.com) on dark energy. *(October 2026 · Interview)*
```

- Types used so far: `Interview`, `Press release`, `Artwork`.
- The `*( ... )*` part at the end is what the page shows small and grey.
  (To type `·` on a Mac: **Option+Shift+9**, or just use a comma.)
- Leave the line `{: .press-list}` directly below the last bullet. It applies
  the Press page styling to the list.

---

## 4. Add a cartoon

Each cartoon is a small post in the **`_posts/`** folder. The Cartoons
gallery picks it up automatically, newest first, using its `image:` as the
thumbnail.

1. **Add the image(s)** to `cartoons/images/`. Use simple file names without
   spaces, e.g. `dark_energy_bite.jpg`.
2. **Copy `_posts/template.md`** and rename the copy
   `YYYY-MM-DD-short-name.md`, e.g. `2026-10-24-dark-energy-bite.md`.
   The date in the file name is the date shown in the gallery and sets the
   order. (A file without a date in its name, like `template.md`, is never
   published.)
3. **Fill in the top section** (the "front matter" between the `---` lines):

   ```yaml
   ---
   layout: post
   title: Dark energy bite
   image: /cartoons/images/dark_energy_bite.jpg
   share-img: http://www.jessiemuir.com/cartoons/images/dark_energy_bite.jpg
   social-share: true
   use-site-title: true
   ---
   ```

   - `title`: the caption in the gallery and the heading on the cartoon's page.
   - `image`: the gallery thumbnail (the whole image is shown, not cropped).
   - `share-img`: the same image as a full web address, for link previews.

4. **Write the page below the front matter** in Markdown, e.g.:

   ```markdown
   This cartoon illustrates ...

   ![alt="Short description of the image for screen readers"](/cartoons/images/dark_energy_bite.jpg)
   ```

To **hide** a cartoon without deleting it, add `published: false` to its
front matter.

---

## 5. Add or update a group member

File: **`_data/group.yml`** (a YAML data file; the Group page, `group.md`,
reads it automatically)

### Current member
Add an entry like this (two spaces before each field, no tabs):

```yaml
- name: "Jane Doe"
  role: "PhD student"
  photo: /img/group/jane-doe.jpg
  blurb: "Jane studies tests of gravity with weak lensing."
  link: https://janedoe.github.io
```

- Only `name` is required. Leave out `photo` to show the person's initials.
- Photos: square images in `img/group/` (create the folder the first time).
  About 400×400 px is plenty.
- `link` turns the name into a link to their website.
- **Remove the `PLACEHOLDER Student Name` entry** once you add a real member.

### Past mentee / alum
Add `alum: true`. They are then listed under **Past mentees** instead of
getting a card:

```yaml
- name: "John Smith"
  role: "Undergraduate capstone project (2026)"
  alum: true
```

When a current member leaves, add `alum: true` and update their `role`.
Past mentees are listed in the order they appear in the file, so keep the
newest first.

### Group page text
The intro paragraphs, the note about other UC astrophysics groups, and the
**Prospective students** section are plain Markdown in **`group.md`**.

---

## 6. Research page: projects and talks

File: **`research.md`**

### Add a project card
Each project is a block like this inside the `card-grid` section. Copy an
existing block, paste it where you want it in the order, and edit:

```markdown
<div class="research-card" markdown="1">
### Project title

![Short description of the figure](/img/research/my-figure.png)
{: .card-figure}

[(paper)](https://arxiv.org/abs/XXXX.XXXXX)
{: .card-links}

One or two paragraphs describing the project.
</div>
```

- **Figure (optional):** the image line and the `{: .card-figure}` line under
  it. Delete both for a card without a figure. The figure is shown whole
  (never cropped), centered, and at most 240 px tall, so wide plots and
  diagrams work best. Put new figures in `img/research/` (create the folder
  the first time), or reuse a cartoon from `cartoons/images/`.
  To make the figure link somewhere (e.g. to its cartoon page), wrap it:
  `[![description](/cartoons/images/Extensions.jpg)](/2022-07-14-y3ext-darkbite/)`.
- **Paper links (optional):** the links line and the `{: .card-links}` line
  under it. Delete both if there are no links. Several links can go on one
  line: `[(paper 1)](...) [(paper 2)](...)`.
- Keep the blank lines, `markdown="1"`, and the closing `</div>`. Without
  them the Markdown inside won't be formatted.
- Cards fill two columns on desktop, left to right.

### Add a recorded talk
In the **Recorded talks** card near the bottom, add a bullet under
`#### For the general public` or `#### Technical`:

```markdown
* [**"Talk title"**](https://youtube.com/...) **(Seminar, 1hr)** - Where and when it was given, and what it covers.
```

### "Under construction" note
It's the `<div class="page-notice" markdown="1">` block at the top. Delete
that whole block (through its `</div>`) when the page is up to date.

---

## 7. Menu bar, new pages, and footer links

### Menu bar
In **`_config.yml`**, under `navbar-links:`

```yaml
navbar-links:
  Research: "research"
  Group: "group"
  Press: "press"
  Cartoons: "cartoons"
```

The left side is the label; the right side is the page's address. The
current page's tab is highlighted automatically. *(Restart the preview after
editing `_config.yml`.)*

### Page headings and side boxes (Group, Press, Cartoons)
These pages start with a left-aligned name and tagline, then the intro text
with a small box beside it ("Join the group", "Media inquiries", "Using these
images").

- **Name and tagline:** `title:` and `subtitle:` in the page's front matter.
  The line `{% raw %}{% include page-heading.html %}{% endraw %}` displays them.
- **Side box text:** inside `<div class="side-box" markdown="1">` near the
  top of the page. Its small heading is the `#### ...` line.

### Add a new page
Create e.g. `teaching.md` in the top folder:

```markdown
---
layout: page
title: Teaching
subtitle: Courses at the University of Cincinnati
hide-title: true
own-heading: true
---

{% raw %}{% include page-heading.html %}{% endraw %}

Page content in Markdown.
```

- `title` is used for the heading and the browser tab ("Teaching | Jessie Muir").
- `subtitle` is the tagline under the heading (optional).
- `hide-title` and `own-heading` replace the theme's large centered header
  with the left-aligned heading. For a plain page with no heading at all,
  keep only `hide-title: true` and leave out the `include` line.

To add a side box next to the intro, copy the `<div class="page-top" ...>`
block from the top of `press.md` and edit it.
- Add `wide: true` for a wider text column (used on the Research page).
- Add it to `navbar-links` in `_config.yml` to put it in the menu.

### Footer icons (email, GitHub, ORCID, ...)
In **`_config.yml`**, under `social-network-links:`. Remove a link by
putting `#` at the start of its line; the order of the lines is the order
of the icons. Each name must match an entry in `_data/SocialNetworks.yml`,
which sets its web address and icon.

---

## 8. Publish your changes

The live site is built by GitHub Pages from the **`master`** branch.
Redesign work is on the **`redesign`** branch until it's merged.

```bash
git status
git add -A
git commit -m "Add October 2026 press item"
git push
```

`git add -A` adds everything that changed, including new images. Check
`git status` first so you don't commit things you didn't mean to (like the
`_site/` build folder or editor backup files ending in `~`).

The live site usually updates within a few minutes of pushing to `master`.

---

## Tips

- **Markdown basics:** `**bold**`, `*italic*`, `[link text](https://...)`,
  `* ` at the start of a line for a bullet,
  `![description](/path/to/image.jpg)` for an image.
- **YAML files** (`_config.yml`, `_data/*.yml`, and the front matter between
  `---` lines):
  - Use **spaces, not tabs**, and keep indentation consistent.
  - Put text in **double quotes** if it contains a colon (`:`), `#`, or
    starts with a special character. Inside double quotes, write an
    apostrophe normally: `"Bachelor's thesis"`.
  - If the preview shows an error after editing a YAML file, the problem is
    almost always indentation or a missing quote.
- **Links to other pages on this site** start with `/`, e.g. `/press`. To
  link to a heading, add `#` and the heading in lowercase with dashes, e.g.
  `/research#recorded-talks`.
- **Images** should be web-sized (well under 1 MB). Use `sips -Z 1200 ...`
  (see section 2) to shrink them.
