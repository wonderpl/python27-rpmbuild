Name: python27-itsdangerous
Version: 0.24
Release: 1
Summary: Various helpers to pass trusted data to untrusted environments
Group: Development/Libraries
License: BSD
URL: http://github.com/mitsuhiko/itsdangerous
Source0: http://pypi.python.org/packages/source/i/itsdangerous/itsdangerous-%{version}.tar.gz

BuildRoot: %(mktemp -ud %{_tmppath}/%{name}-%{version}-%{release}-XXXXXX)
BuildArch: noarch
BuildRequires: python27-setuptools

%description
Various helpers to pass data tountrusted environments and to get it backsafe and sound.

%prep
%setup -q -n itsdangerous-%{version}

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
%doc 
%{python_sitelib}/itsdangerous*

%changelog
* Tue Oct 22 2013 Paul Egan <paulegan@rockpack.com> - 0.23-1
- Latest release

* Mon Apr 08 2013 Paul Egan <paulegan@rockpack.com> - 0.17-1
- Initial release
