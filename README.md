
# ValoRPC

Показ подробной информации в Discord об вашей игре Valorant.

Отображает статус в вашем профиле Discord через функционал самого Дискорда о вашей игре/статусе в Valorant, используя комбинацию чтения с экрана с помощью [оптического распознавания символов Google](https://github.com/tesseract-ocr/tesseract) и внутреннего API Valorant. Не волнуйтесь, это никак не повлияет на память процесса Valorant :)

## ПРИМЕЧАНИЕ

- Пожалуйста, перейдите в Настройки Discord -> Настройки активности -> Приватность активности -> Отображать текущую активность в виде сообщения о статусе. -> Включено
- Поскольку эта программа в значительной степени полагается на способность чтения с экрана, она еще не тестировалась на разрешениях, отличных от 1920x1080, 16:9 для Valorant windowed fullscreen/fullscreen. Это означает, что программа не может гарантировать, что она будет работать с разрешениями экрана, которое отличается от протестированного размера.

## Особенности

- Поддерживаются стандартный режимы, быстрая игра, репликация и бой на смерть.
- Эскалация, спайк-раш  пока не полностью поддерживают rpc в игровых режимах. Будет отображаться только базовый rpc.

## Скриншоты

![Standard](https://i.imgur.com/xvllLWJ.png)
![Deathmatch](https://i.imgur.com/nOzcMHF.png)
![Deathmatch](https://i.imgur.com/3i1XQqh.png)
![Competitive](https://i.imgur.com/v6CKH5Z.png)
![Idling](https://i.imgur.com/TNmCBfK.png)

## Установка

Загрузите exe-файл с [последнии релизы](https://github.com/PenguinDevs/ValoRPC/releases/latest), а затем запустите файл.

Обратите внимание, что по умолчанию windows блокирует запуск приложения, выдавая сообщение "Microsoft Defender SmartScreen предотвратил запуск нераспознанного приложения...". Это происходит потому, что приложение не подписано, как и многие другие исполняемые файлы с открытым исходным кодом в интернете. Поэтому этот проект является открытым не только для вклада/исправления, но и для того, чтобы вы могли доверять исходному коду этого приложения - хотя код действительно довольно запутанный.

Если вы уверены, что мой проект не содержит вредоносных программ, нажмите "Подробнее", а затем "Запустить в любом случае".

## Благодарность

 - [Colinhartigan's Python Valclient](https://github.com/colinhartigan/valclient.py)
 - [Techchrism's Valorant API docs](https://github.com/techchrism/valorant-api-docs)
 - [Floxay's Riot Auth](https://github.com/floxay/python-riot-auth)
 - [Google's Tesseract OCR](https://github.com/tesseract-ocr/tesseract)
 - [Buliasz's GUI for Tesseract OCR training](https://github.com/buliasz/tesstrain-windows-gui)
