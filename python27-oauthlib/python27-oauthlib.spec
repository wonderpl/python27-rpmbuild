Name: python27-oauthlib
Version: 0.6.3
Release: 1
Summary: A generic, spec-compliant, thorough implementation of the OAuth request-signing logic
Group: Development/Libraries
License: BSD
URL: https://github.com/idan/oauthlib
Source0: https://pypi.python.org/packages/source/o/oauthlib/oauthlib-%{version}.tar.gz

BuildRoot: %(mktemp -ud %{_tmppath}/%{name}-%{version}-%{release}-XXXXXX)
BuildArch: noarch
BuildRequires: python27-setuptools

%description
OAuthLib is a generic utility which implements the logic of OAuth without
assuming a specific HTTP request object or web framework. Use it to graft OAuth
client support onto your favorite HTTP library, or provider support onto your
favourite web framework.

%prep
%setup -q -n oauthlib-%{version}

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
%{python_sitelib}/oauthlib*

%changelog
* Mon Jul 07 2014 Paul Egan <paulegan@rockpack.com> - 0.6.3-1
- Initial release
