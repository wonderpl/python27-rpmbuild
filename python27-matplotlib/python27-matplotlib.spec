Name: python27-matplotlib
Version: 1.2.1
Release: 1%{?dist}
Summary: Python plotting package
Group: Development/Libraries
License: Python
URL: http://matplotlib.org
Source0: https://downloads.sourceforge.net/project/matplotlib/matplotlib/matplotlib-%{version}/matplotlib-%{version}.tar.gz

BuildRoot: %(mktemp -ud %{_tmppath}/%{name}-%{version}-%{release}-XXXXXX)
BuildRequires: python27-setuptools python27-numpy python27-pytz
BuildRequires: freetype-devel, libpng-devel, zlib-devel
Requires: python27-numpy python27-pytz

%description
Matplotlib is a python 2D plotting library which produces publication
quality figures in a variety of hardcopy formats and interactive
environments across platforms. matplotlib can be used in python
scripts, the python and ipython shell, web application servers, and
six graphical user interface toolkits.

Matplotlib tries to make easy things easy and hard things possible.
You can generate plots, histograms, power spectra, bar charts,
errorcharts, scatterplots, etc, with just a few lines of code.

%prep
%setup -q -n matplotlib-%{version}

%build
CFLAGS="$RPM_OPT_FLAGS" %{__python} setup.py build

%install
rm -rf %{buildroot}
%{__python} setup.py install -O1 --skip-build --root %{buildroot}

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
%doc README.txt examples/ doc/
%{python_sitearch}/*

%changelog
* Fri Apr 05 2013 Paul Egan <paulegan@rockpack.com> - 1.2.1-1
- Initial release
