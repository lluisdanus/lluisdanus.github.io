import bibtexparser
from scholarly import scholarly
import yaml
from pathlib import Path
import latexcodec
import re 

def latex_to_unicode(s):
    if not s:
        return s
    s = s.encode("utf-8").decode("latex")
    # remove leftover braces around single characters
    s = re.sub(r"\{([^{}])\}", r"\1", s)
    return s

bibfile = Path("assets/publications.bib")
out_pubs = Path("_data/publications.yml")
out_cits = Path("_data/citations.yml")

with bibfile.open() as f:
    bib_database = bibtexparser.load(f)

publications = []
citations = {}

for entry in bib_database.entries:
    key = entry["ID"]

    title = latex_to_unicode(entry.get("title", "").strip("{}"))
    authors = latex_to_unicode(entry.get("author", ""))
    journal = latex_to_unicode(entry.get("journal", ""))
    year = entry.get("year", "")
    doi = entry.get("doi", "")
    abstract = latex_to_unicode(entry.get("abstract", ""))

    try:
        search = scholarly.search_pubs(title)
        pub = next(search)
        filled = scholarly.fill(pub)
        citations[key] = filled.get("num_citations", 0)
    except Exception:
        citations[key] = None

    publications.append({
        "id": key,
        "title": title,
        "authors": authors,
        "journal": journal,
        "year": year,
        "doi": doi,
        "abstract": abstract,
    })

out_pubs.write_text(
    yaml.dump(publications, sort_keys=False, allow_unicode=True)
)
out_cits.write_text(
    yaml.dump(citations, sort_keys=False)
)
