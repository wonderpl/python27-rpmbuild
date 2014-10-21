Name: python27-aniso8601
Version: 0.83
Release: 1
Summary: A library for parsing ISO 8601 strings
Group: Development/Libraries
License: GPLv3+
URL: https://bitbucket.org/nielsenb/aniso8601
Source0: https://pypi.python.org/packages/source/a/aniso8601/aniso8601-%{version}.tar.gz

BuildRoot: %(mktemp -ud %{_tmppath}/%{name}-%{version}-%{release}-XXXXXX)
BuildArch: noarch
BuildRequires: python27-setuptools

%description
* Pure Python implementation
* Python 3 support
* No extra dependencies
* UTC offset represented as fixed-offset tzinfo
* No regular expressions

%prep
%setup -q -n aniso8601-%{version}

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
%doc README.rst
%{python_sitelib}/aniso8601*

%changelog
* Tue Mar 18 2014 Paul Egan <paulegan@rockpack.com> - 0.82-1
- Initial release
