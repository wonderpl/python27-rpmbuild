Name: python27-webassets
Version: 0.9
Release: 1
Summary: Media asset management for Python, with glue code for various web frameworks
Group: Development/Libraries
License: BSD
URL: http://github.com/miracle2k/webassets/
Source0: http://pypi.python.org/packages/source/w/webassets/webassets-%{version}.tar.gz

BuildRoot: %(mktemp -ud %{_tmppath}/%{name}-%{version}-%{release}-XXXXXX)
BuildArch: noarch
BuildRequires: python27-setuptools
Requires: python27-pyyaml

%description
Merges, minifies and compresses Javascript and CSS files, supporting a variety
of different filters, including YUI, jsmin, jspacker or CSS tidy. Also supports
URL rewriting in CSS files.

%prep
%setup -q -n webassets-%{version}

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
%doc README.rst LICENSE
%{python_sitelib}/webassets*
%{_bindir}/*

%changelog
* Tue Mar 19 2013 Paul Egan <paulegan@rockpack.com> - 0.8-1
- Initial release
