Vagrant.configure("2") do |config|
  config.vm.box = "ubuntu/trusty64"
  config.vm.network :private_network, ip: "192.168.1.33"

  config.vm.provider "virtualbox" do |vb|
    vb.name = "hello-world"
    # something is up with my dev machine; https://github.com/jonschipp/vagrant/issues/3
    vb.customize ["modifyvm", :id, "--usb", "on"]
    vb.customize ["modifyvm", :id, "--usbehci", "off"]
  end

  config.vm.provision "ansible_local" do |ansible|
    ansible.playbook = "playbook.yml"
    # ansible.verbose = "v"
  end
end
