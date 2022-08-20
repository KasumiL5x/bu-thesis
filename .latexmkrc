$pdflatex = 'pdflatex -interaction=nonstopmode -shell-escape -halt-on-error -synctex=1 %O %S';
@generated_exts = (@generated_exts, 'synctex.gz');
$pdf_mode = 1; # tex -> pdf
$pdf_previewer = 'C:/Users/kasum/AppData/Local/SumatraPDF/SumatraPDF.exe';
