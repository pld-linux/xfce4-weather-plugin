Summary:	A weather plugin for the Xfce panel
Summary(pl.UTF-8):	Wtyczka panelu Xfce pokazująca pogodę
Name:		xfce4-weather-plugin
Version:	0.12.0
Release:	1
License:	GPL
Group:		X11/Applications
Source0:	https://archive.xfce.org/src/panel-plugins/xfce4-weather-plugin/0.12/%{name}-%{version}.tar.xz
# Source0-md5:	b08980a84183911feced5fe80f79627b
URL:		https://goodies.xfce.org/projects/panel-plugins/xfce4-weather-plugin
BuildRequires:	gettext-tools
BuildRequires:	glib2-devel >= 1:2.64.0
BuildRequires:	gtk+3-devel >= 3.22
BuildRequires:	json-c-devel >= 0.13.1
BuildRequires:	libsoup3-devel >= 3.0.0
BuildRequires:	libtool
BuildRequires:	libxfce4ui-devel >= 4.16
BuildRequires:	libxml2-devel >= 1:2.6.27
BuildRequires:	meson >= 0.54.0
BuildRequires:	ninja
BuildRequires:	pkgconfig
BuildRequires:	rpmbuild(macros) >= 1.601
BuildRequires:	upower-devel >= 0.99.0
BuildRequires:	xfce4-dev-tools >= 4.16.0
BuildRequires:	xfce4-panel-devel >= 4.16.0
Requires:	gtk-update-icon-cache
Requires:	hicolor-icon-theme
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
A weather plugin for the Xfce panel.

%description -l pl.UTF-8
Wtyczka dla panelu Xfce wyświetlająca pogodę.

%prep
%setup -q

%build
%meson
%meson_build

%install
rm -rf $RPM_BUILD_ROOT

%meson_install

%{__rm} -r $RPM_BUILD_ROOT%{_localedir}/{es,hye,ie,ur_PK}

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%post
%update_icon_cache hicolor

%postun
%update_icon_cache hicolor

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS NEWS README
%attr(755,root,root) %{_libdir}/xfce4/panel/plugins/libweather.so
%{_datadir}/xfce4/panel/plugins/weather.desktop
%{_datadir}/xfce4/weather
%{_iconsdir}/hicolor/*/*/org.xfce.panel.weather.png
%{_iconsdir}/hicolor/*/*/org.xfce.panel.weather.svg
