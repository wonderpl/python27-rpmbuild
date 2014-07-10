Name: python27-cffi
Version: 0.8.2
Release: 1%{?dist}
Summary: Foreign Function Interface for Python calling C code
Group: Development/Libraries
License: MIT
URL: http://cffi.readthedocs.org
Source0: https://pypi.python.org/packages/source/c/cffi/cffi-%{version}.tar.gz

BuildRoot: %(mktemp -ud %{_tmppath}/%{name}-%{version}-%{release}-XXXXXX)
BuildRequires: python27-setuptools python27-pycparser

%description
Foreign Function Interface for Python calling C code. The aim of this project
is to provide a convenient and reliable way of calling C code from Python. The
interface is based on LuaJIT’s FFI.

%prep
%setup -q -n cffi-%{version}

%build
CFLAGS="$RPM_OPT_FLAGS" %{__python} setup.py build

%install
rm -rf %{buildroot}
%{__python} setup.py install -O1 --skip-build --root %{buildroot}

%check
%{__python} setup.py test

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
%doc LICENSE
%{python_sitearch}/*

%changelog
* Thu Jul 03 2014 Paul Egan <paulegan@rockpack.com> - 0.8.2-1
- Initial release
