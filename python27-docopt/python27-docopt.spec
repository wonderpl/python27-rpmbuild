Name: python27-docopt
Version: 0.6.1
Release: 1
Summary: Pythonic argument parser, that will make you smile
Group: Development/Libraries
License: MIT
URL: http://docopt.org
Source0: https://pypi.python.org/packages/source/d/docopt/docopt-%{version}.tar.gz

BuildRoot: %(mktemp -ud %{_tmppath}/%{name}-%{version}-%{release}-XXXXXX)
BuildArch: noarch
BuildRequires: python27-setuptools

%description
docopt creates *beautiful* command-line interfaces

%prep
%setup -q -n docopt-%{version}

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
%doc README.rst LICENSE-MIT
%{python_sitelib}/docopt*

%changelog
* Wed Mar 19 2014 Paul Egan <paulegan@rockpack.com> - 0.6.1-1
- Initial release
