Name: python27-iso8601
Version: 0.1.4
Release: 1
Summary: Simple module to parse ISO 8601 dates
Group: Development/Libraries
License: MIT
URL: http://code.google.com/p/pyiso8601/
Source0: http://pypi.python.org/packages/source/i/iso8601/iso8601-%{version}.tar.gz

BuildRoot: %(mktemp -ud %{_tmppath}/%{name}-%{version}-%{release}-XXXXXX)
BuildArch: noarch
BuildRequires: python27-setuptools

%description
This module parses the most common forms of ISO 8601 date strings (e.g.
2007-01-14T20:34:22+00:00) into datetime objects.

%prep
%setup -q -n iso8601-%{version}

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
%doc LICENSE README
%{python_sitelib}/iso8601*

%changelog
* Fri Jan 11 2013 Paul Egan <paulegan@rockpack.com> - 0.1.4-1
- Initial release
