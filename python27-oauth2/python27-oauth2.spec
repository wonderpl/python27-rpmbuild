Name: python27-oauth2
Version: 1.5.211
Release: 1
Summary: Python support for improved oauth
Group: System Environment/Libraries
License: MIT
URL: http://pypi.python.org/pypi/oauth2/
Source0: http://pypi.python.org/packages/source/o/oauth2/oauth2-%{version}.tar.gz
Patch0: python-oauth2-multiple-GET-fix.patch

BuildRoot: %(mktemp -ud %{_tmppath}/%{name}-%{version}-%{release}-XXXXXX)
BuildArch: noarch
BuildRequires: python27-setuptools, python27-simplejson
Requires: python27-simplejson, python27-httplib2

%description
Oauth2 was originally forked from Leah Culver and Andy Smith's oauth.py 
code. Some of the tests come from a fork by Vic Fryzel, while a revamped 
Request class and more tests were merged in from Mark Paschal's fork. A 
number of notable differences exist between this code and its forefathers:

- 100% unit test coverage.
- The DataStore object has been completely ripped out. While creating unit 
  tests for the library I found several substantial bugs with the 
  implementation and confirmed with Andy Smith that it was never fully 
  baked.
- Classes are no longer prefixed with OAuth.
- The Request class now extends from dict.
- The library is likely no longer compatible with Python 2.3.
- The Client class works and extends from httplib2. It's a thin wrapper 
  that handles automatically signing any normal HTTP request you might 
  wish to make.

%prep
%setup -q -n oauth2-%{version}
%patch0 -p1 -b .multiple-GET-fix

%build
%{__python} setup.py build

%install
rm -rf %{buildroot}
%{__python} setup.py install -O1 --skip-build --root %{buildroot}
# Do not package the "tests"
rm -rf %{buildroot}%{python_sitelib}/tests/

%files
%doc PKG-INFO
%{python_sitelib}/oauth2*

%changelog
* Fri Mar  8 2013 Paul Egan <paulegan@rockpack.com> - 1.5.211-1
- Initial release
