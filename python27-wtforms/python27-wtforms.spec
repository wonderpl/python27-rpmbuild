Name: python27-wtforms
Version: 2.0.1
Release: 1
Summary: A flexible forms validation and rendering library for python web development
Group: Development/Libraries
License: BSD
URL: http://wtforms.simplecodes.com/
Source0: http://pypi.python.org/packages/source/W/WTForms/WTForms-%{version}.zip

BuildRoot: %(mktemp -ud %{_tmppath}/%{name}-%{version}-%{release}-XXXXXX)
BuildArch: noarch
BuildRequires: python27-setuptools

%description
WTForms is a flexible forms validation and rendering library for python web
development.

For installation instructions, see INSTALL.txt.

To get started
using WTForms, we recommend reading the crash course on the
website:
http://wtforms.simplecodes.com/.

If you downloaded the package from PyPI,
there will be a prebuilt copy of the
html documentation in the `docs/html/`
directory. If not, you ...

%prep
%setup -q -n WTForms-%{version}

%build
%{__python} setup.py build

%install
rm -rf %{buildroot}
%{__python} setup.py install -O1 --skip-build --root %{buildroot}

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
%doc README.md LICENSE.txt
%{python_sitelib}/*

%changelog
* Fri Jan 11 2013 Paul Egan <paulegan@rockpack.com> - 1.0.2-1
- Initial release
