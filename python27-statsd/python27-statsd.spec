Name: python27-statsd
Version: 0.1.10
Release: 1
Summary: Python implementation of the Statsd client/server
Group: Development/Libraries
License: BSD
URL: https://github.com/sivy/py-statsd
Source0: https://github.com/sivy/pystatsd/archive/%{version}.tar.gz
Patch1: defaults.patch
Patch2: daemon.patch

BuildRoot: %(mktemp -ud %{_tmppath}/%{name}-%{version}-%{release}-XXXXXX)
BuildArch: noarch
BuildRequires: python27-setuptools

%description
pystatsd is a client and server implementation of Etsy's brilliant statsd
server, a front end/proxy for the Graphite stats collection and graphing
server.

%prep
%setup -q -n pystatsd-%{version}
%patch1 -p0
%patch2 -p0

%build
%{__python} setup.py build

%install
rm -rf %{buildroot}
%{__python} setup.py install -O1 --skip-build --root %{buildroot}
%{__install} -D -m755 redhat/pystatsd.init %{buildroot}%{_sysconfdir}/rc.d/init.d/pystatsd

%clean
rm -rf %{buildroot}

%post
/sbin/chkconfig --add pystatsd

%preun
if [ $1 -eq 0 ]; then
	/sbin/service pystatsd stop >/dev/null 2>&1
	/sbin/chkconfig --del pystatsd
fi

%postun
if [ $1 -ge 1 ]; then
	/sbin/service pystatsd restart >/dev/null 2>&1 || :
fi

%files
%defattr(-,root,root,-)
%doc README.md
%{python_sitelib}/pystatsd*
%{_bindir}/pystatsd-server
%{_sysconfdir}/rc.d/init.d/pystatsd

%changelog
* Thu Apr 18 2013 Paul Egan <paulegan@rockpack.com> - 0.1.7-1
- Initial release
