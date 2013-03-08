Name: python27-twitter
Version: 0.8.7
Release: 1
Summary: A Python wrapper around the Twitter API
Group: Development/Libraries
License: ASL
URL: https://github.com/bear/python-twitter
Source0: http://pypi.python.org/packages/source/p/python-twitter/python-twitter-%{version}.tar.gz

BuildRoot: %(mktemp -ud %{_tmppath}/%{name}-%{version}-%{release}-XXXXXX)
BuildArch: noarch
BuildRequires: python27-setuptools
Requires: python27-simplejson python27-oauth2

%description
A Python wrapper around the Twitter API.

%prep
%setup -q -n python-twitter-%{version}

%build
%{__python} setup.py build

%install
rm -rf %{buildroot}
%{__python} setup.py install -O1 --skip-build --root %{buildroot}

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
%doc README.md LICENSE
%{python_sitelib}/*

%changelog
* Fri Mar 08 2013 Paul Egan <paulegan@rockpack.com> - 0.8.7-1
- Initial release
