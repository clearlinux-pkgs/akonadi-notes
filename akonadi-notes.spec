#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0xDBD2CE893E2D1C87 (cfeck@kde.org)
#
Name     : akonadi-notes
Version  : 19.04.0
Release  : 5
URL      : https://download.kde.org/stable/applications/19.04.0/src/akonadi-notes-19.04.0.tar.xz
Source0  : https://download.kde.org/stable/applications/19.04.0/src/akonadi-notes-19.04.0.tar.xz
Source99 : https://download.kde.org/stable/applications/19.04.0/src/akonadi-notes-19.04.0.tar.xz.sig
Summary  : Libraries and daemons to implement management of notes in Akonadi
Group    : Development/Tools
License  : BSD-2-Clause GPL-2.0 LGPL-2.1
Requires: akonadi-notes-lib = %{version}-%{release}
Requires: akonadi-notes-license = %{version}-%{release}
Requires: akonadi-notes-locales = %{version}-%{release}
BuildRequires : akonadi-dev
BuildRequires : boost-dev
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
%setup -q -n akonadi-notes-19.04.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1555679891
mkdir -p clr-build
pushd clr-build
%cmake ..
make  %{?_smp_mflags}
popd

%install
export SOURCE_DATE_EPOCH=1555679891
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/akonadi-notes
cp COPYING %{buildroot}/usr/share/package-licenses/akonadi-notes/COPYING
cp COPYING.BSD %{buildroot}/usr/share/package-licenses/akonadi-notes/COPYING.BSD
cp COPYING.LIB %{buildroot}/usr/share/package-licenses/akonadi-notes/COPYING.LIB
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
/usr/lib64/libKF5AkonadiNotes.so.5.11.0

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/akonadi-notes/COPYING
/usr/share/package-licenses/akonadi-notes/COPYING.BSD
/usr/share/package-licenses/akonadi-notes/COPYING.LIB

%files locales -f akonadinotes5.lang
%defattr(-,root,root,-)

