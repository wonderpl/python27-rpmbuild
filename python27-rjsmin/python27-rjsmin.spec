Name: python27-rjsmin
Version: 1.0.9
Release: 1%{?dist}
Summary: Javascript Minifier
Group: Development/Libraries
License: Apache License
URL: http://opensource.perlig.de/rjsmin/
Source0: https://pypi.python.org/packages/source/r/rjsmin/rjsmin-%{version}.tar.gz

BuildRoot: %(mktemp -ud %{_tmppath}/%{name}-%{version}-%{release}-XXXXXX)
BuildRequires: python27-setuptools

%description
rJSmin is a javascript minifier written in python. The minifier is based on
the semantics of jsmin.c by Douglas Crockford. The module is a
re-implementation aiming for speed, so it can be used at runtime (rather than
during a preprocessing step). Usually it produces the same results as the
original jsmin.c.

%prep
%setup -q -n rjsmin-%{version}

%build
CFLAGS="$RPM_OPT_FLAGS" %{__python} setup.py build

%install
rm -rf %{buildroot}
%{__python} setup.py install -O1 --skip-build --root %{buildroot}
rm -rf %{buildroot}%{_defaultdocdir}/rjsmin

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
%doc README.rst LICENSE
%{python_sitearch}/*rjsmin*

%changelog
* Wed Apr 30 2014 Paul Egan <paulegan@rockpack.com> - 1.0.9-1
- Initial release
