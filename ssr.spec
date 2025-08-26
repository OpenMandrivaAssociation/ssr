%define rname ssr

Summary:	A feature-rich screen recorder that supports X11 and OpenGL
Name:		ssr
Version:	0.4.4
Release:	6
License:	GPLv3+
Group:		Video
Url:		https://www.maartenbaert.be/simplescreenrecorder
Source0:	https://github.com/MaartenBaert/ssr/archive/%{version}/%{name}-%{version}.tar.gz
Source1:	%{name}.rpmlintrc
Patch0:		ssr-0.3.8-non-x86.patch
Patch1:		ssr-0.4.0-free-codecs.patch
Patch2:		ssr-0.4.3-ffmpeg-5.0.patch
Patch3:		ssr-0.4.4-ffmpeg-7.patch
BuildRequires:	cmake ninja
BuildRequires:	qmake5
BuildRequires:	qt5-linguist-tools
BuildRequires:	pkgconfig(libv4l2)
BuildRequires:	pkgconfig(Qt5Core)
BuildRequires:	pkgconfig(Qt5Gui)
BuildRequires:	pkgconfig(Qt5Widgets)
BuildRequires:	pkgconfig(Qt5X11Extras)
BuildRequires:	pkgconfig(alsa)
BuildRequires:	pkgconfig(gl)
BuildRequires:	pkgconfig(glu)
BuildRequires:	pkgconfig(libavformat)
BuildRequires:	pkgconfig(libpulse)
BuildRequires:	pkgconfig(jack)
BuildRequires:	pkgconfig(x11)
BuildRequires:	pkgconfig(xext)
BuildRequires:	pkgconfig(xfixes)
BuildRequires:	pkgconfig(xi)
BuildRequires:  pkgconfig(xinerama)
BuildRequires:  jpeg-devel
%rename		simplescreenrecorder

%description
SimpleScreenRecorder is a Linux program that was created to record programs
and games.

The original goal was to create a program that was just really simple to
use, the result is actually a pretty powerful program. It's 'simple' in
the sense that it's easier to use than ffmpeg/avconv or VLC, because it
has a straightforward user interface.

Features:
 * Graphical user interface (Qt-based).
 * Faster than VLC and ffmpeg/avconv.
 * Records the entire screen or part of it, or records OpenGL applications
   directly (similar to Fraps on Windows).
 * Synchronizes audio and video properly (a common issue with VLC and
   ffmpeg/avconv).
 * Reduces the video frame rate if your computer is too slow (rather than
   using up all your RAM like VLC does).
 * Fully multithreaded: small delays in any of the components will never
   block the other components, resulting is smoother video and better
   performance on computers with multiple processors.
 * Pause and resume recording at any time (either by clicking a button or by
   pressing a hotkey).
 * Shows statistics during recording (file size, bit rate, total recording
   time, actual frame rate, ...).
 * Can show a preview during recording, so you don't waste time recording
   something only to figure out afterwards that some setting was wrong.
 * Uses libav/ffmpeg libraries for encoding, so it supports many different
   codecs and file formats (adding more is trivial).
 * Sensible default settings: no need to change anything if you don't want to.
 * Tooltips for almost everything: no need to read the documentation to find
   out what something does.

%files
%doc COPYING *.txt *.md data/resources/about.htm
%{_bindir}/simplescreenrecorder
%{_bindir}/ssr-glinject
%{_libdir}/libssr-glinject.so
%{_datadir}/applications/simplescreenrecorder.desktop
%{_datadir}/metainfo/simplescreenrecorder.metainfo.xml
%{_datadir}/icons/hicolor/*/apps/simplescreenrecorder*
%{_datadir}/simplescreenrecorder
%{_mandir}/man1/*.1.*
#----------------------------------------------------------------------------

%prep
%setup -q
%autopatch -p1
%cmake_qt5 \
%ifnarch %{ix86} x86_64}
	-DENABLE_X86_ASM:BOOL=OFF \
%endif
	-DWITH_QT5:BOOL=ON \
	-G Ninja

%build
%ninja -C build

%install
%ninja_install -C build
