# -*- rpm-spec -*-
# $Id: rpm-build-tcl.spec,v 1.1 2004/09/16 11:15:04 me Exp $

#==========================================
# all these will be in separate macro file

%define _xemacs_confdir %_sysconfdir/xemacs
%define _xemacs_sitestartdir %_xemacs_confdir/site-start.d

%define _xemacs_infodir %_infodir/xemacs

%define _xemacs_package_root %_datadir/xemacs
%define _xemacs_pkgdir %_xemacs_package_root/xemacs-packages
%define _xemacs_muledir %_xemacs_package_root/mule-packages
%define _xemacs_sitedir %_xemacs_package_root/site-packages
#==========================================

Name: xemacsen
Version: 0.2
Release: alt0.1

Summary: Common directories and start scripts for XEmacsen
License: GPL
Group: Editors
BuildArch: noarch

Source0: %name-%version.tar

BuildPreReq: libalternatives-devel

PreReq: rpm >= 4.0.4-alt1 alternatives >= 0.0.6
Requires: info-install >= 4.3-alt1

%package -n xemacs-common
Summary: Common set of XEmacs packages
Group: Editors
Serial: 1
PreReq: ctags
PreReq: xemacs-minimal
PreReq: xemacs-cc-mode
PreReq: xemacs-dired
PreReq: xemacs-edebug
PreReq: xemacs-ediff
PreReq: xemacs-edit-utils
PreReq: xemacs-efs
PreReq: xemacs-el-devel
PreReq: xemacs-elib
PreReq: xemacs-emerge
PreReq: xemacs-eterm
PreReq: xemacs-fsf-compat
PreReq: xemacs-gnus
PreReq: xemacs-ilisp
PreReq: xemacs-ispell
PreReq: xemacs-mailcrypt
PreReq: xemacs-mail-lib
PreReq: xemacs-mh-e
PreReq: xemacs-pcl-cvs
PreReq: xemacs-prog-modes
PreReq: xemacs-ps-print
PreReq: xemacs-sh-script
PreReq: xemacs-speedbar
PreReq: xemacs-text-modes
PreReq: xemacs-vc
PreReq: xemacs-w3

%package -n xemacs-mule-common
Summary: Common set of MULE-featured XEmacs packages
Group: Editors
Serial: 1
PreReq: xemacs-common = %serial:%version-%release
PreReq: xemacs-latin-unity
PreReq: xemacs-leim 
PreReq: xemacs-mule-ucs

%description
The common site start scripts for XEmacsen contain the default 
configuration for XEmacsen suggetsted by ALT. Administrators can
add some scripts of their own to customize XEmacsen even more.
This package also contains some common, non version- and arch-specific
directories in XEmacsen hierarchy.

%description -n xemacs-common
This virtual package provides common set of the XEmacs packages

%description -n xemacs-mule-common
This virtual package provides common set of the MULE-featured
XEmacs packages

%prep
%setup -qc

%install
%__mkdir_p %buildroot%_xemacs_sitestartdir
%__install -p -m0644 site-start.el %buildroot%_xemacs_confdir
%__install -p -m0644 [01][01]*.el %buildroot%_xemacs_sitestartdir
%__install -p -m0644 -D %name-macros %buildroot%_sysconfdir/rpm/macros.d/xemacs
%__install -p -m0644 -D %name-alternatives %buildroot%_altdir/xemacs
%__install -p -m0644 -D package-index %buildroot%_xemacs_package_root/package-index
%__mkdir_p %buildroot%_xemacs_pkgdir/{etc,lisp,lib-src}
%__mkdir_p %buildroot%_xemacs_muledir/{etc,lisp,lib-src}
%__mkdir_p %buildroot%_xemacs_sitedir/{etc,lisp,lib-src}
%__mkdir_p %buildroot%_xemacs_infodir
touch %buildroot%_xemacs_infodir/dir

%post
%register_alternatives xemacs -- xemacs

%preun
%unregister_alternatives xemacs

%files
%_altdir/xemacs
%_sysconfdir/rpm/macros.d/xemacs
%dir %_xemacs_confdir
%dir %_xemacs_sitestartdir
%dir %_xemacs_infodir
%dir %_xemacs_package_root
%dir %_xemacs_pkgdir
%dir %_xemacs_pkgdir/etc
%dir %_xemacs_pkgdir/lisp
%dir %_xemacs_pkgdir/lib-src
%dir %_xemacs_muledir
%dir %_xemacs_muledir/etc
%dir %_xemacs_muledir/lisp
%dir %_xemacs_muledir/lib-src
%dir %_xemacs_sitedir
%dir %_xemacs_sitedir/etc
%dir %_xemacs_sitedir/lisp
%dir %_xemacs_sitedir/lib-src
%dir %_xemacs_package_root/package-index
%config(noreplace) %_xemacs_confdir/site-start.el
%config(noreplace) %_xemacs_sitestartdir/*.el
%ghost %_xemacs_infodir/dir

%files -n xemacs-common
%files -n xemacs-mule-common

%changelog
* Tue Sep 14 2004 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.2-alt0.1
- added byterecompilation and install macros

* Tue Jun  8 2004 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.1-alt13
- package index updated 2004-05-14
- removed obsolete xterm-keys hack
 
* Sat Feb  7 2004 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.1-alt12
- added CTEXT selection handling hack by SJT
- package index updated 2004-01-30

* Sat Oct  4 2003 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.1-alt11
- package-index updated 2003-10-01

* Sat Jul  5 2003 Sergey Bolshakov <s.bolshakov@sam-solutions.net> 0.1-alt10
- package-index updated 2003-06-28

* Sat Jun 14 2003 Sergey Bolshakov <s.bolshakov@sam-solutions.net> 0.1-alt9
- switched to new alternatives
- keys in xterm adopted for ALT's defaults

* Mon May 19 2003 Sergey Bolshakov <s.bolshakov@sam-solutions.net> 0.1-alt8
- package-index updated 2003-04-10

* Wed Mar  5 2003 Sergey Bolshakov <s.bolshakov@sam-solutions.net> 0.1-alt7
- removed obsolete install-info workaround
- package-index updated 20030125

* Mon Dec 16 2002 Sergey Bolshakov <s.bolshakov@belcaf.com> 0.1-alt6
- package-index updated 20021101

* Sat Nov 23 2002 Sergey Bolshakov <s.bolshakov@belcaf.com> 0.1-alt5
- switch-buffers modifications by Alexey Morozov <morozov@novosoft.ru>

* Mon Oct 28 2002 Sergey Bolshakov <s.bolshakov@belcaf.com> 0.1-alt4
- package index updated 20021014

* Sat Sep 21 2002 Sergey Bolshakov <s.bolshakov@belcaf.com> 0.1-alt3
- package index added

* Mon Sep  9 2002 Sergey Bolshakov <s.bolshakov@belcaf.com> 0.1-alt2
- added macros for byte-compilation

* Sat Sep  7 2002 Sergey Bolshakov <s.bolshakov@belcaf.com> 0.1-alt1
- first build for %distribution distribution


