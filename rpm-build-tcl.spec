# -*- rpm-spec -*-
# $Id: rpm-build-tcl.spec,v 1.13 2006/05/24 20:54:11 me Exp $

Name: rpm-build-tcl
Version: 0.2
Release: alt0.2

Summary: RPM helpers to use with Tcl scripts
License: GPL
Group: Development/Tcl
BuildArch: noarch

Source0: %name-%version.tar

PreReq: rpm-build >= 4.0.4-alt44
Requires: /etc/rpm/macros.d
Conflicts: tcl-devel < 0:8.4.7-alt2

%description
%name is set of scripts and rpm macros to assist in tcl modules
build process

%prep
%setup -qc

%install
%__install -p -m0644 -D tcl-macros %buildroot%_sysconfdir/rpm/macros.d/tcl
%__install -p -m0755 -D tcl.req %buildroot%_rpmlibdir/tcl.req
%__install -p -m0755 tcl.prov %buildroot%_rpmlibdir/tcl.prov

%files
%doc README*
%_sysconfdir/rpm/macros.d/tcl
%_rpmlibdir/tcl.*

%changelog
* Sun May 21 2006 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.2-alt0.2
- %%teapatch macro resurrected

* Wed Jul 13 2005 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.1-alt0.5
- #6488 again

* Sat Apr 16 2005 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.1-alt0.4
- #6488 fixed

* Sat Nov 20 2004 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.1-alt0.3
- catched 'exit' in scripts, which can abort findreq process

* Tue Nov  2 2004 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.1-alt0.2
- added conflicts to older tcl-devel

* Sat Oct 16 2004 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.1-alt0.1
- Initial release
