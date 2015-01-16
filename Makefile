SRCDIR   = _src
BUILDDIR = _build
RSCRIPT := cd $(BUILDDIR) && Rscript -e
TEX2PDF := cd $(BUILDDIR) && pdflatex -shell-escape

all: clean bootcamp

clean:
	rm -rf $(BUILDDIR)/* *.pdf *.png

$(BUILDDIR):
	mkdir -p $(@)

bootcamp: $(SRCDIR)/bootcamp.tex $(BUILDDIR)
	$(RSCRIPT) "library(knitr); knit('../$(SRCDIR)/$(<F)', '$(@).tex')"
	($(TEX2PDF) $(@))
	($(TEX2PDF) $(@))
	cp $(BUILDDIR)/$(@).pdf $(@).pdf 
