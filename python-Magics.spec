%global releaseno 1

Name:           python-Magics
Version:        1.5.6
Release:        1%{?dist}
Summary:        Python bindings for Magics

License:        Apache License, Version 2.0
URL:            https://pypi.org/project/Magics/
Source0:        https://files.pythonhosted.org/packages/source/M/Magics/Magics-%{version}.tar.gz#/python-Magics-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3-numpy
BuildRequires:  python3-pytest
BuildRequires:  python3-setuptools
BuildRequires:  Magics-devel


%description
Python bindings for Magics.


%package     -n python3-Magics
Summary:        Python3 bindings for Magics
Requires:       Magics

%description -n python3-Magics
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

%files -n python3-Magics
%doc README.rst
%{python3_sitelib}/*


%changelog
* Thu Mar 18 2021 Daniele Branchini <dbranchini@arpae.it> - 1.5.6-1
- Upstream update, dropped support for CentOS7

* Wed Feb 26 2020 Daniele Branchini <dbranchini@arpae.it> - 1.1.1-1
- Upstream update

* Mon Jun 10 2019 Emanuele Di Giacomo <edigiacomo@arpae.it> - 1.0.6-2
- Magics dependency

* Tue May 21 2019 Emanuele Di Giacomo <edigiacomo@arpae.it> - 1.0.6-1
- Initial package

