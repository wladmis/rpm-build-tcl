# -*- rpm-spec -*-
# $Id: rpm-build-tcl.spec,v 1.3 2004/10/16 12:30:31 me Exp $

#==========================================
# all these will be in separate macro file
#==========================================

Name: rpm-build-tcl
Version: 0.1
Release: alt0.1

Summary: RPM helpers to use with Tcl scripts
License: GPL
Group: Development/Tcl
BuildArch: noarch

Source0: %name-%version.tar

PreReq: rpm-build >= 4.0.4-alt41

%description
The common site start scripts for XEmacsen contain the default 
configuration for XEmacsen suggetsted by ALT. Administrators can
add some scripts of their own to customize XEmacsen even more.
This package also contains some common, non version- and arch-specific
directories in XEmacsen hierarchy.

%prep
%setup -qc

%install
%__install -p -m0644 -D tcl-macros %buildroot%_sysconfdir/rpm/macros.d/tcl
%__install -p -m0755 -D tcl.req %buildroot%_libdir/rpm/tcl.req
%__install -p -m0755 tcl.prov %buildroot%_libdir/rpm/tcl.prov

%files
%doc README
%_sysconfdir/rpm/macros.d/tcl
%_libdir/rpm/tcl.*

%changelog
* Sat Oct 16 2004 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.1-alt0.1
- Initial release
