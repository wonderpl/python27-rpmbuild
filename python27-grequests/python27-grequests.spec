Name: python27-grequests
Version: 0.2.0
Release: 1
Summary: Requests + Gevent
Group: Development/Libraries
License: BSD
URL: https://github.com/kennethreitz/grequests
Source0: http://pypi.python.org/packages/source/g/grequests/grequests-%{version}.tar.gz

BuildRoot: %(mktemp -ud %{_tmppath}/%{name}-%{version}-%{release}-XXXXXX)
BuildArch: noarch
BuildRequires: python27-setuptools
Requires: python27-requests python27-gevent

%description
GRequests allows you to use Requests with Gevent to make asyncronous HTTP
Requests easily.

%prep
%setup -q -n grequests-%{version}

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
%{python_sitelib}/grequests*

%changelog
* Mon Apr 22 2013 Paul Egan <paulegan@rockpack.com> - 0.2.0-1
- Initial release
