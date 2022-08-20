# Builds the entire project from scratch, including the index for nomenclature.

# Clean the project.
latexmk -C
# Rebuild the project.
latexmk -g -pdf -pv thesis.tex
# Build the index (for nomenclature).
makeindex thesis.nlo -s nomencl.ist -o thesis.nls
# Rebuild the project again.
latexmk -g -pdf -pv thesis.tex
