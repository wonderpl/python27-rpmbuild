Name: python27-psycogreen
Version: 1.0
Release: 1
Summary: psycopg2 integration with coroutine libraries
Group: Development/Libraries
License: BSD
URL: https://bitbucket.org/dvarrazzo/psycogreen
Source0: http://pypi.python.org/packages/source/p/psycogreen/psycogreen-%{version}.tar.gz

BuildRoot: %(mktemp -ud %{_tmppath}/%{name}-%{version}-%{release}-XXXXXX)
BuildArch: noarch
BuildRequires: python27-setuptools

%description
The psycogreen package enables psycopg2 to work with coroutine libraries,
using asynchronous calls internally but offering a blocking interface so that
regular code can run unmodified.

%prep
%setup -q -n psycogreen-%{version}

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
%{python_sitelib}/psycogreen*

%changelog
* Mon Apr 22 2013 Paul Egan <paulegan@rockpack.com> - 1.0-1
- Initial release
