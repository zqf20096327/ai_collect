# sofiakholina-3D-Generation

**Русский** · [English](#english)

**Генерация 3D-модели (без текстуры) по одному или нескольким видам в ComfyUI: 3 workflow + установщик.**

Workflow:

- **3D-Gen_TripoSplat - генерация по одному фото** (точно, но со следами сплатов на меше)
- **3D-Gen_Trellis - генерация по одному фото** (приблизительно, но без артефактов)
- **3D-Gen_Pixal_MV - генерация по 1-4 видам** (результат не слишком хороший, но часто виды нужны)

**Видео по этим Workflow на [YouTube](https://youtu.be/Sw3rYAtZyCk) и [VK](https://vkvideo.ru/video-226908262_456239133)**

**Workflow текстурирования любой вашей 3D-модели здесь:** [sofiakholina-3D-Texturing](https://github.com/sofiakholina/sofiakholina-3D-Texturing).

## Установка

**Только для Windows, видеокарт NVIDIA от 6 GB VRAM с актуальным драйвером и ComfyUI версии 0.45+. Свободное место на диске: ComfyUI — около 6 GB, модели — около 16 GB для 3-х workflow.**

### Автоматически

1. Установите ComfyUI: [Comfy Desktop](https://www.comfy.org/download), также подойдёт [ComfyUI Portable](https://github.com/Comfy-Org/ComfyUI/releases).
2. Скачайте этот репозиторий: зелёная кнопка **Code** вверху страницы → **Download ZIP**, распакуйте в любую папку. После установки эту папку можно удалить (для Check.bat и Uninstall.bat скачайте архив заново).
3. Закройте ComfyUI.
4. Запустите **Install.bat**. 
Если Windows покажет «Система Windows защитила ваш компьютер» — **Подробнее → Выполнить в любом случае**.
5. Выберите, какие workflow установить (Enter — все), и ответьте, скачивать ли модели. При повторном запуске Install.bat загрузка продолжится с места остановки.
6. Запустите ComfyUI: workflow — в левой панели, **Рабочие процессы** (клавиша W).

Проверка: при открытом ComfyUI запустите **Check.bat** — он покажет, все ли ноды и модели на месте.

**После обновления Comfy Desktop** запустите Install.bat ещё раз.

**Удаление:** Uninstall.bat. Удаляет всё, что установил установщик; модели — только после вашего подтверждения. Файлы — в Корзину (с флешки и сетевых дисков — сразу, без Корзины).

### Вручную

Выполните шаги из [MANUAL_INSTALL.md](MANUAL_INSTALL.md) (они же — в заметке **START** внутри workflow).

## Если не работает

1. При открытом ComfyUI запустите **Check.bat** — он покажет, чего не хватает.
2. Перезапустите ComfyUI.
3. После обновления Comfy Desktop запустите Install.bat ещё раз.
4. Не помогло — напишите мне в Telegram: https://t.me/sofiakholina и приложите скриншот ошибки.

## Известные особенности

- Portable не запускается с ошибкой c10.dll — установите Microsoft Visual C++ Redistributable: https://aka.ms/vc14/vc_redist.x64.exe
- В старом интерфейсе Comfy (не Nodes 2.0) видны служебные настройки Save 3D — их не нужно менять.

## Лицензия

GPL-3.0 (файл LICENSE). Сторонние шаблоны workflow и модели — со своими лицензиями, см. [THIRD_PARTY_NOTICES.md](THIRD_PARTY_NOTICES.md). Ноды s_tools — [sofiakholina-s_tools](https://github.com/sofiakholina/sofiakholina-s_tools).

---

## English

**Generate an untextured 3D model from one or several views in ComfyUI: 3 workflows + installer.**

Workflows:

- **3D-Gen_TripoSplat - generation from one photo** (accurate, but with splat traces on the mesh)
- **3D-Gen_Trellis - generation from one photo** (approximate, but without artifacts)
- **3D-Gen_Pixal_MV - generation from 1-4 views** (the result is not very good, but views are often needed)

**Videos about these workflows on [YouTube](https://youtu.be/Sw3rYAtZyCk) and [VK](https://vkvideo.ru/video-226908262_456239133)**

**Workflows for texturing any of your 3D models:** [sofiakholina-3D-Texturing](https://github.com/sofiakholina/sofiakholina-3D-Texturing).

## Install

**Windows only, NVIDIA GPU with 6 GB VRAM or more and a current driver, ComfyUI 0.45+. Free disk space: ComfyUI — about 6 GB, models — about 16 GB for the 3 workflows.**

Workflow notes are in Russian.

### Automatic

1. Install ComfyUI: [Comfy Desktop](https://www.comfy.org/download); [ComfyUI Portable](https://github.com/Comfy-Org/ComfyUI/releases) works too.
2. Download this repository: green **Code** button at the top of the page → **Download ZIP**, unzip it to any folder. You can delete this folder after installing (download the archive again for Check.bat and Uninstall.bat).
3. Close ComfyUI.
4. Run **Install.bat**. 
If Windows shows "Windows protected your PC", click **More info → Run anyway**.
5. Choose which workflows to install (Enter — all) and whether to download the models. Running Install.bat again resumes the download.
6. Start ComfyUI: the workflows are in the left sidebar, **Workflows** (W key).

To verify: with ComfyUI open, run **Check.bat**; it shows whether all nodes and models are in place.

**After a Comfy Desktop update**, run Install.bat again.

**Uninstall:** Uninstall.bat. Removes everything the installer installed; models only after you confirm. Files go to the Recycle Bin (from USB and network drives they are deleted immediately, without the Recycle Bin).

### Manual

Follow [MANUAL_INSTALL.md](MANUAL_INSTALL.md#english).

## Troubleshooting

1. With ComfyUI open, run **Check.bat** — it shows what is missing.
2. Restart ComfyUI.
3. After a Comfy Desktop update, run Install.bat again.
4. Still not working — message me on Telegram: https://t.me/sofiakholina and attach a screenshot of the error.

## Known issues

- Portable fails with a c10.dll error: install the Microsoft Visual C++ Redistributable: https://aka.ms/vc14/vc_redist.x64.exe
- In the legacy Comfy UI (not Nodes 2.0) the internal settings of Save 3D are visible; you don't need to change them.

## License

GPL-3.0 (see LICENSE). Third-party workflow templates and models keep their own licenses, see [THIRD_PARTY_NOTICES.md](THIRD_PARTY_NOTICES.md). s_tools nodes: [sofiakholina-s_tools](https://github.com/sofiakholina/sofiakholina-s_tools).
