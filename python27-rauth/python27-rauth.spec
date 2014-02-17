Name: python27-rauth
Version: 0.6.2
Release: 1
Summary: A Python library for OAuth 1.0/a, 2.0, and Ofly
Group: Development/Libraries
License: MIT
URL: https://github.com/litl/rauth
Source0: http://pypi.python.org/packages/source/r/rauth/rauth-%{version}.tar.gz

BuildRoot: %(mktemp -ud %{_tmppath}/%{name}-%{version}-%{release}-XXXXXX)
BuildArch: noarch
BuildRequires: python27-setuptools
Requires: python27-requests

%description
Rauth is a package that delivers client support for OAuth 1.0/a, 2.0,
and Ofly. It is built on top of the superb Python Requests.

%prep
%setup -q -n rauth-%{version}

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
%{python_sitelib}/rauth*

%changelog
* Tue Jan 15 2013 Paul Egan <paulegan@rockpack.com> - 0.4.17-1
- Initial release
