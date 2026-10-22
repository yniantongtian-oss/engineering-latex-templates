MAIN=main
CHKTEX=chktex -q -H1 -l $(abspath ../../.chktexrc)

.PHONY: all clean lint

all:
	latexmk -xelatex -interaction=nonstopmode -halt-on-error -file-line-error $(MAIN).tex

lint:
	$(CHKTEX) $(shell find . -name '*.tex' -print)

clean:
	latexmk -C $(MAIN).tex
