Name: python27-raven
Version: 4.0.4
Release: 1
Summary: Raven is a client for Sentry
Group: Development/Libraries
License: MIT
URL: http://github.com/getsentry/raven-python
Source0: http://pypi.python.org/packages/source/r/raven/raven-%{version}.tar.gz

BuildArch: noarch
BuildRoot: %(mktemp -ud %{_tmppath}/%{name}-%{version}-%{release}-XXXXXX)
BuildRequires: python27-setuptools
Requires: python27-simplejson, python27-blinker

%description
Raven is a Python client for Sentry. It provides full out-of-the-box support
for many of the popular frameworks, including Django, and Flask. Raven also
includes drop-in support for any WSGI-compatible web application.

%prep
%setup -q -n raven-%{version}

%build
%{__python} setup.py build

%install
rm -rf %{buildroot}
%{__python} setup.py install -O1 --skip-build --root %{buildroot}

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
%doc README.rst LICENSE PKG-INFO
%{python_sitelib}/*
%{_bindir}/raven

%changelog
* Fri Feb 14 2014 Paul Egan <paulegan@rockpack.com> - 4.0.4-1
- Bumped

* Sat Aug 17 2013 Paul Egan <paulegan@rockpack.com> - 3.1.17-3
- Added patch for logging level

* Mon Mar 18 2013 Paul Egan <paulegan@rockpack.com> - 3.1.17-1
- Initial release
