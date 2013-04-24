Name: python27-geventhttpclient
Version: 1.1
Release: 1%{?dist}
Summary: http client library for gevent
Group: Development/Libraries
License: MIT
URL: https://github.com/gwik/geventhttpclient
Source0: https://github.com/gwik/geventhttpclient/archive/master.tar.gz
Patch1: gevent-dns.patch

BuildRoot: %(mktemp -ud %{_tmppath}/%{name}-%{version}-%{release}-XXXXXX)
BuildRequires: python27-setuptools
Requires: python27-gevent

%description
A high performance, concurrent HTTP client library for python using gevent.

%prep
%setup -q -n geventhttpclient-master
%patch1 -p0

%build
CFLAGS="$RPM_OPT_FLAGS" %{__python} setup.py build

%install
rm -rf %{buildroot}
%{__python} setup.py install -O1 --skip-build --root %{buildroot}

%check
%{__python} setup.py test

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
%doc 
%{python_sitearch}/geventhttpclient*


%changelog
* Wed Apr 24 2013 Paul Egan <paulegan@rockpack.com> - 1.1-1
- Initial release
