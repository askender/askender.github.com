sudo apt-get install pandoc
sudo apt-get install texlive-xetex
# texlive-latex-recommended
# texlive-latex-extra

pandoc -N --template=mytemplate.tex -V title-meta="李博 简历" -V author-meta="askender" -V subject-meta="resume" -V keywords-meta="resume create" -V mainfont="WenQuanYi Micro Hei" -V fontsize=16pt -V version=0.1 askender.md --latex-engine=xelatex -o askender.pdf

pandoc -N --template=mytemplate.tex -V title-meta="Resume of Li Bo" -V author-meta="askender" -V subject-meta="resume" -V keywords-meta="resume create" -V mainfont="WenQuanYi Micro Hei" -V fontsize=16pt -V version=0.1 askender_en.md --latex-engine=xelatex -o askender_en.pdf

pandoc -N --template=mytemplate.tex -V title-meta="李博 个人战略计划" -V author-meta="askender" -V subject-meta="plan" -V keywords-meta="life plan" -V mainfont="WenQuanYi Micro Hei" -V fontsize=16pt -V version=0.1 five-year-plan.md --latex-engine=xelatex -o five_year_plan.pdf

pandoc -N --template=mytemplate.tex -V title-meta="李博 简历" -V author-meta="askender" -V subject-meta="resume" -V keywords-meta="resume create" -V mainfont="Hiragino Sans GB" -V fontsize=18pt -V version=0.2 askender.md --latex-engine=/usr/local/texlive/2013basic/bin/x86_64-darwin/xelatex -o askender1.pdf


-V urlcolor="#666"
-V linkcolor="#666"


pandoc -N --template=mytemplate.tex -V title-meta="antina resume" -V author-meta="antina" -V subject-meta="resume" -V keywords-meta="resume create" -V mainfont="华文细黑" -V fontsize=24pt -V version=0.1 antina_en4.md --latex-engine=xelatex -o antina_en4.pdf
