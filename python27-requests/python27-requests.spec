Name: python27-requests
Version: 2.4.3
Release: 1
Summary: Python HTTP for Humans
Group: Development/Libraries
License: ASL
URL: http://python-requests.org
Source0: http://pypi.python.org/packages/source/r/requests/requests-%{version}.tar.gz

BuildRoot: %(mktemp -ud %{_tmppath}/%{name}-%{version}-%{release}-XXXXXX)
BuildArch: noarch
BuildRequires: python27-setuptools

%description
Requests is an Apache2 Licensed HTTP library, written in Python, for human
beings.

Python’s standard urllib2 module provides most of the HTTP capabilities you
need, but the API is thoroughly broken. It was built for a different time -
and a different web. It requires an enormous amount of work (even method
overrides) to perform the simplest of tasks.

%prep
%setup -q -n requests-%{version}

%build
%{__python} setup.py build

%install
rm -rf %{buildroot}
%{__python} setup.py install -O1 --skip-build --root %{buildroot}

%check
%{__python} setup.py test

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
%doc README.rst LICENSE
%{python_sitelib}/requests*

%changelog
* Fri Feb 14 2014 Paul Egan <paulegan@rockpack.com> - 2.2.1-1
- Upgraded to v2

* Thu Aug 29 2013 Paul Egan <paulegan@rockpack.com> - 1.2.3-1
- Bumped to latest

* Mon Jan 14 2013 Paul Egan <paulegan@rockpack.com> - 1.1.0-1
- Initial release
