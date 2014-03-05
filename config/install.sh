brew install thrift --with-java --with-python
brew install maven


To install Ruby binding:
  gem install thrift

To install PHP extension for e.g. PHP 5.5:
  brew install josegonzalez/php/php55-thrift

Set PYTHONPATH if you need Python to find the installed site-packages:
  export PYTHONPATH=/usr/local/lib/python2.7/site-packages:$PYTHONPATH
