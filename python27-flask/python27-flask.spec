Name: python27-flask
Version: 0.10.1
Release: 2
Summary: A micro-framework for Python based on Werkzeug, Jinja 2 and good intentions
Group: Development/Libraries
License: BSD
URL: http://flask.pocoo.org/
Source0: http://pypi.python.org/packages/source/F/Flask/Flask-%{version}.tar.gz

BuildRoot: %(mktemp -ud %{_tmppath}/%{name}-%{version}-%{release}-XXXXXX)
BuildArch: noarch
BuildRequires: python27-setuptools python27-werkzeug
Requires: python27-werkzeug python27-jinja2 python27-itsdangerous

%description
Flask is called a “micro-framework” because the idea to keep the core
simple but extensible. There is no database abstraction layer, no form
validation or anything else where different libraries already exist
that can handle that. However Flask knows the concept of extensions
that can add this functionality into your application as if it was
implemented in Flask itself. There are currently extensions for object
relational mappers, form validation, upload handling, various open
authentication technologies and more.

%prep
%setup -q -n Flask-%{version}

%build
%{__python} setup.py build

%install
rm -rf %{buildroot}
%{__python} setup.py install -O1 --skip-build --root %{buildroot}

%check
#%{__python} setup.py test

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
%doc AUTHORS LICENSE PKG-INFO CHANGES README
%{python_sitelib}/*

%changelog
* Tue Oct 22 2013 Paul Egan <paulegan@rockpack.com> - 0.10.1-1
- Latest release

* Fri Jan 11 2013 Paul Egan <paulegan@rockpack.com> - 0.9-1
- Initial release
