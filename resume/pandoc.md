pandoc -N --template=mytemplate.tex -V title-meta="李博 简历" -V author-meta="askender" -V subject-meta="resume" -V keywords-meta="resume create" -V mainfont="WenQuanYi Micro Hei" -V fontsize=16pt -V version=0.1 askender.md --latex-engine=xelatex -o askender.pdf

pandoc -N --template=mytemplate.tex -V title-meta="Resume of Li Bo" -V author-meta="askender" -V subject-meta="resume" -V keywords-meta="resume create" -V mainfont="WenQuanYi Micro Hei" -V fontsize=16pt -V version=0.1 askender_en.md --latex-engine=xelatex -o askender_en.pdf

pandoc -N --template=mytemplate.tex -V title-meta="李博 个人战略计划" -V author-meta="askender" -V subject-meta="plan" -V keywords-meta="life plan" -V mainfont="WenQuanYi Micro Hei" -V fontsize=16pt -V version=0.1 five-year-plan.md --latex-engine=xelatex -o five_year_plan.pdf
