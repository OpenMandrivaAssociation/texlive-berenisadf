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
Requires(pre):	texlive-tlpkg
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The bundle provides the BerenisADF Pro font collection, in OpenType and
PostScript Type 1 formats, together with support files to use the fonts
in TeXnANSI (LY1) and LaTeX standard T1 and TS1 encodings.

%prep
%setup -q -c -a1 -a2
rm -rf tlpkg
if [ -d RELOC ]; then
	cp -a RELOC/. .
	rm -rf RELOC
fi

%build

%install
mkdir -p %{buildroot}%{_datadir}/texmf-dist
# Flat tlnet layout: tex/ doc/ source/ fonts/ ... -> texmf-dist/
if [ -d texmf-dist ]; then
	cp -a texmf-dist/. %{buildroot}%{_datadir}/texmf-dist/
elif [ -d texmf ]; then
	mkdir -p %{buildroot}%{_datadir}/texmf
	cp -a texmf/. %{buildroot}%{_datadir}/texmf/
else
	for d in * .[!.]* ..?*; do
		[ -e "$d" ] || continue
		case "$d" in tlpkg|RELOC) continue ;; esac
		cp -a "$d" %{buildroot}%{_datadir}/texmf-dist/
	done
fi
rm -rf %{buildroot}%{_datadir}/texmf-dist/tlpkg

