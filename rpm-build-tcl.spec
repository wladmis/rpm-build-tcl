# -*- rpm-spec -*-
# $Id: rpm-build-tcl.spec,v 1.7 2004/10/19 15:28:41 me Exp $

Name: rpm-build-tcl
Version: 0.1
Release: alt0.1

Summary: RPM helpers to use with Tcl scripts
License: GPL
Group: Development/Tcl
BuildArch: noarch

Source0: %name-%version.tar

PreReq: rpm-build >= 4.0.4-alt40.1
Requires: /etc/rpm/macros.d

%description
%name is set of scripts and rpm macros to assist in tcl modules
build process

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
