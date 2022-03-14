%global releaseno 3

Name:           python-Magics
Version:        1.5.7
Release:        %{releaseno}%{?dist}
Summary:        Python bindings for Magics

License:        Apache License, Version 2.0
URL:            https://pypi.org/project/Magics/
Source0:        https://files.pythonhosted.org/packages/source/M/Magics/Magics-%{version}.tar.gz#/python-Magics-%{version}.tar.gz
# see: https://github.com/ARPA-SIMC/python-Magics-rpm/issues/1
Patch1:         https://github.com/arpa-simc/python-Magics-rpm/raw/v%{version}-%{releaseno}/python-Magics-disable-findlibs.patch
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
%autosetup -n Magics-%{version} -p0

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
* Mon Mar 14 2022 Emanuele Di Giacomo <edigiacomo@arpae.it> - 1.5.7-3
- Fixed Patch1 URL

* Mon Mar 14 2022 Emanuele Di Giacomo <edigiacomo@arpae.it> - 1.5.7-2
- Remove findlibs dependency (#1)

* Fri Mar 11 2022 Daniele Branchini <dbranchini@arpae.it> - 1.5.7-1
- Upstream update

* Thu Mar 18 2021 Daniele Branchini <dbranchini@arpae.it> - 1.5.6-1
- Upstream update, dropped support for CentOS7

* Wed Feb 26 2020 Daniele Branchini <dbranchini@arpae.it> - 1.1.1-1
- Upstream update

* Mon Jun 10 2019 Emanuele Di Giacomo <edigiacomo@arpae.it> - 1.0.6-2
- Magics dependency

* Tue May 21 2019 Emanuele Di Giacomo <edigiacomo@arpae.it> - 1.0.6-1
- Initial package
