BU PhD Thesis Template
========================

> A LaTeX / XeLaTeX / LuaLaTeX PhD thesis template for Bournemouth University based on Cambridge University Engineering Department's template.

[![License MIT](http://img.shields.io/badge/license-MIT-brightgreen.svg)](license.md)

## Author(s)
*   Daniel Green

## Notes
* Your main file is ```thesis.tex```.
* You can configure and include custom packages in ```preamble.tex```.
* All of the front matter is defined in the ```front/*.tex``` files.
* You can compile it with the various ```build-*.sh/.bat``` scripts which internally use ```latexmk```.
* Edit ```$pdf_previewer``` in ```.latexmkrc``` to point to your PDF viewer of choice. For Windows, I recommend [Sumatra PDF](https://www.sumatrapdfreader.org), and for macOS, I recommend [Skim](https://skim-app.sourceforge.io/).


Please see the [original README](https://github.com/kks32/phd-thesis-template) for detailed instructions on how to use this thesis.