%files
%dir %{_datadir}/texmf-dist
%dir %{_datadir}/texmf-dist/doc
%dir %{_datadir}/texmf-dist/fonts
%dir %{_datadir}/texmf-dist/source
%dir %{_datadir}/texmf-dist/tex
%dir %{_datadir}/texmf-dist/doc/fonts
%dir %{_datadir}/texmf-dist/fonts/afm
%dir %{_datadir}/texmf-dist/fonts/enc
%dir %{_datadir}/texmf-dist/fonts/map
%dir %{_datadir}/texmf-dist/fonts/opentype
%dir %{_datadir}/texmf-dist/fonts/tfm
%dir %{_datadir}/texmf-dist/fonts/type1
%dir %{_datadir}/texmf-dist/source/fonts
%dir %{_datadir}/texmf-dist/tex/latex
%dir %{_datadir}/texmf-dist/doc/fonts/berenisadf
%dir %{_datadir}/texmf-dist/fonts/afm/arkandis
%dir %{_datadir}/texmf-dist/fonts/enc/dvips
%dir %{_datadir}/texmf-dist/fonts/map/dvips
%dir %{_datadir}/texmf-dist/fonts/opentype/arkandis
%dir %{_datadir}/texmf-dist/fonts/tfm/arkandis
%dir %{_datadir}/texmf-dist/fonts/type1/arkandis
%dir %{_datadir}/texmf-dist/source/fonts/berenisadf
%dir %{_datadir}/texmf-dist/tex/latex/berenisadf
%dir %{_datadir}/texmf-dist/fonts/afm/arkandis/berenisadf
%dir %{_datadir}/texmf-dist/fonts/enc/dvips/berenisadf
%dir %{_datadir}/texmf-dist/fonts/map/dvips/berenisadf
%dir %{_datadir}/texmf-dist/fonts/opentype/arkandis/berenisadf
%dir %{_datadir}/texmf-dist/fonts/tfm/arkandis/berenisadf
%dir %{_datadir}/texmf-dist/fonts/type1/arkandis/berenisadf
%doc %{_datadir}/texmf-dist/doc/fonts/berenisadf/COPYING
%doc %{_datadir}/texmf-dist/doc/fonts/berenisadf/NOTICE.txt
%doc %{_datadir}/texmf-dist/doc/fonts/berenisadf/README.md
%doc %{_datadir}/texmf-dist/doc/fonts/berenisadf/berenisadf-tables.pdf
%doc %{_datadir}/texmf-dist/doc/fonts/berenisadf/berenisadf-tables.tex
%doc %{_datadir}/texmf-dist/doc/fonts/berenisadf/berenisadf.pdf
%doc %{_datadir}/texmf-dist/doc/fonts/berenisadf/ff-ybd.pe
%doc %{_datadir}/texmf-dist/doc/fonts/berenisadf/manifest.txt
%doc %{_datadir}/texmf-dist/doc/fonts/berenisadf/ybd-8t.lig
%doc %{_datadir}/texmf-dist/doc/fonts/berenisadf/ybd-8y.lig
%doc %{_datadir}/texmf-dist/doc/fonts/berenisadf/ybd-encs.tex
%doc %{_datadir}/texmf-dist/doc/fonts/berenisadf/ybd.nam
%{_datadir}/texmf-dist/fonts/afm/arkandis/berenisadf/ybdb.afm
%{_datadir}/texmf-dist/fonts/afm/arkandis/berenisadf/ybdbc.afm
%{_datadir}/texmf-dist/fonts/afm/arkandis/berenisadf/ybdbci.afm
%{_datadir}/texmf-dist/fonts/afm/arkandis/berenisadf/ybdbi.afm
%{_datadir}/texmf-dist/fonts/afm/arkandis/berenisadf/ybdr.afm
%{_datadir}/texmf-dist/fonts/afm/arkandis/berenisadf/ybdrc.afm
%{_datadir}/texmf-dist/fonts/afm/arkandis/berenisadf/ybdrci.afm
%{_datadir}/texmf-dist/fonts/afm/arkandis/berenisadf/ybdri.afm
%{_datadir}/texmf-dist/fonts/enc/dvips/berenisadf/t1-ybd.enc
%{_datadir}/texmf-dist/fonts/enc/dvips/berenisadf/t1-ybd0.enc
%{_datadir}/texmf-dist/fonts/enc/dvips/berenisadf/t1-ybd1.enc
%{_datadir}/texmf-dist/fonts/enc/dvips/berenisadf/t1-ybd2.enc
%{_datadir}/texmf-dist/fonts/enc/dvips/berenisadf/t1-ybd2j.enc
%{_datadir}/texmf-dist/fonts/enc/dvips/berenisadf/t1-ybdj.enc
%{_datadir}/texmf-dist/fonts/enc/dvips/berenisadf/texnansi-ybd.enc
%{_datadir}/texmf-dist/fonts/enc/dvips/berenisadf/texnansi-ybd0.enc
%{_datadir}/texmf-dist/fonts/enc/dvips/berenisadf/texnansi-ybd1.enc
%{_datadir}/texmf-dist/fonts/enc/dvips/berenisadf/texnansi-ybd2.enc
%{_datadir}/texmf-dist/fonts/enc/dvips/berenisadf/texnansi-ybd2j.enc
%{_datadir}/texmf-dist/fonts/enc/dvips/berenisadf/texnansi-ybdj.enc
%{_datadir}/texmf-dist/fonts/enc/dvips/berenisadf/texnansx-ybd2jw.enc
%{_datadir}/texmf-dist/fonts/enc/dvips/berenisadf/texnansx-ybd2w.enc
%{_datadir}/texmf-dist/fonts/enc/dvips/berenisadf/texnansx-ybdjw.enc
%{_datadir}/texmf-dist/fonts/enc/dvips/berenisadf/texnansx-ybdw.enc
%{_datadir}/texmf-dist/fonts/enc/dvips/berenisadf/ts1-ybd.enc
%{_datadir}/texmf-dist/fonts/enc/dvips/berenisadf/ts1-ybd0.enc
%{_datadir}/texmf-dist/fonts/enc/dvips/berenisadf/ts1-ybd1.enc
%{_datadir}/texmf-dist/fonts/enc/dvips/berenisadf/ts1-ybd2.enc
%{_datadir}/texmf-dist/fonts/enc/dvips/berenisadf/ts1-ybd2j.enc
%{_datadir}/texmf-dist/fonts/enc/dvips/berenisadf/ts1-ybdj.enc
%{_datadir}/texmf-dist/fonts/map/dvips/berenisadf/ybd.map
%{_datadir}/texmf-dist/fonts/opentype/arkandis/berenisadf/BerenisADFPro-Bold.otf
%{_datadir}/texmf-dist/fonts/opentype/arkandis/berenisadf/BerenisADFPro-BoldItalic.otf
%{_datadir}/texmf-dist/fonts/opentype/arkandis/berenisadf/BerenisADFPro-Italic.otf
%{_datadir}/texmf-dist/fonts/opentype/arkandis/berenisadf/BerenisADFPro-Regular.otf
%{_datadir}/texmf-dist/fonts/opentype/arkandis/berenisadf/BerenisADFProSC-Bold.otf
%{_datadir}/texmf-dist/fonts/opentype/arkandis/berenisadf/BerenisADFProSC-BoldItalic.otf
%{_datadir}/texmf-dist/fonts/opentype/arkandis/berenisadf/BerenisADFProSC-Italic.otf
%{_datadir}/texmf-dist/fonts/opentype/arkandis/berenisadf/BerenisADFProSC-Regular.otf
%{_datadir}/texmf-dist/fonts/tfm/arkandis/berenisadf/ybdb08c.tfm
%{_datadir}/texmf-dist/fonts/tfm/arkandis/berenisadf/ybdb08t.tfm
%{_datadir}/texmf-dist/fonts/tfm/arkandis/berenisadf/ybdb08y.tfm
%{_datadir}/texmf-dist/fonts/tfm/arkandis/berenisadf/ybdb0c8c.tfm
%{_datadir}/texmf-dist/fonts/tfm/arkandis/berenisadf/ybdb0c8t.tfm
%{_datadir}/texmf-dist/fonts/tfm/arkandis/berenisadf/ybdb0c8y.tfm
%{_datadir}/texmf-dist/fonts/tfm/arkandis/berenisadf/ybdb0ci8c.tfm
%{_datadir}/texmf-dist/fonts/tfm/arkandis/berenisadf/ybdb0ci8t.tfm
%{_datadir}/texmf-dist/fonts/tfm/arkandis/berenisadf/ybdb0ci8y.tfm
%{_datadir}/texmf-dist/fonts/tfm/arkandis/berenisadf/ybdb0i8c.tfm
%{_datadir}/texmf-dist/fonts/tfm/arkandis/berenisadf/ybdb0i8t.tfm
%{_datadir}/texmf-dist/fonts/tfm/arkandis/berenisadf/ybdb0i8y.tfm
%{_datadir}/texmf-dist/fonts/tfm/arkandis/berenisadf/ybdb18c.tfm
%{_datadir}/texmf-dist/fonts/tfm/arkandis/berenisadf/ybdb18t.tfm
%{_datadir}/texmf-dist/fonts/tfm/arkandis/berenisadf/ybdb18y.tfm
%{_datadir}/texmf-dist/fonts/tfm/arkandis/berenisadf/ybdb1c8c.tfm
%{_datadir}/texmf-dist/fonts/tfm/arkandis/berenisadf/ybdb1c8t.tfm
%{_datadir}/texmf-dist/fonts/tfm/arkandis/berenisadf/ybdb1c8y.tfm
%{_datadir}/texmf-dist/fonts/tfm/arkandis/berenisadf/ybdb1ci8c.tfm
%{_datadir}/texmf-dist/fonts/tfm/arkandis/berenisadf/ybdb1ci8t.tfm
%{_datadir}/texmf-dist/fonts/tfm/arkandis/berenisadf/ybdb1ci8y.tfm
%{_datadir}/texmf-dist/fonts/tfm/arkandis/berenisadf/ybdb1i8c.tfm
%{_datadir}/texmf-dist/fonts/tfm/arkandis/berenisadf/ybdb1i8t.tfm
%{_datadir}/texmf-dist/fonts/tfm/arkandis/berenisadf/ybdb1i8y.tfm
%{_datadir}/texmf-dist/fonts/tfm/arkandis/berenisadf/ybdb28c.tfm
%{_datadir}/texmf-dist/fonts/tfm/arkandis/berenisadf/ybdb28t.tfm
%{_datadir}/texmf-dist/fonts/tfm/arkandis/berenisadf/ybdb28y.tfm
%{_datadir}/texmf-dist/fonts/tfm/arkandis/berenisadf/ybdb2c8c.tfm
%{_datadir}/texmf-dist/fonts/tfm/arkandis/berenisadf/ybdb2c8t.tfm
%{_datadir}/texmf-dist/fonts/tfm/arkandis/berenisadf/ybdb2c8y.tfm
%{_datadir}/texmf-dist/fonts/tfm/arkandis/berenisadf/ybdb2ci8c.tfm
%{_datadir}/texmf-dist/fonts/tfm/arkandis/berenisadf/ybdb2ci8t.tfm
%{_datadir}/texmf-dist/fonts/tfm/arkandis/berenisadf/ybdb2ci8y.tfm
%{_datadir}/texmf-dist/fonts/tfm/arkandis/berenisadf/ybdb2cij8c.tfm
%{_datadir}/texmf-dist/fonts/tfm/arkandis/berenisadf/ybdb2cij8t.tfm
%{_datadir}/texmf-dist/fonts/tfm/arkandis/berenisadf/ybdb2cij8y.tfm
%{_datadir}/texmf-dist/fonts/tfm/arkandis/berenisadf/ybdb2cijw8y.tfm
%{_datadir}/texmf-dist/fonts/tfm/arkandis/berenisadf/ybdb2ciw8y.tfm
%{_datadir}/texmf-dist/fonts/tfm/arkandis/berenisadf/ybdb2cj8c.tfm
%{_datadir}/texmf-dist/fonts/tfm/arkandis/berenisadf/ybdb2cj8t.tfm
%{_datadir}/texmf-dist/fonts/tfm/arkandis/berenisadf/ybdb2cj8y.tfm
%{_datadir}/texmf-dist/fonts/tfm/arkandis/berenisadf/ybdb2cjw8y.tfm
%{_datadir}/texmf-dist/fonts/tfm/arkandis/berenisadf/ybdb2cw8y.tfm
%{_datadir}/texmf-dist/fonts/tfm/arkandis/berenisadf/ybdb2i8c.tfm
%{_datadir}/texmf-dist/fonts/tfm/arkandis/berenisadf/ybdb2i8t.tfm
%{_datadir}/texmf-dist/fonts/tfm/arkandis/berenisadf/ybdb2i8y.tfm
%{_datadir}/texmf-dist/fonts/tfm/arkandis/berenisadf/ybdb2ij8c.tfm
%{_datadir}/texmf-dist/fonts/tfm/arkandis/berenisadf/ybdb2ij8t.tfm
%{_datadir}/texmf-dist/fonts/tfm/arkandis/berenisadf/ybdb2ij8y.tfm
%{_datadir}/texmf-dist/fonts/tfm/arkandis/berenisadf/ybdb2ijw8y.tfm
%{_datadir}/texmf-dist/fonts/tfm/arkandis/berenisadf/ybdb2iw8y.tfm
%{_datadir}/texmf-dist/fonts/tfm/arkandis/berenisadf/ybdb2j8c.tfm
%{_datadir}/texmf-dist/fonts/tfm/arkandis/berenisadf/ybdb2j8t.tfm
%{_datadir}/texmf-dist/fonts/tfm/arkandis/berenisadf/ybdb2j8y.tfm
%{_datadir}/texmf-dist/fonts/tfm/arkandis/berenisadf/ybdb2jw8y.tfm
%{_datadir}/texmf-dist/fonts/tfm/arkandis/berenisadf/ybdb2w8y.tfm
%{_datadir}/texmf-dist/fonts/tfm/arkandis/berenisadf/ybdb8c.tfm
%{_datadir}/texmf-dist/fonts/tfm/arkandis/berenisadf/ybdb8t.tfm
%{_datadir}/texmf-dist/fonts/tfm/arkandis/berenisadf/ybdb8y.tfm
%{_datadir}/texmf-dist/fonts/tfm/arkandis/berenisadf/ybdbc8c.tfm
%{_datadir}/texmf-dist/fonts/tfm/arkandis/berenisadf/ybdbc8t.tfm
%{_datadir}/texmf-dist/fonts/tfm/arkandis/berenisadf/ybdbc8y.tfm
%{_datadir}/texmf-dist/fonts/tfm/arkandis/berenisadf/ybdbci8c.tfm
%{_datadir}/texmf-dist/fonts/tfm/arkandis/berenisadf/ybdbci8t.tfm
%{_datadir}/texmf-dist/fonts/tfm/arkandis/berenisadf/ybdbci8y.tfm
%{_datadir}/texmf-dist/fonts/tfm/arkandis/berenisadf/ybdbcij8c.tfm
%{_datadir}/texmf-dist/fonts/tfm/arkandis/berenisadf/ybdbcij8t.tfm
%{_datadir}/texmf-dist/fonts/tfm/arkandis/berenisadf/ybdbcij8y.tfm
%{_datadir}/texmf-dist/fonts/tfm/arkandis/berenisadf/ybdbcijw8y.tfm
%{_datadir}/texmf-dist/fonts/tfm/arkandis/berenisadf/ybdbciw8y.tfm
%{_datadir}/texmf-dist/fonts/tfm/arkandis/berenisadf/ybdbcj8c.tfm
%{_datadir}/texmf-dist/fonts/tfm/arkandis/berenisadf/ybdbcj8t.tfm
%{_datadir}/texmf-dist/fonts/tfm/arkandis/berenisadf/ybdbcj8y.tfm
%{_datadir}/texmf-dist/fonts/tfm/arkandis/berenisadf/ybdbcjw8y.tfm
%{_datadir}/texmf-dist/fonts/tfm/arkandis/berenisadf/ybdbcw8y.tfm
%{_datadir}/texmf-dist/fonts/tfm/arkandis/berenisadf/ybdbi8c.tfm
%{_datadir}/texmf-dist/fonts/tfm/arkandis/berenisadf/ybdbi8t.tfm
%{_datadir}/texmf-dist/fonts/tfm/arkandis/berenisadf/ybdbi8y.tfm
%{_datadir}/texmf-dist/fonts/tfm/arkandis/berenisadf/ybdbij8c.tfm
%{_datadir}/texmf-dist/fonts/tfm/arkandis/berenisadf/ybdbij8t.tfm
%{_datadir}/texmf-dist/fonts/tfm/arkandis/berenisadf/ybdbij8y.tfm
%{_datadir}/texmf-dist/fonts/tfm/arkandis/berenisadf/ybdbijw8y.tfm
%{_datadir}/texmf-dist/fonts/tfm/arkandis/berenisadf/ybdbiw8y.tfm
%{_datadir}/texmf-dist/fonts/tfm/arkandis/berenisadf/ybdbj8c.tfm
%{_datadir}/texmf-dist/fonts/tfm/arkandis/berenisadf/ybdbj8t.tfm
%{_datadir}/texmf-dist/fonts/tfm/arkandis/berenisadf/ybdbj8y.tfm
%{_datadir}/texmf-dist/fonts/tfm/arkandis/berenisadf/ybdbjw8y.tfm
%{_datadir}/texmf-dist/fonts/tfm/arkandis/berenisadf/ybdbw8y.tfm
%{_datadir}/texmf-dist/fonts/tfm/arkandis/berenisadf/ybdr08c.tfm
%{_datadir}/texmf-dist/fonts/tfm/arkandis/berenisadf/ybdr08t.tfm
%{_datadir}/texmf-dist/fonts/tfm/arkandis/berenisadf/ybdr08y.tfm
%{_datadir}/texmf-dist/fonts/tfm/arkandis/berenisadf/ybdr0c8c.tfm
%{_datadir}/texmf-dist/fonts/tfm/arkandis/berenisadf/ybdr0c8t.tfm
%{_datadir}/texmf-dist/fonts/tfm/arkandis/berenisadf/ybdr0c8y.tfm
%{_datadir}/texmf-dist/fonts/tfm/arkandis/berenisadf/ybdr0ci8c.tfm
%{_datadir}/texmf-dist/fonts/tfm/arkandis/berenisadf/ybdr0ci8t.tfm
%{_datadir}/texmf-dist/fonts/tfm/arkandis/berenisadf/ybdr0ci8y.tfm
%{_datadir}/texmf-dist/fonts/tfm/arkandis/berenisadf/ybdr0i8c.tfm
%{_datadir}/texmf-dist/fonts/tfm/arkandis/berenisadf/ybdr0i8t.tfm
%{_datadir}/texmf-dist/fonts/tfm/arkandis/berenisadf/ybdr0i8y.tfm
%{_datadir}/texmf-dist/fonts/tfm/arkandis/berenisadf/ybdr18c.tfm
%{_datadir}/texmf-dist/fonts/tfm/arkandis/berenisadf/ybdr18t.tfm
%{_datadir}/texmf-dist/fonts/tfm/arkandis/berenisadf/ybdr18y.tfm
%{_datadir}/texmf-dist/fonts/tfm/arkandis/berenisadf/ybdr1c8c.tfm
%{_datadir}/texmf-dist/fonts/tfm/arkandis/berenisadf/ybdr1c8t.tfm
%{_datadir}/texmf-dist/fonts/tfm/arkandis/berenisadf/ybdr1c8y.tfm
%{_datadir}/texmf-dist/fonts/tfm/arkandis/berenisadf/ybdr1ci8c.tfm
%{_datadir}/texmf-dist/fonts/tfm/arkandis/berenisadf/ybdr1ci8t.tfm
%{_datadir}/texmf-dist/fonts/tfm/arkandis/berenisadf/ybdr1ci8y.tfm
%{_datadir}/texmf-dist/fonts/tfm/arkandis/berenisadf/ybdr1i8c.tfm
%{_datadir}/texmf-dist/fonts/tfm/arkandis/berenisadf/ybdr1i8t.tfm
%{_datadir}/texmf-dist/fonts/tfm/arkandis/berenisadf/ybdr1i8y.tfm
%{_datadir}/texmf-dist/fonts/tfm/arkandis/berenisadf/ybdr28c.tfm
%{_datadir}/texmf-dist/fonts/tfm/arkandis/berenisadf/ybdr28t.tfm
%{_datadir}/texmf-dist/fonts/tfm/arkandis/berenisadf/ybdr28y.tfm
%{_datadir}/texmf-dist/fonts/tfm/arkandis/berenisadf/ybdr2c8c.tfm
%{_datadir}/texmf-dist/fonts/tfm/arkandis/berenisadf/ybdr2c8t.tfm
%{_datadir}/texmf-dist/fonts/tfm/arkandis/berenisadf/ybdr2c8y.tfm
%{_datadir}/texmf-dist/fonts/tfm/arkandis/berenisadf/ybdr2ci8c.tfm
%{_datadir}/texmf-dist/fonts/tfm/arkandis/berenisadf/ybdr2ci8t.tfm
%{_datadir}/texmf-dist/fonts/tfm/arkandis/berenisadf/ybdr2ci8y.tfm
%{_datadir}/texmf-dist/fonts/tfm/arkandis/berenisadf/ybdr2cij8c.tfm
%{_datadir}/texmf-dist/fonts/tfm/arkandis/berenisadf/ybdr2cij8t.tfm
%{_datadir}/texmf-dist/fonts/tfm/arkandis/berenisadf/ybdr2cij8y.tfm
%{_datadir}/texmf-dist/fonts/tfm/arkandis/berenisadf/ybdr2cijw8y.tfm
%{_datadir}/texmf-dist/fonts/tfm/arkandis/berenisadf/ybdr2ciw8y.tfm
%{_datadir}/texmf-dist/fonts/tfm/arkandis/berenisadf/ybdr2cj8c.tfm
%{_datadir}/texmf-dist/fonts/tfm/arkandis/berenisadf/ybdr2cj8t.tfm
%{_datadir}/texmf-dist/fonts/tfm/arkandis/berenisadf/ybdr2cj8y.tfm
%{_datadir}/texmf-dist/fonts/tfm/arkandis/berenisadf/ybdr2cjw8y.tfm
%{_datadir}/texmf-dist/fonts/tfm/arkandis/berenisadf/ybdr2cw8y.tfm
%{_datadir}/texmf-dist/fonts/tfm/arkandis/berenisadf/ybdr2i8c.tfm
%{_datadir}/texmf-dist/fonts/tfm/arkandis/berenisadf/ybdr2i8t.tfm
%{_datadir}/texmf-dist/fonts/tfm/arkandis/berenisadf/ybdr2i8y.tfm
%{_datadir}/texmf-dist/fonts/tfm/arkandis/berenisadf/ybdr2ij8c.tfm
%{_datadir}/texmf-dist/fonts/tfm/arkandis/berenisadf/ybdr2ij8t.tfm
%{_datadir}/texmf-dist/fonts/tfm/arkandis/berenisadf/ybdr2ij8y.tfm
%{_datadir}/texmf-dist/fonts/tfm/arkandis/berenisadf/ybdr2ijw8y.tfm
%{_datadir}/texmf-dist/fonts/tfm/arkandis/berenisadf/ybdr2iw8y.tfm
%{_datadir}/texmf-dist/fonts/tfm/arkandis/berenisadf/ybdr2j8c.tfm
%{_datadir}/texmf-dist/fonts/tfm/arkandis/berenisadf/ybdr2j8t.tfm
%{_datadir}/texmf-dist/fonts/tfm/arkandis/berenisadf/ybdr2j8y.tfm
%{_datadir}/texmf-dist/fonts/tfm/arkandis/berenisadf/ybdr2jw8y.tfm
%{_datadir}/texmf-dist/fonts/tfm/arkandis/berenisadf/ybdr2w8y.tfm
%{_datadir}/texmf-dist/fonts/tfm/arkandis/berenisadf/ybdr8c.tfm
%{_datadir}/texmf-dist/fonts/tfm/arkandis/berenisadf/ybdr8t.tfm
%{_datadir}/texmf-dist/fonts/tfm/arkandis/berenisadf/ybdr8y.tfm
%{_datadir}/texmf-dist/fonts/tfm/arkandis/berenisadf/ybdrc8c.tfm
%{_datadir}/texmf-dist/fonts/tfm/arkandis/berenisadf/ybdrc8t.tfm
%{_datadir}/texmf-dist/fonts/tfm/arkandis/berenisadf/ybdrc8y.tfm
%{_datadir}/texmf-dist/fonts/tfm/arkandis/berenisadf/ybdrci8c.tfm
%{_datadir}/texmf-dist/fonts/tfm/arkandis/berenisadf/ybdrci8t.tfm
%{_datadir}/texmf-dist/fonts/tfm/arkandis/berenisadf/ybdrci8y.tfm
%{_datadir}/texmf-dist/fonts/tfm/arkandis/berenisadf/ybdrcij8c.tfm
%{_datadir}/texmf-dist/fonts/tfm/arkandis/berenisadf/ybdrcij8t.tfm
%{_datadir}/texmf-dist/fonts/tfm/arkandis/berenisadf/ybdrcij8y.tfm
%{_datadir}/texmf-dist/fonts/tfm/arkandis/berenisadf/ybdrcijw8y.tfm
%{_datadir}/texmf-dist/fonts/tfm/arkandis/berenisadf/ybdrciw8y.tfm
%{_datadir}/texmf-dist/fonts/tfm/arkandis/berenisadf/ybdrcj8c.tfm
%{_datadir}/texmf-dist/fonts/tfm/arkandis/berenisadf/ybdrcj8t.tfm
%{_datadir}/texmf-dist/fonts/tfm/arkandis/berenisadf/ybdrcj8y.tfm
%{_datadir}/texmf-dist/fonts/tfm/arkandis/berenisadf/ybdrcjw8y.tfm
%{_datadir}/texmf-dist/fonts/tfm/arkandis/berenisadf/ybdrcw8y.tfm
%{_datadir}/texmf-dist/fonts/tfm/arkandis/berenisadf/ybdri8c.tfm
%{_datadir}/texmf-dist/fonts/tfm/arkandis/berenisadf/ybdri8t.tfm
%{_datadir}/texmf-dist/fonts/tfm/arkandis/berenisadf/ybdri8y.tfm
%{_datadir}/texmf-dist/fonts/tfm/arkandis/berenisadf/ybdrij8c.tfm
%{_datadir}/texmf-dist/fonts/tfm/arkandis/berenisadf/ybdrij8t.tfm
%{_datadir}/texmf-dist/fonts/tfm/arkandis/berenisadf/ybdrij8y.tfm
%{_datadir}/texmf-dist/fonts/tfm/arkandis/berenisadf/ybdrijw8y.tfm
%{_datadir}/texmf-dist/fonts/tfm/arkandis/berenisadf/ybdriw8y.tfm
%{_datadir}/texmf-dist/fonts/tfm/arkandis/berenisadf/ybdrj8c.tfm
%{_datadir}/texmf-dist/fonts/tfm/arkandis/berenisadf/ybdrj8t.tfm
%{_datadir}/texmf-dist/fonts/tfm/arkandis/berenisadf/ybdrj8y.tfm
%{_datadir}/texmf-dist/fonts/tfm/arkandis/berenisadf/ybdrjw8y.tfm
%{_datadir}/texmf-dist/fonts/tfm/arkandis/berenisadf/ybdrw8y.tfm
%{_datadir}/texmf-dist/fonts/type1/arkandis/berenisadf/ybdb.pfb
%{_datadir}/texmf-dist/fonts/type1/arkandis/berenisadf/ybdbc.pfb
%{_datadir}/texmf-dist/fonts/type1/arkandis/berenisadf/ybdbci.pfb
%{_datadir}/texmf-dist/fonts/type1/arkandis/berenisadf/ybdbi.pfb
%{_datadir}/texmf-dist/fonts/type1/arkandis/berenisadf/ybdr.pfb
%{_datadir}/texmf-dist/fonts/type1/arkandis/berenisadf/ybdrc.pfb
%{_datadir}/texmf-dist/fonts/type1/arkandis/berenisadf/ybdrci.pfb
%{_datadir}/texmf-dist/fonts/type1/arkandis/berenisadf/ybdri.pfb
%{_datadir}/texmf-dist/fonts/type1/arkandis/berenisadf/yrdd8a.pfb
%{_datadir}/texmf-dist/fonts/type1/arkandis/berenisadf/yrddc8a.pfb
%{_datadir}/texmf-dist/fonts/type1/arkandis/berenisadf/yrddi8a.pfb
%{_datadir}/texmf-dist/fonts/type1/arkandis/berenisadf/yrdr8a.pfb
%{_datadir}/texmf-dist/fonts/type1/arkandis/berenisadf/yrdrc8a.pfb
%{_datadir}/texmf-dist/fonts/type1/arkandis/berenisadf/yrdri8a.pfb
%{_datadir}/texmf-dist/fonts/type1/arkandis/berenisadf/yrdriw8a.pfb
%doc %{_datadir}/texmf-dist/source/fonts/berenisadf/Makefile.make
%doc %{_datadir}/texmf-dist/source/fonts/berenisadf/berenisadf.dtx
%doc %{_datadir}/texmf-dist/source/fonts/berenisadf/berenisadf.ins
%{_datadir}/texmf-dist/tex/latex/berenisadf/berenis.sty
%{_datadir}/texmf-dist/tex/latex/berenisadf/ly1ybd.fd
%{_datadir}/texmf-dist/tex/latex/berenisadf/ly1ybd0.fd
%{_datadir}/texmf-dist/tex/latex/berenisadf/ly1ybd1.fd
%{_datadir}/texmf-dist/tex/latex/berenisadf/ly1ybd2.fd
%{_datadir}/texmf-dist/tex/latex/berenisadf/ly1ybd2j.fd
%{_datadir}/texmf-dist/tex/latex/berenisadf/ly1ybd2jw.fd
%{_datadir}/texmf-dist/tex/latex/berenisadf/ly1ybd2w.fd
%{_datadir}/texmf-dist/tex/latex/berenisadf/ly1ybdj.fd
%{_datadir}/texmf-dist/tex/latex/berenisadf/ly1ybdjw.fd
%{_datadir}/texmf-dist/tex/latex/berenisadf/ly1ybdw.fd
%{_datadir}/texmf-dist/tex/latex/berenisadf/t1ybd.fd
%{_datadir}/texmf-dist/tex/latex/berenisadf/t1ybd0.fd
%{_datadir}/texmf-dist/tex/latex/berenisadf/t1ybd1.fd
%{_datadir}/texmf-dist/tex/latex/berenisadf/t1ybd2.fd
%{_datadir}/texmf-dist/tex/latex/berenisadf/t1ybd2j.fd
%{_datadir}/texmf-dist/tex/latex/berenisadf/t1ybdj.fd
%{_datadir}/texmf-dist/tex/latex/berenisadf/ts1ybd.fd
%{_datadir}/texmf-dist/tex/latex/berenisadf/ts1ybd0.fd
%{_datadir}/texmf-dist/tex/latex/berenisadf/ts1ybd1.fd
%{_datadir}/texmf-dist/tex/latex/berenisadf/ts1ybd2.fd
%{_datadir}/texmf-dist/tex/latex/berenisadf/ts1ybd2j.fd
%{_datadir}/texmf-dist/tex/latex/berenisadf/ts1ybd2jw.fd
%{_datadir}/texmf-dist/tex/latex/berenisadf/ts1ybd2w.fd
%{_datadir}/texmf-dist/tex/latex/berenisadf/ts1ybdj.fd
%{_datadir}/texmf-dist/tex/latex/berenisadf/ts1ybdjw.fd
%{_datadir}/texmf-dist/tex/latex/berenisadf/ts1ybdw.fd
