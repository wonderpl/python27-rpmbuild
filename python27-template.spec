{%- set pv_suffix = '27' -%}
Name: {{ 'python-'|name_for_python_version(pv_suffix) }}{{ data.name|lower }}
Version: {{ data.version }}
Release: 1{% if data.has_extension %}%{?dist}{% endif %}
Summary: {{ data.summary }}
Group: Development/Libraries
License: {{ data.license }}
URL: {{ data.home_page }}
Source0: {{ data.url|replace(data.version, '%{version}') }}

BuildRoot: %(mktemp -ud %{_tmppath}/%{name}-%{version}-%{release}-XXXXXX)
{%- if not data.has_extension %}
BuildArch: noarch
{%- endif %}
{%- for dep in [('BuildRequires', 'setuptools')] + data.build_deps + data.runtime_deps %}
{{ dep[0] }}: {{ dep[1]|name_for_python_version(pv_suffix)|lower }}
{%- endfor %}

%description
{{ data.description|truncate(400)|wordwrap }}

%prep
%setup -q -n {{ data.name }}-%{version}

%build
{% if data.has_extension %}CFLAGS="$RPM_OPT_FLAGS" {% endif %}%{__python} setup.py build

%install
rm -rf %{buildroot}
%{__python} setup.py install -O1 --skip-build --root %{buildroot}

%check
%{__python} setup.py test

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
%doc {{ data.doc_files|join(' ') }}
{%- if data.has_extension %}
%{python_sitearch}/{{ data.underscored_name }}*
{% else %}
%{python_sitelib}/{{ data.underscored_name }}*
{%- endif %}
{%- if data.scripts %}
%{_bindir}/*
{%- endif %}

%changelog
* {{ data.changelog_date_packager }} - {{ data.version }}-1
- Initial release
