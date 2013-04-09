Name: python27-pycairo
Version: 1.8.8
Release: 1%{?dist}
License: MPLv1.1 or LGPLv2
Group: Development/Languages
Summary: Python bindings for the cairo library
URL: http://cairographics.org/pycairo
Source: http://cairographics.org/releases/pycairo-%{version}.tar.gz

BuildRequires: cairo-devel
BuildRequires: pkgconfig
BuildRequires: python2-devel >= %python_version

%description
Python bindings for the cairo library.

%package devel
Summary: Libraries and headers for pycairo
Group: Development/Libraries
Requires: %{name} = %{version}-%{release}
Requires: cairo-devel
Requires: pkgconfig
Requires: python2-devel >= %python_version

%description devel
This package contains files required to build wrappers for cairo add-on
libraries so that they interoperate with pycairo.

%prep
%setup -q -n pycairo-%{version}

%build
export PYTHON=%{__python}
%configure
make %{?_smp_mflags}

%install
make DESTDIR=%{buildroot} install
find %{buildroot} -name '*.la' | xargs rm -f

%files
%defattr(-,root,root,-)
%doc AUTHORS COPYING* INSTALL NEWS README
%doc examples doc/faq.rst doc/overview.rst doc/README
%{python_sitearch}/cairo/

%files devel
%defattr(-,root,root,-)
%{_includedir}/pycairo/
%{_libdir}/pkgconfig/pycairo.pc
