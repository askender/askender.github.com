gem install sass
npm -g install coffee-script
sudo gem install haml
brew install watch

coffee --watch --output javascripts raws/coffee/
watch haml raws/haml/tabs.html.haml tabs.html
sass --watch raws/sass/:stylesheets/

watch haml raws/haml/*.html.haml *.html
