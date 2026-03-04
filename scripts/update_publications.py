import bibtexparser
from scholarly import scholarly
import yaml
from pathlib import Path
from pylatexenc.latex2text import LatexNodes2Text

# Function to convert LaTeX accented chars to Unicode
def latex_to_unicode(s):
    return LatexNodes2Text().latex_to_text(s)

# Paths
bibfile = Path("assets/publications.bib")
out_pubs = Path("_data/publications.yml")
out_cits = Path("_data/citations.yml")

# Load BibTeX database
with bibfile.open(encoding="utf-8") as f:
    bib_database = bibtexparser.load(f)

publications = []
citations = {}

for entry in bib_database.entries:
    key = entry["ID"]

    # Convert LaTeX fields to Unicode
    title = latex_to_unicode(entry.get("title", ""))
    authors = latex_to_unicode(entry.get("author", ""))
    journal = latex_to_unicode(entry.get("journal", ""))
    year = entry.get("year", "")
    doi = entry.get("doi", "")
    abstract = latex_to_unicode(entry.get("abstract", ""))

    # Fetch Google Scholar citations
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
        "abstract": abstract
    })

# Save publications.yml
out_pubs.write_text(
    yaml.dump(publications, sort_keys=False, allow_unicode=True),
    encoding="utf-8"
)

# Save citations.yml
out_cits.write_text(
    yaml.dump(citations, sort_keys=False),
    encoding="utf-8"
)

print("Publications and citations updated successfully!")
