#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0xBB463350D6EF31EF (heiko@shruuf.de)
#
Name     : akonadi-notes
Version  : 22.12.2
Release  : 49
URL      : https://download.kde.org/stable/release-service/22.12.2/src/akonadi-notes-22.12.2.tar.xz
Source0  : https://download.kde.org/stable/release-service/22.12.2/src/akonadi-notes-22.12.2.tar.xz
Source1  : https://download.kde.org/stable/release-service/22.12.2/src/akonadi-notes-22.12.2.tar.xz.sig
Summary  : No detailed summary available
Group    : Development/Tools
License  : BSD-3-Clause CC0-1.0 LGPL-2.0
Requires: akonadi-notes-lib = %{version}-%{release}
Requires: akonadi-notes-license = %{version}-%{release}
Requires: akonadi-notes-locales = %{version}-%{release}
BuildRequires : buildreq-cmake
BuildRequires : buildreq-kde
BuildRequires : extra-cmake-modules-data
BuildRequires : ki18n-dev
BuildRequires : kmime-dev
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
SPDX-License-Identifier: CC0-1.0

%package dev
Summary: dev components for the akonadi-notes package.
Group: Development
Requires: akonadi-notes-lib = %{version}-%{release}
Provides: akonadi-notes-devel = %{version}-%{release}
Requires: akonadi-notes = %{version}-%{release}

%description dev
dev components for the akonadi-notes package.


%package lib
Summary: lib components for the akonadi-notes package.
Group: Libraries
Requires: akonadi-notes-license = %{version}-%{release}

%description lib
lib components for the akonadi-notes package.


%package license
Summary: license components for the akonadi-notes package.
Group: Default

%description license
license components for the akonadi-notes package.


%package locales
Summary: locales components for the akonadi-notes package.
Group: Default

%description locales
locales components for the akonadi-notes package.


%prep
%setup -q -n akonadi-notes-22.12.2
cd %{_builddir}/akonadi-notes-22.12.2

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1675656592
mkdir -p clr-build
pushd clr-build
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz "
export FCFLAGS="$FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz "
export FFLAGS="$FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz "
export CXXFLAGS="$CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz "
%cmake ..
make  %{?_smp_mflags}
popd

%install
export SOURCE_DATE_EPOCH=1675656592
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/akonadi-notes
cp %{_builddir}/akonadi-notes-%{version}/.codespellrc.license %{buildroot}/usr/share/package-licenses/akonadi-notes/c011fda7746c087a127999da1c4044854ee42238 || :
cp %{_builddir}/akonadi-notes-%{version}/CMakePresets.json.license %{buildroot}/usr/share/package-licenses/akonadi-notes/c085897bc39e05746ffd2d889a6e84ff1b7ae2d9 || :
cp %{_builddir}/akonadi-notes-%{version}/LICENSES/BSD-3-Clause.txt %{buildroot}/usr/share/package-licenses/akonadi-notes/9950d3fdce1cff1f71212fb5abd31453c6ee2f8c || :
cp %{_builddir}/akonadi-notes-%{version}/LICENSES/CC0-1.0.txt %{buildroot}/usr/share/package-licenses/akonadi-notes/8287b608d3fa40ef401339fd907ca1260c964123 || :
cp %{_builddir}/akonadi-notes-%{version}/LICENSES/LGPL-2.0-or-later.txt %{buildroot}/usr/share/package-licenses/akonadi-notes/20079e8f79713dce80ab09774505773c926afa2a || :
cp %{_builddir}/akonadi-notes-%{version}/README.md.license %{buildroot}/usr/share/package-licenses/akonadi-notes/cadc9e08cb956c041f87922de84b9206d9bbffb2 || :
cp %{_builddir}/akonadi-notes-%{version}/metainfo.yaml.license %{buildroot}/usr/share/package-licenses/akonadi-notes/7ff5a7dd2c915b2b34329c892e06917c5f82f3a4 || :
pushd clr-build
%make_install
popd
%find_lang akonadinotes5

%files
%defattr(-,root,root,-)

%files dev
%defattr(-,root,root,-)
/usr/include/KF5/AkonadiNotes/Akonadi/NoteUtils
/usr/include/KF5/AkonadiNotes/akonadi-notes_version.h
/usr/include/KF5/AkonadiNotes/akonadi/NoteUtils
/usr/include/KF5/AkonadiNotes/akonadi/akonadi-notes_export.h
/usr/include/KF5/AkonadiNotes/akonadi/noteutils.h
/usr/lib64/cmake/KF5AkonadiNotes/KF5AkonadiNotesConfig.cmake
/usr/lib64/cmake/KF5AkonadiNotes/KF5AkonadiNotesConfigVersion.cmake
/usr/lib64/cmake/KF5AkonadiNotes/KF5AkonadiNotesTargets-relwithdebinfo.cmake
/usr/lib64/cmake/KF5AkonadiNotes/KF5AkonadiNotesTargets.cmake
/usr/lib64/libKF5AkonadiNotes.so
/usr/lib64/qt5/mkspecs/modules/qt_AkonadiNotes.pri

%files lib
%defattr(-,root,root,-)
/usr/lib64/libKF5AkonadiNotes.so.5
/usr/lib64/libKF5AkonadiNotes.so.5.22.2

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/akonadi-notes/20079e8f79713dce80ab09774505773c926afa2a
/usr/share/package-licenses/akonadi-notes/7ff5a7dd2c915b2b34329c892e06917c5f82f3a4
/usr/share/package-licenses/akonadi-notes/8287b608d3fa40ef401339fd907ca1260c964123
/usr/share/package-licenses/akonadi-notes/9950d3fdce1cff1f71212fb5abd31453c6ee2f8c
/usr/share/package-licenses/akonadi-notes/c011fda7746c087a127999da1c4044854ee42238
/usr/share/package-licenses/akonadi-notes/c085897bc39e05746ffd2d889a6e84ff1b7ae2d9
/usr/share/package-licenses/akonadi-notes/cadc9e08cb956c041f87922de84b9206d9bbffb2

%files locales -f akonadinotes5.lang
%defattr(-,root,root,-)

