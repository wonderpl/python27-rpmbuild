Name: python27-numpy
Version: 1.9.0
Release: 1%{?dist}
Summary: NumPy: array processing for numbers, strings, records, and objects.
License: BSD
Group: Development/Libraries
Url: http://www.numpy.org/
Source0: http://downloads.sourceforge.net/numpy/numpy-%{version}.tar.gz

BuildRoot: %(mktemp -ud %{_tmppath}/%{name}-%{version}-%{release}-XXXXXX)
BuildRequires: python2-devel >= %python_version

%description
NumPy is a general-purpose array-processing package designed to
efficiently manipulate large multi-dimensional arrays of arbitrary
records without sacrificing too much speed for small multi-dimensional
arrays.  NumPy is built on the Numeric code base and adds features
introduced by numarray as well as an extended C-API and the ability to
create arrays of arbitrary type which also makes NumPy suitable for
interfacing with general-purpose data-base applications.

There are also basic facilities for discrete fourier transform,
basic linear algebra and random number generation.

%prep
%setup -n numpy-%{version}

%build
env CFLAGS="$RPM_OPT_FLAGS" %{__python} setup.py build

%install
rm -rf %{buildroot}
%{__python} setup.py install -O1 --root=%{buildroot}
mkdir -p %{buildroot}%{_includedir}
ln -s %{python_sitearch}/numpy/core/include/numpy/ %{buildroot}%{_includedir}/numpy
sed -e '1s,/usr/bin/env python.*,%{__python},' -i %{buildroot}%{_bindir}/*

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
%doc LICENSE.txt README.txt doc/release/* site.cfg.example
%{python_sitearch}/*
%{_bindir}/*
%{_includedir}/*

%changelog
* Fri Feb 14 2014 Paul Egan <paulegan@rockpack.com> - 1.8.0-1
- Bumped

* Fri Apr  5 2013 Paul Egan <paulegan@rockpack.com> - 1.7.0-1
- Initial release
