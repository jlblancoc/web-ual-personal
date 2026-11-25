# AGENTS.md

Personal web site (Pelican). Layout and build commands: `README.md`. American spelling, no long dashes.

## Keep the search metadata in sync with every change

Google indexes the site from `sitemap.xml`, the Open Graph tags and the schema.org JSON-LD (Google
Dataset Search for the dataset pages). All of them are generated at build time from the sources below,
so every content change must also update them:

- **Page dates**: bump `Modified:` (today's date) in every page you change, including small edits and
  link additions. `sitemap.xml` (plugin `pelican.plugins.sitemap`) takes each page's `lastmod` from it.
  New pages get `Date:` and `Modified:`; they enter the sitemap by themselves.
- **Summary and image**: keep `Summary:` (meta description and `og:description`) and, on dataset pages,
  `image:` (`og:image`, JSON-LD `image`) in line with the page content.
- **Datasets** (`data/datasets.json`, read by `templates/partial/jsonld_dataset.html`): when the data
  changes, update `date_modified`, `description`, `keywords`, `license`, `creators` and the download
  fields. A new dataset needs:
  - its entry in `data/datasets.json` and a page in `content/pages/` with `template: dataset`,
    `dataset: <key>`, `parent: datasets`;
  - a card in the `hub` macro of `templates/partial/dataset_macros.html`, newest first;
  - its key in the `ItemList` loop of `jsonld_dataset.html` (same order), and a `distribution` branch
    there if its download fields differ from the existing ones;
  - a line in "How to cite" of `content/pages/datasets.md` (same order), and its `Summary:` and
    `Modified:`;
  - links from the "Related datasets" of the pages that relate to it.
- **Check**: `make html OUTPUTDIR=<tmp dir>`, then confirm the changed pages are in `sitemap.xml` with the
  new `lastmod`, and that their `application/ld+json` blocks parse as JSON.
- **After publishing** (`make ftp_upload`, done by the owner): remind the owner to resubmit
  `https://w3.ual.es/~jlblanco/sitemap.xml` in Google Search Console when pages were added or removed.
  There is no `robots.txt` (the site is not at the domain root).

## Notes

- Pelican rewrites only one `{static}`/`{filename}` attribute per tag: for a `<video>` with a poster,
  put the file in a `<source src=...>` child.
- Static files go under `content/imgs/`, `content/docs/` or `content/css/` (`STATIC_PATHS`).
