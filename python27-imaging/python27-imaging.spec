%global py_incdir %{_includedir}/python%{python_version}
%global py_libbuilddir %(%__python -c 'import sys; import sysconfig; print("lib.{p}-{v[0]}.{v[1]}".format(p=sysconfig.get_platform(), v=sys.version_info))')

Name: python27-imaging
Version: 2.4.0
Release: 1%{?dist}
Summary: Python image processing library
License: MIT
URL: http://python-imaging.github.com/Pillow/
Source0: https://github.com/python-imaging/Pillow/archive/%{version}.tar.gz
Patch0: test_render_multiline_hack.patch

BuildRoot: %(mktemp -ud %{_tmppath}/%{name}-%{version}-%{release}-XXXXXX)

BuildRequires: python27-setuptools
BuildRequires: libjpeg-devel, zlib-devel, freetype-devel, lcms-devel
BuildRequires: ghostscript

Requires: ghostscript

Provides: python27-pillow = %{version}-%{release}

%description
Python image processing library, fork of the Python Imaging Library (PIL)

This library provides extensive file format support, an efficient
internal representation, and powerful image processing capabilities.

%package devel
Summary: Development files for %{name}
Group: Development/Libraries
Requires: %{name}%{?_isa} = %{version}-%{release}
Requires: python2-devel >= %python_version
Requires: libjpeg-devel, zlib-devel

%description devel
Development files for %{name}.

%prep
%setup -q -n Pillow-%{version}
%patch0 -p0

%build
find -name '*.py' | xargs sed -i '1s|^#!.*python|#!%{__python}|'
CFLAGS="$RPM_OPT_FLAGS" %{__python} setup.py build

%install
rm -rf %{buildroot}

install -d %{buildroot}/%{py_incdir}/Imaging
install -m 644 libImaging/*.h %{buildroot}/%{py_incdir}/Imaging
%{__python} setup.py install -O1 --skip-build --root %{buildroot}

# The scripts are packaged in %%doc
rm -rf %{buildroot}%{_bindir}


%check
ln -s $PWD/Images $PWD/build/%py_libbuilddir/Images
cp -R $PWD/Tests $PWD/build/%py_libbuilddir/Tests
cp -R $PWD/selftest.py $PWD/build/%py_libbuilddir/selftest.py
pushd build/%py_libbuilddir
PYTHONPATH=$PWD/build/%py_libbuilddir %{__python} selftest.py
PYTHONPATH=$PWD/build/%py_libbuilddir %{__python} Tests/run.py
popd

%files
%defattr (-,root,root,-)
%doc README.rst CHANGES.rst docs/COPYING
%{python_sitearch}/*

%files devel
%defattr (0644,root,root,755)
%{py_incdir}/Imaging/

%changelog
* Tue May  6 2014 Paul Egan <paulegan@rockpack.com> - 2.4.0-1
- Moved to Pillow
