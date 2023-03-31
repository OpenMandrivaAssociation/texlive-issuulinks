Name:		texlive-issuulinks
Version:	25742
Release:	2
Summary:	Produce external links instead of internal ones
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/issuulinks
License:	LPPL1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/issuulinks.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/issuulinks.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/issuulinks.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The PDF visualizer http://issuu.com/ISSUU is a popular service
allowing to show PDF documents "a page a time". Due to the way
it is implemented, internal links in these documents are not
allowed. Instead, they must be converted to external ones in
the form http://issuu.com/action/page?page=PAGENUMBER. The
package patches hyperref to produce external links in the
required form instead of internal links created by \ref, \cite
and other commands. Since the package redefines the internals
of hyperref, it must be loaded it AFTER hyperref.

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
%setup -c -a1 -a2
%autopatch -p1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
