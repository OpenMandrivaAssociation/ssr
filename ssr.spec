%define rname ssr

Summary:	A feature-rich screen recorder that supports X11 and OpenGL
Name:		ssr
Version:	0.3.6
Release:	1
License:	GPLv3+
Group:		Video
Url:		http://www.maartenbaert.be/simplescreenrecorder
Source0:	https://github.com/MaartenBaert/ssr/archive/%{name}-%{version}.tar.gz
Source1:	%{name}.rpmlintrc
BuildRequires:	pkgconfig(Qt5Core)
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
%{_datadir}/applications/simplescreenrecorder.desktop
%{_datadir}/icons/hicolor/*/apps/simplescreenrecorder*
%{_datadir}/simplescreenrecorder
%{_mandir}/man1/*.1.*
#----------------------------------------------------------------------------

%prep
%setup -q

%build
%configure2_5x \
	--disable-static \
%ifarch %{ix86} x86_64
	--disable-x86-asm \
	--disable-glinjectlib \
%endif
	--with-qt5 \
	--without-jack

%make

%install
%makeinstall_std
