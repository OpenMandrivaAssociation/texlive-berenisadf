%global tl_name berenisadf
%global tl_revision 77682

Name:		texlive-%{tl_name}
Epoch:		1
Version:	2.1
Release:	%{tl_revision}.1
Summary:	Berenis ADF fonts and TeX/LaTeX support
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/fonts/berenisadf
License:	lppl1.3c gpl2
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/berenisadf.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/berenisadf.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/berenisadf.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
BuildRequires:	texlive-tlpkg
%texlive_base_requires
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The bundle provides the BerenisADF Pro font collection, in OpenType and
PostScript Type 1 formats, together with support files to use the fonts
in TeXnANSI (LY1) and LaTeX standard T1 and TS1 encodings.

