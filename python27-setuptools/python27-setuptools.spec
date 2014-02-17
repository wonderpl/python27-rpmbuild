Name: python27-setuptools
Version: 0.6.49
Release: 1
Summary: Easily download, build, install, upgrade, and uninstall Python packages
Group: Applications/System
License: Python or ZPLv2.0
URL: http://pypi.python.org/pypi/distribute
Source0: http://pypi.python.org/packages/source/d/distribute/distribute-%{version}.tar.gz

BuildRoot: %(mktemp -ud %{_tmppath}/%{name}-%{version}-%{release}-XXXXXX)
BuildArch: noarch
BuildRequires: python2-devel >= %python_version

%if 0%{?fedora} > 16
Provides: python-setuptools
Obsoletes: python-setuptools
%endif

%description
Setuptools is a collection of enhancements to the Python distutils that allow
you to more easily build and distribute Python packages, especially ones that
have dependencies on other packages.

%prep
%setup -q -n distribute-%{version}
find . -name '*.py' -print0 | xargs -0 sed -i '1s|^#!.*python$|#!%{__python}|'

%build
CFLAGS="$RPM_OPT_FLAGS" %{__python} setup.py build

%install
rm -rf %{buildroot}
%{__python} setup.py install -O1 --skip-build --root %{buildroot}
rm -rf %{buildroot}%{python_sitelib}/setuptools/tests
find %{buildroot}%{python_sitelib} -name '*.exe' -delete

%check
%{__python} setup.py test

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
%doc *.txt docs
%{_bindir}/*
%exclude %{_bindir}/easy_install
%{python_sitelib}/*

%changelog
* Thu Feb 13 2014 Paul Egan <paulegan@rockpack.com> - 0.6.49-1
- Bumped

* Wed Jan  2 2013 Paul Egan <paulegan@rockpack.com> - 0.6.34-1
- Initial release

