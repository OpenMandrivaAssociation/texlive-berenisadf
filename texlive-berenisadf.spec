%global tl_name berenisadf
%global tl_revision 77682
%global tl_version 2.1

Name:		texlive-%{tl_name}
Epoch:		1
Version:	%{tl_version}
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
Requires:	texlive-tlpkg
Provides:	texlive(%{tl_name}) = %{version}

%description
The bundle provides the BerenisADF Pro font collection, in OpenType and
PostScript Type 1 formats, together with support files to use the fonts
in TeXnANSI (LY1) and LaTeX standard T1 and TS1 encodings.


%install -a
mkdir -p %{buildroot}%{_texmf_updmap_d}
cat > %{buildroot}%{_texmf_updmap_d}/%{tl_name} <<'TL_DROPIN_EOF'
# from berenisadf:
Map ybd.map
TL_DROPIN_EOF
