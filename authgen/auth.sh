#!/bin/sh

# Run Script when first setting up/adding RPI server to grant key auth to master

if [ -d ~/.ssh ]; then
        if [ -f ~/.ssh/id_rsa.pub ]; then
                cat ~/.ssh/id_rsa.pub >> pi@10.10.100.144:~/.ssh/authorized_keys
                echo "id_rsa.pub already exists. Added to list of authorized_keys"
        else
                scp -r pi@10.10.100.144:~/.ssh/id_rsa ~/.ssh
                echo "Valid key established"
        fi
else
        mkdir .ssh
        echo "Directory Made"
        scp -r pi@10.10.100.144:~/.ssh/id_rsa ~/.ssh
        echo "Valid key established"
fi

