import sys, getopt, os, re
import bibtexparser
from bibtexparser.bwriter import BibTexWriter
from bibtexparser.bparser import BibTexParser

# Options from the CLI.
in_file = ''
out_file = ''
sort_manually = False

# Order of fields within the individual references.
display_order = [
	'author',
	'translator',
	'editor',
	'title',
	'booktitle',
	'eventtitle',
	'series',
	'publisher',
	'location',
	'journal',
	'pages',
	'edition',
	'volume',
	'number',
	'school',
	'isbn',
	'issn',
	'doi',
	'url',
	'type',
	'institution',
	'date'
]
# Order of actual references. Used in both built-in and manual sort.
sort_order = [
	'ENTRYTYPE',
	'author',
	'date'
]


def usage():
	print('sortrefs.py [-h help] -i <inputfile> [-o overwrite] [-m manual]\n  -o\tOverwrite input file.\n  -m\tHandle reference ordering manually.')

# Get passed arguments.
try:
	opts, args = getopt.getopt(sys.argv[1:], "hi:om")
except getopt.GetoptError:
	usage()
	sys.exit(2)

# Invalid arguments check.
if not len(opts):
	usage()
	assert False, 'Unknown options provided.'

# Get input file and handle overwrite flag (also checks file exists).
for opt, arg in opts:
	if '-h' == opt:
		usage()
		sys.exit(2)
	if '-i' == opt:
		if not os.path.exists(arg):
			assert False, 'File does not exist.'
		in_file = arg
	elif '-o' == opt:
		if not len(in_file):
			assert False, '-o must come after -i.'
		out_file = in_file
	elif '-m' == opt:
		sort_manually = True
	else:
		usage()
		assert False, 'Unknown options provided.'

# If overwrite isn't provided, generate a copy file.
if not len(out_file):
	out_file = f'{os.path.splitext(in_file)[0]}.sorted.bib'


# Expanded from BibDatabase.entry_sort_key
def sort_by_tuple(entry, fields):
	result = []
	for field in fields:
		result.append(re.sub(r'[^A-Za-z\s0-9]+', '', str(entry.get(field, ''))).lower())
	return tuple(result)

# Open and sort, then write to file.
with open(in_file) as f:
	parser = BibTexParser()
	parser.ignore_nonstandard_types = False # Don't delete unrecognized types.
	bib_db = bibtexparser.load(f, parser)

	# The built-in sort method fails if you have double {} surrounding the entry, but this method ignores that.
	if sort_manually:
		bib_db.entries = sorted(bib_db.entries, key=lambda x: sort_by_tuple(x, sort_order))

	# Configure and perform the actual sorting.
	writer = BibTexWriter()
	writer.order_entries_by = None if sort_manually else tuple(sort_order)
	writer.display_order = display_order
	writer.indent = '\t'
	bibtex_str = bibtexparser.dumps(bib_db, writer)
	
	with open(out_file, 'w') as out:
		out.write(bibtex_str)
		print(f'References sorted and written to file: {out_file}')
