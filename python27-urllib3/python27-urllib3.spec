Name: python27-urllib3
Version: 1.7.1
Release: 1
Summary: HTTP library with thread-safe connection pooling, file post, and more
Group: Development/Libraries
License: MIT
URL: http://urllib3.readthedocs.org/
Source0: http://pypi.python.org/packages/source/u/urllib3/urllib3-%{version}.tar.gz

BuildRoot: %(mktemp -ud %{_tmppath}/%{name}-%{version}-%{release}-XXXXXX)
BuildArch: noarch
BuildRequires: python27-setuptools

%description
Python HTTP library with thread-safe connection pooling, file post support,
sanity friendly, and more.

%prep
%setup -q -n urllib3-%{version}

%build
%{__python} setup.py build

%install
rm -rf %{buildroot}
%{__python} setup.py install -O1 --skip-build --root %{buildroot}

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
%doc README.rst LICENSE.txt
%{python_sitelib}/urllib3*
%{python_sitelib}/dummyserver

%changelog
* Tue Apr 23 2013 Paul Egan <paulegan@rockpack.com> - 1.5-1
- Initial release
