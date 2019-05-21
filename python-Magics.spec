%if 0%{?rhel} == 7
%define python3_vers python36
%else
%define python3_vers python3
%endif

%global releaseno 1

Name:           python-Magics
Version:        1.0.6
Release:        1%{?dist}
Summary:        Python bindings for Magics

License:        Apache License, Version 2.0
URL:            https://pypi.org/project/Magics/
Source0:        https://files.pythonhosted.org/packages/source/M/Magics/Magics-%{version}.tar.gz#/python-Magics-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  %{python3_vers}-devel
BuildRequires:  %{python3_vers}-numpy
BuildRequires:  %{python3_vers}-pytest
BuildRequires:  %{python3_vers}-setuptools
BuildRequires:  Magics-devel

%description
Python bindings for Magics.


%package     -n %{python3_vers}-Magics
Summary:        Python3 bindings for Magics

%description -n %{python3_vers}-Magics
Python3 bindings for Magics.


%prep
%autosetup -n Magics-%{version}

%build
%py3_build

%install
%py3_install

%check
# TODO: it seems that the tests are missing
# %{__python3} setup.py test

%files -n %{python3_vers}-Magics
%doc README.rst
%{python3_sitelib}/*


%changelog
* Tue May 21 2019 Emanuele Di Giacomo <edigiacomo@arpae.it>
- Initial package

