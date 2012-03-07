# revision 25534
# category Package
# catalog-ctan /macros/latex/contrib/issuulinks
# catalog-date 2012-02-28 11:35:03 +0100
# catalog-license lppl1.3
# catalog-version 1.0
Name:		texlive-issuulinks
Version:	1.0
Release:	1
Summary:	Produce external links instead of internal ones
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/issuulinks
License:	LPPL1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/issuulinks.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/issuulinks.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/issuulinks.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The PDF visualizer ISSUU is a popular service allowing to show
PDF documents "a page a time". Due to the way it is
implemented, internal links in these documents are not allowed.
Instead, they must be converted to external ones in the form
http://issuu.com/action/page?page=PAGENUMBER. The package
patches hyperref to produce external links in the required form
instead of internal links created by \ref, \cite and other
commands. Since the package redefines the internals of
hyperref, it must be loaded it AFTER hyperref.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/issuulinks/issuulinks.sty
%doc %{_texmfdistdir}/doc/latex/issuulinks/Makefile
%doc %{_texmfdistdir}/doc/latex/issuulinks/README
%doc %{_texmfdistdir}/doc/latex/issuulinks/issuulinks.pdf
%doc %{_texmfdistdir}/doc/latex/issuulinks/sample.pdf
%doc %{_texmfdistdir}/doc/latex/issuulinks/sample.tex
#- source
%doc %{_texmfdistdir}/source/latex/issuulinks/issuulinks.dtx
%doc %{_texmfdistdir}/source/latex/issuulinks/issuulinks.ins

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
