# web-ual-personal

Source of my personal web site at <https://w3.ual.es/~jlblanco>, built with
[Pelican](https://getpelican.com/) and the [Flex](https://github.com/alexandrevicenzi/Flex) theme.

## Setup

```bash
git clone --recurse-submodules https://github.com/jlblancoc/web-ual-personal.git
# or, in an existing clone: git submodule update --init
pip install -r requirements.txt
```

## Layout

- `content/pages/`: one file per page. The `myorder` metadata sets the menu order.
- `content/imgs/`, `content/docs/`, `content/css/`: static files.
- `content/extra/`: legacy redirects and verification files, copied to the site root.
- `templates/`: overrides of the Flex templates (sidebar icons, footer, Open Graph and schema.org metadata).
- `pelican-plugins/embed_http/`: embeds the Aigaion2 publication list at build time.
- `themes/Flex/`: git submodule, pinned to a release tag.

## Build and publish

```bash
make serve        # local preview at http://localhost:8000 with auto-reload
make publish      # production build (publishconf.py) into $(OUTPUTDIR)
make ftp_upload   # clean + publish + upload to w3.ual.es via lftp
```
