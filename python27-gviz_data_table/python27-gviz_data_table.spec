Name: python27-gviz_data_table
Version: 1.0.1
Release: 1
Summary: Python API for Google Visualization
Group: Development/Libraries
License: BSD
URL: https://bitbucket.org/charlie_x/gviz-data-table
Source0: https://pypi.python.org/packages/source/g/gviz_data_table/gviz_data_table-%{version}.tar.gz
Patch1: types.patch

BuildRoot: %(mktemp -ud %{_tmppath}/%{name}-%{version}-%{release}-XXXXXX)
BuildArch: noarch
BuildRequires: python27-setuptools
#BuildRequires: python27-sphinx

%description
Gviz Data Table is a simple Python library for converting Python data types
to the Google Visualization Data Table JSON format.

The Google Visualization Library itself is a Javascript library that provides
interactive charts that work in pretty much any browser. The libraries cover
most use cases including tables as well as charts, so you can have a chart
and a table of the same data.

%prep
%setup -q -n gviz_data_table-%{version}
%patch1 -p0

%build
%{__python} setup.py build

%install
rm -rf %{buildroot}
%{__python} setup.py install -O1 --skip-build --root %{buildroot}
rm -rf %{buildroot}%{python_sitelib}/{docs,examples}
rm -rf %{buildroot}%{python_sitelib}/gviz_data_table/tests

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
%doc README.rst examples
%{python_sitelib}/gviz_data_table*

%changelog
* Thu Aug 22 2013 Paul Egan <paulegan@rockpack.com> - 1.0.1-1
- Initial release
