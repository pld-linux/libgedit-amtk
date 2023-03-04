#
# Conditional build:
%bcond_without	static_libs	# don't build static libraries
#
Summary:	Amtk - Actions, Menus and Toolbars Kit for GTK+ applications
Summary(pl.UTF-8):	Amtk - zestaw akcji, menu i pasków narzędzi dla aplikacji GTK+
Name:		amtk
Version:	5.6.1
Release:	1
License:	LGPL v3+
Group:		Libraries
Source0:	https://download.gnome.org/sources/amtk/5.6/%{name}-%{version}.tar.xz
# Source0-md5:	26edf5c301e66a02f0ea7829855807f5
URL:		https://wiki.gnome.org/Projects/Amtk
BuildRequires:	gettext-tools >= 0.19.6
BuildRequires:	glib2-devel >= 1:2.56
BuildRequires:	gobject-introspection-devel >= 1.42.0
BuildRequires:	gtk+3-devel >= 3.22
BuildRequires:	gtk-doc >= 1.25
BuildRequires:	meson >= 0.53
BuildRequires:	ninja >= 1.5
BuildRequires:	pkgconfig
BuildRequires:	rpm-build >= 4.6
BuildRequires:	rpmbuild(macros) >= 1.736
Requires:	glib2 >= 1:2.56
Requires:	gtk+3 >= 3.22
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Amtk is the acronym for "Actions, Menus and Toolbars Kit". It is a
basic GtkUIManager replacement based on GAction. It is suitable for
both a traditional UI or a modern UI with a GtkHeaderBar.

%description -l pl.UTF-8
Amtk to krót od "Actions, Menus and Toolbars Kit" (zestaw akcji, menu
i pasków narzędziowych). Jest to podstawowy zamiennik GtkUIManagera
oparty na GAction. Nadaje się zarówno dla tradycyjnych, jak i
nowoczesnych interfejsów użytkownika z GtkHeaderBarem.

%package devel
Summary:	Header files for Amtk library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki Amtk
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	glib2-devel >= 1:2.56
Requires:	gtk+3-devel >= 3.22

%description devel
Header files for Amtk library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki Amtk.

%package static
Summary:	Static Amtk library
Summary(pl.UTF-8):	Statyczna biblioteka Amtk
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static Amtk library.

%description static -l pl.UTF-8
Statyczna biblioteka Amtk.

%package apidocs
Summary:	API documentation for Amtk library
Summary(pl.UTF-8):	Dokumentacja API biblioteki Amtk
Group:		Documentation
BuildArch:	noarch

%description apidocs
API documentation for Amtk library.

%description apidocs -l pl.UTF-8
Dokumentacja API biblioteki Amtk.

%prep
%setup -q

%build
%meson build \
	%{!?with_static_libs:--default-library=shared}

%ninja_build -C build

%install
rm -rf $RPM_BUILD_ROOT

%ninja_install -C build

%find_lang amtk-5

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files -f amtk-5.lang
%defattr(644,root,root,755)
%doc NEWS README.md
%attr(755,root,root) %{_libdir}/libamtk-5.so.0
%{_libdir}/girepository-1.0/Amtk-5.typelib

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libamtk-5.so
%{_includedir}/amtk-5
%{_datadir}/gir-1.0/Amtk-5.gir
%{_pkgconfigdir}/amtk-5.pc

%if %{with static_libs}
%files static
%defattr(644,root,root,755)
%{_libdir}/libamtk-5.a
%endif

%files apidocs
%defattr(644,root,root,755)
%{_gtkdocdir}/amtk-5
