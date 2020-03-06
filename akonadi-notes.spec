#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0xDBD2CE893E2D1C87 (cfeck@kde.org)
#
Name     : akonadi-notes
Version  : 19.12.3
Release  : 19
URL      : https://download.kde.org/stable/release-service/19.12.3/src/akonadi-notes-19.12.3.tar.xz
Source0  : https://download.kde.org/stable/release-service/19.12.3/src/akonadi-notes-19.12.3.tar.xz
Source1  : https://download.kde.org/stable/release-service/19.12.3/src/akonadi-notes-19.12.3.tar.xz.sig
Summary  : Libraries and daemons to implement management of notes in Akonadi
Group    : Development/Tools
License  : BSD-2-Clause GPL-2.0 LGPL-2.1
Requires: akonadi-notes-lib = %{version}-%{release}
Requires: akonadi-notes-license = %{version}-%{release}
Requires: akonadi-notes-locales = %{version}-%{release}
BuildRequires : buildreq-cmake
BuildRequires : buildreq-kde
BuildRequires : kmime-dev

%description
# Akonadi Notes #
Akonadi Notes is a library that effectively bridges the type-agnostic API of
the Akonadi client libraries and the domain-specific KMime library. It provides
a helper class for note attachments and for wrapping notes into KMime::Message
objects.

%package dev
Summary: dev components for the akonadi-notes package.
Group: Development
Requires: akonadi-notes-lib = %{version}-%{release}
Provides: akonadi-notes-devel = %{version}-%{release}
Requires: akonadi-notes = %{version}-%{release}
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
%setup -q -n akonadi-notes-19.12.3
cd %{_builddir}/akonadi-notes-19.12.3

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1583457093
mkdir -p clr-build
pushd clr-build
# -Werror is for werrorists
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FCFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=4 "
%cmake ..
make  %{?_smp_mflags}  VERBOSE=1
popd

%install
export SOURCE_DATE_EPOCH=1583457093
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/akonadi-notes
cp %{_builddir}/akonadi-notes-19.12.3/COPYING %{buildroot}/usr/share/package-licenses/akonadi-notes/7c203dee3a03037da436df03c4b25b659c073976
cp %{_builddir}/akonadi-notes-19.12.3/COPYING.BSD %{buildroot}/usr/share/package-licenses/akonadi-notes/d0f83c8198fdd5464d2373015b7b64ce7cae607e
cp %{_builddir}/akonadi-notes-19.12.3/COPYING.LIB %{buildroot}/usr/share/package-licenses/akonadi-notes/9a1929f4700d2407c70b507b3b2aaf6226a9543c
pushd clr-build
%make_install
popd
%find_lang akonadinotes5

%files
%defattr(-,root,root,-)

%files dev
%defattr(-,root,root,-)
/usr/include/KF5/Akonadi/Notes/NoteUtils
/usr/include/KF5/akonadi-notes_version.h
/usr/include/KF5/akonadi/notes/NoteUtils
/usr/include/KF5/akonadi/notes/akonadi-notes_export.h
/usr/include/KF5/akonadi/notes/noteutils.h
/usr/lib64/cmake/KF5AkonadiNotes/KF5AkonadiNotesConfig.cmake
/usr/lib64/cmake/KF5AkonadiNotes/KF5AkonadiNotesConfigVersion.cmake
/usr/lib64/cmake/KF5AkonadiNotes/KF5AkonadiNotesTargets-relwithdebinfo.cmake
/usr/lib64/cmake/KF5AkonadiNotes/KF5AkonadiNotesTargets.cmake
/usr/lib64/libKF5AkonadiNotes.so
/usr/lib64/qt5/mkspecs/modules/qt_AkonadiNotes.pri

%files lib
%defattr(-,root,root,-)
/usr/lib64/libKF5AkonadiNotes.so.5
/usr/lib64/libKF5AkonadiNotes.so.5.13.3

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/akonadi-notes/7c203dee3a03037da436df03c4b25b659c073976
/usr/share/package-licenses/akonadi-notes/9a1929f4700d2407c70b507b3b2aaf6226a9543c
/usr/share/package-licenses/akonadi-notes/d0f83c8198fdd5464d2373015b7b64ce7cae607e

%files locales -f akonadinotes5.lang
%defattr(-,root,root,-)

