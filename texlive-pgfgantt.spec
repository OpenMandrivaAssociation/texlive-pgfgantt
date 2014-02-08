# revision 25204
# category Package
# catalog-ctan /graphics/pgf/contrib/pgfgantt
# catalog-date 2012-01-26 11:19:33 +0100
# catalog-license lppl1.3
# catalog-version 3.0
Name:		texlive-pgfgantt
Version:	3.0
Release:	2
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

%description
The package provides an environment for drawing Gantt charts
that contain various elements (titles, bars, milestones, groups
and links). Several keys customize the appearance of the chart
elements.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/pgfgantt/pgfgantt.sty
%doc %{_texmfdistdir}/doc/latex/pgfgantt/README
%doc %{_texmfdistdir}/doc/latex/pgfgantt/pgfgantt.pdf
#- source
%doc %{_texmfdistdir}/source/latex/pgfgantt/pgfgantt.dtx
%doc %{_texmfdistdir}/source/latex/pgfgantt/pgfgantt.ins

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}


%changelog
* Tue Jan 31 2012 Paulo Andrade <pcpa@mandriva.com.br> 3.0-1
+ Revision: 770236
- Update to latest upstream package

* Wed Jan 04 2012 Paulo Andrade <pcpa@mandriva.com.br> 2.1-2
+ Revision: 754816
- Rebuild to reduce used resources

* Tue Nov 22 2011 Paulo Andrade <pcpa@mandriva.com.br> 2.1-1
+ Revision: 732607
- texlive-pgfgantt

* Sat Nov 05 2011 Paulo Andrade <pcpa@mandriva.com.br> 2.0-1
+ Revision: 719241
- texlive-pgfgantt
- texlive-pgfgantt
- texlive-pgfgantt
- texlive-pgfgantt

