# revision 24273
# category Package
# catalog-ctan /graphics/pgf/contrib/pgfgantt
# catalog-date 2011-10-12 17:03:26 +0200
# catalog-license lppl1.3
# catalog-version 2.0
Name:		texlive-pgfgantt
Version:	2.0
Release:	1
Summary:	Draw Gantt charts with TikZ
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/graphics/pgf/contrib/pgfgantt
License:	LPPL1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/pgfgantt.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/pgfgantt.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/pgfgantt.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-doc <= 20110705-3
Conflicts:	texlive-source <= 20110705-3

%description
The package provides an environment for drawing Gantt charts
that contain various elements (titles, bars, milestones, groups
and links). Several keys customize the appearance of the chart
elements.

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
%{_texmfdistdir}/tex/latex/pgfgantt/pgfgantt.sty
%doc %{_texmfdistdir}/doc/latex/pgfgantt/README
%doc %{_texmfdistdir}/doc/latex/pgfgantt/pgfgantt.pdf
#- source
%doc %{_texmfdistdir}/source/latex/pgfgantt/pgfgantt.dtx
%doc %{_texmfdistdir}/source/latex/pgfgantt/pgfgantt.ins
%doc %{_tlpkgobjdir}/*.tlpobj

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
mkdir -p %{buildroot}%{_tlpkgobjdir}
cp -fpa tlpkg/tlpobj/*.tlpobj %{buildroot}%{_tlpkgobjdir}
