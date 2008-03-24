Summary:	Simple unified package and service management
Name:		xsync
Version:	0.8.3
Release:	0.1
License:	GPL
Group:		Applications
Source0:	http://www.openfusion.com.au/labs/dist/%{name}-%{version}.tar.gz
# Source0-md5:	d96644d79fdeb80e72b1eb2ec7350c1e
URL:		http://www.openfusion.com.au/labs/xsync/
BuildRequires:	perl-tools-pod
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
xsync provides basic package and services management via a unified
directory/file interface - touching a file in the appropriate
directory indicates that a package should be installed or uninstalled,
or a service configured to run or not run. Running xsync then ensures
that the running system is in sync those policies. The interface is
simple, easy to understand, and amenable to remote large-scale
administration.

This version supports chkconfig- and daemontools-based services,
package management via rpm, apt, and yum, the installation of perl
CPAN modules, and the execution of scripts.

%prep
%setup -q

%build
pod2man --section=8 -r "xsync %{version}" doc/xsync.pod > doc/xsync.8

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_sysconfdir}/xsync $RPM_BUILD_ROOT/etc/sysconfig $RPM_BUILD_ROOT%{_sbindir}
install -d $RPM_BUILD_ROOT%{_mandir}/man8 $RPM_BUILD_ROOT/var/cache/xsync
cp -r etc/* $RPM_BUILD_ROOT%{_sysconfdir}/xsync
mv $RPM_BUILD_ROOT%{_sysconfdir}/xsync/xsync $RPM_BUILD_ROOT/etc/sysconfig/xsync
cp -r var/* $RPM_BUILD_ROOT/var/cache/xsync
cp sbin/* $RPM_BUILD_ROOT%{_sbindir}
cp -a doc/xsync.8 $RPM_BUILD_ROOT%{_mandir}/man8/xsync.8

%clean
rm -rf $RPM_BUILD_ROOT


%files
%defattr(644,root,root,755)
%doc README TODO
%attr(755,root,root) %{_sbindir}/xsync_functions
%attr(755,root,root) %{_sbindir}/xsync
%attr(755,root,root) %{_sbindir}/xsync-*
%attr(755,root,root) %config %{_sysconfdir}/xsync
%attr(755,root,root) %config /var/cache/xsync
%config(noreplace) %verify(not md5 mtime size) /etc/sysconfig/xsync
%{_mandir}/man8/*
