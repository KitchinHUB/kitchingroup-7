pt3d:
	pdflatex Pt3d_version2
	bibtex Pt3d_version2
	pdflatex Pt3d_version2
	pdflatex Pt3d_version2
	pdflatex Pt3d_version2
	acroread Pt3d_version2.pdf &

clean:
	rm -f *.aux *.blg *.bbl *.tbx *.log *.out *.fgx *.pdf