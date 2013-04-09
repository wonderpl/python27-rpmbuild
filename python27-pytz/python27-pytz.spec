Name: python27-pytz
Version: 2013b
Release: 1
Summary: World timezone definitions, modern and historical
Group: Development/Libraries
License: MIT
URL: http://pytz.sourceforge.net
Source0: http://pypi.python.org/packages/source/p/pytz/pytz-%{version}.tar.bz2

BuildRoot: %(mktemp -ud %{_tmppath}/%{name}-%{version}-%{release}-XXXXXX)
BuildArch: noarch
BuildRequires: python27-setuptools

%description
pytz brings the Olson tz database into Python. This library allows accurate and
cross platform timezone calculations using Python 2.4 or higher. It also solves
the issue of ambiguous times at the end of daylight savings, which you can read
more about in the Python Library Reference (datetime.tzinfo).

%prep
%setup -q -n pytz-%{version}

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
%doc README.txt CHANGES.txt
%{python_sitelib}/pytz*

%changelog
* Mon Apr 08 2013 Paul Egan <paulegan@rockpack.com> - 2013b-1
- Initial release
