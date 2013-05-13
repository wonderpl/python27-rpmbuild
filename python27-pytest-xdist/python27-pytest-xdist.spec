Name: python27-pytest-xdist
Version: 1.8
Release: 1
Summary: py.test xdist plugin for distributed testing and loop-on-failing modes
Group: Development/Libraries
License: GPL
URL: http://bitbucket.org/hpk42/pytest-xdist
Source0: http://pypi.python.org/packages/source/p/pytest-xdist/pytest-xdist-%{version}.zip

BuildRoot: %(mktemp -ud %{_tmppath}/%{name}-%{version}-%{release}-XXXXXX)
BuildArch: noarch
BuildRequires: python27-setuptools python27-execnet
Requires: python27-pytest python27-execnet

%description
The pytest-xdist plugin extends py.test with some unique test execution modes:

    test run parallelization: if you have multiple CPUs or hosts you can use
        those for a combined test run. This allows to speed up development or to use
        special resources of remote machines.
    --boxed: (not available on Windows) run each test in a boxed subprocess to
        survive SEGFAULTS or otherwise dying processes
    --looponfail: run your tests repeatedly in a subprocess. After each run
        py.test waits until a file in your project changes and then re-runs the
        previously failing tests. This is repeated until all tests pass after which
        again a full run is performed.
    Multi-Platform coverage: you can specify different Python interpreters or
        different platforms and run tests in parallel on all of them.

%prep
%setup -q -n pytest-xdist-%{version}

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
%doc README.txt LICENSE
%{python_sitelib}/*xdist*

%changelog
* Thu May 09 2013 Paul Egan <paulegan@rockpack.com> - 1.8-1
- Initial release
