help:
	@echo "Please use \`make <target>' where <target> is one of"
	@echo "  validate    to validate the WCS files"

validate:
	@find . -type f -name '*.wcs' -exec xmllint --noout {} \;
