%define _requires_exceptions	/usr/local/bin/fontforge

Name:		texlive-berenisadf
Version:	1.004
Release:	1
Summary:	Berenis ADF fonts and TeX/LaTeX support
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/fonts/berenisadf
License:	OTHER-FREE
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/berenisadf.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/berenisadf.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/berenisadf.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(post):	texlive-tlpkg
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-doc <= 20110705-3
Conflicts:	texlive-source <= 20110705-3

%description
The bundle provides the BerenisADF Pro font collection, in
OpenType and PostScript Type 1 formats, together with support
files to use the fonts in TeXnANSI (LY1) encoding.

%pre
    %_texmf_mktexlsr_pre

%post
    %_texmf_mktexlsr_post

%preun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_pre
    fi

%postun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/fonts/afm/arkandis/berenisadf/ybdb.afm
%{_texmfdistdir}/fonts/afm/arkandis/berenisadf/ybdbc.afm
%{_texmfdistdir}/fonts/afm/arkandis/berenisadf/ybdbci.afm
%{_texmfdistdir}/fonts/afm/arkandis/berenisadf/ybdbi.afm
%{_texmfdistdir}/fonts/afm/arkandis/berenisadf/ybdr.afm
%{_texmfdistdir}/fonts/afm/arkandis/berenisadf/ybdrc.afm
%{_texmfdistdir}/fonts/afm/arkandis/berenisadf/ybdrci.afm
%{_texmfdistdir}/fonts/afm/arkandis/berenisadf/ybdri.afm
%{_texmfdistdir}/fonts/enc/dvips/berenisadf/texnansi-ybd.enc
%{_texmfdistdir}/fonts/enc/dvips/berenisadf/texnansi-ybd0.enc
%{_texmfdistdir}/fonts/enc/dvips/berenisadf/texnansi-ybd1.enc
%{_texmfdistdir}/fonts/enc/dvips/berenisadf/texnansi-ybd2.enc
%{_texmfdistdir}/fonts/enc/dvips/berenisadf/texnansi-ybd2j.enc
%{_texmfdistdir}/fonts/enc/dvips/berenisadf/texnansi-ybdj.enc
%{_texmfdistdir}/fonts/enc/dvips/berenisadf/texnansx-ybd2jw.enc
%{_texmfdistdir}/fonts/enc/dvips/berenisadf/texnansx-ybd2w.enc
%{_texmfdistdir}/fonts/enc/dvips/berenisadf/texnansx-ybdjw.enc
%{_texmfdistdir}/fonts/enc/dvips/berenisadf/texnansx-ybdw.enc
%{_texmfdistdir}/fonts/map/dvips/berenisadf/ybd.map
%{_texmfdistdir}/fonts/tfm/arkandis/berenisadf/ybdb08y.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/berenisadf/ybdb0c8y.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/berenisadf/ybdb0ci8y.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/berenisadf/ybdb0i8y.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/berenisadf/ybdb18y.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/berenisadf/ybdb1c8y.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/berenisadf/ybdb1ci8y.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/berenisadf/ybdb1i8y.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/berenisadf/ybdb28y.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/berenisadf/ybdb2c8y.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/berenisadf/ybdb2ci8y.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/berenisadf/ybdb2cij8y.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/berenisadf/ybdb2cijw8y.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/berenisadf/ybdb2ciw8y.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/berenisadf/ybdb2cj8y.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/berenisadf/ybdb2cjw8y.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/berenisadf/ybdb2cw8y.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/berenisadf/ybdb2i8y.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/berenisadf/ybdb2ij8y.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/berenisadf/ybdb2ijw8y.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/berenisadf/ybdb2iw8y.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/berenisadf/ybdb2j8y.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/berenisadf/ybdb2jw8y.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/berenisadf/ybdb2w8y.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/berenisadf/ybdb8y.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/berenisadf/ybdbc8y.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/berenisadf/ybdbci8y.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/berenisadf/ybdbcij8y.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/berenisadf/ybdbcijw8y.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/berenisadf/ybdbciw8y.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/berenisadf/ybdbcj8y.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/berenisadf/ybdbcjw8y.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/berenisadf/ybdbcw8y.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/berenisadf/ybdbi8y.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/berenisadf/ybdbij8y.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/berenisadf/ybdbijw8y.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/berenisadf/ybdbiw8y.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/berenisadf/ybdbj8y.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/berenisadf/ybdbjw8y.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/berenisadf/ybdbw8y.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/berenisadf/ybdr08y.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/berenisadf/ybdr0c8y.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/berenisadf/ybdr0ci8y.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/berenisadf/ybdr0i8y.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/berenisadf/ybdr18y.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/berenisadf/ybdr1c8y.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/berenisadf/ybdr1ci8y.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/berenisadf/ybdr1i8y.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/berenisadf/ybdr28y.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/berenisadf/ybdr2c8y.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/berenisadf/ybdr2ci8y.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/berenisadf/ybdr2cij8y.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/berenisadf/ybdr2cijw8y.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/berenisadf/ybdr2ciw8y.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/berenisadf/ybdr2cj8y.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/berenisadf/ybdr2cjw8y.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/berenisadf/ybdr2cw8y.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/berenisadf/ybdr2i8y.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/berenisadf/ybdr2ij8y.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/berenisadf/ybdr2ijw8y.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/berenisadf/ybdr2iw8y.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/berenisadf/ybdr2j8y.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/berenisadf/ybdr2jw8y.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/berenisadf/ybdr2w8y.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/berenisadf/ybdr8y.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/berenisadf/ybdrc8y.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/berenisadf/ybdrci8y.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/berenisadf/ybdrcij8y.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/berenisadf/ybdrcijw8y.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/berenisadf/ybdrciw8y.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/berenisadf/ybdrcj8y.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/berenisadf/ybdrcjw8y.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/berenisadf/ybdrcw8y.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/berenisadf/ybdri8y.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/berenisadf/ybdrij8y.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/berenisadf/ybdrijw8y.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/berenisadf/ybdriw8y.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/berenisadf/ybdrj8y.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/berenisadf/ybdrjw8y.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/berenisadf/ybdrw8y.tfm
%{_texmfdistdir}/fonts/type1/arkandis/berenisadf/ybdb.pfb
%{_texmfdistdir}/fonts/type1/arkandis/berenisadf/ybdbc.pfb
%{_texmfdistdir}/fonts/type1/arkandis/berenisadf/ybdbci.pfb
%{_texmfdistdir}/fonts/type1/arkandis/berenisadf/ybdbi.pfb
%{_texmfdistdir}/fonts/type1/arkandis/berenisadf/ybdr.pfb
%{_texmfdistdir}/fonts/type1/arkandis/berenisadf/ybdrc.pfb
%{_texmfdistdir}/fonts/type1/arkandis/berenisadf/ybdrci.pfb
%{_texmfdistdir}/fonts/type1/arkandis/berenisadf/ybdri.pfb
%{_texmfdistdir}/tex/latex/berenisadf/berenis.sty
%{_texmfdistdir}/tex/latex/berenisadf/ly1ybd.fd
%{_texmfdistdir}/tex/latex/berenisadf/ly1ybd0.fd
%{_texmfdistdir}/tex/latex/berenisadf/ly1ybd1.fd
%{_texmfdistdir}/tex/latex/berenisadf/ly1ybd2.fd
%{_texmfdistdir}/tex/latex/berenisadf/ly1ybd2j.fd
%{_texmfdistdir}/tex/latex/berenisadf/ly1ybd2jw.fd
%{_texmfdistdir}/tex/latex/berenisadf/ly1ybd2w.fd
%{_texmfdistdir}/tex/latex/berenisadf/ly1ybdj.fd
%{_texmfdistdir}/tex/latex/berenisadf/ly1ybdjw.fd
%{_texmfdistdir}/tex/latex/berenisadf/ly1ybdw.fd
%doc %{_texmfdistdir}/doc/fonts/berenisadf/COPYING
%doc %{_texmfdistdir}/doc/fonts/berenisadf/NOTICE.txt
%doc %{_texmfdistdir}/doc/fonts/berenisadf/README
%doc %{_texmfdistdir}/doc/fonts/berenisadf/berenisadf.pdf
%doc %{_texmfdistdir}/doc/fonts/berenisadf/berenisadf.tex
%doc %{_texmfdistdir}/doc/fonts/berenisadf/manifest.txt
#- source
%doc %{_texmfdistdir}/source/fonts/berenisadf/BerenisADFPro-Bold.otf
%doc %{_texmfdistdir}/source/fonts/berenisadf/BerenisADFPro-BoldItalic.otf
%doc %{_texmfdistdir}/source/fonts/berenisadf/BerenisADFPro-Italic.otf
%doc %{_texmfdistdir}/source/fonts/berenisadf/BerenisADFPro-Regular.otf
%doc %{_texmfdistdir}/source/fonts/berenisadf/BerenisADFProSC-Bold.otf
%doc %{_texmfdistdir}/source/fonts/berenisadf/BerenisADFProSC-BoldItalic.otf
%doc %{_texmfdistdir}/source/fonts/berenisadf/BerenisADFProSC-Italic.otf
%doc %{_texmfdistdir}/source/fonts/berenisadf/BerenisADFProSC-Regular.otf
%doc %{_texmfdistdir}/source/fonts/berenisadf/Makefile
%doc %{_texmfdistdir}/source/fonts/berenisadf/cfr.make.public
%doc %{_texmfdistdir}/source/fonts/berenisadf/ff-ybd.pe
%doc %{_texmfdistdir}/source/fonts/berenisadf/ybd-8y.nam
%doc %{_texmfdistdir}/source/fonts/berenisadf/ybd.lig

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar fonts tex doc source %{buildroot}%{_texmfdistdir}
