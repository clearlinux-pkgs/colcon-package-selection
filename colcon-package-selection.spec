#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : colcon-package-selection
Version  : 0.2.1
Release  : 3
URL      : https://files.pythonhosted.org/packages/8f/56/a44e9c778905c2ed98101e8366460f9a4b5c13bad3aa0157627fe385dcc5/colcon-package-selection-0.2.1.tar.gz
Source0  : https://files.pythonhosted.org/packages/8f/56/a44e9c778905c2ed98101e8366460f9a4b5c13bad3aa0157627fe385dcc5/colcon-package-selection-0.2.1.tar.gz
Summary  : Extension for colcon to select the packages to process.
Group    : Development/Tools
License  : Apache-2.0
Requires: colcon-package-selection-python = %{version}-%{release}
Requires: colcon-package-selection-python3 = %{version}-%{release}
Requires: colcon-core
BuildRequires : buildreq-distutils3

%description
========================

%package python
Summary: python components for the colcon-package-selection package.
Group: Default
Requires: colcon-package-selection-python3 = %{version}-%{release}

%description python
python components for the colcon-package-selection package.


%package python3
Summary: python3 components for the colcon-package-selection package.
Group: Default
Requires: python3-core

%description python3
python3 components for the colcon-package-selection package.


%prep
%setup -q -n colcon-package-selection-0.2.1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1539915563
python3 setup.py build

%install
rm -rf %{buildroot}
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
