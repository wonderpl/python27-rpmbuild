Name: python27-cython
Version: 0.19
Release: 1%{?dist}
Summary: A language for writing Python extension modules
Group: Development/Tools
License: Python
URL: http://www.cython.org
Source0: http://pypi.python.org/packages/source/C/Cython/Cython-%{version}.tar.gz

BuildRoot: %(mktemp -ud %{_tmppath}/%{name}-%{version}-%{release}-XXXXXX)
BuildRequires: python27-setuptools

%description
The Cython language makes writing C extensions for the Python language as
easy as Python itself.  Cython is a source code translator based on the
well-known Pyrex, but supports more cutting edge functionality and
optimizations.

%prep
%setup -q -n Cython-%{version}

%build
CFLAGS="$RPM_OPT_FLAGS" %{__python} setup.py build

%install
rm -rf %{buildroot}
%{__python} setup.py install -O1 --skip-build --root %{buildroot}
find -name '*.py' | xargs sed -i '1s|^#!.*python|#!%{__python}|'

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
%doc *.txt Demos Doc Tools
%{python_sitearch}/*
%{_bindir}/*

%changelog
* Mon Apr 22 2013 Paul Egan <paulegan@rockpack.com> - 0.19-1
- Initial release
