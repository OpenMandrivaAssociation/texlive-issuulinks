%global tl_name issuulinks
%global tl_revision 25742

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.1
Release:	%{tl_revision}.1
Summary:	Produce external links instead of internal ones
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/issuulinks
License:	lppl1.3
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/issuulinks.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/issuulinks.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/issuulinks.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The PDF visualizer http://issuu.com/ISSUU is a popular service which
shows PDF documents "a page a time". Due to the way it is implemented,
internal links in these documents are not allowed. Instead, they must be
converted to external ones in the form
http://issuu.com/action/page?page=PAGENUMBER. The package patches
hyperref to produce external links in the required form instead of
internal links created by \ref, \cite and other commands. Since the
package redefines the internals of hyperref, it must be loaded it AFTER
hyperref.

