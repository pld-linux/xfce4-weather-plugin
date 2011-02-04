Summary:	A weather plugin for the Xfce panel
Summary(pl.UTF-8):	Wtyczka panelu Xfce pokazująca pogodę
Name:		xfce4-weather-plugin
Version:	0.7.3
Release:	3
License:	GPL
Group:		X11/Applications
Source0:	http://archive.xfce.org/src/panel-plugins/xfce4-weather-plugin/0.7/%{name}-%{version}.tar.bz2
# Source0-md5:	b3436929dd94cdd8acc744c474cca5c4
URL:		http://goodies.xfce.org/projects/panel-plugins/xfce4-weather-plugin
BuildRequires:	gettext-devel
BuildRequires:	intltool
BuildRequires:	libxml2-devel >= 1:2.6.27
BuildRequires:	pkgconfig
BuildRequires:	rpmbuild(macros) >= 1.311
BuildRequires:	xfce4-dev-tools >= 4.4.0
BuildRequires:	xfce4-panel-devel >= 4.4.0
Requires(post,postun):	gtk-update-icon-cache
Requires(post,postun):	hicolor-icon-theme
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

rm -r $RPM_BUILD_ROOT%{_datadir}/locale/ur_PK

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%post
%update_icon_cache hicolor

%postun
%update_icon_cache hicolor

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog README
%attr(755,root,root) %{_libdir}/xfce4/panel-plugins/xfce4-weather-plugin
%{_datadir}/xfce4/panel-plugins/weather.desktop
%{_datadir}/xfce4/weather
%{_iconsdir}/hicolor/*/*/xfce4-weather.png
