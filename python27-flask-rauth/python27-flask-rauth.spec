Name: python27-flask-rauth
Version: 0.3.2
Release: 1
Summary: Adds OAuth 1.0/a, 2.0, and Ofly consumer support for Flask
Group: Development/Libraries
License: BSD
URL: https://github.com/joelverhagen/flask-rauth
Source0: http://pypi.python.org/packages/source/F/Flask-Rauth/Flask-Rauth-%{version}.tar.gz

BuildRoot: %(mktemp -ud %{_tmppath}/%{name}-%{version}-%{release}-XXXXXX)
BuildArch: noarch
BuildRequires: python27-setuptools python27-rauth
Requires: python27-flask python27-rauth

%description
Flask-Rauth is a Flask extensions that allows you to easily interact with
OAuth 2.0, OAuth 1.0a, and Ofly enabled applications. Please note that
Flask-Rauth is meant to only provide consumer support. This means that
Flask-Rauth will allow users on your Flask website to sign in to external
web services (i.e. the Twitter API, Facebook Graph API, GitHub, etc).

%prep
%setup -q -n Flask-Rauth-%{version}

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
%doc 
%{python_sitelib}/*

%changelog
* Tue Jan 15 2013 Paul Egan <paulegan@rockpack.com> - 0.3.2-1
- Initial release
