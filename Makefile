PACKAGE	  = rpm-build-tcl
SHELL	  = /bin/sh
RPM	  = /bin/rpm
RPMSPEC	  = $(PACKAGE).spec
VERSION	= $(shell $(RPM) -q --qf '[%{VERSION} ]' --specfile $(RPMSPEC) |cut -f1 -d ' ')
RELEASE	= $(shell $(RPM) -q --qf '[%{RELEASE} ]' --specfile $(RPMSPEC) |cut -f1 -d ' ')
TARFILE = $(PACKAGE)-$(VERSION).tar
TARDIR	= $(shell $(RPM) --eval %_sourcedir)

PKGSRC	= \
	tcl-macros

PKGALL	= $(PKGSRC) $(RPMSPEC)

all:	bte

bte:	$(PKGALL)
	@tar cf $(TARDIR)/$(TARFILE) $(PKGALL)
	@cat $(PACKAGE).spec

clean:	
	rm -f *~ *.tar

.PHONY:	all clean
