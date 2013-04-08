Name: python27-mechanize
Version: 0.2.5
Release: 1
Summary: Stateful programmatic web browsing
Group: Development/Libraries
License: BSD and ZPL
URL: http://wwwsearch.sourceforge.net/mechanize/
Source0: http://pypi.python.org/packages/source/m/mechanize/mechanize-%{version}.tar.gz

BuildRoot: %(mktemp -ud %{_tmppath}/%{name}-%{version}-%{release}-XXXXXX)
BuildArch: noarch
BuildRequires: python27-setuptools

%description
Stateful programmatic web browsing, after Andy Lester's Perl module
WWW::Mechanize.

mechanize.Browser implements the urllib2.OpenerDirector interface.  Browser
objects have state, including navigation history, HTML form state, cookies,
etc.  The set of features and URL schemes handled by Browser objects is
configurable.

%prep
%setup -q -n mechanize-%{version}

%build
%{__python} setup.py build

%install
rm -rf %{buildroot}
%{__python} setup.py install -O1 --skip-build --root %{buildroot}

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
%doc README.txt COPYING.txt
%{python_sitelib}/mechanize*

%changelog
* Thu Apr 04 2013 Paul Egan <paulegan@rockpack.com> - 0.2.5-1
- Initial release
