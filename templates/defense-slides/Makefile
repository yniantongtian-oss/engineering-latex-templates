MAIN=main

.PHONY: all clean

all:
	latexmk -xelatex -interaction=nonstopmode -halt-on-error $(MAIN).tex

clean:
	latexmk -C $(MAIN).tex
