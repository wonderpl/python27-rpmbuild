Name: python27-pyp2rpm
Version: 1.1.1
Release: 1
Summary: Convert Python packages to RPM SPECFILES
Group: Development/Libraries
License: MIT
URL: https://bitbucket.org/bkabrda/pyp2rpm/
Source0: http://pypi.python.org/packages/source/p/pyp2rpm/pyp2rpm-%{version}.tar.gz

BuildRoot: %(mktemp -ud %{_tmppath}/%{name}-%{version}-%{release}-XXXXXX)
BuildArch: noarch
BuildRequires: python27-setuptools
Requires: python27-jinja2

%description
Convert Python packages to RPM SPECFILES. The packages can be downloaded from
PyPI and the produced SPEC is in line with Fedora Packaging Guidelines or
Mageia Python Policy.

Users can provide their own templates for rendering the package metadata.
Both the package source and metadata can be extracted from PyPI or from local
filesystem (local file doesn't provide that much information though).

%prep
%setup -q -n pyp2rpm-%{version}

%build
%{__python} setup.py build

%install
rm -rf %{buildroot}
%{__python} setup.py install -O1 --skip-build --root %{buildroot}

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
%doc README.rst LICENSE
%{python_sitelib}/*
%{_bindir}/pyp2rpm

%changelog
* Fri Jan 11 2013 Paul Egan <paulegan@rockpack.com> - 1.0.1-1
- Initial release
