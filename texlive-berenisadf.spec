# revision 32215
# category Package
# catalog-ctan /fonts/berenisadf
# catalog-date 2013-11-21 13:05:24 +0100
# catalog-license other-free
# catalog-version 1.004
Name:		texlive-berenisadf
Version:	1.004
Release:	9
Summary:	Berenis ADF fonts and TeX/LaTeX support
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/fonts/berenisadf
License:	OTHER-FREE
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/berenisadf.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/berenisadf.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea
Requires:	fontforge

%description
The bundle provides the BerenisADF Pro font collection, in
OpenType and PostScript Type 1 formats, together with support
files to use the fonts in TeXnANSI (LY1) and LaTeX standard T1
and TS1 encodings.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
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
%{_texmfdistdir}/fonts/enc/dvips/berenisadf/t1-ybd.enc
%{_texmfdistdir}/fonts/enc/dvips/berenisadf/t1-ybd0.enc
%{_texmfdistdir}/fonts/enc/dvips/berenisadf/t1-ybd1.enc
%{_texmfdistdir}/fonts/enc/dvips/berenisadf/t1-ybd2.enc
%{_texmfdistdir}/fonts/enc/dvips/berenisadf/t1-ybd2j.enc
%{_texmfdistdir}/fonts/enc/dvips/berenisadf/t1-ybdj.enc
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
%{_texmfdistdir}/fonts/enc/dvips/berenisadf/ts1-ybd.enc
%{_texmfdistdir}/fonts/enc/dvips/berenisadf/ts1-ybd0.enc
%{_texmfdistdir}/fonts/enc/dvips/berenisadf/ts1-ybd1.enc
%{_texmfdistdir}/fonts/enc/dvips/berenisadf/ts1-ybd2.enc
%{_texmfdistdir}/fonts/enc/dvips/berenisadf/ts1-ybd2j.enc
%{_texmfdistdir}/fonts/enc/dvips/berenisadf/ts1-ybdj.enc
%{_texmfdistdir}/fonts/map/dvips/berenisadf/ybd.map
%{_texmfdistdir}/fonts/opentype/arkandis/berenisadf/BerenisADFPro-Bold.otf
%{_texmfdistdir}/fonts/opentype/arkandis/berenisadf/BerenisADFPro-BoldItalic.otf
%{_texmfdistdir}/fonts/opentype/arkandis/berenisadf/BerenisADFPro-Italic.otf
%{_texmfdistdir}/fonts/opentype/arkandis/berenisadf/BerenisADFPro-Regular.otf
%{_texmfdistdir}/fonts/opentype/arkandis/berenisadf/BerenisADFProSC-Bold.otf
%{_texmfdistdir}/fonts/opentype/arkandis/berenisadf/BerenisADFProSC-BoldItalic.otf
%{_texmfdistdir}/fonts/opentype/arkandis/berenisadf/BerenisADFProSC-Italic.otf
%{_texmfdistdir}/fonts/opentype/arkandis/berenisadf/BerenisADFProSC-Regular.otf
%{_texmfdistdir}/fonts/tfm/arkandis/berenisadf/ybdb08c.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/berenisadf/ybdb08t.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/berenisadf/ybdb08y.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/berenisadf/ybdb0c8c.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/berenisadf/ybdb0c8t.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/berenisadf/ybdb0c8y.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/berenisadf/ybdb0ci8c.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/berenisadf/ybdb0ci8t.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/berenisadf/ybdb0ci8y.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/berenisadf/ybdb0i8c.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/berenisadf/ybdb0i8t.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/berenisadf/ybdb0i8y.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/berenisadf/ybdb18c.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/berenisadf/ybdb18t.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/berenisadf/ybdb18y.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/berenisadf/ybdb1c8c.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/berenisadf/ybdb1c8t.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/berenisadf/ybdb1c8y.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/berenisadf/ybdb1ci8c.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/berenisadf/ybdb1ci8t.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/berenisadf/ybdb1ci8y.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/berenisadf/ybdb1i8c.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/berenisadf/ybdb1i8t.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/berenisadf/ybdb1i8y.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/berenisadf/ybdb28c.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/berenisadf/ybdb28t.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/berenisadf/ybdb28y.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/berenisadf/ybdb2c8c.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/berenisadf/ybdb2c8t.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/berenisadf/ybdb2c8y.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/berenisadf/ybdb2ci8c.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/berenisadf/ybdb2ci8t.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/berenisadf/ybdb2ci8y.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/berenisadf/ybdb2cij8c.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/berenisadf/ybdb2cij8t.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/berenisadf/ybdb2cij8y.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/berenisadf/ybdb2cijw8y.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/berenisadf/ybdb2ciw8y.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/berenisadf/ybdb2cj8c.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/berenisadf/ybdb2cj8t.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/berenisadf/ybdb2cj8y.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/berenisadf/ybdb2cjw8y.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/berenisadf/ybdb2cw8y.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/berenisadf/ybdb2i8c.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/berenisadf/ybdb2i8t.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/berenisadf/ybdb2i8y.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/berenisadf/ybdb2ij8c.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/berenisadf/ybdb2ij8t.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/berenisadf/ybdb2ij8y.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/berenisadf/ybdb2ijw8y.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/berenisadf/ybdb2iw8y.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/berenisadf/ybdb2j8c.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/berenisadf/ybdb2j8t.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/berenisadf/ybdb2j8y.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/berenisadf/ybdb2jw8y.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/berenisadf/ybdb2w8y.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/berenisadf/ybdb8c.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/berenisadf/ybdb8t.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/berenisadf/ybdb8y.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/berenisadf/ybdbc8c.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/berenisadf/ybdbc8t.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/berenisadf/ybdbc8y.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/berenisadf/ybdbci8c.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/berenisadf/ybdbci8t.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/berenisadf/ybdbci8y.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/berenisadf/ybdbcij8c.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/berenisadf/ybdbcij8t.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/berenisadf/ybdbcij8y.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/berenisadf/ybdbcijw8y.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/berenisadf/ybdbciw8y.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/berenisadf/ybdbcj8c.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/berenisadf/ybdbcj8t.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/berenisadf/ybdbcj8y.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/berenisadf/ybdbcjw8y.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/berenisadf/ybdbcw8y.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/berenisadf/ybdbi8c.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/berenisadf/ybdbi8t.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/berenisadf/ybdbi8y.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/berenisadf/ybdbij8c.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/berenisadf/ybdbij8t.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/berenisadf/ybdbij8y.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/berenisadf/ybdbijw8y.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/berenisadf/ybdbiw8y.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/berenisadf/ybdbj8c.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/berenisadf/ybdbj8t.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/berenisadf/ybdbj8y.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/berenisadf/ybdbjw8y.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/berenisadf/ybdbw8y.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/berenisadf/ybdr08c.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/berenisadf/ybdr08t.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/berenisadf/ybdr08y.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/berenisadf/ybdr0c8c.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/berenisadf/ybdr0c8t.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/berenisadf/ybdr0c8y.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/berenisadf/ybdr0ci8c.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/berenisadf/ybdr0ci8t.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/berenisadf/ybdr0ci8y.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/berenisadf/ybdr0i8c.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/berenisadf/ybdr0i8t.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/berenisadf/ybdr0i8y.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/berenisadf/ybdr18c.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/berenisadf/ybdr18t.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/berenisadf/ybdr18y.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/berenisadf/ybdr1c8c.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/berenisadf/ybdr1c8t.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/berenisadf/ybdr1c8y.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/berenisadf/ybdr1ci8c.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/berenisadf/ybdr1ci8t.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/berenisadf/ybdr1ci8y.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/berenisadf/ybdr1i8c.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/berenisadf/ybdr1i8t.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/berenisadf/ybdr1i8y.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/berenisadf/ybdr28c.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/berenisadf/ybdr28t.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/berenisadf/ybdr28y.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/berenisadf/ybdr2c8c.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/berenisadf/ybdr2c8t.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/berenisadf/ybdr2c8y.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/berenisadf/ybdr2ci8c.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/berenisadf/ybdr2ci8t.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/berenisadf/ybdr2ci8y.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/berenisadf/ybdr2cij8c.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/berenisadf/ybdr2cij8t.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/berenisadf/ybdr2cij8y.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/berenisadf/ybdr2cijw8y.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/berenisadf/ybdr2ciw8y.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/berenisadf/ybdr2cj8c.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/berenisadf/ybdr2cj8t.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/berenisadf/ybdr2cj8y.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/berenisadf/ybdr2cjw8y.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/berenisadf/ybdr2cw8y.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/berenisadf/ybdr2i8c.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/berenisadf/ybdr2i8t.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/berenisadf/ybdr2i8y.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/berenisadf/ybdr2ij8c.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/berenisadf/ybdr2ij8t.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/berenisadf/ybdr2ij8y.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/berenisadf/ybdr2ijw8y.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/berenisadf/ybdr2iw8y.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/berenisadf/ybdr2j8c.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/berenisadf/ybdr2j8t.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/berenisadf/ybdr2j8y.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/berenisadf/ybdr2jw8y.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/berenisadf/ybdr2w8y.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/berenisadf/ybdr8c.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/berenisadf/ybdr8t.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/berenisadf/ybdr8y.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/berenisadf/ybdrc8c.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/berenisadf/ybdrc8t.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/berenisadf/ybdrc8y.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/berenisadf/ybdrci8c.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/berenisadf/ybdrci8t.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/berenisadf/ybdrci8y.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/berenisadf/ybdrcij8c.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/berenisadf/ybdrcij8t.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/berenisadf/ybdrcij8y.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/berenisadf/ybdrcijw8y.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/berenisadf/ybdrciw8y.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/berenisadf/ybdrcj8c.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/berenisadf/ybdrcj8t.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/berenisadf/ybdrcj8y.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/berenisadf/ybdrcjw8y.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/berenisadf/ybdrcw8y.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/berenisadf/ybdri8c.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/berenisadf/ybdri8t.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/berenisadf/ybdri8y.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/berenisadf/ybdrij8c.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/berenisadf/ybdrij8t.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/berenisadf/ybdrij8y.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/berenisadf/ybdrijw8y.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/berenisadf/ybdriw8y.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/berenisadf/ybdrj8c.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/berenisadf/ybdrj8t.tfm
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
%{_texmfdistdir}/tex/latex/berenisadf/t1ybd.fd
%{_texmfdistdir}/tex/latex/berenisadf/t1ybd0.fd
%{_texmfdistdir}/tex/latex/berenisadf/t1ybd1.fd
%{_texmfdistdir}/tex/latex/berenisadf/t1ybd2.fd
%{_texmfdistdir}/tex/latex/berenisadf/t1ybd2j.fd
%{_texmfdistdir}/tex/latex/berenisadf/t1ybdj.fd
%{_texmfdistdir}/tex/latex/berenisadf/ts1ybd.fd
%{_texmfdistdir}/tex/latex/berenisadf/ts1ybd0.fd
%{_texmfdistdir}/tex/latex/berenisadf/ts1ybd1.fd
%{_texmfdistdir}/tex/latex/berenisadf/ts1ybd2.fd
%{_texmfdistdir}/tex/latex/berenisadf/ts1ybd2j.fd
%{_texmfdistdir}/tex/latex/berenisadf/ts1ybdj.fd
%doc %{_texmfdistdir}/doc/fonts/berenisadf/COPYING
%doc %{_texmfdistdir}/doc/fonts/berenisadf/COPYING.unix
%doc %{_texmfdistdir}/doc/fonts/berenisadf/Makefile.source
%doc %{_texmfdistdir}/doc/fonts/berenisadf/NOTICE.txt
%doc %{_texmfdistdir}/doc/fonts/berenisadf/README.doc
%doc %{_texmfdistdir}/doc/fonts/berenisadf/berenisadf.pdf
%doc %{_texmfdistdir}/doc/fonts/berenisadf/berenisadf.tex
%doc %{_texmfdistdir}/doc/fonts/berenisadf/cfr.gwneud.cyhoeddus
%doc %{_texmfdistdir}/doc/fonts/berenisadf/ff-ybd.pe
%doc %{_texmfdistdir}/doc/fonts/berenisadf/manifest.txt
%doc %{_texmfdistdir}/doc/fonts/berenisadf/ybd-8t.lig
%doc %{_texmfdistdir}/doc/fonts/berenisadf/ybd-8y.lig
%doc %{_texmfdistdir}/doc/fonts/berenisadf/ybd.nam

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
perl -pi -e 's|/usr/local/bin/fontforge|/usr/bin/fontforge|'		\
    fonts/berenisadf/ff-ybd.pe
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar fonts tex doc %{buildroot}%{_texmfdistdir}
