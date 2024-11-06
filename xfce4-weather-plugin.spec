Summary:	A weather plugin for the Xfce panel
Summary(pl.UTF-8):	Wtyczka panelu Xfce pokazująca pogodę
Name:		xfce4-weather-plugin
Version:	0.11.3
Release:	1
License:	GPL
Group:		X11/Applications
Source0:	https://archive.xfce.org/src/panel-plugins/xfce4-weather-plugin/0.11/%{name}-%{version}.tar.bz2
# Source0-md5:	df742378e58d6018f49bb43a794044f9
URL:		https://goodies.xfce.org/projects/panel-plugins/xfce4-weather-plugin
BuildRequires:	autoconf >= 2.63
BuildRequires:	automake
BuildRequires:	gettext-tools
BuildRequires:	libsoup-devel >= 2.26.0
BuildRequires:	libtool
BuildRequires:	libxfce4ui-devel
BuildRequires:	libxml2-devel >= 1:2.6.27
BuildRequires:	pkgconfig
BuildRequires:	rpmbuild(macros) >= 1.601
BuildRequires:	xfce4-dev-tools >= 4.14.0
BuildRequires:	xfce4-panel-devel >= 4.14.0
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
%configure \
	--disable-static

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%{__rm} -r $RPM_BUILD_ROOT%{_localedir}/{es,hye,ur_PK}
%{__rm} -r $RPM_BUILD_ROOT%{_libdir}/xfce4/panel/plugins/libweather.la

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%post
%update_icon_cache hicolor

%postun
%update_icon_cache hicolor

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README
%attr(755,root,root) %{_libdir}/xfce4/panel/plugins/libweather.so
%{_datadir}/xfce4/panel/plugins/weather.desktop
%{_datadir}/xfce4/weather
%{_iconsdir}/hicolor/*/*/org.xfce.panel.weather.png
%{_iconsdir}/hicolor/*/*/org.xfce.panel.weather.svg
