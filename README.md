<h1 align="center">MIAVI(Ministry of Internal Affairs Vision) scan tool for linux</h1>

<p align="center">

<img src="https://img.shields.io/badge/made%20by-INCEDOS-blueviolet" >

<img src="https://img.shields.io/badge/python-v3.8.10-blueviolet">

<img src="https://img.shields.io/badge/PyQt5-v5.15.6-blueviolet">

<img src="https://badges.frapsoft.com/os/v1/open-source.svg?v=103" >

<img src="https://img.shields.io/github/stars/AlanLeinhard/incident.svg?style=flat">

<img src="https://img.shields.io/github/languages/top/AlanLeinhard/incident.svg">

<img src="https://img.shields.io/github/issues/AlanLeinhard/incident.svg">

<!-- <img src="https://img.shields.io/badge/PRs-welcome-brightgreen.svg?style=flat"> -->
</p>

---
# Установка

`git clobe https://github.com/AlanLeinhard/incident.git`<br>
`cd incident`<br>
`python3 setup.py --command-packages=stdeb.command bdist_deb`<br>
`sudo dpkg -i ./deb_dist/python3-ext4scanner_0.1.1-1_all.deb`<br>
`sudo ext4scanner --install`<br>

## Usage

### Global Usage

После установки есть 2 варианта запуска приложения:


- **консоль**
  - для запуска через консоль нужно выполнить комманду `ext4scanner`
- **ярлык приложения**
  - для запуска через ярлык нужно найти его в списке установленных приложений и нажать на него

<p align="center"><img src="https://i.ibb.co/M8N2wVx/screen-icon.png"></p>

### Инструкция
При запуске приложения у пользователя будет запрошен пароль, который понядобится для дальнейшей работы приложения

<p align="center"><img src="https://i.ibb.co/VLBGLBM/screen-sudo.png"></p>

Если был введен неверный пароль, то интерфейс уведомит вас об этом и не допустит вас до возможностей приложения

<p align="center"><img src="https://i.ibb.co/8cvcy7r/screen-sudo-false.png"></p>

После успешного введения пароля пользователю будет предоставлен интерфейс приложения, который на данном этапе позволяет:


- **просмотр дисков**
  - просмотреть диски, подключенные к системе
- **ярлык приложенияинформация о дисках**
  - просмотреть имеющуюся информацию о подключенных(конкретном) дисках(диске)

<p align="center"><img src="https://i.ibb.co/tL17zzR/screen-inter-1.png"></p>

<p align="center"><img src="https://i.ibb.co/9bj7sFV/screen-inter-2.png"></p>

<p align="center"><img src="https://i.ibb.co/j8qTfSb/screen-inter-3.png" ></p>
  





<!-- 

sudo apt-get install python3-pyqt5
sudo apt-get install qtcreator pyqt5-dev-tools
sudo apt-get install qttools5-dev-tools
cd ext4scanner && pyuic5 -x script5.ui -o script5.py && cd ..

pytopip

python3 setup.py sdist
pip install dist/EXT4_SCANNER-0.1.1.tar.gz


pytodeb

python3 setup.py --command-packages=stdeb.command bdist_deb
sudo dpkg -i ./deb_dist/python3-ext4scanner_0.1.1-1_all.deb


cd /usr/bin
ext4scanner


dpkg -l | grep ext4
sudo dpkg -r ext4scanner 





python3 setup.py --command-packages=stdeb.command bdist_deb && sudo dpkg -r ext4scanner && sudo dpkg -i ./deb_dist/python3-ext4scanner_0.1.1-1_all.deb && ext4scanner

 -->