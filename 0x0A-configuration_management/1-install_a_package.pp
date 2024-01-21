#Using Puppet, install flask from pip3.
#Install flask
#Version must be 2.1.0
package { 'werkzeung':
    ensure   => '2.2.2',
    provider => 'pip3',
}

package { 'flask':
  ensure   => '2.1.0',
  provider => 'pip3',
  require  => Package['werkzeung'],
}

