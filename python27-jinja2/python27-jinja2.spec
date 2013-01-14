Name: python27-jinja2
Version: 2.6
Release: 1%{?dist}
Summary: General purpose template engine
Group: Development/Libraries
License: BSD
URL: http://jinja.pocoo.org/
Source0: http://pypi.python.org/packages/source/J/Jinja2/Jinja2-%{version}.tar.gz

BuildRoot: %(mktemp -ud %{_tmppath}/%{name}-%{version}-%{release}-XXXXXX)
BuildArch: noarch
BuildRequires: python27-setuptools
Requires: python27-markupsafe

%description
Jinja2 is a template engine written in pure Python.  It provides a
Django inspired non-XML syntax but supports inline expressions and an
optional sandboxed environment.

If you have any exposure to other text-based template languages, such
as Smarty or Django, you should feel right at home with Jinja2. It's
both designer and developer friendly by sticking to Python's
principles and adding functionality useful for templating
environments.

%prep
%setup -q -n Jinja2-%{version}

%build
%{__python} setup.py build

%install
rm -rf %{buildroot}
%{__python} setup.py install -O1 --skip-build --root %{buildroot}
rm %{buildroot}/%{python_sitelib}/jinja2/*.c

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
%doc AUTHORS CHANGES LICENSE
%{python_sitelib}/*

%changelog
* Fri Jan 11 2013 Paul Egan <paulegan@rockpack.com> - 2.6-1
- Initial release
